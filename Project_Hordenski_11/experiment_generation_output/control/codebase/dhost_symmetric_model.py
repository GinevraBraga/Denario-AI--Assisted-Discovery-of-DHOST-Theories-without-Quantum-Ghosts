# filename: codebase/dhost_symmetric_model.py
import sympy

def find_symmetric_model():
    """
    Finds a simple, explicit symmetric model and its corresponding symmetry generators.

    This function follows these steps:
    1.  Defines symbolic variables and functions for F, A1, A3, alpha, and Lambda.
    2.  Imposes a simplifying ansatz where F, A1, and A3 are functions of phi only.
    3.  Derives the coefficient 'R' from the PDE for alpha under this ansatz.
    4.  Solves the integrability condition R=0 by treating it as a polynomial in X
        and setting the coefficients of powers of X to zero.
    5.  Identifies the resulting simple model where F and A1 are constants and A3 is zero.
    6.  Solves for the symmetry generators alpha and Lambda for this specific model.
    7.  Prints all steps, assumptions, and the final results.
    """
    print("--- Step 2: Find a Simple, Explicit Symmetric Model ---")

    # 1. Symbolic Setup
    phi, X = sympy.symbols('phi X')
    c0, c1, alpha0 = sympy.symbols('c0 c1 alpha0')

    # General functions of phi
    F_phi = sympy.Function('F')(phi)
    A1_phi = sympy.Function('A1')(phi)
    A3_phi = sympy.Function('A3')(phi)

    # Derivatives wrt phi
    F_phi_d = sympy.diff(F_phi, phi)
    A1_phi_d = sympy.diff(A1_phi, phi)

    print("\n--- Step 2.1: Proposing a Simplifying Ansatz ---")
    print("To find a simple model, we assume the free functions depend only on phi:")
    print("F = F(phi), A1 = A1(phi), A3 = A3(phi)")
    print("This implies that all partial derivatives with respect to X are zero:")
    print("F_X = 0, F_XX = 0, A1_X = 0, A3_X = 0\n")
    print("This ansatz is physically motivated as it represents a class of theories where")
    print("the couplings of higher-order terms depend on the scalar field's value, not its kinetic energy.\n")

    print("--- Step 2.2: Applying the Integrability Condition (R=0) ---")
    print("The PDE for the generator alpha is of the form: P*alpha_phi + Q*alpha_X + R*alpha = 0.")
    print("We impose the integrability condition R = 0 to find a symmetric subclass.")
    
    # Derivation of R under the phi-only ansatz
    # R = 5/2*X*A3 - F*A3/A1 - X**2*A3**2/(2*A1) + F_phi - X*A1_phi
    R_coeff = (sympy.Rational(5, 2) * X * A3_phi - F_phi * A3_phi / A1_phi -
               X**2 * A3_phi**2 / (2 * A1_phi) + F_phi_d - X * A1_phi_d)

    print("\nFor the chosen ansatz, the coefficient R is:")
    sympy.pprint(R_coeff)
    
    print("\nSetting R = 0. This equation must hold for all X.")
    print("We can therefore set the coefficient of each power of X to zero.\n")

    # 2. Solve R=0 by powers of X
    R_poly = sympy.Poly(R_coeff, X)
    coeffs = R_poly.all_coeffs()

    # Coeff of X^2
    coeff_X2 = coeffs[0]
    print("Coefficient of X^2:")
    sympy.pprint(sympy.Eq(coeff_X2, 0))
    print("Assuming A1 is non-zero, this implies A3(phi) = 0.\n")
    
    # With A3 = 0, R simplifies
    R_simplified = R_coeff.subs(A3_phi, 0)
    
    # Coeff of X^1
    R_poly_simp = sympy.Poly(R_simplified, X)
    coeffs_simp = R_poly_simp.all_coeffs()
    coeff_X1 = coeffs_simp[0]
    print("With A3=0, the coefficient of X^1 is:")
    sympy.pprint(sympy.Eq(coeff_X1, 0))
    print("This implies that A1(phi) must be a constant.\n")
    
    # Coeff of X^0
    coeff_X0 = coeffs_simp[1]
    print("The constant term (X^0) is:")
    sympy.pprint(sympy.Eq(coeff_X0, 0))
    print("This implies that F(phi) must be a constant.\n")

    # 3. The resulting simple model
    print("--- Step 2.3: The Identified Symmetric Model ---")
    print("The integrability condition R=0 for the phi-only ansatz leads to the following simple model:")
    print("F(phi, X) = c0 (constant)")
    print("A1(phi, X) = c1 (constant, non-zero)")
    print("A3(phi, X) = 0\n")

    # 4. Determine the symmetry generators for this model
    print("--- Step 2.4: Determining the Symmetry Generators ---")
    print("We now solve the original PDEs for alpha and Lambda using this specific model.")
    
    F_model, A1_model, A3_model = c0, c1, 0
    alpha = sympy.Function('alpha')(phi, X)
    Lambda = sympy.Function('Lambda')(phi, X)

    # The two original PDEs
    pde1 = (X * A3_model - 2 * sympy.diff(F_model, X)) * alpha + 2 * A1_model * Lambda
    
    # The second PDE simplifies significantly
    # All derivatives of the constant functions are zero
    pde2_term1 = X * (X * sympy.diff(A3_model, X) + A3_model - 2 * sympy.diff(F_model, X, 2)) * alpha
    pde2_term2 = (F_model - X * A1_model) * (2 * sympy.diff(Lambda, X) + sympy.diff(alpha, phi))
    pde2_term3 = (X * A3_model / 2 - 2 * sympy.diff(F_model, X)) * alpha
    pde2_term4 = (X * A3_model - 2 * sympy.diff(F_model, X)) * Lambda
    pde2_term5 = (sympy.diff(F_model, phi) - X * sympy.diff(A1_model, phi)) * alpha
    pde2 = pde2_term1 + pde2_term2 + pde2_term3 + pde2_term4 + pde2_term5

    print("\nOriginal PDE 1 with the model substituted:")
    print(str(pde1) + " = 0")
    solution_pde1 = sympy.solve(pde1, Lambda)
    print("Solving for Lambda gives: Lambda = " + str(solution_pde1[0]))
    
    print("\nOriginal PDE 2 with the model substituted:")
    print(str(pde2) + " = 0")
    print("Since Lambda = 0, this simplifies to:")
    pde2_simplified = pde2.subs(Lambda, 0)
    print(str(pde2_simplified) + " = 0")
    print("Given that (c0 - c1*X) is not identically zero, this implies diff(alpha, phi) = 0.")
    print("Therefore, alpha must be a function of X only: alpha = alpha(X).\n")
    
    print("The simplest non-trivial choice for alpha(X) is a constant.")

    print("\n--- Summary of Results for Step 2 ---")
    print("A simple, non-trivial symmetric model satisfying the Type Ia DHOST conditions is found:")
    print("F(phi, X) = c0")
    print("A1(phi, X) = c1")
    print("A3(phi, X) = 0")
    print("\nThe corresponding symmetry generators are:")
    print("alpha(phi, X) = alpha0 (a constant)")
    print("Lambda(phi, X) = 0")
    print("\nThis implies a symmetry where the scalar field is invariant (delta_phi = 0),")
    print("and the metric transforms under a field-dependent Lie derivative along the vector xi^mu = alpha0 * g^munu * d_nu(phi).")


if __name__ == '__main__':
    find_symmetric_model()
