# filename: codebase/extract_lagrangian.py
import sympy

def extract_lagrangian():
    """
    Symbolically defines and prints the Lagrangian for the all-order stable
    massive DHOST theory from the paper DHOSTS.pdf (arXiv:1804.06262).

    This function uses the sympy library to create a symbolic representation
    of the theory's action, preparing it for further analysis.
    """
    # ----------------------------------------------------------------------
    # 1. Define Base Symbols and Functions
    # ----------------------------------------------------------------------

    # Define independent variables: scalar field 'phi' and its kinetic term 'X'
    phi = sympy.Symbol('phi')
    X = sympy.Symbol('X')

    # Define constants: Planck mass, graviton mass, and c4 parameter
    M_P = sympy.Symbol('M_P')
    m_g = sympy.Symbol('m_g')
    c4 = sympy.Symbol('c4')

    # Define arbitrary functions of phi that appear in the theory
    G_2_0 = sympy.Function('G_2_0')(phi)
    G_3_0 = sympy.Function('G_3_0')(phi)
    alpha_0 = sympy.Function('alpha_0')(phi)
    alpha_1 = sympy.Function('alpha_1')(phi)
    alpha_2 = sympy.Function('alpha_2')(phi)
    alpha_3 = sympy.Function('alpha_3')(phi)
    alpha_4 = sympy.Function('alpha_4')(phi)

    # Derivative of G_3_0 with respect to phi
    G_3_0_phi = sympy.diff(G_3_0, phi)

    print("--- All-Order Stable Massive DHOST Lagrangian ---")
    print("\nThis script symbolically defines the Lagrangian from DHOSTS.pdf (arXiv:1804.06262).")
    print("\n--- 1. Fundamental Definitions ---")
    print("Scalar field: " + str(phi))
    print("Kinetic term: X = -g^{mu nu} * d_mu(phi) * d_nu(phi)")
    print("Arbitrary functions of phi:")
    print("G_2_0(phi): " + str(G_2_0))
    print("G_3_0(phi): " + str(G_3_0))
    print("alpha_n(phi): Coefficients of the mass potential.")

    # ----------------------------------------------------------------------
    # 2. Define the DHOST Functions G_i and F_i
    # ----------------------------------------------------------------------

    # G4 is fixed to the Einstein-Hilbert term
    G4 = M_P**2 / 2

    # F4 is part of the "beyond Horndeski" sector
    F4 = c4 / X

    # G3 is constrained by the stability conditions
    G3 = G_3_0 - c4 * X

    # G2 is also constrained by the stability conditions
    G2 = G_2_0 - G_3_0_phi * X + (c4 / 2) * X**2

    print("\n--- 2. DHOST Function Definitions ---")
    print("G_2(phi, X) = " + str(G2))
    print("G_3(phi, X) = " + str(G3))
    print("G_4(phi)    = " + str(G4))
    print("F_4(phi, X) = " + str(F4))
    print("G_5, F_5 are assumed to be zero for this theory.")

    # ----------------------------------------------------------------------
    # 3. Define Symbolic Placeholders for Geometric Terms
    # ----------------------------------------------------------------------

    R = sympy.Symbol('R')
    Box_phi = sympy.Symbol('Box_phi')
    phi_mu_nu_sq = sympy.Symbol('(phi_mn)^2')
    phi_mu_nu_phi_mu_rho_phi_nu_rho = sympy.Symbol('(phi_mn)(phi_mr)(phi_nr)')
    Box_phi_phi_m_phi_n_phi_mn = sympy.Symbol('(Box_phi)(phi_m)(phi_n)(phi_mn)')

    # The "beyond Horndeski" Lagrangian term L_4^bH
    L_bH4 = X * (Box_phi**2 - phi_mu_nu_sq) \
            - 2 * phi_mu_nu_phi_mu_rho_phi_nu_rho \
            + 2 * Box_phi_phi_m_phi_n_phi_mn

    print("\n--- 3. DHOST Lagrangian Construction ---")
    print("Using symbolic placeholders for geometric quantities:")
    print("R: Ricci Scalar")
    print("Box_phi: Covariant d'Alembertian of phi")
    print("(phi_mn)^2: (nabla_mu nabla_nu phi) * (nabla^mu nabla^nu phi)")
    print("...")

    # Construct the DHOST part of the Lagrangian
    L_DHOST = G2 - G3 * Box_phi + G4 * R + F4 * L_bH4

    print("\nThe DHOST part of the Lagrangian is L_DHOST = G_2 - G_3*Box_phi + G_4*R + F_4*L_bH4")
    print("L_DHOST = " + str(L_DHOST))

    # ----------------------------------------------------------------------
    # 4. Define the Massive Gravity Potential
    # ----------------------------------------------------------------------

    # Symbolic representation of the traces of the matrix K
    # K^mu_nu = delta^mu_nu - sqrt(g^{mu alpha} * eta_{alpha nu})
    tr_K = sympy.Symbol('[K]')
    tr_K2 = sympy.Symbol('[K^2]')
    tr_K3 = sympy.Symbol('[K^3]')
    tr_K4 = sympy.Symbol('[K^4]')

    # Elementary symmetric polynomials U_n of the eigenvalues of K
    U0 = 1
    U1 = tr_K
    U2 = sympy.Rational(1, 2) * (tr_K**2 - tr_K2)
    U3 = sympy.Rational(1, 6) * (tr_K**3 - 3 * tr_K * tr_K2 + 2 * tr_K3)
    U4 = sympy.Rational(1, 24) * (tr_K**4 - 6 * tr_K**2 * tr_K2 + 8 * tr_K * tr_K3 + 3 * tr_K2**2 - 6 * tr_K4)

    # Construct the mass term Lagrangian
    L_mass = (m_g**2 * M_P**2) * (alpha_0 * U0 + alpha_1 * U1 + alpha_2 * U2 + alpha_3 * U3 + alpha_4 * U4)

    print("\n--- 4. Massive Gravity Potential Construction ---")
    print("The mass term is constructed from elementary symmetric polynomials U_n of K.")
    print("K^mu_nu = delta^mu_nu - (g^{-1/2})^mu_nu")
    print("U_0 = " + str(U0))
    print("U_1 = " + str(U1))
    print("U_2 = " + str(U2))
    print("U_3 = " + str(U3))
    print("U_4 = " + str(U4))
    print("\nThe mass Lagrangian is L_mass = m_g^2 * M_P^2 * Sum_{n=0 to 4} alpha_n(phi) * U_n(K)")
    print("L_mass = " + str(L_mass))

    # ----------------------------------------------------------------------
    # 5. Total Lagrangian
    # ----------------------------------------------------------------------

    L_total = L_DHOST + L_mass

    print("\n--- 5. Total Lagrangian Density (L / sqrt(-g)) ---")
    print("\nL_total = L_DHOST + L_mass")
    print("\nL_total = " + str(L_total))
    print("\n\nExtraction complete. The symbolic Lagrangian is ready for the next analysis steps.")


if __name__ == '__main__':
    extract_lagrangian()