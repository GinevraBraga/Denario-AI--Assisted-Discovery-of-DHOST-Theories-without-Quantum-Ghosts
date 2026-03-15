# filename: codebase/setup_dhost_unitary_gauge.py
import sympy

def setup_dhost_unitary_gauge():
    """
    Sets up the symbolic framework for quadratic DHOST theories in the unitary gauge.

    This function defines the necessary symbolic variables and functions to represent
    the kinetic part of the quadratic action for scalar perturbations. It constructs
    and prints the kinetic matrix for the fields (zeta, A), where zeta is the
    curvature perturbation and A is the lapse perturbation.

    The kinetic part of the Lagrangian is of the form:
    L_kin = K_11 * dot(zeta)^2 + 2 * K_12 * dot(zeta) * A + K_22 * A^2

    The degeneracy condition, which ensures the absence of a ghost-like Ostrogradski
    instability, is det(K) = 0. This script provides the symbolic matrix K,
    paving the way for the subsequent derivation of this condition.

    The expressions for the matrix elements are taken from the standard literature
    on quadratic DHOST theories.
    """
    # Initialize sympy for pretty printing
    sympy.init_printing(use_unicode=True)

    # --- 1. Define Symbolic Variables and Functions ---

    # Time coordinate
    t = sympy.Symbol('t')

    # Background quantities as functions of time
    phi = sympy.Function('phi')(t)
    a = sympy.Function('a')(t)

    # Background scalar field kinetic term X and its relation to phi_dot
    # X = -1/2 * g^munu * nabla_mu(phi) * nabla_nu(phi)
    # On an FLRW background, X = 1/2 * dot(phi)^2
    X = sympy.Symbol('X')
    phi_dot = sympy.Symbol('phidot')  # Represents dot(phi) at the background level

    # Hubble parameter
    H = sympy.Symbol('H')  # Represents H(t) = dot(a)/a at the background level

    # DHOST free functions A_i(phi, X)
    # We define them as symbolic functions of phi and X
    A1 = sympy.Function('A1')(phi, X)
    A2 = sympy.Function('A2')(phi, X)
    A3 = sympy.Function('A3')(phi, X)
    A4 = sympy.Function('A4')(phi, X)
    A5 = sympy.Function('A5')(phi, X)

    # Derivatives of A_i with respect to X
    A1X = sympy.Symbol('A1X')  # Represents dA1/dX
    A2X = sympy.Symbol('A2X')  # Represents dA2/dX
    A3X = sympy.Symbol('A3X')  # Represents dA3/dX
    A4X = sympy.Symbol('A4X')  # Represents dA4/dX
    A5X = sympy.Symbol('A5X')  # Represents dA5/dX

    print("--- DHOST Theory Setup ---")
    print("This script formalizes the kinetic matrix for scalar perturbations in quadratic DHOST theories.")
    print("The analysis is performed in the unitary gauge (delta_phi = 0).")
    print("The dynamical fields are the curvature perturbation 'zeta' and the lapse perturbation 'A'.")
    print("\nBackground quantities:")
    print("Scalar field: phi(t)")
    print("Scale factor: a(t)")
    print("Scalar kinetic term: X = 1/2 * dot(phi)^2")
    print("Hubble parameter: H = dot(a)/a")
    print("\nFree functions of quadratic DHOST theory: A_i(phi, X) for i=1..5")
    print("Derivatives w.r.t. X are denoted as AiX (e.g., A1X = dA1/dX).")
    print("-" * 30 + "\n")


    # --- 2. Construct the Kinetic Matrix in Unitary Gauge ---

    # The kinetic part of the Lagrangian for scalar perturbations (zeta, A) is:
    # L_kin = K_11 * dot(zeta)^2 + 2 * K_12 * dot(zeta) * A + K_22 * A^2
    # The coefficients K_ij for quadratic DHOST theories are well-known.

    # Coefficient of dot(zeta)^2
    K11 = 2 * X * (A1 + 2 * X * A1X) - A2 - 2 * X * A2X

    # Coefficient of dot(zeta) * A (halved for the symmetric matrix)
    K12 = A2 + 2 * X * A3X

    # Coefficient of A^2
    K22 = 2 * (A3 + A4 + 2 * X * A4X) - A5 - 2 * X * A5X

    # Create the symbolic kinetic matrix
    K = sympy.Matrix([[K11, K12], [K12, K22]])

    # --- 3. Output the Results ---

    print("Symbolic Kinetic Matrix K for Scalar Perturbations in Unitary Gauge:")
    print("The Lagrangian kinetic terms are L_kin = [dot(zeta), A] * K * [dot(zeta), A]^T")
    print("\nMatrix K:")
    sympy.pprint(K)

    print("\n" + "-" * 30)
    print("The degeneracy condition that eliminates the ghost is det(K) = 0.")
    print("The derivation of this condition will be performed in the next step.")
    print("This script has successfully set up the symbolic framework for the unitary gauge analysis.")
    print("The setup for covariant and longitudinal gauges will be developed subsequently.")


if __name__ == '__main__':
    setup_dhost_unitary_gauge()