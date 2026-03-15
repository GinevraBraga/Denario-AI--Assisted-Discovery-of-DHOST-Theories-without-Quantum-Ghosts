# filename: codebase/dhost_effective_action.py
import sympy

def compute_effective_action():
    """
    Symbolically computes the one-loop effective action by adding quantum
    counter-terms to the classical action of the symmetric DHOST model.

    This function performs the following steps:
    1.  Defines symbolic variables for the background fields, curvature tensors,
        and model constants.
    2.  Constructs the classical Lagrangian for the simple symmetric model
        (F=c0, A1=c1, A3=0).
    3.  Discusses the heat kernel method and the expected structure of one-loop
        divergences for a fourth-order operator.
    4.  Constructs the counter-term Lagrangian (L_ct) with general coefficients
        (beta functions) for the expected curvature-squared terms.
    5.  Defines the full one-loop effective Lagrangian (L_eff) as the sum of
        the classical and counter-term Lagrangians.
    6.  Prints all components and the final result in a clear, documented format.
    """
    print("--- Step 4: Compute the One-Loop Effective Action ---")

    # 1. Symbolic Setup
    phi_bar, X_bar = sympy.symbols('bar_phi bar_X')
    c0, c1 = sympy.symbols('c0 c1')
    
    # Background curvature tensors
    R_bar = sympy.Symbol('bar_R')
    R_bar_mn = sympy.Symbol('bar_R_munu')
    R_bar_mnrs = sympy.Symbol('bar_R_munurhosigma')
    
    # Background scalar field derivatives
    nabla_phi = sympy.Symbol('nabla_phi')
    nabla2_phi = sympy.Symbol('nabla2_phi')

    # 2. Classical Action for the Symmetric Model
    print("\n--- Step 4.1: Classical Lagrangian ---")
    print("We start with the classical action for the symmetric model identified in Step 2:")
    print("F(phi, X) = c0")
    print("A1(phi, X) = c1")
    print("A3(phi, X) = 0")
    
    # From degeneracy conditions with F_X=0, A3=0:
    # A1 = -A2
    # A4 = (-16*X*A1^3 + 12*F*A1^2) / (8*(F - X*A1)^2)
    # A5 = (-2*A1) * (-2*A1^2) / (8*(F - X*A1)^2)
    F_model = c0
    A1_model = c1
    A2_model = -c1
    A4_model = (-16 * X_bar * c1**3 + 12 * c0 * c1**2) / (8 * (c0 - X_bar * c1)**2)
    A5_model = (4 * c1**3) / (8 * (c0 - X_bar * c1)**2)

    # The C_munurhosigma tensor part of the Lagrangian
    # For simplicity, we represent the full higher-order term symbolically
    L_DHOST_class = sympy.Symbol('L_DHOST(A1,A2,A4,A5)')

    # Full classical Lagrangian
    L_class = c0 * R_bar + L_DHOST_class
    
    print("\nThe classical Lagrangian is L_class = F*R + C_...*nabla^2phi*nabla^2phi")
    print("For our model, this is:")
    print("L_class = " + str(c0) + "*bar_R + L_DHOST(c1, -c1, A4(X), A5(X))")
    print("where A4 and A5 are determined by the degeneracy conditions to ensure classical stability.\n")

    # 3. One-Loop Divergences via Heat Kernel
    print("--- Step 4.2: Computing Divergences with the Heat Kernel Method ---")
    print("The one-loop contribution to the effective action, Gamma^(1), is computed from the functional determinant of the quadratic fluctuation operator K_gf.")
    print("Gamma^(1)_div = 1 / (16*pi^2 * (d-4)) * integral(d^4x * sqrt(-g) * Tr[a_2(K_gf)])")
    print("where a_2 is the Seeley-DeWitt coefficient.\n")
    
    print("The operator K_gf for our DHOST model contains up to fourth-order derivatives (e.g., Box^2).")
    print("A standard result in QFT in curved spacetime is that a general fourth-order operator")
    print("generates divergences proportional to terms quadratic in the curvature tensor.\n")

    # 4. Counter-Term Lagrangian
    print("--- Step 4.3: The Counter-Term Lagrangian ---")
    print("The divergent terms can be absorbed into a local counter-term Lagrangian, L_ct.")
    print("The most general such Lagrangian built from curvature-squared terms is a linear combination")
    print("of the Gauss-Bonnet invariant (GB) and the square of the Weyl tensor (W^2).\n")

    # Define the curvature-squared invariants
    GB = R_bar_mnrs**2 - 4 * R_bar_mn**2 + R_bar**2
    W2 = sympy.Symbol('C_munurhosigma^2')  # Weyl tensor squared

    # Define the coefficients (beta functions)
    beta_GB = sympy.Symbol('beta_GB')
    beta_W2 = sympy.Symbol('beta_W2')
    

    # Construct the counter-term Lagrangian
    L_ct = beta_GB * GB + beta_W2 * W2
    
    print("The counter-term Lagrangian has the form:")
    print("L_ct = beta_GB * (bar_R_munurhosigma^2 - 4*bar_R_munu^2 + bar_R^2) + beta_W2 * C_munurhosigma^2")
    print("\nHere, beta_GB and beta_W2 are constants (the 'beta functions' of the theory)")
    print("whose exact values would come from the full a_2 coefficient calculation.")
    # Note: These beta functions are just the coefficients multiplying the logarithmic divergences
    # and NOT the ones defined to study the RG flow
    print("The crucial point is that these terms are generated, and they have a structure")
    print("different from the original classical Lagrangian.\n")

    # 5. Full One-Loop Effective Action
    print("--- Step 4.4: The Full One-Loop Effective Action ---")
    print("The full one-loop effective Lagrangian, L_eff, is the sum of the classical Lagrangian and the counter-terms.")
    
    L_eff = L_class + L_ct
    
    print("\nL_eff = L_class + L_ct")
    print("\nExplicitly:")
    print("L_eff = " + str(c0) + "*bar_R + L_DHOST(c1, -c1, A4(X), A5(X)) + " + str(L_ct))
    
    print("\nThis effective Lagrangian must now be tested for two things:")
    print("1. Whether it remains invariant under the original gauge symmetry (anomaly test).")
    print("2. Whether its structure still satisfies the DHOST degeneracy conditions (stability test).")
    print("\nThis concludes the construction of the one-loop effective action.")


if __name__ == '__main__':
    compute_effective_action()
