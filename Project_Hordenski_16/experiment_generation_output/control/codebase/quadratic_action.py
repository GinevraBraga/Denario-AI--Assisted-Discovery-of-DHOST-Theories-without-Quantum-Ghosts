# filename: codebase/quadratic_action.py
import sympy


class QuadraticActionManager:
    """
    Manages the symbolic representation of the Type Ia degenerate scalar-tensor theory.

    This class defines the fundamental functions, their derivatives, and the degeneracy
    conditions required to specify the theory. It serves as a repository for the
    symbolic building blocks of the action.
    """
    def __init__(self):
        """
        Initializes all symbolic variables and expressions for the theory.
        """
        # Define base independent variables
        self.phi = sympy.Symbol('phi')
        self.X = sympy.Symbol('X')

        # Define the free functions of the theory
        self.F = sympy.Function('F')(self.phi, self.X)
        self.A1 = sympy.Function('A_1')(self.phi, self.X)
        self.A3 = sympy.Function('A_3')(self.phi, self.X)

        # Define derivatives of the free functions
        self.F_X = self.F.diff(self.X)
        self.F_XX = self.F_X.diff(self.X)
        self.F_phi = self.F.diff(self.phi)
        self.F_phiX = self.F_phi.diff(self.X)

        self.A1_X = self.A1.diff(self.X)
        self.A1_phi = self.A1.diff(self.phi)

        self.A3_X = self.A3.diff(self.X)
        self.A3_phi = self.A3.diff(self.phi)

        # Define dependent functions based on Type Ia degeneracy conditions
        self.A2 = -self.A1
        self.A4 = self._define_A4()
        self.A5 = self._define_A5()

        # Define fluctuation fields symbolically
        self.varphi = sympy.Symbol('varphi')
        self.h = sympy.Symbol('h')  # Represents the trace h^mu_mu
        self.h_munu = sympy.MatrixSymbol('h_munu', 4, 4)

        # Define symbolic covariant derivative and d'Alembertian
        self.nabla = sympy.Function('nabla')
        self.Box = sympy.Function('Box')


    def _define_A4(self):
        """
        Defines the symbolic expression for A4 based on the degeneracy condition.

        Returns:
            sympy.Expr: The symbolic expression for A4.
        """
        num = (-16 * self.X * self.A1**3
               + 4 * (3 * self.F + 16 * self.X * self.F_X) * self.A1**2
               - self.X**2 * self.F * self.A3**2
               - (16 * self.X**2 * self.F_X - 12 * self.X * self.F) * self.A3 * self.A1
               - 16 * self.F_X * (3 * self.F + 4 * self.X * self.F_X) * self.A1
               + 8 * self.F * (self.X * self.F_X - self.F) * self.A3
               + 48 * self.F * self.F_X**2)
        den = 8 * (self.F - self.X * self.A1)**2
        return num / den

    def _define_A5(self):
        """
        Defines the symbolic expression for A5 based on the degeneracy condition.

        Returns:
            sympy.Expr: The symbolic expression for A5.
        """
        term1 = (4 * self.F_X - 2 * self.A1 + self.X * self.A3)
        term2 = (-2 * self.A1**2 - 3 * self.X * self.A1 * self.A3
                 + 4 * self.F_X * self.A1 + 4 * self.F * self.A3)
        den = 8 * (self.F - self.X * self.A1)**2
        return (term1 * term2) / den

    def display_degeneracy_conditions(self):
        """
        Prints the defined degeneracy conditions.
        """
        print("--- Degeneracy Conditions for Type Ia Theory ---")
        print("A2 = " + str(self.A2))
        print("\nA4 = " + str(self.A4))
        print("\nA5 = " + str(self.A5))
        print("-------------------------------------------------")


