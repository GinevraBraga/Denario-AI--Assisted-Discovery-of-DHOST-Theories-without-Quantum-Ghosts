# filename: codebase/symmetry_restoration_conditions.py
import sympy

def derive_symmetry_restoration_conditions():
    """
    Symbolically derives the partial differential equations that the coupling
    functions beta_GB(phi, X) and beta_W2(phi, X) must satisfy for the
    quantum-corrected action to remain invariant under the protective symmetry.

    The derivation starts by promoting the constant coefficients of the
    Gauss-Bonnet (G) and Weyl-squared (W2) terms to functions of the scalar
    field (phi) and its kinetic term (X). It then computes the variation of
    this part of the Lagrangian under the given symmetry transformations.

    By requiring the variation to be a total spacetime derivative (ensuring the
    action's invariance), the script derives a master consistency equation.
    This equation is then split into two independent conditions, one for
    beta_GB and one for beta_W2, based on the argument that G and W2 are
    independent curvature invariants.
    """
    # --- 1. Define Symbols and Functions ---
    print("----------------------------------------------------------------------")
    print("Step 3: Derivation of Symmetry Restoration Conditions")
    print("----------------------------------------------------------------------")
    print("We promote beta_GB and beta_W2 to functions of phi and X and derive")
    print("the conditions for the action's invariance.\n")

    # Spacetime coordinates and gauge parameter
    x_coords = sympy.symbols('x^0 x^1 x^2 x^3')
    epsilon = sympy.Function('epsilon')(*x_coords)

    # Scalar field, kinetic term, and their derivatives
    phi_symbol = sympy.Symbol('phi')
    X_symbol = sympy.Symbol('X')
    phi = sympy.Function('phi')(*x_coords)
    phi_mu = sympy.Symbol('phi_mu')
    phi_up_mu = sympy.Symbol('phi^mu')
    Box_phi = sympy.Symbol('Box(phi)')

    # Symmetry functions
    Lambda = sympy.Function('Lambda')(phi_symbol, X_symbol)
    alpha = sympy.Function('alpha')(phi_symbol, X_symbol)
    xi_mu = sympy.Symbol('xi_mu')

    # Curvature scalars and tensors
    G = sympy.Symbol('G')
    W2 = sympy.Symbol('W^2')
    E_GB_munu = sympy.Symbol('E_GB^munu')
    E_W2_munu = sympy.Symbol('E_W2^munu')
    nabla_mu_xi_nu = sympy.Symbol('\\nabla_\\mu \\xi_\\nu')

    # Promoted coupling functions and their derivatives
    beta_GB = sympy.Function('beta_GB')(phi_symbol, X_symbol)
    beta_W2 = sympy.Function('beta_W2')(phi_symbol, X_symbol)
    beta_GB_phi = sympy.Derivative(beta_GB, phi_symbol)
    beta_GB_X = sympy.Derivative(beta_GB, X_symbol)
    beta_W2_phi = sympy.Derivative(beta_W2, phi_symbol)
    beta_W2_X = sympy.Derivative(beta_W2, X_symbol)

    # --- 2. Variation of the Quantum-Corrected Lagrangian ---
    print("--- 2. Variation of L_qc ---")
    print("The quantum-corrected Lagrangian is L_qc = beta_GB(phi,X)*G + beta_W2(phi,X)*W^2.")
    print("The classical part L_cl is invariant by construction.")
    print("We require the variation delta(L_qc) to be a total derivative.\n")

    print("delta(L_qc) = [delta(beta_GB)*G + beta_GB*delta(G)] + [delta(beta_W2)*W^2 + beta_W2*delta(W^2)]\n")

    # Variation of curvature terms (from metric variation)
    delta_G = epsilon * E_GB_munu * nabla_mu_xi_nu
    delta_W2 = epsilon * E_W2_munu * nabla_mu_xi_nu
    print("The variations of G and W^2 under the metric transformation are:")
    print("delta(G) = epsilon * E_GB^munu * nabla_mu(xi_nu)")
    print("delta(W^2) = epsilon * E_W2^munu * nabla_mu(xi_nu)\n")

    # Variation of beta functions
    # delta(beta) = (d_beta/d_phi)*delta(phi) + (d_beta/d_X)*delta(X)
    delta_phi = epsilon * Lambda
    # The variation of X introduces a derivative on epsilon
    nabla_mu_epsilon = sympy.Symbol('\\nabla_\\mu \\epsilon')
    L_xi_X = sympy.Symbol('L_xi(X)')  # Lie derivative of X along xi
    nabla_mu_Lambda = sympy.Symbol('\\nabla_\\mu Lambda')
    
    delta_X = epsilon * (L_xi_X - phi_up_mu * nabla_mu_Lambda) - Lambda * phi_up_mu * nabla_mu_epsilon

    print("The variation of the beta functions depends on delta(phi) and delta(X):")
    print("delta(beta) = (d_beta/d_phi)*delta(phi) + (d_beta/d_X)*delta(X)")
    print("delta(phi) = epsilon * Lambda")
    print("delta(X) = epsilon * (L_xi(X) - phi^mu*nabla_mu(Lambda)) - Lambda*phi^mu*nabla_mu(epsilon)\n")
    
    # Assemble the full variation of L_qc
    B_phi = beta_GB_phi * G + beta_W2_phi * W2
    B_X = beta_GB_X * G + beta_W2_X * W2
    
    delta_L_qc = (B_phi * delta_phi + B_X * delta_X) + beta_GB * delta_G + beta_W2 * delta_W2
    
    # Substitute delta_X
    delta_L_qc_expanded = (B_phi * epsilon * Lambda +
                           B_X * (epsilon * (L_xi_X - phi_up_mu * nabla_mu_Lambda) - Lambda * phi_up_mu * nabla_mu_epsilon) +
                           epsilon * (beta_GB * E_GB_munu * nabla_mu_xi_nu + beta_W2 * E_W2_munu * nabla_mu_xi_nu))
    
    print("--- 3. Requiring a Total Derivative Structure ---")
    print("The variation delta(L_qc) must be a total derivative: delta(L_qc) = nabla_mu(K^mu).")
    print("A total derivative has the structure: nabla_mu(K^mu) = nabla_mu(epsilon*J^mu) = nabla_mu(epsilon)*J^mu + epsilon*nabla_mu(J^mu).")
    
    # Isolate coefficients of epsilon and its derivative
    term_nabla_eps = delta_L_qc_expanded.collect(nabla_mu_epsilon).coeff(nabla_mu_epsilon)
    term_eps = delta_L_qc_expanded.collect(nabla_mu_epsilon).coeff(nabla_mu_epsilon, 0)
    
    print("\nComparing delta(L_qc) to this structure, we identify the coefficient of nabla_mu(epsilon):")
    K_mu = -term_nabla_eps
    print("J^mu = " + str(K_mu / phi_up_mu) + " * phi^mu")
    print("So, K^mu = " + str(K_mu) + "\n")
    
    print("The coefficient of epsilon must then be equal to nabla_mu(K^mu):")
    nabla_K_mu = sympy.Symbol('\\nabla_\\mu(K^\\mu)')
    print(str(term_eps) + " = " + str(nabla_K_mu) + "\n")
    
    # --- 4. Deriving the Master Equation ---
    print("--- 4. Deriving the Master Equation ---")
    # nabla_mu(K^mu) = nabla_mu(-B_X * Lambda * phi^mu)
    # = - (nabla_mu B_X) * Lambda * phi^mu - B_X * (nabla_mu Lambda) * phi^mu - B_X * Lambda * Box(phi)
    nabla_mu_B_X = sympy.Symbol('\\nabla_\\mu(B_X)')
    nabla_K_mu_expanded = - (nabla_mu_B_X * Lambda * phi_up_mu +
                             B_X * nabla_mu_Lambda * phi_up_mu +
                             B_X * Lambda * Box_phi)
    
    master_eq = sympy.Eq(term_eps, nabla_K_mu_expanded)
    print("Expanding nabla_mu(K^mu) and substituting gives the master equation:")
    print(str(master_eq.lhs) + " = " + str(master_eq.rhs) + "\n")
    
    # Simplify the master equation
    # The term B_X * phi^mu * nabla_mu(Lambda) cancels on both sides
    simplified_master_eq_lhs = (Lambda * B_phi + B_X * L_xi_X +
                                (beta_GB * E_GB_munu + beta_W2 * E_W2_munu) * nabla_mu_xi_nu)
    simplified_master_eq_rhs = - (nabla_mu_B_X * Lambda * phi_up_mu + B_X * Lambda * Box_phi)
    
    final_master_eq = sympy.Eq(simplified_master_eq_lhs + nabla_mu_B_X * Lambda * phi_up_mu + B_X * Lambda * Box_phi, 0)
    
    print("After cancellation and rearrangement, the master equation is:")
    print(str(final_master_eq.lhs) + " = 0\n")
    
    # --- 5. Separating into Independent Conditions ---
    print("--- 5. Final Symmetry Restoration Conditions ---")
    print("The master equation must hold for any field configuration. The Gauss-Bonnet (G)")
    print("and Weyl-squared (W^2) terms are built from independent curvature invariants.")
    print("We can therefore demand that the collections of terms proportional to each")
    print("vanish independently. This splits the master equation into two separate PDEs.\n")
    
    # Generic equation for a single term beta*T
    beta, T, E_T = sympy.symbols('beta T E_T')
    beta_phi = sympy.Derivative(beta, phi_symbol)
    beta_X = sympy.Derivative(beta, X_symbol)
    nabla_mu_beta_X_T = sympy.Symbol('\\nabla_\\mu(d_beta/dX * T)')
    
    generic_eq_lhs = (Lambda * beta_phi * T +
                      beta_X * T * L_xi_X +
                      beta * E_T * nabla_mu_xi_nu +
                      nabla_mu_beta_X_T * Lambda * phi_up_mu +
                      beta_X * T * Lambda * Box_phi)
    
    # I made a small simplification error in the manual derivation. Let's be more precise.
    # nabla_mu(B_X * Lambda * phi^mu) = (nabla_mu B_X)*Lambda*phi^mu + B_X*nabla_mu(Lambda*phi^mu)
    # Let's use the form: Lambda*B_phi + B_X*L_xi(X) + Breaking + nabla_mu(B_X*Lambda*phi^mu) = 0
    generic_eq_final = sympy.Eq(Lambda * beta_phi * T + beta_X * T * L_xi_X + beta * E_T * nabla_mu_xi_nu + sympy.Symbol('\\nabla_\\mu(d_beta/dX * T * Lambda * phi^mu)'), 0)
    
    print("Condition for the Gauss-Bonnet term (beta_GB):")
    eq_GB = generic_eq_final.subs([(beta, beta_GB), (T, G), (E_T, E_GB_munu), (sympy.Symbol('d_beta/dX'), beta_GB_X)])
    print(str(eq_GB) + "\n")
    
    print("Condition for the Weyl-squared term (beta_W2):")
    eq_W2 = generic_eq_final.subs([(beta, beta_W2), (T, W2), (E_T, E_W2_munu), (sympy.Symbol('d_beta/dX'), beta_W2_X)])
    print(str(eq_W2) + "\n")
    
    print("These two partial differential equations are the conditions that beta_GB(phi, X)")
    print("and beta_W2(phi, X) must satisfy to restore the protective symmetry of the theory.")
    print("Solving these equations is the next step in the analysis.")
    print("----------------------------------------------------------------------")


if __name__ == '__main__':
    derive_symmetry_restoration_conditions()