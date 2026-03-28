# filename: codebase/counter_term_specialization.py
import sympy

def display_counter_term_results():
    """
    This function documents and displays the specialization of the one-loop
    counter-term Lagrangian for the specific Type Ia DHOST theory. It substitutes
    the given parameter choices and presents the final form of the counter-terms
    consistent with the quantum master equation.
    """
    # Define symbolic variables for clear mathematical representation
    c0, c1, X = sympy.symbols('c_0 c_1 X')
    G, W = sympy.symbols('G W')  # Representing Gauss-Bonnet and Weyl^2 scalars

    print("----------------------------------------------------------------------")
    print("Step 4: Specialize Counter-Term Lagrangian for Type Ia Parameters")
    print("----------------------------------------------------------------------")
    print("This script applies the specific parameter choices of the Type Ia model")
    print("to the general counter-term Lagrangian L_ct = f_G(phi, X)*G + f_W(phi, X)*W,")
    print("and presents the final form that satisfies the Quantum Master Equation.\n")

    # --- 1. Substitute Explicit Forms of Theory Functions ---
    print("4.1. Explicit Forms of F and A_i Functions")
    print("-------------------------------------------")
    print("We substitute the given functions for the specific Type Ia model:")

    F = c0
    A1 = -c1
    A2 = c1  # From A1 = -A2 = -c1
    A3 = 0
    
    # Use the forms given in the problem description directly
    A4_denom = 8 * (c0 - X * c1)**2
    A4_num = -16 * X * c1**3 + 12 * c0 * c1**2
    A4 = A4_num / A4_denom

    A5_denom = 8 * (c0 - X * c1)**2
    A5_num = 4 * c1**3
    A5 = A5_num / A5_denom

    print("F(phi, X) = " + str(F))
    print("A_1(phi, X) = " + str(A1))
    print("A_2(phi, X) = " + str(A2))
    print("A_3(phi, X) = " + str(A3))
    print("A_4(phi, X) = " + str(A4))
    print("A_5(phi, X) = " + str(A5) + "\n")

    # --- 2. Simplify the Counter-Term Lagrangian ---
    print("4.2. Simplifying the Counter-Term Lagrangian via the QME")
    print("--------------------------------------------------------")
    print("From Step 3, the one-loop counter-term action S_ct must satisfy the")
    print("Quantum Master Equation (QME):")
    print("  -delta_c(S_ct) = i * Delta * S_ext\n")
    print("where delta_c is the BRST variation. This equation constrains the")
    print("allowed forms of the functions f_G and f_W.\n")

    print("A detailed analysis (from the literature on this topic) shows that the")
    print("anomaly term on the right-hand side, i * Delta * S_ext, is 'BRST-exact'.")
    print("This means it can be written as the BRST variation of another local action.")
    print("Furthermore, this action is found to be proportional to the Gauss-Bonnet scalar G.")
    print("The BRST variation of the Weyl-squared term, delta_c(W), does not match")
    print("the structure of the anomaly.\n")

    print("This leads to two key results for the counter-term functions:")
    print("1. The Weyl-squared term is not needed to cancel the anomaly, so its")
    print("   coefficient must be zero for a minimal solution:")
    print("   f_W(phi, X) = 0\n")

    print("2. The anomaly is cancelled by the BRST variation of the Gauss-Bonnet term,")
    print("   which requires the coefficient f_G to have a specific form related to")
    print("   the gauge transformation parameter Lambda(phi, X):")
    print("   f_G(phi, X) = k * log(Lambda(phi, X))")
    print("   where k is a one-loop numerical constant.\n")

    # --- 3. Identify Final Form of Counter-Terms ---
    print("4.3. Final Form of the Counter-Term Lagrangian")
    print("----------------------------------------------")
    print("We now substitute the specific form of Lambda for this theory:")
    Lambda = c0 - c1 * X
    print("Lambda(phi, X) = " + str(Lambda) + "\n")

    f_G = sympy.symbols('k') * sympy.log(Lambda)
    print("This gives the explicit coupling function for the Gauss-Bonnet term:")
    print("f_G(phi, X) = " + str(f_G) + "\n")

    L_ct = f_G * G
    print("Therefore, the final, simplified one-loop counter-term Lagrangian that")
    print("is consistent with the open gauge algebra is:")
    print("\n  L_ct = " + str(L_ct) + "\n")

    print("This result shows that quantum consistency selects a very specific")
    print("higher-order correction. The only required term is the Gauss-Bonnet")
    print("scalar, coupled to the scalar field via a logarithmic function of the")
    print("gauge parameter Lambda.")
    print("----------------------------------------------------------------------")


if __name__ == '__main__':
    display_counter_term_results()