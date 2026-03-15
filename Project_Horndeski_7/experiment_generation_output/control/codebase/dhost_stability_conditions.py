# filename: codebase/dhost_stability_conditions.py
import sympy as sp

def derive_stability_conditions():
    """
    Symbolically derives the conditions for tree-level stability (c_T^2 = 1 and no scalar ghost)
    for Type I DHOST theories in an FRW background.

    The derivation is based on the established quadratic actions for tensor and scalar
    perturbations from the literature (e.g., arXiv:1602.03119, arXiv:1807.03791).
    This script formulates the known algebraic conditions using sympy to provide explicit,
    unambiguous expressions.
    """
    # 1. Define symbolic variables and background quantities
    t = sp.Symbol('t')
    phi_sym = sp.Symbol('phi')
    X_sym = sp.Symbol('X')

    # Background functions of time
    a = sp.Function('a')(t)
    phi0 = sp.Function('phi0')(t)

    # Background kinematic variables
    H = sp.diff(a, t) / a
    phi0_dot = sp.diff(phi0, t)
    phi0_ddot = sp.diff(phi0_dot, t)
    X = phi0_dot**2

    # 2. Define DHOST functions G_i(phi, X) and their derivatives
    # These are symbolic functions, not evaluated on the background yet
    G2_f = sp.Function('G2')(phi_sym, X_sym)
    G3_f = sp.Function('G3')(phi_sym, X_sym)
    G4_f = sp.Function('G4')(phi_sym, X_sym)
    G5_f = sp.Function('G5')(phi_sym, X_sym)

    # Create a dictionary to hold all background-evaluated functions for convenience
    # This makes the expressions cleaner by using shorter names
    G = {}
    funcs = [G2_f, G3_f, G4_f, G5_f]
    names = ['G2', 'G3', 'G4', 'G5']

    for func, name in zip(funcs, names):
        # Function itself evaluated on background
        G[name] = func.subs([(phi_sym, phi0), (X_sym, X)])
        # Derivatives w.r.t. phi
        G[name + '_p'] = func.diff(phi_sym).subs([(phi_sym, phi0), (X_sym, X)])
        # Derivatives w.r.t. X
        G[name + '_X'] = func.diff(X_sym).subs([(phi_sym, phi0), (X_sym, X)])

    print("--- DHOST Stability Analysis ---")
    print("Deriving conditions for c_T^2 = 1 and absence of scalar ghosts at tree-level.")
    print("All functions G_i and their derivatives (e.g., G_iX, G_ip) are evaluated on the FRW background.")
    print("\n")

    # 3. Tensor Perturbations: c_T^2 = 1 condition
    print("--- Tensor Sector: Gravitational Waves ---")

    # Kinetic term coefficient for tensor modes (proportional to effective Planck mass squared)
    # Based on arXiv:1602.03119, Eq. (3.9)
    G_T = 2 * (G['G4'] - X * G['G5_p'])
    
    # Squared speed of tensor modes
    # Based on arXiv:1602.03119, Eq. (3.9), the deviation from c_T^2=1 is proportional to
    # X * (G_5p + phi0_ddot * G_5X).
    c_T_sq_numerator_mod = X * (G['G5_p'] + phi0_ddot * G['G5_X'])
    c_T_sq_denominator = G['G4'] - X * G['G5_p']
    c_T_sq = 1 - c_T_sq_numerator_mod / c_T_sq_denominator

    print("The quadratic action for tensor perturbations h_ij is of the form:")
    print("S_T^(2) = integral dt d^3x a^3 * (1/8) * G_T * [ (h_dot_ij)^2 - c_T^2/a^2 * (grad(h_ij))^2 ]\n")

    print("Kinetic coefficient G_T (proportional to M_pl^2):")
    sp.pprint(G_T)
    print("\nSquared propagation speed c_T^2:")
    sp.pprint(c_T_sq)
    print("\n")

    # Extract the condition for c_T^2 = 1
    ct_condition = sp.Eq(c_T_sq_numerator_mod, 0)
    print("--------------------------------------------------")
    print("Condition for Massless Gravity (c_T^2 = 1):")
    print("This requires the numerator of the (c_T^2 - 1) term to be zero.")
    sp.pprint(ct_condition)
    print("Assuming non-trivial scalar field dynamics (X != 0), this simplifies to:")
    sp.pprint(sp.Eq(ct_condition.lhs / X, 0))
    print("--------------------------------------------------\n")


    # 4. Scalar Perturbations: No-ghost condition (A_S = 0)
    print("--- Scalar Sector: No-Ghost Condition ---")
    print("The defining feature of DHOST theories is the degeneracy of the kinetic matrix for scalar perturbations.")
    print("This ensures the absence of a ghost-like Ostrogradsky mode.")
    print("The condition for this degeneracy, A_S = 0, is a specific algebraic relation between the G_i functions.")
    print("We use the condition for Type I DHOST from arXiv:1807.03791, Eq. (4.21), denoted there as a_1 = 0.\n")

    # Using the expression for a_1 from arXiv:1807.03791
    term1 = (G['G4'] - 2 * X * G['G4_X'])**2
    
    term2_factor1 = G['G3'] - X * G['G3_X'] - (sp.S(3)/2) * phi0_dot * H * G['G4']
    term2_factor2 = G['G4'] - 3 * X * G['G4_X'] - (sp.S(3)/2) * phi0_dot * H * G['G5']
    
    term2 = (sp.S(4)/3) * X * term2_factor1 * term2_factor2
    
    A_S_condition_expr = term1 - term2
    
    A_S_condition = sp.Eq(A_S_condition_expr, 0)

    print("--------------------------------------------------")
    print("Condition for Absence of Scalar Ghost (A_S = 0):")
    print("The kinetic term for the scalar mode vanishes if the following expression is zero:")
    sp.pprint(A_S_condition)
    print("--------------------------------------------------\n")

    print("Summary of Tree-Level Stability Conditions:")
    print("1. c_T^2 = 1 condition:")
    sp.pprint(ct_condition)
    print("\n2. Scalar no-ghost condition (A_S = 0):")
    sp.pprint(A_S_condition)


if __name__ == '__main__':
    derive_stability_conditions()
