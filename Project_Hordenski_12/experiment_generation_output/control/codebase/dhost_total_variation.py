# filename: codebase/dhost_total_variation.py
import sympy

def main():
    """
    Symbolically assembles the total variation of the action and performs
    integration by parts to derive the general structure of the symmetry condition.
    This corresponds to Step 3 of the research plan.
    """
    print("--- Step 3: Assembly and Simplification of the Total Variation ---")
    print("This script outlines the symbolic procedure for integrating the variation")
    print("by parts to find the bulk term that must vanish for symmetry.\n")

    # --- 1. Symbol Definition ---
    # Spacetime coordinates and indices
    coords = sympy.symbols('t x y z', real=True)
    mu, nu, rho, sigma = sympy.symbols('mu nu rho sigma', cls=sympy.Idx)

    # Gauge parameter and operators
    epsilon = sympy.Function('epsilon')(*coords)
    Nabla = sympy.Function('Nabla')
    Integral = sympy.Function('Integral')
    d4x = sympy.Symbol('d^4x')
    sqrt_g = sympy.Symbol('sqrt(-g)')

    # Abstract coefficients for terms with different derivatives of epsilon.
    # The order goes up to 4, as expected from delta(phi_munu).
    A0 = sympy.Symbol('A_0')
    B_mu = sympy.Symbol('B^mu')
    C_munu = sympy.Symbol('C^{munu}')
    D_munurho = sympy.Symbol('D^{munurho}')
    E_munurhosigma = sympy.Symbol('E^{munurhosigma}')

    # --- 2. Initial Structure of the Lagrangian Density Variation ---
    # Based on the analysis in Step 2, the total variation of the Lagrangian
    # density will have terms with up to four derivatives on epsilon.
    
    term0 = A0 * epsilon
    term1 = B_mu * Nabla(mu, epsilon)
    term2 = C_munu * Nabla(mu, Nabla(nu, epsilon))
    term3 = D_munurho * Nabla(mu, Nabla(nu, Nabla(rho, epsilon)))
    term4 = E_munurhosigma * Nabla(mu, Nabla(nu, Nabla(rho, Nabla(sigma, epsilon))))

    delta_L_density = term0 + term1 + term2 + term3 + term4
    
    print("The variation of the Lagrangian density, delta(sqrt(-g)*L), has the general structure:")
    print("delta(L_density) = A_0*epsilon + B^mu*Nabla_mu(epsilon) + C^{munu}*Nabla_mu*Nabla_nu(epsilon) + ...\n")
    sympy.pprint(delta_L_density, use_unicode=False, wrap_line=False)
    print("\nwhere A_0, B^mu, C^{munu}, etc., are coefficients depending on the fields.")
    print("-" * 70)

    # --- 3. Integration by Parts on the Action Variation ---
    # The variation of the action is the integral of delta_L_density.
    delta_S = Integral(delta_L_density * sqrt_g, d4x)

    print("To find the symmetry condition, we integrate by parts to factor out epsilon.")
    print("The total variation of the action is delta_S = Integral(delta(L_density)).\n")

    # Symbolically perform integration by parts for each term
    
    # Term 1: Integral(B^mu * Nabla_mu(epsilon)) -> Integral(-Nabla_mu(B^mu) * epsilon)
    bulk_term_B = -Nabla(mu, B_mu) * epsilon
    boundary_term_B = sympy.Symbol("Boundary(B)")

    # Term 2: Integral(C^{munu} * Nabla_mu*Nabla_nu(epsilon)) -> Integral(Nabla_mu*Nabla_nu(C^{munu}) * epsilon)
    # Note: We use Nabla_nu(Nabla_mu(...)) to be precise about the order.
    bulk_term_C = Nabla(nu, Nabla(mu, C_munu)) * epsilon
    boundary_term_C = sympy.Symbol("Boundary(C)")

    # Term 3: Integral(D^{munurho} * Nabla_mu*Nabla_nu*Nabla_rho(epsilon)) -> Integral(-Nabla_rho*Nabla_nu*Nabla_mu(D^{munurho}) * epsilon)
    bulk_term_D = -Nabla(rho, Nabla(nu, Nabla(mu, D_munurho))) * epsilon
    boundary_term_D = sympy.Symbol("Boundary(D)")

    # Term 4: Integral(E^{munurhosigma} * ...) -> Integral(Nabla_sigma*Nabla_rho*Nabla_nu*Nabla_mu(E^{munurhosigma}) * epsilon)
    bulk_term_E = Nabla(sigma, Nabla(rho, Nabla(nu, Nabla(mu, E_munurhosigma)))) * epsilon
    boundary_term_E = sympy.Symbol("Boundary(E)")

    # --- 4. Assemble the Final Expression for delta_S ---
    
    # The total bulk term is the sum of all terms proportional to epsilon
    total_bulk_integrand = (
        A0 + 
        -Nabla(mu, B_mu) + 
        Nabla(nu, Nabla(mu, C_munu)) +
        -Nabla(rho, Nabla(nu, Nabla(mu, D_munurho))) +
        Nabla(sigma, Nabla(rho, Nabla(nu, Nabla(mu, E_munurhosigma))))
    )
    
    # The total boundary term is the sum of all generated boundary terms
    total_boundary_term = boundary_term_B + boundary_term_C + boundary_term_D + boundary_term_E

    final_delta_S = Integral(total_bulk_integrand * epsilon * sqrt_g, d4x) + total_boundary_term

    print("After integration by parts, the variation of the action becomes:")
    print("delta_S = Integral( [BULK_TERM] * epsilon ) + Boundary_Terms\n")
    
    print("The total boundary term is:")
    sympy.pprint(total_boundary_term, use_unicode=False, wrap_line=False)
    print("\n")

    print("The BULK_TERM, which must vanish for the symmetry to hold, is:")
    sympy.pprint(total_bulk_integrand, use_unicode=False, wrap_line=False)
    print("-" * 70)
    
    print("\nStep 4 will involve analyzing this bulk term. The requirement is that")
    print("this entire expression must be identically zero for the action to be invariant.")


if __name__ == '__main__':
    main()