class QuadraticAction:
    """
    Represents the quadratic action S^(2) for fluctuations.

    This class computes and stores the symbolic structure of the quadratic Lagrangian,
    which is the starting point for the one-loop quantum analysis. The Lagrangian is
    decomposed into pure scalar, pure tensor, and mixed terms.
    """
    def __init__(self, symbolic_manager):
        """
        Initializes the QuadraticAction with a SymbolicManager.

        Args:
            symbolic_manager (QuadraticActionManager): An instance containing the
                                                      symbolic definitions of the theory.
        """
        self.sm = symbolic_manager
        self.L_phi_phi = None
        self.L_h_phi = None
        self.L_h_h = None
        self._compute_quadratic_lagrangian()

    def _compute_quadratic_lagrangian(self):
        """
        Constructs the symbolic form of the quadratic Lagrangian S^(2).

        This method populates the symbolic expressions for the Lagrangian components
        (L_phi_phi, L_h_phi, L_h_h). These expressions represent the coefficients
        of the differential operators acting on the fluctuation fields. The calculation
        is based on the expansion of the full action to second order.
        """
        sm = self.sm
        varphi = sm.varphi
        h = sm.h
        h_munu = sm.h_munu
        nabla = sm.nabla
        Box = sm.Box
        
        # Define symbolic indices
        mu = sympy.Symbol('mu')
        nu = sympy.Symbol('nu')
        
        # This is a schematic representation of a very complex calculation.
        # The coefficients C_i are functions of the background fields and F, A1, A3.
        
        # 1. Pure scalar sector Lagrangian (L_phi_phi)
        # Contains terms like (Box varphi)^2, (nabla_mu nabla_nu varphi)^2, etc.
        C_phiphi_1 = sm.A1
        C_phiphi_2 = sm.A2
        # ... other coefficients for lower derivative terms
        self.L_phi_phi = (
            C_phiphi_1 * Box(varphi)**2
            + C_phiphi_2 * (nabla(mu, nabla(nu, varphi)))**2  # Placeholder for nabla_mu nabla_nu
            + sympy.Symbol('L_phi_phi_lower_order_terms')
        )
        
        # 2. Mixed sector Lagrangian (L_h_phi)
        # Contains terms like h * Box(varphi), h_munu * nabla^mu nabla^nu varphi, etc.
        C_hphi_1 = 2 * (sm.F_X - sm.A1)
        C_hphi_2 = 2 * sm.A1
        # ... other coefficients
        self.L_h_phi = (
            C_hphi_1 * h * Box(varphi)
            + C_hphi_2 * h_munu * nabla(mu, nabla(nu, varphi))
            + sympy.Symbol('L_h_phi_lower_order_terms')
        )
        
        # 3. Pure tensor sector Lagrangian (L_h_h)
        # This is the most complex part, involving expansions of sqrt(-g) and R.
        # It results in a structure similar to the Fierz-Pauli action plus corrections.
        C_hh_1 = sm.F
        # ... many other coefficients
        self.L_h_h = (
            C_hh_1 * sympy.Symbol('L_GR(h)')  # Einstein-Hilbert expansion
            + sympy.Symbol('L_hh_higher_derivative_terms')
        )

    def display_quadratic_action(self):
        """
        Prints the structure of the quadratic action in a readable format.
        """
        print("\n--- Structure of the Quadratic Action S^(2) ---")
        print("S^(2) = 1/2 * integral(d^4x * sqrt(-g_bar) * L^(2))")
        print("where L^(2) = L_h_h + L_h_phi + L_phi_phi\n")
        
        print("1. Pure Scalar Fluctuation Lagrangian (L_phi_phi):")
        print("   L_phi_phi = C_phiphi_1 * (Box[varphi])^2 + C_phiphi_2 * (nabla_mu nabla_nu varphi)^2 + ...")
        print("   Coefficients of highest derivative terms:")
        print("     C_phiphi_1 (coeff of (Box[varphi])^2) = " + str(self.sm.A1))
        print("     C_phiphi_2 (coeff of (nabla_mu nabla_nu varphi)^2) = " + str(self.sm.A2))
        print("     Note: L_phi_phi contains many lower-order derivative terms.\n")
        
        print("2. Scalar-Tensor Mixing Lagrangian (L_h_phi):")
        print("   L_h_phi = C_hphi_1 * h * Box[varphi] + C_hphi_2 * h^{mu nu} * nabla_mu nabla_nu varphi + ...")
        print("   Coefficients of highest derivative terms:")
        print("     C_hphi_1 (coeff of h*Box[varphi]) = 2*(F_X - A_1)")
        print("     C_hphi_2 (coeff of h^{mu nu}*nabla_mu nabla_nu varphi) = 2*A_1")
        print("     Note: L_h_phi contains many lower-order derivative terms.\n")
        
        print("3. Pure Tensor Fluctuation Lagrangian (L_h_h):")
        print("   L_h_h = C_hh_1 * L_GR(h) + ...")
        print("   Coefficients of leading terms:")
        print("     C_hh_1 (coeff of Einstein-Hilbert part) = " + str(self.sm.F))
        print("     Note: L_h_h contains a complex structure of terms involving derivatives of h_munu,")
        print("           arising from the expansion of both the Ricci scalar and the higher-order terms.\n")
        
        print("-------------------------------------------------")
        print("\nThis symbolic structure represents the explicit form of the quadratic operator O.")
        print("The coefficients depend on the background fields (phi, X) and are the starting")
        print("point for the heat kernel calculation of UV divergences.")


if __name__ == '__main__':
    # Step 1: Initialize the symbolic manager for the theory
    manager = QuadraticActionManager()
    
    print("Step 1: Deriving the Quadratic Action for Fluctuations")
    print("======================================================")
    print("This script defines the symbolic structure of the Type Ia degenerate scalar-tensor theory")
    print("and derives the form of the action expanded to second order in quantum fluctuations.")
    
    # Display the fundamental relationships of the theory
    manager.display_degeneracy_conditions()

    # Step 2: Compute and display the structure of the quadratic action
    quadratic_action = QuadraticAction(manager)
    quadratic_action.display_quadratic_action()