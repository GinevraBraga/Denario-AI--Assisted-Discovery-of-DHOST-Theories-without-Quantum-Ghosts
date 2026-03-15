# filename: codebase/massless_limit_analysis.py
import sympy

def analyze_massless_limit():
    """
    Analyzes the massless limit (m_g -> 0) of the all-order stable massive
    DHOST theory, identifies the resulting theory, and discusses the
    uniqueness of the limit.
    """
    # ----------------------------------------------------------------------
    # 1. Define the Full Lagrangian Symbolically
    # ----------------------------------------------------------------------
    print("--- Analysis of the Massless Limit (m_g -> 0) ---")
    print("\nStep 1: Redefining the full massive DHOST Lagrangian.")

    # Define symbols
    phi = sympy.Symbol('phi')
    X = sympy.Symbol('X')
    M_P = sympy.Symbol('M_P')
    m_g = sympy.Symbol('m_g')
    c4 = sympy.Symbol('c4')
    G_2_0 = sympy.Function('G_2_0')(phi)
    G_3_0 = sympy.Function('G_3_0')(phi)
    G_3_0_phi = sympy.diff(G_3_0, phi)

    # Define DHOST functions
    G4 = M_P**2 / 2
    F4 = c4 / X
    G3 = G_3_0 - c4 * X
    G2 = G_2_0 - G_3_0_phi * X + (c4 / 2) * X**2

    # Define symbolic placeholders for geometric terms
    R = sympy.Symbol('R')
    Box_phi = sympy.Symbol('Box_phi')
    L_bH4 = sympy.Symbol('L_bH4')  # Placeholder for the beyond-Horndeski term

    # DHOST part of the Lagrangian
    L_DHOST = G2 - G3 * Box_phi + G4 * R + F4 * L_bH4

    # Mass term placeholders
    alpha_0 = sympy.Function('alpha_0')(phi)
    alpha_1 = sympy.Function('alpha_1')(phi)
    alpha_2 = sympy.Function('alpha_2')(phi)
    alpha_3 = sympy.Function('alpha_3')(phi)
    alpha_4 = sympy.Function('alpha_4')(phi)
    U0, U1, U2, U3, U4 = sympy.symbols('U_0 U_1 U_2 U_3 U_4')

    # Mass term Lagrangian
    L_mass = (m_g**2 * M_P**2) * (alpha_0 * U0 + alpha_1 * U1 + alpha_2 * U2 + alpha_3 * U3 + alpha_4 * U4)

    # Total Lagrangian
    L_total = L_DHOST + L_mass

    print("Original Total Lagrangian (schematic): L_total = L_DHOST + L_mass")
    print("L_DHOST = " + str(L_DHOST))
    print("L_mass = " + str(L_mass))

    # ----------------------------------------------------------------------
    # 2. Taking the Massless Limit
    # ----------------------------------------------------------------------
    print("\nStep 2: Applying the massless limit by setting m_g = 0.")

    L_massless = L_total.subs(m_g, 0)

    print("The procedure involves a direct substitution of m_g = 0 into the total Lagrangian.")
    print("L_massless = L_total.subs(m_g, 0)")
    print("\nResulting Massless Lagrangian:")
    print("L_massless = " + str(L_massless))

    # ----------------------------------------------------------------------
    # 3. Analysis of the Limit and Decoupling of Stueckelberg Fields
    # ----------------------------------------------------------------------
    print("\nStep 3: Interpretation of the limit.")
    print("As m_g -> 0, the mass term L_mass, which is proportional to m_g^2, vanishes entirely.")
    print("L_mass -> 0")
    print("\nThe Stueckelberg fields, introduced to restore diffeomorphism invariance for the")
    print("massive graviton, exist entirely within the U_n terms of L_mass.")
    print("Since the entire L_mass term disappears, all interactions involving the")
    print("Stueckelberg fields are eliminated. They decouple from the physical degrees")
    print("of freedom (graviton and scalar field) and become free fields with no dynamics")
    print("linked to the theory. Therefore, they can be consistently ignored in the massless theory.")
    print("\nThe remaining degrees of freedom are the two polarizations of the massless graviton")
    print("and the single scalar field phi.")

    # ----------------------------------------------------------------------
    # 4. Identification of the Resulting Massless Theory
    # ----------------------------------------------------------------------
    print("\nStep 4: Identification of the resulting massless theory.")
    print("The resulting action is described solely by the L_DHOST Lagrangian:")
    print("L_massless = G_2 - G_3*Box_phi + G_4*R + F_4*L_bH4")
    
    print("\nLet's examine its components:")
    print("G_4 term: G_4*R = (" + str(G4) + ")*R")
    print("This is the standard Einstein-Hilbert term for General Relativity.")

    print("\nG_3 term: -G_3*Box_phi = -(" + str(G3) + ")*Box_phi")
    print("This is a standard Horndeski L_3 term.")

    print("\nG_2 term: G_2 = " + str(G2))
    print("This is a standard Horndeski L_2 term (k-essence like).")

    print("\nF_4 term: F_4*L_bH4 = (" + str(F4) + ")*L_bH4")
    print("This is a 'beyond Horndeski' term. Since F_4 is non-zero (for c4 != 0),")
    print("the massless theory is not a simple Horndeski theory.")

    print("\nConclusion on Theory Identification:")
    print("The massless limit of the all-order stable massive DHOST theory is a specific")
    print("massless scalar-tensor theory belonging to the 'beyond Horndeski' class.")
    print("It is characterized by the following functions:")
    print("  G_2(phi, X) = " + str(G2))
    print("  G_3(phi, X) = " + str(G3))
    print("  G_4(phi)    = " + str(G4))
    print("  F_4(phi, X) = " + str(F4))
    print("  G_5 = F_5 = 0")
    print("\nThis is precisely the kinetic structure of the original massive theory, which was")
    print("classified as a DHOST Class N-I theory. The massless limit smoothly recovers")
    print("the underlying ghost-free massless scalar-tensor framework upon which the")
    print("massive theory was built.")

    # ----------------------------------------------------------------------
    # 5. Investigation of Limit Branches
    # ----------------------------------------------------------------------
    print("\nStep 5: Analysis of the uniqueness of the limit.")
    print("The limit m_g -> 0 is direct and unambiguous. The mass term is analytically")
    print("proportional to m_g^2 and vanishes without any subtleties.")
    print("The functions alpha_n(phi) that define the mass potential are assumed to be")
    print("independent of m_g. Therefore, there are no hidden dependencies that could")
    print("lead to different outcomes.")
    print("\nAs a result, the massless limit is unique. For any given set of defining")
    print("functions (G_2_0, G_3_0) and the parameter c4, the theory flows to a single,")
    print("well-defined massless 'beyond Horndeski' theory.")
    print("There are no bifurcations or distinct branches in this limit.")
    print("\n\n--- Massless Limit Analysis Complete ---")

if __name__ == '__main__':
    analyze_massless_limit()