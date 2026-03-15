# filename: codebase/dhost_lagrangian_variations.py
import sympy

def main():
    """
    Symbolically computes the variation of each term in the effective Lagrangian.
    This corresponds to Step 2 of the research plan. It uses abstract symbols
    for variations of fundamental quantities to maintain clarity and focuses on
    the structure of the resulting expressions.
    """
    print("--- Step 2: Symbolic Variation of the Effective Lagrangian ---")
    print("This script computes the variation of each term in the Lagrangian density,")
    print("delta(sqrt(-g) * L_term), using abstract symbols for variations.\n")

    # --- 1. Symbol Definition ---
    # Constants
    c0, c1, beta_GB, beta_W2 = sympy.symbols('c_0 c_1 beta_GB beta_W2', real=True)
    X_bar = sympy.Symbol('X_bar') # Using X_bar as in the problem description for A4, A5

    # Scalar field and its kinetic term
    phi, X = sympy.symbols('phi X')

    # Functions Lambda and alpha
    Lambda = sympy.Function('Lambda')(phi, X)
    alpha = sympy.Function('alpha')(phi, X)

    # Metric determinant
    sqrt_g = sympy.Symbol('sqrt(-g)')

    # Tensors and scalar quantities in the Lagrangian
    R = sympy.Symbol('R')
    R_dd = sympy.Symbol('R_munu')
    R_dddd = sympy.Symbol('R_munurhosigma')
    C_dddd = sympy.Symbol('C_munurhosigma')
    G_dd = sympy.Symbol('G_munu')
    phi_d_u = sympy.Symbol('phi^mu')
    phi_dd_uu = sympy.Symbol('phi^munu')
    phi_dd_dd = sympy.Symbol('phi_munu')
    Box_phi = sympy.Symbol('Box_phi')

    # Abstract symbols for the variations of the above quantities
    delta_sqrt_g = sympy.Symbol('delta_sqrt(-g)')
    delta_phi = sympy.Symbol('delta_phi')
    delta_X = sympy.Symbol('delta_X')
    delta_R = sympy.Symbol('delta_R')
    delta_R_dd = sympy.Symbol('delta_R_munu')
    delta_R_dddd = sympy.Symbol('delta_R_munurhosigma')
    delta_C_dddd = sympy.Symbol('delta_C_munurhosigma')
    delta_G_dd = sympy.Symbol('delta_G_munu')
    delta_phi_d_u = sympy.Symbol('delta_phi^mu')
    delta_phi_dd_uu = sympy.Symbol('delta_phi^munu')
    delta_phi_dd_dd = sympy.Symbol('delta_phi_munu')
    delta_Box_phi = sympy.Symbol('delta_Box_phi')

    # --- 2. Coefficient Definition and Variation ---
    # Note: The problem uses X_bar in A4, A5 definitions. We treat it as a constant.
    # The variation delta_X is with respect to the dynamical field X.
    A4_expr = (-16 * X_bar * c1**3 + 12 * c0 * c1**2) / (8 * (c0 - X_bar * c1)**2)
    A5_expr = (4 * c1**3) / (8 * (c0 - X_bar * c1)**2)
    
    # For the purpose of variation, we need to define A4 and A5 as functions of the
    # dynamical variables phi and X. The provided forms only depend on constants.
    # If we assume A4 and A5 are general functions A(phi, X) with the given
    # values on some background, their variations would be:
    A4 = sympy.Function('A_4')(phi, X)
    A5 = sympy.Function('A_5')(phi, X)
    
    A4_phi = sympy.diff(A4, phi)
    A4_X = sympy.diff(A4, X)
    A5_phi = sympy.diff(A5, phi)
    A5_X = sympy.diff(A5, X)

    delta_A4 = A4_phi * delta_phi + A4_X * delta_X
    delta_A5 = A5_phi * delta_phi + A5_X * delta_X

    # --- 3. Lagrangian Term Definition ---
    L_EH = c0 * R
    L_DHOST = c1 * (phi_dd_uu * phi_dd_dd - Box_phi**2)
    L_A4 = A4 * C_dddd * phi_dd_uu * phi_dd_uu # Schematic contraction
    L_A5 = A5 * G_dd * phi_d_u * phi_d_u       # Schematic contraction
    L_GB = beta_GB * (R**2 - 4 * R_dd**2 + R_dddd**2)
    L_W2 = beta_W2 * C_dddd**2

    # --- 4. Computation of Variations ---
    
    # Variation of Einstein-Hilbert term
    delta_L_EH_total = delta_sqrt_g * L_EH + sqrt_g * c0 * delta_R

    # Variation of DHOST term
    delta_L_DHOST = c1 * (
        delta_phi_dd_uu * phi_dd_dd + phi_dd_uu * delta_phi_dd_dd - 2 * Box_phi * delta_Box_phi
    )
    delta_L_DHOST_total = delta_sqrt_g * L_DHOST + sqrt_g * delta_L_DHOST

    # Variation of A4 term
    delta_L_A4 = (
        delta_A4 * C_dddd * phi_dd_uu * phi_dd_uu +
        A4 * delta_C_dddd * phi_dd_uu * phi_dd_uu +
        A4 * C_dddd * (delta_phi_dd_uu * phi_dd_uu + phi_dd_uu * delta_phi_dd_uu) # Simplified 2*phi*delta_phi
    )
    delta_L_A4_total = delta_sqrt_g * L_A4 + sqrt_g * delta_L_A4

    # Variation of A5 term
    delta_L_A5 = (
        delta_A5 * G_dd * phi_d_u * phi_d_u +
        A5 * delta_G_dd * phi_d_u * phi_d_u +
        A5 * G_dd * (delta_phi_d_u * phi_d_u + phi_d_u * delta_phi_d_u) # Simplified 2*phi*delta_phi
    )
    delta_L_A5_total = delta_sqrt_g * L_A5 + sqrt_g * delta_L_A5

    # Variation of Gauss-Bonnet term
    delta_L_GB = beta_GB * (
        2 * R * delta_R - 8 * R_dd * delta_R_dd + 2 * R_dddd * delta_R_dddd
    )
    delta_L_GB_total = delta_sqrt_g * L_GB + sqrt_g * delta_L_GB

    # Variation of Weyl-squared term
    delta_L_W2 = beta_W2 * (2 * C_dddd * delta_C_dddd)
    delta_L_W2_total = delta_sqrt_g * L_W2 + sqrt_g * delta_L_W2

    # --- 5. Print Results and Annotations ---
    
    results = {
        "Einstein-Hilbert (c0*R)": {
            "variation": delta_L_EH_total,
            "epsilon_deriv_order": "Contains up to 2nd derivatives of epsilon (from delta_R)."
        },
        "DHOST (c1*...)": {
            "variation": delta_L_DHOST_total,
            "epsilon_deriv_order": "Contains up to 4th derivatives of epsilon (from delta_phi_munu)."
        },
        "A4 Term": {
            "variation": delta_L_A4_total,
            "epsilon_deriv_order": "Contains up to 4th derivatives of epsilon (from delta_phi_munu)."
        },
        "A5 Term": {
            "variation": delta_L_A5_total,
            "epsilon_deriv_order": "Contains up to 3rd derivatives of epsilon (from delta_G_munu and delta_X)."
        },
        "Gauss-Bonnet (beta_GB*...)": {
            "variation": delta_L_GB_total,
            "epsilon_deriv_order": "Contains up to 3rd derivatives of epsilon (from delta_R_munurhosigma)."
        },
        "Weyl-squared (beta_W2*...)": {
            "variation": delta_L_W2_total,
            "epsilon_deriv_order": "Contains up to 3rd derivatives of epsilon (from delta_C_munurhosigma)."
        }
    }

    print("-" * 100)
    for term, data in results.items():
        print("Variation of " + term + ":")
        sympy.pprint(data["variation"], use_unicode=False, wrap_line=False)
        print("\nAnnotation: " + data["epsilon_deriv_order"])
        print("-" * 100)


if __name__ == '__main__':
    main()