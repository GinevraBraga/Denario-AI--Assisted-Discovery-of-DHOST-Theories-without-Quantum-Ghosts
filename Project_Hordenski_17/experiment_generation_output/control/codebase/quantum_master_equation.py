# filename: codebase/quantum_master_equation.py

def display_qme_setup():
    """
    This function documents the analytical framework for the one-loop counter-term
    analysis of the DHOST theory using the Batalin-Vilkovisky (BV) formalism.
    It sets up the quantum master equation and defines the terms to be analyzed.
    """
    print("----------------------------------------------------------------------")
    print("Step 3: Quantum Master Equation and One-Loop Counter-Term Analysis")
    print("----------------------------------------------------------------------")
    print("This script outlines the setup for testing the consistency of potential")
    print("one-loop quantum corrections using the BV framework.\n")

    # --- Quantum Master Equation ---
    print("3.1. The Quantum Master Equation (QME)")
    print("---------------------------------------")
    print("The guiding principle for quantum consistency is the QME. To one-loop")
    print("order, it relates the extended action S_ext to the one-loop")
    print("counter-term action, S_1:\n")
    print("  {S_ext, S_1} = i * Delta * S_ext\n")
    print("Here, S_1 is the action for the candidate counter-terms, which we will")
    print("denote as S_ct. The operator Delta is the BV Laplacian.\n")

    # --- Anomaly Term ---
    print("3.2. The Anomaly Term: Delta * S_ext")
    print("------------------------------------")
    print("The right-hand side of the QME, i * Delta * S_ext, represents the")
    print("quantum anomaly that must be cancelled. The BV Laplacian is defined as:")
    print("  Delta = (-1)^(epsilon_I+1) * (delta_r / delta Psi^I) * (delta_l / delta Psi*_I)\n")
    print("where Psi^I are the fields (phi, g_munu, c) and Psi*_I are the antifields")
    print("(phi*, g*_munu, c*). Applying this to S_ext from Step 2 yields:\n")
    print("  Delta S_ext = (d/d_phi)(d/d_phi*)S_ext + (d/d_g)(d/d_g*)S_ext - (d/d_c)(d/d_c*)S_ext\n")
    print("This is a direct but lengthy functional derivative calculation. For example,")
    print("the contribution from the ghost sector is:\n")
    print("  - (delta_r/delta c) * (delta_l S_ext / delta c*)")
    print("  = - (delta_r/delta c) * (c_1 * c * d^mu(c) * d_mu(phi))")
    print("  = c_1 * c * Box(phi)  (after integration by parts)\n")
    print("The full Delta S_ext is a non-zero local functional of the fields and ghosts.")
    print("The term i * Delta S_ext must be cancelled by the left-hand side of the QME.\n")

    # --- Candidate Counter-Terms ---
    print("3.3. Proposing Candidate Counter-Terms (S_ct)")
    print("---------------------------------------------")
    print("We construct the most general, local, and diffeomorphism-invariant")
    print("Lagrangian of counter-terms, L_ct, at the correct mass dimension.")
    print("We focus on terms built from higher-order curvature invariants:\n")
    print("  S_ct = integral(d^4x * sqrt(-g) * L_ct)")
    print("  L_ct = f_G(phi, X) * G + f_W(phi, X) * W\n")
    print("Where:")
    print("  G = R^2 - 4*R_munu*R^munu + R_munurhosigma*R^munurhosigma (Gauss-Bonnet scalar)")
    print("  W = C_munurhosigma*C^munurhosigma (Weyl tensor squared)\n")
    print("Properties Verification:")
    print("- Diffeomorphism Invariance: G, W, phi, and X are all scalars, so L_ct is invariant.")
    print("- Mass Dimension: In d=4, [R]~p^2, so [G]~p^4 and [W]~p^4. For [L_ct]~p^4,")
    print("  the functions f_G(phi, X) and f_W(phi, X) must be dimensionless.\n")

    # --- Consistency Condition ---
    print("3.4. Deriving the Consistency Condition")
    print("---------------------------------------")
    print("We now evaluate the left-hand side of the QME, {S_ext, S_ct}.\n")
    print("The antibracket is: {A, B} = (dA/dPsi)(dB/dPsi*) - (dA/dPsi*)(dB/dPsi)")
    print("Since S_ct depends only on classical fields, it has no antifields, so:")
    print("  delta S_ct / delta Psi*_I = 0\n")
    print("The antibracket simplifies significantly:")
    print("  {S_ext, S_ct} = - (delta S_ext / delta Psi*_I) * (delta S_ct / delta Psi^I)")
    print("  {S_ext, S_ct} = - [ (d_S_ext/d_phi*) (d_S_ct/d_phi) + (d_S_ext/d_g*) (d_S_ct/d_g) ]\n")
    print("From the definition of S_ext, we know that (delta S_ext / delta Psi*_I) gives")
    print("the BRST transformations of the fields. For example:")
    print("  delta S_ext / delta phi* = c * Lambda = delta_c(phi)\n")
    print("Therefore, the antibracket is precisely the negative of the BRST variation of S_ct:")
    print("  {S_ext, S_ct} = - delta_c(S_ct)\n")

    # --- Final Constraint ---
    print("3.5. The Final Constraint Equation")
    print("----------------------------------")
    print("Equating the two sides of the QME, we arrive at the final constraint:")
    print("  -delta_c(S_ct) = i * Delta S_ext\n")
    print("This is the central result. It states that the BRST variation of the")
    print("candidate counter-terms must cancel the quantum anomaly.")
    print("Explicitly, this means that applying the BRST transformations delta_c(phi)")
    print("and delta_c(g_munu) to the full counter-term action S_ct must yield")
    print("a result that matches -i * Delta S_ext.\n")
    print("This provides a powerful algebraic equation that constrains the allowed")
    print("functional forms of f_G(phi, X) and f_W(phi, X), thereby selecting")
    print("the quantum corrections consistent with the gauge symmetry.")
    print("----------------------------------------------------------------------")


if __name__ == '__main__':
    display_qme_setup()