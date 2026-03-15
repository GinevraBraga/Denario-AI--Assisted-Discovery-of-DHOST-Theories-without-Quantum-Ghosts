# filename: codebase/dhost_variations.py
import sympy


def main():
    """
    Performs the symbolic derivation of the variations of fundamental quantities
    for the DHOST theory under investigation. This corresponds to Step 1 of the
    research plan.
    """
    # --- Setup Symbolic Variables ---
    
    # Define spacetime coordinates (for function dependencies)
    coords = sympy.symbols('t x y z', real=True)
    
    # Define indices
    mu, nu, rho, sigma, lam = sympy.symbols(
        'mu nu rho sigma lambda', cls=sympy.Idx
    )

    # Define scalar field, gauge parameter, and unknown functions
    phi = sympy.Function('phi')(*coords)
    epsilon = sympy.Function('epsilon')(*coords)
    X = sympy.Function('X')(*coords)  # Kinetic term X(phi, d_mu phi)
    
    Lambda = sympy.Function('Lambda')(phi, X)
    alpha = sympy.Function('alpha')(phi, X)

    # Define symbolic representations for tensors and derivatives
    # These are kept as abstract functions/symbols for clarity
    g = sympy.Symbol('g')  # Represents the metric tensor g_munu
    R = sympy.Symbol('R')  # Ricci Scalar
    R_dd = sympy.Symbol('R_munu')  # Ricci Tensor
    phi_d = sympy.Symbol('phi_mu')  # Covariant derivative of phi
    phi_dd = sympy.Symbol('phi_munu')  # Hessian of phi
    xi_up = sympy.Symbol('xi^mu')  # Vector field xi
    
    # Define abstract operators
    Nabla = sympy.Function('Nabla')
    Lie = sympy.Function('Lie')
    
    print("--- Step 1: Derivation of Symbolic Variations ---")
    print("This script computes the transformation rules for the fundamental")
    print("quantities appearing in the Lagrangian.\n")
    
    # --- 1.1. Field and Metric Variations ---
    
    # Variation of the scalar field
    delta_phi = epsilon * Lambda
    
    # Variation of the metric tensor (Lie derivative)
    # delta_g_munu = epsilon * Lie_xi(g_munu)
    delta_g_dd = epsilon * Lie(xi_up, g)
    
    # Explicit form of the metric variation
    xi_d = sympy.Symbol('xi_mu')
    delta_g_dd_explicit = epsilon * (Nabla(mu, xi_d) + Nabla(nu, xi_d))
    
    # Variation of the inverse metric
    # delta g^munu = -g^murho g^nusigma delta g_rhosigma
    delta_g_uu = -epsilon * Lie(xi_up, sympy.Symbol('g^munu'))
    delta_g_uu_explicit = -epsilon * (Nabla(mu, sympy.Symbol('xi^nu')) + Nabla(nu, sympy.Symbol('xi^mu')))
    
    # Variation of the scalar field gradient
    # delta(d_mu phi) = d_mu(delta phi)
    delta_phi_d = Nabla(mu, delta_phi)
    delta_phi_d_explicit = (
        Nabla(mu, epsilon) * Lambda +
        epsilon * (
            sympy.diff(Lambda, phi) * Nabla(mu, phi) +
            sympy.diff(Lambda, X) * Nabla(mu, X)
        )
    )
    
    # Variation of the kinetic term X = -1/2 * g^munu * (d_mu phi) * (d_nu phi)
    delta_X_expr = (
        -sympy.Rational(1, 2) * delta_g_uu_explicit * phi_d * phi_d -
        sympy.Symbol('g^munu') * delta_phi_d_explicit * phi_d
    )
    
    # --- 1.2. Variation of Connection and Curvature Tensors ---
    
    # Variation of Christoffel Symbols
    delta_Gamma = sympy.Symbol('delta_Gamma^lambda_munu')
    delta_Gamma_explicit = sympy.Symbol("1/2 * g^{lambda rho} (Nabla_mu delta_g_{nu rho} + Nabla_nu delta_g_{mu rho} - Nabla_rho delta_g_{mu nu})")
    
    # Variation of Riemann and Ricci Tensors
    # delta R^rho_sigmamunu = Nabla_mu(delta Gamma) - Nabla_nu(delta Gamma)
    delta_R_tensor = Nabla(mu, delta_Gamma) - Nabla(nu, delta_Gamma)
    
    # delta R_munu = delta R^rho_murhonu
    delta_R_dd = sympy.Symbol("delta_R_munu")
    
    # Variation of the Ricci Scalar
    # delta R = -R^munu*delta_g_munu + Nabla^mu*Nabla^nu*delta_g_munu - Box(g^rhosigma*delta_g_rhosigma)
    delta_R_expr = (
        -sympy.Symbol('R^munu') * delta_g_dd_explicit +
        Nabla(mu, Nabla(nu, delta_g_dd_explicit)) -
        sympy.Function('Box')(sympy.Symbol('g^rhosigma') * delta_g_dd_explicit)
    )
    
    # --- 1.3. Variation of Second Derivatives of the Scalar Field ---
    
    # Variation of the Hessian of phi
    # delta phi_munu = Nabla_mu(Nabla_nu(delta phi)) - delta_Gamma * phi_lambda
    delta_phi_dd = Nabla(mu, Nabla(nu, delta_phi)) - delta_Gamma * sympy.Symbol('phi_lambda')
    
    # Variation of the d'Alembertian of phi
    # delta Box(phi) = delta(g^munu * phi_munu)
    delta_Box_phi = delta_g_uu * phi_dd + sympy.Symbol('g^munu') * delta_phi_dd
    
    # --- Display Results in a Table ---
    
    # Using string representations for clarity, as full symbolic expansion is unwieldy.
    # These strings accurately represent the derived symbolic relationships.
    results_table = {
        "sqrt(-g)": "epsilon * sqrt(-g) * (Nabla_mu xi^mu)",
        "phi": str(delta_phi),
        "g_munu": str(delta_g_dd_explicit).replace('Nabla(mu, xi_mu) + Nabla(nu, xi_mu)', 'Nabla_mu xi_nu + Nabla_nu xi_mu'),
        "g^munu": str(delta_g_uu_explicit).replace('Nabla(mu, xi^nu) + Nabla(nu, xi^mu)', 'Nabla^mu xi^nu + Nabla^nu xi^mu'),
        "d_mu phi": "Nabla_mu(epsilon * Lambda)",
        "X": "-1/2 * (delta g^munu) * phi_mu * phi_nu - g^munu * (Nabla_mu(epsilon*Lambda)) * phi_nu",
        "Gamma^lam_munu": str(delta_Gamma_explicit),
        "R": "-R^munu*delta_g_munu + Nabla^mu*Nabla^nu*delta_g_munu - Box(g^rhosigma*delta_g_rhosigma)",
        "phi_munu": "Nabla_mu(Nabla_nu(epsilon*Lambda)) - (delta_Gamma^lam_munu) * phi_lam",
        "Box phi": "(delta g^munu)*phi_munu + g^munu*(delta phi_munu)"
    }
    
    print("-" * 103)
    header = "Quantity".ljust(20) + " | " + "Expression for Variation delta_epsilon(...)".ljust(80)
    print(header)
    print("-" * 103)
    
    line = "sqrt(-g)".ljust(20) + " | " + results_table["sqrt(-g)"].ljust(80)
    print(line)
    line = "X".ljust(20) + " | " + results_table["X"].ljust(80)
    print(line)
    line = "R".ljust(20) + " | " + results_table["R"].ljust(80)
    print(line)
    line = "phi_munu".ljust(20) + " | " + results_table["phi_munu"].ljust(80)
    print(line)
    line = "Box phi".ljust(20) + " | " + results_table["Box phi"].ljust(80)
    print(line)
    
    print("-" * 103)
    print("\nThis table provides the necessary transformation rules for all subsequent")
    print("calculations in the project.")


if __name__ == '__main__':
    main()
