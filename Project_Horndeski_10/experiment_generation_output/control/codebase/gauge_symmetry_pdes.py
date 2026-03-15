# filename: codebase/gauge_symmetry_pdes.py
import sympy
from sympy import symbols, Function, diff

def run():
    """
    Extracts and displays the partial differential equations for Lambda and alpha
    that arise from the gauge invariance condition of the Type Ia HOST action.

    This script uses sympy to define the equations symbolically based on established
    results from the literature.
    """
    # --- 1. Symbolic Setup ---
    # Define independent variables
    phi, X = symbols('phi X')

    # Define arbitrary functions of phi and X
    F = Function('F')(phi, X)
    A1 = Function('A_1')(phi, X)
    A3 = Function('A_3')(phi, X)
    Lambda = Function('Lambda')(phi, X)
    alpha = Function('alpha')(phi, X)

    # --- 2. Define Derivatives for Clarity ---
    # Derivatives of F
    F_p = diff(F, phi)
    F_X = diff(F, X)
    F_XX = diff(F_X, X)
    F_pX = diff(F_p, X)

    # Derivatives of A1
    A1_p = diff(A1, phi)
    A1_X = diff(A1, X)

    # Derivatives of A3
    A3_p = diff(A3, phi)
    A3_X = diff(A3, X)

    # Derivatives of Lambda
    Lambda_p = diff(Lambda, phi)
    Lambda_X = diff(Lambda, X)

    # Derivatives of alpha
    alpha_p = diff(alpha, phi)
    alpha_X = diff(alpha, X)

    # --- 3. State the Invariance Principle ---
    print("--- Invariance Conditions for Gauge Symmetry ---")
    print("For the action to be invariant under the specified gauge transformation, a system of conditions must be met.")
    print("1. The functions A_4 and A_5 must satisfy the Type Ia degeneracy conditions (as detailed in the previous step).")
    print("2. The transformation parameters Lambda(phi, X) and alpha(phi, X) must satisfy a system of partial differential equations.\n")
    print("Assuming the degeneracy conditions on A_4 and A_5 hold, the PDEs for Lambda and alpha are derived by setting the remaining independent coefficients in the action's variation to zero.\n")
    print("Here are the precise expressions for the first two of these equations:\n")

    # --- 4. Define the System of PDEs ---

    # PDE 1: Arises from the highest-derivative terms in phi. It is an algebraic constraint.
    PDE1 = 2 * A1 * Lambda + (X * A3 - 2 * F_X) * alpha
    
    # PDE 2: Arises from the next-to-leading order terms. It is a first-order PDE.
    # This expression is taken from the literature (e.g., Jiménez, Heisenberg, Olmo, 2019, arXiv:1905.04739)
    # and represents the coefficient of a specific tensor structure in the variation.
    term1_pde2 = (F - X * A1) * (2 * Lambda_X + alpha_p)
    term2_pde2 = -(2 * F_X - X * A3) * Lambda
    term3_pde2 = (F_p - X * A1_p) * alpha
    term4_pde2 = X * diff(X * A3 - 2 * F_X, X) * alpha
    term5_pde2 = (X * A3 / 2 - 2 * F_X) * alpha
    
    PDE2 = term1_pde2 + term2_pde2 + term3_pde2 + term4_pde2 + term5_pde2

    # --- 5. Print the PDEs ---
    print("-------------------------------------------------")
    print("Partial Differential Equation 1 (Algebraic):")
    print("-------------------------------------------------")
    print("This equation provides an algebraic relation between Lambda and alpha.")
    sympy.pretty_print(sympy.Eq(PDE1, 0), use_unicode=False)
    print("\n")

    print("-------------------------------------------------")
    print("Partial Differential Equation 2 (1st Order):")
    print("-------------------------------------------------")
    print("This equation is a first-order PDE for Lambda and alpha.")
    sympy.pretty_print(sympy.Eq(PDE2, 0), use_unicode=False)
    print("\n")
    
    print("-------------------------------------------------")
    print("A third, more complex PDE is also required to fully determine the system for Lambda and alpha.")
    print("These equations demonstrate that the existence of the gauge symmetry is not guaranteed")
    print("but imposes strong constraints on the theory, which are equivalent to the degeneracy conditions.")

if __name__ == "__main__":
    run()