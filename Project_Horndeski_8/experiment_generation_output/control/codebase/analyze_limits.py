# filename: codebase/analyze_limits.py
import sympy

def analyze_horndeski_limits():
    """
    Analyzes the degeneracy-induced gauge symmetry in the Beyond Horndeski
    and Horndeski limits of DHOST theories.

    This function provides a theoretical analysis of what happens to the
    degeneracy condition, the gauge transformation, and the one-loop
    protection mechanism when the Type Ia DHOST Lagrangian is reduced to
    these important subclasses.
    """
    # --- Introduction ---
    print("--- Step 5: Analysis of Horndeski and Beyond Horndeski Limits ---")
    print("We now investigate how the degeneracy-induced gauge symmetry and its associated")
    print("protection mechanism manifest in the well-known Beyond Horndeski and Horndeski subclasses.")

    # --- Symbolic Setup ---
    X, phi = sympy.symbols('X phi')
    A1 = sympy.Function('A_1')(X, phi)
    A2 = sympy.Function('A_2')(X, phi)
    F2 = sympy.Function('F_2')(X, phi)
    G3 = sympy.Function('G_3')(X, phi)
    alpha = sympy.Function('alpha')(X, phi)
    Lambda = sympy.Function('Lambda')(X, phi)
    c1, c2 = sympy.symbols('c_1 c_2')

    # --- 1. Beyond Horndeski Limit ---
    print("\n\n--- 1. Beyond Horndeski Limit ---")
    print("Beyond Horndeski theories are a subset of degenerate theories.")
    print("The reduction from a general Type Ia DHOST theory to this class is achieved by imposing:")
    print("A_1(X, phi) = 0")
    print("A_2(X, phi) = 0")
    print("These conditions eliminate the quintic part of the DHOST Lagrangian.")

    # Re-evaluate the degeneracy condition
    print("\n* Degeneracy Condition:")
    degeneracy_condition = sympy.Eq(A1 + 2 * A2, 0)
    bh_degeneracy = degeneracy_condition.subs({A1: 0, A2: 0})
    print("The Type Ia degeneracy condition is: " + str(degeneracy_condition))
    print("Substituting the Beyond Horndeski conditions (A_1=0, A_2=0), we get: " + str(bh_degeneracy))
    print("The condition is trivially satisfied. Beyond Horndeski theories are, by construction, degenerate.")

    # Re-evaluate the transformation functions
    print("\n* Gauge Transformation:")
    symmetry_relation = sympy.Eq(Lambda, -2 * X * alpha)
    print("The gauge transformation functions are related by: " + str(symmetry_relation))
    print("This relationship is a direct consequence of the degeneracy, not the specific values of A_1 and A_2.")
    print("Therefore, the symmetry transformation remains valid and non-trivial in the Beyond Horndeski limit.")
    print("The function alpha(X, phi) can still be chosen freely, generating the symmetry.")

    # Re-evaluate the Ward identities
    print("\n* Ward Identities and Quantum Stability:")
    ward_identity = sympy.Eq(c1 + 2 * c2, 0)
    print("The Ward identity constrains the coefficients of one-loop counterterms: " + str(ward_identity))
    print("In the Beyond Horndeski limit, the classical A_1 and A_2 terms are zero.")
    print("However, quantum corrections could potentially generate them (i.e., c_1 != 0, c_2 != 0).")
    print("The Ward identity ensures that if such terms are generated, they must appear in the 'healthy' combination c_1 + 2*c_2 = 0.")
    print("Conclusion: The symmetry persists and continues to protect the theory from radiative instabilities.")

    # --- 2. Horndeski Limit ---
    print("\n\n--- 2. Horndeski (Healthy EFT) Limit ---")
    print("Horndeski theories are a further restriction of Beyond Horndeski.")
    print("They are defined by having second-order equations of motion, which requires (among other things):")
    print("A_1 = 0, A_2 = 0 (as in Beyond Horndeski)")
    print("F_2 = 0")
    print("G_3 is a function of phi only, i.e., Derivative(G_3(X, phi), X) = 0")
    print("\nCrucially, Horndeski theories are NOT degenerate in the DHOST sense. They propagate only one")
    print("scalar degree of freedom from the outset, so there is no ghost to remove via a degeneracy constraint.")

    # Re-evaluate the degeneracy condition
    print("\n* Degeneracy Condition:")
    print("The condition A_1 + 2*A_2 = 0 is trivially satisfied because the functions are zero.")
    print("However, its physical meaning changes. It's not a constraint that removes a ghost, but a reflection")
    print("that the higher-derivative terms that would produce a ghost are absent from the Lagrangian.")

    # Re-evaluate the transformation functions
    print("\n* Gauge Transformation:")
    print("The gauge symmetry was derived from the specific structure of the DHOST equations of motion, which is tied to the degeneracy.")
    print("Since Horndeski theories are not degenerate, this structure is lost.")
    print("The symmetry transformation delta_phi = Lambda * epsilon, with Lambda = -2*alpha*X, is a direct consequence of cancelling the ghost.")
    print("In the Horndeski limit, there is no ghost to cancel.")
    print("Therefore, the symmetry must become trivial.")
    print("This implies that the generator of the transformation must vanish: alpha(X, phi) = 0.")
    trivial_lambda = symmetry_relation.subs(alpha, 0)
    print("If alpha = 0, then " + str(trivial_lambda) + ". The transformation becomes delta_phi = 0, delta_g = 0.")

    # Re-evaluate the Ward identities
    print("\n* Ward Identities and Quantum Stability:")
    print("The Ward identity c_1 + 2*c_2 = 0 protected against the generation of problematic quintic operators.")
    print("Since the Horndeski Lagrangian does not contain these operators (A_1=A_2=0), the corresponding")
    print("counterterms c_1 and c_2 are not generated from renormalizing existing terms.")
    print("The stability of Horndeski theories is ensured by their fundamental structure (second-order EOMs),")
    print("not by the degeneracy-induced gauge symmetry, which has vanished.")
    print("Conclusion: The gauge symmetry becomes trivial and the associated protection mechanism is no longer relevant or necessary in the Horndeski limit.")


if __name__ == '__main__':
    analyze_horndeski_limits()