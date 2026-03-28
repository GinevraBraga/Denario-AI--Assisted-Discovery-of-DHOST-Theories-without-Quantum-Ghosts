# filename: codebase/beta_function_extraction.py
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
        
        # Define the functions that are constrained by the degeneracy conditions
        self.A4 = sympy.Function('A_4')(self.phi, self.X)
        self.A5 = sympy.Function('A_5')(self.phi, self.X)

        # Define the explicit solutions for A4 and A5 from the degeneracy conditions
        self.A4_sol = self._define_A4_sol()
        self.A5_sol = self._define_A5_sol()

    def _define_A4_sol(self):
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

    def _define_A5_sol(self):
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


class RGFlowAnalysis:
    """
    Performs the symbolic analysis of the Renormalization Group (RG) flow.

    This class extracts the beta-functionals and computes the RG flow of the
    degeneracy constraints to test the quantum stability of the theory.
    """
    def __init__(self, symbolic_manager):
        """
        Initializes the RG flow analysis.

        Args:
            symbolic_manager (QuadraticActionManager): An instance with the theory's definitions.
        """
        self.sm = symbolic_manager
        self.phi = self.sm.phi
        self.X = self.sm.X

        # Define symbolic beta-functionals for all functions
        self.beta_F = sympy.Function('beta_F')(self.phi, self.X)
        self.beta_A1 = sympy.Function('beta_A1')(self.phi, self.X)
        self.beta_A3 = sympy.Function('beta_A3')(self.phi, self.X)
        self.beta_A4 = sympy.Function('beta_A4')(self.phi, self.X)
        self.beta_A5 = sympy.Function('beta_A5')(self.phi, self.X)
        
        # Beta-functional for the derivative F_X
        self.beta_F_X = self.beta_F.diff(self.X)

        # Define the degeneracy constraints
        self.C4 = self.sm.A4 - self.sm.A4_sol
        self.C5 = self.sm.A5 - self.sm.A5_sol
        
        # Compute the RG flow of the constraints
        self.dC4_dt = None
        self.dC5_dt = None
        self._compute_constraint_flow()

    def _apply_rg_operator(self, expr):
        """
        Applies the RG operator mu*d/dmu to a symbolic expression.
        This is equivalent to applying the chain rule with beta-functionals.
        
        Args:
            expr (sympy.Expr): The expression to differentiate.

        Returns:
            sympy.Expr: The result of applying the RG operator.
        """
        # List of functions the expression might depend on
        func_list = [self.sm.F, self.sm.A1, self.sm.A3, self.sm.F_X]
        # Corresponding beta-functionals
        beta_list = [self.beta_F, self.beta_A1, self.beta_A3, self.beta_F_X]
        
        rg_derivative = sympy.S(0)
        for func, beta in zip(func_list, beta_list):
            if expr.has(func):
                rg_derivative += expr.diff(func) * beta
        
        return rg_derivative

    def _compute_constraint_flow(self):
        """
        Computes the RG flow of the degeneracy constraints C4 and C5.
        The flow is given by mu * dC/dmu.
        """
        # Flow of C4: d(C4)/dt = d(A4)/dt - d(A4_sol)/dt
        # d(A4)/dt is beta_A4
        # d(A4_sol)/dt is computed using the chain rule via _apply_rg_operator
        flow_A4_sol = self._apply_rg_operator(self.sm.A4_sol)
        self.dC4_dt = self.beta_A4 - flow_A4_sol

        # Flow of C5: d(C5)/dt = d(A5)/dt - d(A5_sol)/dt
        flow_A5_sol = self._apply_rg_operator(self.sm.A5_sol)
        self.dC5_dt = self.beta_A5 - flow_A5_sol

    def display_results(self):
        """
        Prints the results of the RG flow analysis in a structured format.
        """
        sympy.init_printing(use_unicode=False, wrap_line=False)
        print("\n--- Step 4: Extraction of Beta-Functionals and RG Flow of Constraints ---")
        print("========================================================================")
        
        print("\n1. Matching Counter-Terms to Beta-Functionals:")
        print("The one-loop counter-term Lagrangian L_ct is matched to the original action.")
        print("L_ct = delta_F * R + delta_A1 * (...) + ...")
        print("The beta-functional for a function 'f' is beta_f = mu * df/dmu, which is")
        print("proportional to the counter-term delta_f computed from the heat kernel.")
        print("We define the following symbolic beta-functionals:")
        print("  beta_F, beta_A1, beta_A3, beta_A4, beta_A5")

        print("\n2. RG Flow of Degeneracy Constraints:")
        print("For the theory to be quantum-stable, the RG flow must be tangent to the")
        print("degeneracy manifold. This requires mu*dC_k/dmu = 0 on the manifold.")
        print("We compute this for the constraints C4 and C5.")

        print("\n--- Stability Condition for Constraint C4 ---")
        print("mu * dC4/dmu = beta_A4 - (d(A4_sol)/dF * beta_F + d(A4_sol)/dA1 * beta_A1 + ...)")
        print("\nResulting equation that must be zero for stability:")
        sympy.pprint(self.dC4_dt, use_unicode=False)
        
        print("\n--- Stability Condition for Constraint C5 ---")
        print("mu * dC5/dmu = beta_A5 - (d(A5_sol)/dF * beta_F + d(A5_sol)/dA1 * beta_A1 + ...)")
        print("\nResulting equation that must be zero for stability:")
        sympy.pprint(self.dC5_dt, use_unicode=False)

        print("\n--- Interpretation ---")
        print("The expressions above define the conditions for quantum stability.")
        print("If these expressions cannot be shown to be identically zero for any arbitrary")
        print("choice of F, A1, A3, it implies that the RG flow will, in general, drive")
        print("the theory off the degeneracy manifold.")
        print("This would mean that the Ostrogradsky ghost is reintroduced by quantum corrections,")
        print("rendering the classical theory an unstable fine-tuning.")
        print("The next step is to analyze these conditions to determine if a non-tangential")
        print("flow is inevitable.")
        print("--------------------------------------------------------------------------")


if __name__ == '__main__':
    print("Step 4: Analyzing the Renormalization Group Flow of Degeneracy Constraints")
    
    # Initialize the symbolic manager for the theory
    manager = QuadraticActionManager()
    
    # Perform the RG flow analysis
    rg_analyzer = RGFlowAnalysis(manager)
    
    # Display the results
    rg_analyzer.display_results()
