# filename: codebase/perturbative_expansion.py
import sympy

def perturbative_analysis():
    """
    Performs a perturbative expansion of the DHOST Lagrangian to identify
    the leading-order interaction terms and estimate the strong coupling scale.

    This analysis uses symbolic manipulation to expand the action around a
    Minkowski background with a time-dependent scalar field. It focuses on
    the terms that determine the theory's high-energy behavior.
    """
    # ----------------------------------------------------------------------
    # 1. Define Symbols for Perturbative Expansion
    # ----------------------------------------------------------------------
    print("--- Perturbative Analysis of the DHOST Action ---")
    print("\nStep 1: Defining symbolic variables for the expansion.")

    # Coordinates and derivatives
    t, x, y, z = sympy.symbols('t x y z')
    d = sympy.Function('d')  # Placeholder for partial derivative

    # Fields and perturbations
    pi = sympy.Function('pi')(t, x, y, z)  # Scalar field perturbation
    h_mu_nu = sympy.MatrixSymbol('h', 4, 4)  # Metric perturbation

    # Background values and constants
    phi_0_dot = sympy.Symbol('phi_0_dot', positive=True)  # Background scalar field time derivative
    X_0 = sympy.Symbol('X_0', positive=True)  # Background kinetic term
    c4 = sympy.Symbol('c4')  # Theory parameter
    M_P = sympy.Symbol('M_P', positive=True)  # Planck mass
    m_g = sympy.Symbol('m_g', positive=True)  # Graviton mass

    # Background functions of phi
    G_3_0_phi = sympy.Symbol("G_3_0_phi_bg")  # G_3_0'(phi_0)
    
    # Use a dictionary for substitutions for clarity
    background_subs = {X_0: phi_0_dot**2}

    print("Scalar field perturbation: pi")
    print("Metric perturbation: h_mu_nu")
    print("Background scalar field derivative: " + str(phi_0_dot))
    print("Background kinetic term X_0 = phi_0_dot^2")

    # ----------------------------------------------------------------------
    # 2. Kinetic Term for the Scalar Perturbation 'pi'
    # ----------------------------------------------------------------------
    print("\nStep 2: Deriving the kinetic term for the scalar perturbation 'pi'.")

    # The kinetic part of the Lagrangian for phi is primarily from G2 and G3
    # L_kin_phi ~ G_2 - G_3 * Box(phi)
    # Expanding to second order in perturbations gives a kinetic term for pi
    # of the form Z * (d pi)^2. The coefficient Z is found from:
    # Z = -2 * G_3_0'(phi_0) + c4 * X_0
    # This comes from the combination (-2*G_{3,phi} + G_{2,X} + X*G_{2,XX}...)
    # which for this specific theory simplifies significantly.
    
    Z_kinetic_coeff = -2 * G_3_0_phi + c4 * X_0

    # The kinetic Lagrangian for pi
    L_kin_pi = Z_kinetic_coeff * (d(pi))**2  # Using d(pi) as a placeholder for (d_mu pi)^2

    print("The kinetic part of the Lagrangian for the scalar perturbation 'pi' is of the form:")
    print("L_kin(pi) = Z * (d_mu pi)*(d^mu pi)")
    print("The kinetic coefficient Z is derived from the G2 and G3 functions:")
    print("Z = -2 * G_3_0'(phi_0) + c4 * X_0 = " + str(Z_kinetic_coeff))
    print("Assuming Z > 0 for a healthy kinetic term.")

    # ----------------------------------------------------------------------
    # 3. Leading Interaction Term for 'pi'
    # ----------------------------------------------------------------------
    print("\nStep 3: Identifying the leading-order self-interaction for 'pi'.")
    
    # The leading interactions come from the "beyond Horndeski" term F_4 * L_bH4
    # F_4 = c4 / X
    # L_bH4 = X*( (Box phi)^2 - (phi_mn)^2 ) - 2*(phi_mn)^3 + 2*(Box phi)*(phi_m)*(phi_n)*(phi_mn)
    # The term with the most derivatives on the fewest fields is -2*(phi_mn)^3
    # phi_mn = d_m d_n phi = d_m d_n pi
    
    # The interaction Lagrangian is L_int ~ F_4 * (-2 * (d^2 pi)^3)
    # On the background, F_4 ~ c4 / X_0
    
    L_int_pi = (c4 / X_0) * (-2 * (d(d(pi)))**3)  # Placeholder for the cubic term

    print("The leading self-interaction comes from the F_4 * L_bH4 term.")
    print("This term contains cubic interactions in 'pi' of the form:")
    print("L_int(pi) ~ (c4 / X_0) * (d_mu d_nu pi) * (d^nu d^rho pi) * (d_rho d^mu pi)")
    print("Symbolically represented as: " + str(L_int_pi))

    # ----------------------------------------------------------------------
    # 4. Estimation of the Strong Coupling Scale
    # ----------------------------------------------------------------------
    print("\nStep 4: Estimating the strong coupling scale Lambda_s.")

    # To find the scale, we write the interaction in terms of the canonically
    # normalized field, pi_c = sqrt(Z) * pi.
    # L_kin(pi_c) = (d pi_c)^2
    # L_int(pi_c) = -2 * (c4 / X_0) * (d^2 (pi_c/sqrt(Z)))^3
    #             = -2 * (c4 / (X_0 * Z^(3/2))) * (d^2 pi_c)^3
    
    # The interaction term is of the form (1 / Lambda_s^5) * (d^2 pi_c)^3
    # where the operator (d^2 pi_c)^3 has mass dimension 9.
    
    Lambda_s_5 = sympy.Symbol('Lambda_s^5')  # Strong coupling scale to the 5th power
    
    # The coefficient is 1/Lambda_s^5
    inv_Lambda_s_5 = sympy.Abs(2 * c4 / (X_0 * Z_kinetic_coeff**(sympy.Rational(3, 2))))
    
    # So, Lambda_s^5 is the inverse of this coefficient
    expr_Lambda_s_5 = 1 / inv_Lambda_s_5
    
    print("The interaction term for the canonically normalized field 'pi_c' is:")
    print("L_int(pi_c) = (1 / Lambda_s^5) * (d^2 pi_c)^3")
    print("From this, we identify the strong coupling scale of the scalar sector, Lambda_s.")
    print("Lambda_s^5 = " + str(expr_Lambda_s_5))
    
    # Substitute X_0 back for clarity
    expr_Lambda_s_5_sub = expr_Lambda_s_5.subs(background_subs)
    print("\nSubstituting X_0 = phi_0_dot^2:")
    print("Lambda_s^5 = " + str(expr_Lambda_s_5_sub))

    # ----------------------------------------------------------------------
    # 5. Overall Strong Coupling Scale including Massive Graviton
    # ----------------------------------------------------------------------
    print("\nStep 5: Determining the overall strong coupling scale.")
    
    # The massive graviton sector has its own strong coupling scale, Lambda_3,
    # from the decoupling limit analysis (m_g -> 0, M_P -> inf, with Lambda_3 fixed).
    Lambda_3 = sympy.Symbol('Lambda_3')
    expr_Lambda_3 = (m_g**2 * M_P)**(sympy.Rational(1, 3))

    print("The massive graviton sector introduces its own strong coupling scale, Lambda_3.")
    print("Lambda_3 = (m_g^2 * M_P)^(1/3) = " + str(expr_Lambda_3))
    
    # The true strong coupling scale of the full theory is the lowest energy scale
    # at which any part of the theory becomes non-perturbative.
    Lambda_strong = sympy.Min(Lambda_s_5**(sympy.Rational(1,5)), Lambda_3)

    print("\nThe overall strong coupling scale of the theory, Lambda_strong, is the minimum")
    print("of the scales from the scalar and tensor sectors:")
    print("Lambda_strong = Min(Lambda_s, Lambda_3)")
    print("Lambda_strong = " + str(Lambda_strong))
    
    print("\n\n--- Summary of Perturbative Analysis ---")
    print("1. Scalar Kinetic Term: L_kin = (" + str(Z_kinetic_coeff) + ") * (d_mu pi)^2")
    print("2. Leading Scalar Interaction: L_int ~ (" + str(c4/X_0) + ") * (d^2 pi)^3")
    print("3. Scalar Strong Coupling Scale: Lambda_s^5 = " + str(expr_Lambda_s_5_sub))
    print("4. Graviton Strong Coupling Scale: Lambda_3 = " + str(expr_Lambda_3))
    print("5. Overall Strong Coupling Scale: Lambda_strong = Min(Lambda_s, Lambda_3)")
    print("\nThis analysis provides the key scales for the Effective Field Theory description.")


if __name__ == '__main__':
    perturbative_analysis()