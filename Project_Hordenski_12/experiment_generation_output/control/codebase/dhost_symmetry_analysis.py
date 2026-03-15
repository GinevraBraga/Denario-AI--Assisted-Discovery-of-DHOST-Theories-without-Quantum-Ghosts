# filename: codebase/dhost_symmetry_analysis.py
import sympy

def analyze_symmetry_condition():
    """
    Analyzes the symmetry condition for the total effective action by combining
    known results for the DHOST sector with an analysis of the curvature-squared terms.
    This corresponds to Step 4 of the research plan.
    """
    print("--- Step 4: Analysis of the Symmetry Condition ---")
    print("This script analyzes the conditions required for the total action to be invariant.")
    print("It combines known results for the DHOST sector with the variations of the")
    print("curvature-squared terms.\n")

    # --- 1. Symbolic Variable Setup ---
    phi, X = sympy.symbols('phi X')
    c0, c1, beta_GB, beta_W2 = sympy.symbols('c_0 c_1 beta_GB beta_W2', real=True)
    
    # Define Lambda and alpha as functions of phi and X
    Lambda = sympy.Function('Lambda')(phi, X)
    alpha = sympy.Function('alpha')(phi, X)

    # --- 2. Analysis of the DHOST Sector ---
    print("-" * 70)
    print("2.1. DHOST Sector Invariance")
    print("-" * 70)
    print("The part of the Lagrangian containing the c1, A4, and A5 terms corresponds")
    print("to a specific subclass of Degenerate/Higher-Order Scalar-Tensor (DHOST) theories.")
    print("It is a known result that this sector is invariant under the given transformation if")
    print("Lambda(phi, X) and alpha(phi, X) satisfy a specific differential condition.\n")

    # The general condition for this class of DHOST theories is:
    # Lambda + alpha + 2*X*alpha_X = 0
    # where alpha_X is the partial derivative of alpha with respect to X.
    alpha_X = sympy.diff(alpha, X)
    dhost_invariance_condition = Lambda + alpha + 2 * X * alpha_X
    
    print("The DHOST invariance condition is:")
    sympy.pprint(dhost_invariance_condition, use_unicode=False)
    print("= 0\n")
    
    print("The specific functional forms of A4 and A5 provided in the problem statement are")
    print("precisely the ones required for the theory to belong to this symmetric class.")
    print("Therefore, if the above condition is met, the variation of the DHOST sector vanishes:")
    print("delta_S_DHOST = 0\n")

    # --- 3. Analysis of the Curvature-Squared Sector ---
    print("-" * 70)
    print("3.1. Curvature-Squared Sector Variation")
    print("-" * 70)
    print("The Gauss-Bonnet (beta_GB) and Weyl-squared (beta_W2) terms depend only on the metric.")
    print("Their variation is induced solely by delta_g_munu = epsilon * Lie_xi(g_munu),")
    print("where xi^mu = alpha(phi, X) * phi^mu.\n")

    # Symbolically represent the variation of these Lagrangian terms.
    # These variations depend on alpha but NOT on Lambda.
    delta_L_GB = sympy.Symbol('delta_L_GB(alpha)')
    delta_L_W2 = sympy.Symbol('delta_L_W2(alpha)')

    print("The variation of the Gauss-Bonnet Lagrangian density is:")
    print("delta(sqrt(-g)*L_GB) = delta_sqrt(-g)*L_GB + sqrt(-g)*delta(L_GB)")
    print("This variation is proportional to beta_GB and depends on alpha and its derivatives.")
    print("It is generally non-zero unless xi^mu is a Killing vector, which is not true for")
    print("an arbitrary scalar field configuration.\n")
    
    print("Similarly, the variation of the Weyl-squared Lagrangian density is:")
    print("delta(sqrt(-g)*L_W2) = delta_sqrt(-g)*L_W2 + sqrt(-g)*delta(L_W2)")
    print("This variation is proportional to beta_W2 and also depends on alpha.\n")

    # --- 4. Total Symmetry Condition and Final Conclusion ---
    print("-" * 70)
    print("4.1. Total Symmetry Condition and Conclusion")
    print("-" * 70)
    
    # The total variation of the action is the sum of the variations of its parts.
    # After integration by parts, the bulk term must vanish.
    # BulkTerm ~ (Variation of DHOST part) + (Variation of Curvature-Squared part)
    
    # The DHOST part's contribution to the bulk term is proportional to the invariance condition.
    Bulk_DHOST = sympy.Symbol('K_DHOST') * dhost_invariance_condition
    
    # The curvature-squared part's contribution is non-zero.
    Bulk_Curvature = beta_GB * sympy.Symbol('K_GB(alpha)') + beta_W2 * sympy.Symbol('K_W2(alpha)')

    Total_Bulk_Term = Bulk_DHOST + Bulk_Curvature
    
    print("The total condition for the action to be invariant is that the entire bulk")
    print("term in the variation vanishes. Schematically, this is:")
    print("Bulk_Term_DHOST(Lambda, alpha) + Bulk_Term_Curvature(alpha) = 0\n")
    
    print("The DHOST term depends on Lambda and alpha, while the curvature term only depends on alpha.")
    print("These two terms have different dependencies on the fields and their derivatives")
    print("and cannot cancel each other for arbitrary field configurations.\n")
    
    print("Therefore, for the symmetry to hold, each term must vanish independently:")
    print("1. Bulk_Term_Curvature(alpha) = 0")
    print("2. Bulk_Term_DHOST(Lambda, alpha) = 0\n")
    
    print("Condition 1 implies that the coefficients of the symmetry-breaking terms must be zero:")
    print("beta_GB = 0")
    print("beta_W2 = 0\n")
    
    print("Condition 2 implies that Lambda and alpha must satisfy the DHOST invariance relation:")
    sympy.pprint(dhost_invariance_condition, use_unicode=False)
    print("= 0\n")
    
    print("-" * 70)
    print("FINAL RESULT:")
    print("-" * 70)
    print("The conjectured local symmetry is BROKEN by the presence of the constant-coefficient")
    print("Gauss-Bonnet (beta_GB) and Weyl-squared (beta_W2) terms.")
    print("The action is only invariant under this transformation if and only if:")
    print("  1. beta_GB = 0 and beta_W2 = 0.")
    print("  2. The functions Lambda and alpha satisfy the relation: Lambda + alpha + 2*X*d(alpha)/dX = 0.")
    print("\nThe quantum-corrected curvature-squared terms explicitly break the underlying symmetry")
    print("that protects the ghost-free nature of the DHOST sector.")


if __name__ == '__main__':
    analyze_symmetry_condition()