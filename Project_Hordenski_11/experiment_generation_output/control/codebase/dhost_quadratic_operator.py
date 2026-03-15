# filename: codebase/dhost_quadratic_operator.py
import sympy

def construct_quadratic_operator():
    """
    Symbolically constructs the quadratic action and operator for the one-loop calculation.

    This function does not perform the full, explicit expansion, which is
    computationally prohibitive. Instead, it uses sympy to define the components
    and conceptually build the structure of the quadratic action, explaining each
    step as per the project plan.

    Steps:
    1. Define the simple symmetric model from Step 2.
    2. Define background fields and fluctuations symbolically.
    3. Describe the expansion of the action S = S_class + S^(1) + S^(2).
    4. Symbolically represent the components of the quadratic action S^(2)
       for the Einstein-Hilbert part and the DHOST part.
    5. Discuss the structure of the resulting kinetic operator K.
    6. Discuss the need for gauge fixing and the resulting ghost action.
    7. Print a summary of the full quadratic operator structure.
    """
    # --- Setup ---
    # Symbols for constants and fields
    c0, c1 = sympy.symbols('c0 c1')
    g, g_bar, h_fluc = sympy.symbols('g g_bar h')  # h_fluc is the fluctuation field
    phi, phi_bar, varphi = sympy.symbols('phi bar_phi varphi')
    mu, nu, rho, sigma = sympy.symbols('mu nu rho sigma')
    
    # Background fields and curvature
    g_bar_mn = sympy.MatrixSymbol('bar_g', 4, 4)
    phi_bar_func = sympy.Function('bar_phi')
    R_bar = sympy.Symbol('bar_R')
    nabla_bar = sympy.Symbol('bar_nabla')
    Box_bar = sympy.Symbol('bar_Box')

    # Fluctuations
    h_mn = sympy.MatrixSymbol('h', 4, 4)
    
    print("--- Step 3: Constructing the Quadratic Operator ---")
    print("\n--- Step 3.1: The Symmetric Model and Field Expansion ---")
    
    # 1. The Model
    F = c0
    A1 = c1
    A2 = -c1
    A3 = 0
    X_bar = sympy.Symbol('bar_X')
    A4 = sympy.Function('A4')(X_bar)
    A5 = sympy.Function('A5')(X_bar)
    
    print("We start with the simple symmetric model identified in Step 2:")
    print("F(phi, X) = " + str(F))
    print("A1(phi, X) = " + str(A1))
    print("A2(phi, X) = " + str(A2))
    print("A3(phi, X) = " + str(A3))
    print("A4 and A5 are non-zero functions of X determined by the degeneracy conditions.\n")
    
    # 2. Background Field Expansion
    print("The fields are expanded around a classical background solution:")
    print("g_munu = bar_g_munu + h_munu")
    print("phi = bar_phi + varphi\n")
    
    # 3. Action Expansion
    print("The action is expanded to second order in the fluctuations (h, varphi):")
    print("S[bar_g + h, bar_phi + varphi] = S[bar_g, bar_phi] + S^(1) + S^(2) + O(3)")
    print("S^(1) vanishes as the background fields satisfy the equations of motion.")
    print("S^(2) is the quadratic action governing the dynamics of the fluctuations.\n")
    
    # 4. Structure of the Quadratic Action S^(2)
    print("--- Step 3.2: Structure of the Quadratic Action ---")
    print("S^(2) is composed of contributions from the Einstein-Hilbert term and the DHOST terms.")
    
    print("\n1. Einstein-Hilbert (EH) Part (c0 * R):")
    print("The expansion of sqrt(-g)*c0*R is standard. To second order in h, it gives:")
    print("S^(2)_EH = 1/2 * integral(d^4x * sqrt(-bar_g) * h^munu * K_Lich * h_munu)")
    print("where K_Lich is the Lichnerowicz operator, a second-order differential operator.")
    
    print("\n2. DHOST Part (C^... * nabla^2 phi * nabla^2 phi):")
    print("This part is significantly more complex. Expanding it yields terms quadratic in h, varphi, and their mixings.")
    print("The expansion involves derivatives up to the fourth order.")
    
    K_vv = sympy.Symbol('K_varphi_varphi')
    K_vh = sympy.Symbol('K_varphi_h')
    K_hh = sympy.Symbol('K_h_h')
    
    print("\nThe resulting structure for the full quadratic action is:")
    print("S^(2) = 1/2 * integral(d^4x * sqrt(-bar_g) * [")
    print("    varphi * K_vv * varphi +")
    print("    2 * varphi * K_vh^munu * h_munu +")
    print("    h^munu * K_hh_munu_rhosigma * h^rhosigma")
    print("])\n")
    
    print("Where the operators K have the following properties:")
    print(" - K_vv: A scalar differential operator acting on varphi. It contains up to fourth-order derivatives, e.g., c1*(bar_Box)^2.")
    print(" - K_vh: A tensor-valued operator describing the mixing between scalar and metric fluctuations. Contains up to third-order derivatives.")
    print(" - K_hh: A fourth-rank tensor operator acting on h_munu. It includes the Lichnerowicz operator from the EH part and additional complex terms from the DHOST part, with up to fourth-order derivatives.\n")
    
    # 5. Gauge Fixing
    print("--- Step 3.3: Gauge Fixing and Ghosts ---")
    print("The operator K derived from S^(2) is singular due to diffeomorphism invariance.")
    print("To perform the path integral, we must add a gauge-fixing term S_gf.")
    print("A standard choice is the de Donder gauge condition on the metric fluctuation h_munu.")
    
    alpha_gf = sympy.Symbol('alpha_gf')
    h_trace = sympy.Symbol('h')  # trace of h_munu
    
    print("\nGauge-fixing action:")
    print("S_gf = 1/(2*alpha_gf) * integral(d^4x * sqrt(-bar_g) * G_mu * G^mu)")
    print("where G_mu = bar_nabla^nu * h_numu - 1/2 * bar_nabla_mu * h")
    print("This term modifies the K_hh part of the kinetic operator, making it invertible.\n")
    
    # 6. Ghost Action
    print("The introduction of a gauge-fixing term necessitates the inclusion of a Faddeev-Popov ghost action S_ghost.")
    
    c_bar = sympy.Symbol('bar_c')
    c = sympy.Symbol('c')
    
    print("\nGhost action:")
    print("S_ghost = integral(d^4x * sqrt(-bar_g) * bar_c^mu * K_ghost_munu * c^nu)")
    print("The ghost operator K_ghost is a second-order differential operator:")
    print("K_ghost_munu = - (delta_mu_nu * bar_Box + bar_R_munu)")
    print("The ghosts are vector fields and do not couple to the scalar fluctuation varphi at the quadratic level.\n")
    
    # 7. Summary
    print("--- Step 3.4: Summary of the Quadratic Operator Structure ---")
    print("The complete action at quadratic order, used for the one-loop calculation, is:")
    print("S_quad = S^(2) + S_gf + S_ghost")
    
    print("\nThe one-loop effective action is then formally given by the path integral over the fluctuations:")
    print("exp(i * Gamma^(1)) = integral(D[varphi] D[h] D[c] D[bar_c] * exp(i * S_quad))")
    
    print("\nThis leads to the formal expression for the one-loop correction:")
    print("Gamma^(1) = (i/2) * Tr(log(K_gf)) - i * Tr(log(K_ghost))")
    print("where K_gf is the gauge-fixed kinetic operator for the (varphi, h) system.")
    
    print("\nThe key takeaway is the structure of the kinetic operator K_gf. It is a matrix operator")
    print("containing up to fourth-order spatial derivatives, acting on the (varphi, h) field space.")
    print("The subsequent calculation of the one-loop divergences via the heat kernel method will")
    print("depend on the coefficients of the highest derivative terms in this operator.")
    print("\nExplicitly deriving every term of the operator is beyond the scope of this step; its conceptual structure is the crucial input for the next part of the analysis.")


if __name__ == '__main__':
    construct_quadratic_operator()