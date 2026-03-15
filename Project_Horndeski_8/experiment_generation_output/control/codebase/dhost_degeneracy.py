# filename: codebase/dhost_degeneracy.py
import sympy

def derive_degeneracy_condition():
    """
    Symbolically derives the general degeneracy condition for DHOST theories.

    This function follows the procedure outlined in arXiv:1811.06271.
    1. It starts from the kinetic part of the quadratic action for metric
       perturbations in unitary gauge, which is characterized by two
       functions, A_cal and B_cal.
    2. The degeneracy condition, which eliminates a ghostly scalar degree of
       freedom, is given by 3*A_cal + B_cal = 0.
    3. The functions A_cal and B_cal are expressed in terms of intermediate
       functions f_n, g_n, h_n (for n=2,3,4,5), which depend on the
       free functions of the general DHOST Lagrangian.
    4. The script defines all these functions symbolically and computes the
       final degeneracy condition.
    """
    # Define symbolic variables
    X = sympy.Symbol('X')
    
    # Define the free functions of the DHOST Lagrangian and their derivatives
    F2 = sympy.Function('F_2')(X)
    
    # Cubic functions a_A and their derivatives
    a = [sympy.Function('a_' + str(i))(X) for i in range(1, 6)]
    a_X = [sympy.diff(f, X) for f in a]
    a_XX = [sympy.diff(f, X, 2) for f in a]

    # Quartic functions b_A and their derivatives
    b = [sympy.Function('b_' + str(i))(X) for i in range(1, 11)]
    b_X = [sympy.diff(f, X) for f in b]
    b_XX = [sympy.diff(f, X, 2) for f in b]

    # Quintic functions c_A and their derivatives
    c = [sympy.Function('c_' + str(i))(X) for i in range(1, 11)]
    c_X = [sympy.diff(f, X) for f in c]
    c_XX = [sympy.diff(f, X, 2) for f in c]

    # Unpack for easier access
    a1, a2, a3, a4, a5 = a
    a1_X, a2_X, a3_X, a4_X, a5_X = a_X
    a5_XX = a_XX[4]

    b1, b2, b3, b4, b5, b6, b7, b8, b9, b10 = b
    b3_X, b4_X, b6_X, b7_X, b8_X = b_X[2], b_X[3], b_X[5], b_X[6], b_X[7]
    b6_XX, b9_XX, b10_XX = b_XX[5], b_XX[8], b_XX[9]

    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = c
    c1_X, c2_X, c3_X, c4_X, c5_X, c6_X, c7_X = c_X[0], c_X[1], c_X[2], c_X[3], c_X[4], c_X[5], c_X[6]
    c1_XX, c2_XX, c3_XX, c4_XX, c5_XX = c_XX[0], c_XX[1], c_XX[2], c_XX[3], c_XX[4]
    
    print("--- Step 1: Deriving the General DHOST Degeneracy Condition ---")
    print("\nWe start with the quadratic action for metric perturbations h_ij in unitary gauge:")
    print("S^(2) = integral(dt d^3x * a^3 * [1/2 * K_ijkl * dot(h)_ij * dot(h)_kl + ...])")
    print("The kinetic matrix K_ijkl can be decomposed as:")
    print("K_ijkl = A_cal * delta_ij * delta_kl + B_cal * (delta_ik*delta_jl + delta_il*delta_jk)")
    print("\nTo avoid a ghost instability, the kinetic term for the scalar mode must vanish.")
    print("This imposes the degeneracy condition: 3*A_cal + B_cal = 0\n")
    
    # Define f_n, h_n functions from arXiv:1811.06271, Appendix B
    # n=2 (Quadratic)
    f2 = 2 * F2
    
    # n=3 (Cubic)
    f3 = -2*a1 - a2 - 2*X*a2_X
    h3 = -2*a1 - a2 - (sympy.S(2)/3)*X*a3_X - (sympy.S(4)/3)*X**2*a4_X - (sympy.S(4)/3)*X**3*a5_XX

    # n=4 (Quartic)
    f4 = 6*(b1 + b2) + 2*(b3 + b4 + b5) + 4*X*(b3_X + b4_X) + 4*X**2*b6_XX
    h4 = 2*(b3 + b4 + b5) + (sympy.S(4)/3)*X*(b7_X + b8_X) + (sympy.S(4)/3)*X**2*(b9_XX + b10_XX)

    # n=5 (Quintic)
    f5 = -2*(c1 + c2 + c3 + c4 + c5) - 2*X*(c1_X + c2_X + c3_X + c4_X) - 2*X**2*(c1_XX + c2_XX)
    h5 = -2*(c1 + c2 + c3 + c4 + c5) - (sympy.S(4)/3)*X*(c6_X + c7_X) - (sympy.S(2)/3)*X**2*(c3_XX + c4_XX) - (sympy.S(4)/3)*X**3*(c5_XX)

    print("The coefficients A_cal and B_cal depend on the DHOST Lagrangian functions.")
    print("Following arXiv:1811.06271, the degeneracy condition can be expressed using a set of intermediate functions f_n and h_n (n=2..5).")
    print("The condition is: f_2 + X*(f_3 - 3*h_3) + X^2*(f_4 - 3*h_4) + X^3*(f_5 - 3*h_5) = 0\n")
    
    # The degeneracy condition is 3*A_cal + B_cal = 0.
    # From arXiv:1811.06271, Eq. (B2), this is equivalent to:
    # f_2 + X*(f_3 - 3*h_3) + X^2*(f_4 - 3*h_4) + X^3*(f_5 - 3*h_5) = 0
    
    degeneracy_condition = f2 + X*(f3 - 3*h3) + X**2*(f4 - 3*h4) + X**3*(f5 - 3*h5)
    
    # Simplify the expression
    degeneracy_condition_simplified = sympy.simplify(degeneracy_condition)

    print("--- General DHOST Degeneracy Condition ---")
    print("Substituting the expressions for f_n and h_n, we obtain the explicit degeneracy condition.")
    print("The theory is degenerate (free of a ghost-like instability at the classical level) if the following equation holds:")
    
    print("\nDegeneracy Condition = 0, where:")
    print("Degeneracy Condition = " + str(degeneracy_condition_simplified))

    print("\n\nThis expression is the general degeneracy condition for the full DHOST Lagrangian as presented in arXiv:1811.06271.")
    print("It is an algebraic constraint on the free functions (F2, a_A, b_A, c_A) and their derivatives with respect to X.")
    print("In the next step, we will restrict this general condition to the Type Ia subclass and verify that it is automatically satisfied.")

if __name__ == '__main__':
    derive_degeneracy_condition()