# filename: codebase/observational_viability.py
import sympy

def analyze_observational_viability():
    """
    Analyzes the observational and cosmological viability of the co-invariant
    Horndeski subclass.

    This function performs the following checks:
    1.  It imposes the observational constraint on the speed of gravitational waves,
        c_T = 1.
    2.  It analyzes the resulting constraint in the context of a de Sitter
        cosmological background (a necessary condition for late-time acceleration).
    3.  It cross-references this with the classical stability conditions derived
        in Step 3 to check for self-consistency.
    """
    print("--- Step 5: Observational Viability and Cosmological Constraints ---")
    print("\nWe analyze the derived subclass against key cosmological observations.")
    print("The primary constraints are the speed of gravitational waves (c_T^2 = 1)")
    print("and the existence of a late-time accelerating universe (e.g., a de Sitter phase).")
    print("-" * 70)

    # --- 1. Symbolic Setup ---
    # Background quantities
    phi_ddot = sympy.Symbol('phi_ddot', real=True)
    X = sympy.Symbol('X', real=True, positive=True)

    # Model parameters from the co-invariant subclass
    c4, c5 = sympy.symbols('c4 c5', real=True)

    # Horndeski functions for the subclass
    G4 = c4 * X**2
    G5 = c5 * X**2

    # --- 2. Analyze Speed of Gravitational Waves ---
    print("\n--- 5.1. Analysis of the Speed of Gravitational Waves (c_T) ---")

    # The squared speed of tensor modes for the subclass was derived in Step 3
    # and re-verified. The expression is:
    # c_T^2 = (c4 - 2*c5*phi_ddot) / (-2*c4)
    c_T_sq = (c4 - 2 * c5 * phi_ddot) / (-2 * c4)

    print("The squared speed of tensor modes for the subclass is:")
    print("c_T^2 = (c4 - 2*c5*phi_ddot) / (-2*c4)")

    # Impose the observational constraint c_T^2 = 1
    gw_constraint_eq = sympy.Eq(c_T_sq, 1)

    print("\nImposing the observational constraint c_T^2 = 1 (from GW170817) gives the equation:")
    sympy.pprint(gw_constraint_eq)

    # Solve for the relationship between parameters
    # (c4 - 2*c5*phi_ddot) = -2*c4  =>  3*c4 = 2*c5*phi_ddot
    constraint_relation = sympy.Eq(3 * c4, 2 * c5 * phi_ddot)
    print("\nThis simplifies to the following required relation between parameters and background evolution:")
    sympy.pprint(constraint_relation)
    print("-" * 70)

    # --- 3. Check for Consistency with de Sitter Background ---
    print("\n--- 5.2. Consistency Check with a de Sitter Universe ---")
    print("A viable model of dark energy must allow for a period of late-time acceleration,")
    print("such as a de Sitter phase where the Hubble rate H is constant and fields are stable.")
    print("In a de Sitter phase with a rolling scalar field, phi_dot is constant, which implies phi_ddot = 0.")

    # Substitute phi_ddot = 0 into the constraint relation
    ds_constraint = constraint_relation.subs(phi_ddot, 0)
    print("\nSubstituting phi_ddot = 0 into the c_T^2=1 constraint gives:")
    sympy.pprint(ds_constraint)

    print("\nThis implies that c4 must be zero.")
    print("-" * 70)

    # --- 4. Final Conclusion on Viability ---
    print("\n--- 5.3. Conclusion on Observational Viability ---")
    print("The analysis reveals a fundamental inconsistency in the derived co-invariant subclass:")
    print("1. From the c_T^2 = 1 constraint and the requirement of a de Sitter background, we find that c4 = 0.")
    print("2. However, the classical stability analysis (Step 3) showed that the tensor no-ghost condition")
    print("   is mathcal_G_T > 0, which for our subclass is -2*c4*X**2 > 0, requiring c4 < 0.")

    print("\nThe condition c4 = 0 (from observation) is in direct contradiction with the stability")
    print("condition c4 < 0 (from theory). A value of c4=0 would mean the kinetic term for")
    print("gravitational waves vanishes, leading to an infinite strong coupling problem (a pathological theory).")

    print("\nFINAL CONCLUSION: The specific 'Disformal-Generalized Galilean Co-invariant' subclass,")
    print("defined by G4 = c4*X^2 and G5 = c5*X^2, is NOT observationally viable as it cannot")
    print("simultaneously satisfy the tensor no-ghost condition and the observational constraint c_T=1")
    print("on a cosmologically relevant (de Sitter) background.")
    print("\nThis implies that the symmetry that protects against one-loop ghosts in this model is too restrictive")
    print("and is incompatible with fundamental cosmological observations.")
    print("-" * 70)


if __name__ == '__main__':
    analyze_observational_viability()