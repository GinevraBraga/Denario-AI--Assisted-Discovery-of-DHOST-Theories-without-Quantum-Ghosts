# filename: codebase/dhost_degeneracy_verification.py
import sympy

def derive_degeneracy_and_verify_type_ia():
    """
    Derives the degeneracy condition for quadratic DHOST theories in the unitary
    gauge and verifies it for the Type Ia subclass.

    This function first constructs the kinetic matrix for scalar perturbations,
    then computes its determinant. Setting the determinant to zero gives the
    degeneracy condition required to eliminate the ghost degree of freedom.

    Finally, it substitutes the specific functional forms of Type Ia DHOST
    theories into this condition to explicitly show that they satisfy it,
    confirming their classical stability.
    """
    # Initialize sympy for pretty printing
    sympy.init_printing(use_unicode=True)

    # --- 1. Define Symbolic Variables and Functions ---
    t = sympy.Symbol('t')
    phi = sympy.Function('phi')(t)
    X = sympy.Symbol('X')
    H = sympy.Symbol('H')

    # DHOST free functions A_i(phi, X) and their X-derivatives
    A1 = sympy.Function('A1')(phi, X)
    A2 = sympy.Function('A2')(phi, X)
    A3 = sympy.Function('A3')(phi, X)
    A4 = sympy.Function('A4')(phi, X)
    A5 = sympy.Function('A5')(phi, X)

    A1X = sympy.Symbol('A1X')
    A2X = sympy.Symbol('A2X')
    A3X = sympy.Symbol('A3X')
    A4X = sympy.Symbol('A4X')
    A5X = sympy.Symbol('A5X')

    # --- 2. Construct the Kinetic Matrix in Unitary Gauge ---
    print("--- Step 2.1: Deriving Degeneracy Condition in Unitary Gauge ---")

    # Coefficients of the kinetic matrix K
    K11 = 2 * X * (A1 + 2 * X * A1X) - A2 - 2 * X * A2X
    K12 = A2 + 2 * X * A3X
    K22 = 2 * (A3 + A4 + 2 * X * A4X) - A5 - 2 * X * A5X

    # Symbolic kinetic matrix
    K = sympy.Matrix([[K11, K12], [K12, K22]])

    print("\nReconstructing the Kinetic Matrix K:")
    sympy.pprint(K)

    # --- 3. Compute the Determinant to find the Degeneracy Condition ---
    print("\nComputing the determinant of K...")
    det_K = sympy.det(K)
    
    # Simplify the expression
    det_K_simplified = sympy.simplify(det_K)
    
    # Collect terms for better readability
    det_K_collected = sympy.collect(det_K_simplified, [A1, A2, A3, A4, A5, A1X, A2X, A3X, A4X, A5X])

    print("\nThe degeneracy condition is det(K) = 0.")
    print("Symbolic expression for det(K):")
    sympy.pprint(det_K_collected)
    print("-" * 60)

    # --- 4. Verify the Condition for Type Ia DHOST Theories ---
    print("\n--- Step 2.2: Verifying the Condition for Type Ia DHOST Theories ---")
    print("Type Ia DHOST theories are defined by the following constraints:")
    print("A1 = 0")
    print("A3 = -A4")
    print("A5 = 0")
    print("\nThis implies the following for their X-derivatives:")
    print("A1X = 0")
    print("A3X = -A4X")
    print("A5X = 0")

    # Define the substitution rules for Type Ia theories
    type_ia_subs = {
        A1: 0,
        A1X: 0,
        A3: -A4,
        A3X: -A4X,
        A5: 0,
        A5X: 0
    }

    # Apply the substitutions to the determinant
    det_K_type_ia = det_K_collected.subs(type_ia_subs)

    print("\nSubstituting these constraints into the expression for det(K)...")
    
    # Simplify the result after substitution
    det_K_type_ia_simplified = sympy.simplify(det_K_type_ia)

    print("\nResulting expression for det(K) for Type Ia theories:")
    sympy.pprint(det_K_type_ia_simplified)

    if det_K_type_ia_simplified == 0:
        print("\nVerification successful: The degeneracy condition is identically satisfied (det(K) = 0).")
        print("This confirms that Type Ia DHOST theories are free from the ghost instability at the classical level.")
    else:
        print("\nVerification failed: The degeneracy condition is NOT satisfied for Type Ia theories.")
        print("There might be an error in the definitions or the calculation.")
    
    print("-" * 60)

if __name__ == '__main__':
    derive_degeneracy_and_verify_type_ia()
