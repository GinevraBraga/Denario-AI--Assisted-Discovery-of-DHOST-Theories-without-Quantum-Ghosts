# filename: codebase/heat_kernel_computation.py
import sympy

class HeatKernelCalculator:
    """
    Manages the symbolic computation of the one-loop UV divergences.

    This class implements the heat kernel (Schwinger-DeWitt) method to derive the
    Seeley-DeWitt a2 coefficient and the resulting counter-term Lagrangian, L_ct.
    The calculation is performed schematically, representing the complex operators
    and their components with symbolic placeholders to outline the methodology.
    """

    def __init__(self):
        """
        Initializes the calculator, defines symbols, and runs the computation.
        """
        self._define_symbols()
        self._define_operators_schematically()
        self._compute_a2_coefficients()
        self._compute_counter_term_lagrangian()

    def _define_symbols(self):
        """
        Defines all necessary symbolic variables for the heat kernel calculation.
        """
        # --- Fundamental Spacetime and Field Symbols ---
        self.g_munu = sympy.Symbol('g_munu')
        self.R = sympy.Symbol('R')
        self.R_munu = sympy.Symbol('R_munu')
        self.R_munusigma = sympy.Symbol('R_munusigma')
        self.nabla = sympy.Function('nabla')
        self.Box = sympy.Symbol('Box') # Using a symbol for the operator itself

        # --- Field and Ghost Multiplets ---
        # Represents the collection of fields (h_munu, varphi)
        self.Psi = sympy.Symbol('Psi')
        # Represents the collection of ghosts (c_mu, c_s)
        self.C = sympy.Symbol('C')

        # --- Operator Components in Standard Form D = Box*1 + 2W^mu*nabla_mu + Pi ---
        # For the physical fields + metric
        self.W_mu_fields = sympy.Symbol('W_mu_fields')
        self.Pi_fields = sympy.Symbol('Pi_fields')
        self.Omega_munu_fields = sympy.Symbol('Omega_munu_fields') # Field-space curvature

        # For the ghost fields
        self.W_mu_ghosts = sympy.Symbol('W_mu_ghosts')
        self.Pi_ghosts = sympy.Symbol('Pi_ghosts')
        self.Omega_munu_ghosts = sympy.Symbol('Omega_munu_ghosts') # Ghost field-space curvature

        # --- a2 Coefficients and Counter-term Lagrangian ---
        self.a2_fields = None
        self.a2_ghosts = None
        self.L_ct = None
        
        # --- Identity matrix in field space ---
        self.I = sympy.Symbol('I')

    def _define_operators_schematically(self):
        """
        Defines the schematic structure of the kinetic operators.

        The full kinetic operators for fields (O_gf) and ghosts (M_ghost) are assumed
        to be brought into the standard form for the heat kernel expansion:
        D = g^{ab} nabla_a nabla_b * I + 2W^a nabla_a + Pi.

        Here, we symbolically define the W and Pi matrices, which are derived from
        the quadratic and ghost Lagrangians of the previous steps. They are complex
        matrices in the space of fields and contain derivatives of background fields.
        """
        # The field-space curvature Omega_munu is defined as:
        # Omega_munu = [nabla_mu + W_mu, nabla_nu + W_nu]
        # We represent it symbolically.
        self.Omega_munu_fields = sympy.Symbol('Omega_munu(W_fields)')
        self.Omega_munu_ghosts = sympy.Symbol('Omega_munu(W_ghosts)')
        
        print("Schematic Operator Definitions:")
        print("Field Operator D_fields = Box*I + 2*W_mu_fields*nabla^mu + Pi_fields")
        print("Ghost Operator D_ghosts = Box*I + 2*W_mu_ghosts*nabla^mu + Pi_ghosts")
        print("Where W and Pi are matrices in field space derived from S^(2)_gf and S_ghost.")
        print("--------------------")


    def _compute_a2_coefficients(self):
        """
        Computes the symbolic form of the Seeley-DeWitt a2 coefficients.
        """
        # General formula for the a2 coefficient trace
        # a2 = (1/180)*(R_munusigma^2 - R_munu^2)*I + (1/2)*Pi^2 + (1/12)*Omega_munu^2
        # The terms with covariant derivatives of Omega and Pi are total derivatives
        # and do not contribute to the beta functions, so they are often omitted
        # when calculating counter-terms for renormalization. We include them for completeness.
        
        # a2 for fields
        term1_f = sympy.Rational(1, 180) * (self.R_munusigma**2 - self.R_munu**2) * self.I
        term2_f = sympy.Rational(1, 2) * self.Pi_fields**2
        term3_f = sympy.Rational(1, 12) * self.Omega_munu_fields**2
        term4_f = sympy.Rational(1, 6) * self.nabla(self.nabla(self.Pi_fields))  # Represents Box(Pi)
        
        self.a2_fields = term1_f + term2_f + term3_f + term4_f

        # a2 for ghosts
        term1_g = sympy.Rational(1, 180) * (self.R_munusigma**2 - self.R_munu**2) * self.I
        term2_g = sympy.Rational(1, 2) * self.Pi_ghosts**2
        term3_g = sympy.Rational(1, 12) * self.Omega_munu_ghosts**2
        term4_g = sympy.Rational(1, 6) * self.nabla(self.nabla(self.Pi_ghosts))  # Represents Box(Pi)

        self.a2_ghosts = term1_g + term2_g + term3_g + term4_g

    def _compute_counter_term_lagrangian(self):
        """
        Computes the one-loop counter-term Lagrangian L_ct from the a2 coefficients.
        L_ct = (1 / (16*pi^2)) * (Tr(a2_fields) - 2*Tr(a2_ghosts))
        The factor of 2 for ghosts comes from them being complex scalars (or vectors).
        The 1/epsilon pole from dimensional regularization is conventionally absorbed
        into the definition of the beta function.
        """
        
        # The trace 'Tr' is over the indices of the field multiplets.
        self.Tr_a2_fields_expr = sympy.Function('Tr')(self.a2_fields)
        self.Tr_a2_ghosts_expr = sympy.Function('Tr')(self.a2_ghosts)

        # The counter-term Lagrangian
        # The overall constant factor is often denoted as 'Pole'
        Pole = sympy.Symbol('1/(16*pi**2 * epsilon)')
        
        self.L_ct = Pole * (self.Tr_a2_fields_expr - 2 * self.Tr_a2_ghosts_expr)

    def display_results(self):
        """
        Prints the results of the heat kernel calculation in a structured format.
        """
        print("\n--- Step 3: Heat Kernel Calculation of UV Divergences ---")
        print("=========================================================")
        
        print("\n1. Standard Heat Kernel Formula for a2 coefficient:")
        print("   a2 = (1/180)*(R_munusigma^2 - R_munu^2)*I + (1/2)*Pi^2 + (1/12)*Omega_munu^2 + (1/6)*Box(Pi) + ...")
        print("   where Omega_munu = [nabla_mu + W_mu, nabla_nu + W_nu] is the field-space curvature.")
        
        print("\n2. Symbolic a2 Coefficients:")
        print("   a2_fields = " + str(self.a2_fields))
        print("   a2_ghosts = " + str(self.a2_ghosts))
        
        print("\n3. One-Loop Divergent Action Gamma^(1)_div:")
        print("   Gamma^(1)_div = integral(d^4x * sqrt(-g) * L_ct)")
        print("   where L_ct = (1 / (16*pi^2 * epsilon)) * (Tr(a2_fields) - 2*Tr(a2_ghosts))")
        
        print("\n4. Explicit Counter-Term Lagrangian L_ct:")
        print("   L_ct = " + str(self.L_ct))
        
        print("\n   Breaking down the trace terms:")
        print("   Tr(a2_fields) = " + str(self.Tr_a2_fields_expr))
        print("   Tr(a2_ghosts) = " + str(self.Tr_a2_ghosts_expr))
        
        print("\n--- Interpretation ---")
        print("The expression for L_ct is the central result of this step.")
        print("It is a local Lagrangian constructed from the background fields (g_munu, phi).")
        print("It contains terms like R^2, R_munu^2, R_munusigma^2, Box(R), etc., as well as")
        print("terms involving the scalar field, like (nabla_mu phi)^4, R*(nabla phi)^2, etc.")
        print("The coefficients of these terms are functions of F, A1, A3 and their derivatives.")
        print("In the next step, L_ct will be matched against the original action to extract")
        print("the beta-functionals for F, A1, and A3.")
        print("---------------------------------------------------------")


if __name__ == '__main__':
    print("Step 3: Computing the One-Loop Effective Action and Extracting UV Divergences")
    print("This script outlines the symbolic application of the heat kernel method")
    print("to find the one-loop counter-term Lagrangian L_ct.")
    
    calculator = HeatKernelCalculator()
    calculator.display_results()