# filename: codebase/horndeski_pipeline.py
import sympy as sp


class HorndeskiPipeline:
    """
    A symbolic computation pipeline for the perturbative analysis of Horndeski gravity.

    This class provides a modular framework to:
    1. Define the necessary symbolic variables for Horndeski gravity.
    2. Expand the Horndeski action around a given background (e.g., Minkowski).
    3. Extract and analyze terms from the expanded action at different orders.
    """

    def __init__(self):
        """
        Initializes the pipeline by defining symbols for fields, perturbations,
        and the Horndeski functions evaluated at the background.
        """
        print("Initializing Horndeski Symbolic Pipeline...")
        self._define_symbols()
        print("Initialization complete.")

    def _define_symbols(self):
        """
        Defines all necessary symbolic variables and functions using sympy.
        """
        # 1. Coordinates
        self.t, self.x, self.y, self.z = sp.symbols('t x y z', real=True)
        self.coords = [self.t, self.x, self.y, self.z]

        # 2. Background fields and constants
        self.phi_0 = sp.Symbol('phi_0')  # Constant background scalar field
        self.X_0 = 0  # Background kinetic term is zero in Minkowski

        # 3. Perturbations
        self.pi = sp.Function('pi')(*self.coords)  # Scalar field perturbation
        self.h = sp.Matrix(4, 4, lambda i, j: sp.Function('h_{' + str(i) + str(j) + '}')(*self.coords))

        # 4. Metric
        self.eta = sp.diag(1, -1, -1, -1)

        # 5. Horndeski functions and their derivatives evaluated at the background (phi_0, X_0=0)
        # This is more efficient than substituting at the end.
        G2_b, G2p_b, G2X_b = sp.symbols('G_2 G_2_phi G_2_X')
        G3_b, G3p_b, G3X_b = sp.symbols('G_3 G_3_phi G_3_X')
        G4_b, G4p_b, G4X_b = sp.symbols('G_4 G_4_phi G_4_X')
        G5_b, G5p_b, G5X_b = sp.symbols('G_5 G_5_phi G_5_X')
        
        self.G_background = {
            'G2': G2_b, 'G2p': G2p_b, 'G2X': G2X_b,
            'G3': G3_b, 'G3p': G3p_b, 'G3X': G3X_b,
            'G4': G4_b, 'G4p': G4p_b, 'G4X': G4X_b,
            'G5': G5_b, 'G5p': G5p_b, 'G5X': G5X_b,
        }
        print("Defined symbols: pi, h_munu")
        print("Defined background Horndeski functions: G_i, G_i_phi, G_i_X")


    def expand_action_minkowski(self, order):
        """
        Expands the Horndeski action around a Minkowski background up to a given order.

        This method computes the series expansion of each component of the Lagrangian
        (sqrt(-g), X, Box(phi), etc.) and combines them to get the full action density.

        Args:
            order (int): The order of the expansion in perturbations (pi, h).
        """
        print("\n" + "="*60)
        print("Starting Action Expansion around Minkowski Background to Order: " + str(order))
        print("="*60)

        epsilon = sp.Symbol('epsilon')

        # Perturbed metric and its inverse
        g_pert = self.eta + epsilon * self.h
        g_inv_pert = g_pert.inv().applyfunc(lambda f: f.series(epsilon, 0, order + 1).removeO())

        # 1. Expand sqrt(-g)
        det_g_pert = g_pert.det()
        sqrt_g_series = sp.sqrt(-det_g_pert).series(epsilon, 0, order + 1).removeO()
        print("\n[Step 1/4] Computed expansion for sqrt(-g).")

        # 2. Expand scalar field and its kinetic term X
        phi_pert = self.phi_0 + epsilon * self.pi
        d_phi_pert = sp.Matrix([phi_pert.diff(c) for c in self.coords])
        
        X_expr = -sp.Rational(1, 2) * (d_phi_pert.T * g_inv_pert * d_phi_pert)[0]
        X_series = X_expr.series(epsilon, 0, order + 1).removeO()
        print("[Step 2/4] Computed expansion for kinetic term X.")

        # 3. Expand Box(phi) = g^munu * (d_mu d_nu phi - Gamma^k_munu d_k phi)
        # Term 1: g^munu * d_mu d_nu phi
        d2_phi_pert = sp.hessian(phi_pert, self.coords)
        term1_box = (g_inv_pert.multiply_elementwise(d2_phi_pert)).trace()

        # Term 2: -g^munu * Gamma^k_munu d_k phi
        # This term is O(eps^2) because Gamma is O(eps) and d_phi is O(eps)
        term2_box = 0
        if order >= 2:
            d_h = sp.MutableDenseNDimArray.zeros(4, 4, 4)
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        d_h[i, j, k] = self.h[j, k].diff(self.coords[i])
            
            chris = sp.MutableDenseNDimArray.zeros(4, 4, 4)  # This is Gamma/epsilon
            for k in range(4):
                for i in range(4):
                    for j in range(4):
                        chris_sum = 0
                        for l_idx in range(4):
                            chris_sum += sp.Rational(1, 2) * self.eta[k, l_idx] * (d_h[j, i, l_idx] + d_h[i, j, l_idx] - d_h[l_idx, i, j])
                        chris[k, i, j] = chris_sum
            
            # We only need g^munu at order 0 (eta)
            # The term is -eta^ij * (eps*chris^k_ij) * (eps*d_k pi)
            chris_contracted = 0
            d_pi = sp.Matrix([self.pi.diff(c) for c in self.coords])
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        chris_contracted += self.eta[i, j] * chris[k, i, j] * d_pi[k]
            term2_box = -epsilon**2 * chris_contracted

        Box_phi_expr = term1_box + term2_box
        Box_phi_series = Box_phi_expr.series(epsilon, 0, order + 1).removeO()
        print("[Step 3/4] Computed expansion for Box(phi).")

        # 4. Expand each Lagrangian term
        # L2 = G2(phi, X)
        G2_series = (self.G_background['G2'] +
                     self.G_background['G2p'] * (epsilon * self.pi) +
                     self.G_background['G2X'] * X_series)
        L2_density = (sqrt_g_series * G2_series).series(epsilon, 0, order + 1).removeO()

        # L3 = -G3(phi, X) * Box(phi)
        G3_series = (self.G_background['G3'] +
                     self.G_background['G3p'] * (epsilon * self.pi) +
                     self.G_background['G3X'] * X_series)
        L3_density = (-sqrt_g_series * G3_series * Box_phi_series).series(epsilon, 0, order + 1).removeO()
        
        # L4 and L5 are placeholders due to high complexity
        L4_density = sp.Integer(0)
        L5_density = sp.Integer(0)
        print("[Step 4/4] Assembled expanded Lagrangians L2 and L3.")
        print("NOTE: L4 and L5 expansions are placeholders for future work.")

        # Total Lagrangian density
        self.total_L_density_series = (L2_density + L3_density + L4_density + L5_density).expand()
        self.final_L_density = self.total_L_density_series.subs(epsilon, 1).doit().expand()

        print("\n--- Total Lagrangian Density Expanded to Order " + str(order) + " ---")
        sp.pprint(self.final_L_density)

        if order >= 2:
            self._analyze_quadratic_action()

    def _analyze_quadratic_action(self):
        """
        Extracts and analyzes the quadratic part of the action.
        """
        print("\n" + "-"*60)
        print("Analyzing Quadratic Action (Order 2)")
        print("-"*60)

        # Extract the coefficient of epsilon^2 from the full series
        quadratic_lagrangian = self.total_L_density_series.coeff(sp.Symbol('epsilon')**2)
        if quadratic_lagrangian is None:
            print("No quadratic terms found.")
            return
            
        quadratic_lagrangian = quadratic_lagrangian.expand()

        print("\n--- Quadratic Lagrangian Density L_2 ---")
        sp.pprint(quadratic_lagrangian)

        # --- Kinetic Term Analysis for Scalar Field 'pi' ---
        print("\n--- Scalar Field Kinetic Term Analysis ---")
        
        # Define the canonical kinetic term for pi
        d_pi_d_t = self.pi.diff(self.t)
        
        # We extract the coefficient of (d_t pi)^2.
        kinetic_coeff_term = d_pi_d_t**2
        Z_factor_half = quadratic_lagrangian.coeff(kinetic_coeff_term)

        print("Coefficient of (d_t pi)^2 in L_2: ")
        sp.pprint(Z_factor_half)

        # The kinetic part of the Lagrangian is L_kin = Z_pi/2 * (d_t pi)^2 + ...
        # So, Z_pi = 2 * coefficient of (d_t pi)^2
        Z_pi = (2 * Z_factor_half).simplify()
        print("\nDeduced kinetic term normalization Z_pi:")
        sp.pprint(Z_pi)

        # Consistency Check
        # The kinetic term comes from L2 = G2(phi, X).
        # To second order, L2 contains G_{2,X} * X.
        # X = -1/2 * g^munu d_mu phi d_nu phi, which at second order is
        # X = -1/2 * eta^munu (d_mu pi)(d_nu pi) = -1/2 * ((d_t pi)^2 - (d_i pi)^2).
        # So the term in the Lagrangian is G_{2,X} * (-1/2 * (d_t pi)^2).
        # The coefficient of (d_t pi)^2 is -G_{2,X}/2.
        # We defined Z_pi such that L_kin = Z_pi/2 * (d_t pi)^2.
        # Therefore, the expected Z_pi is -G_{2,X}.
        expected_Z_pi = -self.G_background['G2X']
        
        print("\nExpected Z_pi from theory (-G_{2,X} at background):")
        sp.pprint(expected_Z_pi)

        if (Z_pi - expected_Z_pi).simplify() == 0:
            print("\n[SUCCESS] Consistency Check Passed: The scalar kinetic term matches the theoretical prediction.")
        else:
            print("\n[FAILURE] Consistency Check Failed: Mismatch in scalar kinetic term.")
            print("   Calculated Z_pi: ", Z_pi)
            print("   Expected Z_pi:   ", expected_Z_pi)


if __name__ == '__main__':
    # Instantiate the pipeline
    pipeline = HorndeskiPipeline()

    # Expand the action to quadratic order to check for tree-level stability
    # This provides the kinetic terms and mass terms.
    pipeline.expand_action_minkowski(order=2)

    # The cubic and quartic terms, which can be obtained by setting order=3 or order=4,
    # would define the interaction vertices for one-loop calculations.
    # For example:
    # pipeline.expand_action_minkowski(order=3)
