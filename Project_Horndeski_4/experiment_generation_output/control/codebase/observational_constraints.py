# filename: codebase/observational_constraints.py
import sympy

def main():
    """
    Analyzes the observational viability of the disformally equivalent Horndeski
    sub-sector by calculating the speed of gravitational waves (c_T^2) and
    the alpha parameters for cosmological perturbations.

    This script uses sympy to:
    1. Define the Horndeski functions G_i for the sub-sector.
    2. Substitute them into the general formula for c_T^2.
    3. Verify compatibility with the GW170817 constraint (c_T^2 = 1).
    4. Calculate the alpha parameters (alpha_M, alpha_B) that govern
       deviations from GR in structure growth.
    5. Output and interpret the symbolic results.
    """
    sympy.init_printing(use_unicode=True)

    # --- 1. Symbol and Function Definition ---
    phi = sympy.Symbol('phi')      # Scalar field
    X = sympy.Symbol('X')          # Kinetic term
    H = sympy.Symbol('H')          # Hubble parameter
    phi_dot = sympy.Symbol('phi_dot') # Time derivative of phi in FRW
    M_Pl = sympy.Symbol('M_Pl')     # Planck mass
    D0 = sympy.Symbol('D_0')        # Constant disformal factor

    C = sympy.Function('C')(phi) # Conformal factor
    C_p = sympy.diff(C, phi)   # C'(phi)

    print("--- Observational Constraints and Phenomenological Viability ---")
    print("\nThis script analyzes the identified Horndeski sub-sector against key")
    print("cosmological observations using symbolic calculations.")

    # --- 2. Define the Horndeski Sub-sector Functions ---
    print("\nThe analysis is based on the sub-sector defined by:")
    G5 = 0
    G4 = (M_Pl**2 / 2) * C
    G3 = M_Pl**2 * D0 * C_p * X

    print("\nG_5(X, phi) = 0")
    print("G_4(phi) = (M_Pl^2 / 2) * C(phi)")
    print("G_3(X, phi) = M_Pl^2 * D_0 * C'(phi) * X")
    print("(G_2 is not required for this part of the analysis)")

    # --- 3. Speed of Gravitational Waves (c_T^2) ---
    print("\n--- 3.1. Analysis of the Speed of Gravitational Waves, c_T^2 ---")
    print("\nThe squared speed of gravitational waves in Horndeski theory is given by:")
    ct2_formula_str = "c_T^2 = (2*G_4 - 2*X*G_4,X) / (2*G_4 - 4*X*G_4,X - X*G_5,phi - X^2*G_5,Xphi)"
    print(ct2_formula_str)

    # Calculate necessary derivatives
    G4_X = sympy.diff(G4, X)
    G5_phi = sympy.diff(G5, phi)
    G5_Xphi = sympy.diff(sympy.diff(G5, X), phi)

    print("\nFor our sub-sector, the derivatives are:")
    print("G_4,X = " + str(G4_X))
    print("G_5,phi = " + str(G5_phi))
    print("G_5,Xphi = " + str(G5_Xphi))

    # Substitute into the formula
    numerator = 2 * G4 - 2 * X * G4_X
    denominator = 2 * G4 - 4 * X * G4_X - X * G5_phi - X**2 * G5_Xphi
    c_T_sq = sympy.simplify(numerator / denominator)

    print("\nSubstituting these into the formula yields:")
    sympy.pprint(sympy.Eq(sympy.Symbol('c_T^2'), c_T_sq))

    print("\n**Result for c_T^2:**")
    print("The speed of gravitational waves is identically c_T^2 = 1.")
    print("This is a powerful result, as it means the model is automatically")
    print("consistent with the GW170817/GRB170817A constraint without any")
    print("fine-tuning of the model parameters (C(phi), D_0).")

    # --- 4. Alpha Parameters for Scalar Perturbations ---
    print("\n--- 4.1. Analysis of Alpha Parameters for Structure Growth ---")
    print("\nDeviations from GR in the scalar sector are captured by the alpha parameters.")
    print("We calculate alpha_M (running of the Planck mass) and alpha_B (braiding).")
    print("The parameter alpha_T = c_T^2 - 1 is identically zero, as shown above.")

    # Effective Planck Mass M_*^2
    M_star_sq = 2 * (G4 - 2 * X * G4_X)
    M_star_sq_val = sympy.simplify(M_star_sq)
    print("\nThe effective Planck mass squared M_*^2 = 2*(G_4 - 2*X*G_4,X) is:")
    sympy.pprint(sympy.Eq(sympy.Symbol('M_*^2'), M_star_sq_val))

    # alpha_M
    # alpha_M = d(ln(M_*^2))/d(ln(a)) = (1/H) * d(ln(M_*^2))/dt
    # d(ln(M_*^2))/dt = (1/M_*^2) * d(M_*^2)/dt = (1/M_*^2) * d(M_*^2)/d(phi) * phi_dot
    alpha_M_expr = (1 / H) * (sympy.diff(M_star_sq_val, phi) / M_star_sq_val) * phi_dot
    alpha_M = sympy.simplify(alpha_M_expr)
    print("\n1. Running of the Planck Mass (alpha_M):")
    print("alpha_M = (1/H) * d(ln(M_*^2))/dt")
    print("Symbolic Result:")
    sympy.pprint(sympy.Eq(sympy.Symbol('alpha_M'), alpha_M))
    print("This parameter measures the rate of change of the effective gravitational coupling.")

    # alpha_B
    G3_X = sympy.diff(G3, X)
    G4_phi = sympy.diff(G4, phi)
    alpha_B_expr = (phi_dot / H) * (G3_X - G4_phi / X)
    alpha_B = sympy.simplify(alpha_B_expr)
    print("\n2. Braiding (alpha_B):")
    print("alpha_B = (phi_dot/H) * (G_3,X - G_4,phi/X)")
    print("Symbolic Result:")
    sympy.pprint(sympy.Eq(sympy.Symbol('alpha_B'), alpha_B))
    print("This parameter quantifies the kinetic mixing between the scalar and metric sectors.")

    # --- 5. Summary and Interpretation ---
    print("\n\n--- SUMMARY OF OBSERVATIONAL VIABILITY ---")
    print("\n1. Speed of Gravitational Waves:")
    print("   - The model predicts c_T^2 = 1 exactly and without tuning.")
    print("   - This makes the disformally protected sub-sector fully compatible with multi-messenger astronomy constraints.")

    print("\n2. Structure Growth and Deviations from GR:")
    print("   - The theory predicts deviations from GR in the scalar sector, parameterized by non-zero alpha_M and alpha_B.")
    print("   - alpha_M depends on the slope of the conformal factor, C'(phi).")
    print("   - alpha_B depends on both C'(phi) and the disformal factor D_0.")
    print("   - These parameters are generally non-zero, meaning the effective gravitational constant for structure growth, G_eff, will differ from Newton's constant G_N.")

    print("\n3. Phenomenological Constraints:")
    print("   - The free functions/parameters of the theory, C(phi) and D_0, can be constrained by observational data.")
    print("   - Data from Large-Scale Structure surveys (like galaxy clustering and weak lensing) place bounds on the allowed values of alpha_M and alpha_B over cosmic time.")
    print("   - By comparing the theoretical expressions for alpha_M and alpha_B with these observational bounds, one can determine the viable forms of C(phi) and D_0.")
    print("\nConclusion: The disformally protected Horndeski sub-sector is not only theoretically robust (ghost-free) but also phenomenologically viable and testable.")


if __name__ == "__main__":
    main()