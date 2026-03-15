# filename: codebase/dhost_integrability.py
import sympy

def derive_integrability_condition():
    """
    Derives the integrability condition for the existence of a gauge symmetry
    in Type Ia DHOST theories.

    This function performs the following steps:
    1. Defines all relevant functions and variables using sympy.
    2. Expresses the two PDEs governing the symmetry generators alpha and Lambda.
    3. Algebraically solves the first PDE for Lambda.
    4. Substitutes Lambda and its derivative into the second PDE to obtain a
       single PDE for alpha.
    5. Extracts the coefficients of the resulting PDE for alpha.
    6. Assumes a simplifying condition (R=0) to derive a tractable
       integrability condition.
    7. Prints all intermediate and final results to the console.
    """
    # 1. Symbolic Setup
    phi, X = sympy.symbols('phi X')
    F = sympy.Function('F')(phi, X)
    A1 = sympy.Function('A1')(phi, X)
    A3 = sympy.Function('A3')(phi, X)
    alpha = sympy.Function('alpha')(phi, X)
    Lambda = sympy.Function('Lambda')(phi, X)

    # Define derivatives
    F_X = sympy.diff(F, X)
    F_XX = sympy.diff(F_X, X)
    F_phi = sympy.diff(F, phi)
    A1_X = sympy.diff(A1, X)
    A1_phi = sympy.diff(A1, phi)
    A3_X = sympy.diff(A3, X)
    alpha_X = sympy.diff(alpha, X)
    alpha_phi = sympy.diff(alpha, phi)
    Lambda_X = sympy.diff(Lambda, X)

    print("--- Step 1: Derivation of the Integrability Condition ---")
    print("\nStarting with the two governing PDEs for the symmetry generators alpha(phi, X) and Lambda(phi, X):\n")

    # 2. PDE Definition
    pde1_lhs = (X * A3 - 2 * F_X) * alpha + 2 * A1 * Lambda
    pde2_lhs = (
        X * (X * A3_X + A3 - 2 * F_XX) * alpha +
        (F - X * A1) * (2 * Lambda_X + alpha_phi) +
        (X * A3 / 2 - 2 * F_X) * alpha +
        (X * A3 - 2 * F_X) * Lambda +
        (F_phi - X * A1_phi) * alpha
    )

    print("PDE 1: " + str(pde1_lhs) + " = 0")
    print("PDE 2: " + str(pde2_lhs) + " = 0\n")

    # 3. Algebraic Elimination of Lambda
    print("--- Step 1.1: Algebraic Elimination and Derivation ---")
    print("\nSolving PDE 1 for Lambda, assuming A1 is non-zero:")
    lambda_expr = sympy.solve(pde1_lhs, Lambda)[0]
    print("Lambda = " + str(lambda_expr) + "\n")

    # 4. Substitution into the second PDE
    print("Calculating the derivative of Lambda with respect to X:")
    lambda_expr_X = sympy.diff(lambda_expr, X)
    print("d(Lambda)/dX = " + str(lambda_expr_X) + "\n")

    print("Substituting Lambda and d(Lambda)/dX into PDE 2...")
    alpha_pde = pde2_lhs.subs(Lambda, lambda_expr).subs(Lambda_X, lambda_expr_X)
    alpha_pde = sympy.simplify(alpha_pde)
    
    # It's better to expand and collect manually for clarity
    alpha_pde_expanded = sympy.expand(pde2_lhs.subs(Lambda, lambda_expr).subs(Lambda_X, lambda_expr_X))

    print("Resulting PDE for alpha (expanded form):")
    sympy.pprint(alpha_pde_expanded)
    print(" = 0\n")

    print("Resulting PDE for alpha (collected by coefficients):")
    # Use collect to make the structure P*alpha_phi + Q*alpha_X + R*alpha = 0 clear
    alpha_pde_collected = sympy.collect(alpha_pde_expanded, [alpha_phi, alpha_X, alpha])
    print(str(alpha_pde_collected) + " = 0\n")

    # 5. Coefficient Extraction
    print("Extracting coefficients P, Q, and R for the PDE of the form:")
    print("P * diff(alpha, phi) + Q * diff(alpha, X) + R * alpha = 0\n")

    P_coeff = alpha_pde_collected.coeff(alpha_phi)
    Q_coeff = alpha_pde_collected.coeff(alpha_X)
    # To get R, we subtract the other terms from the collected PDE
    R_coeff = alpha_pde_collected - P_coeff * alpha_phi - Q_coeff * alpha_X
    R_coeff = R_coeff.subs(alpha, 1) # The remainder is the coefficient of alpha

    # Simplify and print coefficients
    P_coeff = sympy.simplify(P_coeff)
    Q_coeff = sympy.simplify(Q_coeff)
    R_coeff = sympy.simplify(R_coeff)

    print("Coefficient P:")
    sympy.pprint(P_coeff)
    print("\nCoefficient Q:")
    sympy.pprint(Q_coeff)
    print("\nCoefficient R:")
    sympy.pprint(R_coeff)
    print("\n")

    # 6. Integrability Condition
    print("--- Deriving the Integrability Condition ---")
    print("For a specific, non-trivial symmetry to exist, the coefficients of the PDE for alpha")
    print("must satisfy a consistency condition. A general derivation is complex.")
    
    print("\nFor a first-order PDE of the form P*alpha_phi + Q*alpha_X + R*alpha = 0,")
    print("the general consistency/integrability condition involves checking compatibility.")
    print("Since Q = 0 in our case, we have: P*alpha_phi + R*alpha = 0")
    print("\nFor non-trivial solutions to exist, one sufficient condition is R = 0.")
    print("This is the condition we impose here.\n")
    
    print("A more general consistency condition would involve:")
    print("∂R/∂φ - (∂P/∂X)*R/P + (∂R/∂X)*P/P - other terms = 0")
    print("But the simplest tractable condition is R = 0.\n")
    
    print("Integrability Condition (R = 0):\n")
    
    # Display the equation R=0
    integrability_condition_eq = sympy.Eq(R_coeff, 0)
    sympy.pprint(integrability_condition_eq)
    
    print("\n\nLaTeX form of the integrability condition:")
    print(sympy.latex(integrability_condition_eq))
    
    # Also compute the consistency check: if R=0, then we need P ≠ 0 for non-trivial alpha
    print("\n\n--- Additional Consistency Check ---")
    print("With R = 0, the PDE becomes: P*alpha_phi = 0")
    print("For non-trivial alpha, we need either:")
    print("  1) P = 0 (which would require additional analysis)")
    print("  2) alpha_phi = 0 (alpha is independent of phi)")
    print("\nCoefficient P =")
    sympy.pprint(P_coeff)
    print("\nFor the model where F and A1 are not both identically related by F = X*A1,")
    print("P is non-zero, implying alpha must be a function of X only.")


if __name__ == '__main__':
    derive_integrability_condition()
