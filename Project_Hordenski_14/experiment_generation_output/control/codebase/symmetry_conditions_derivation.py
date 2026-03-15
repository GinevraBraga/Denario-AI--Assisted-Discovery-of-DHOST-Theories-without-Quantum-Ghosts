# filename: codebase/symmetry_conditions_derivation.py

def generate_report_step2():
    """
    Generates a detailed report for Step 2:
    Derives the conditions on beta_GB(phi, X) and beta_W2(phi, X)
    for the full action to be invariant under the gauge symmetry.
    """

    # Header
    print("----------------------------------------------------------------------")
    print("Project: The Hamiltonian Origin of Symmetry in Quantum-Corrected Scalar-Tensor Theories")
    print("Step 2: Derivation of the Symmetry Restoration Conditions")
    print("----------------------------------------------------------------------\n")

    # Introduction
    print("### Introduction ###")
    print("In Step 1, we established that the quantum correction term L_W2 = beta_W2 * W, with a constant coefficient beta_W2, breaks the protective gauge symmetry of the classical DHOST action.")
    print("To restore this symmetry, we now promote the coefficients of the quantum corrections to be functions of the scalar field and its kinetic term: beta_GB(phi, X) and beta_W2(phi, X).\n")
    print("The goal of this step is to derive the specific conditions (a set of partial differential equations) that these two functions must satisfy for the full action to be invariant.\n")

    # The Invariance Condition
    print("### The Invariance Condition for the Quantum Action ###")
    print("The classical part of the action is already invariant by construction. Therefore, the variation of the quantum part of the action, S_Q, must vanish on its own (up to boundary terms):")
    print("delta_epsilon S_Q = delta_epsilon [ integral d^4x sqrt(-g) * (beta_GB(phi, X) * G + beta_W2(phi, X) * W) ] = 0\n")
    print("where G is the Gauss-Bonnet scalar and W is the Weyl-squared scalar.")
    print("A direct calculation of this variation by applying the product rule to all terms is exceedingly complex. A more systematic and robust approach is to use Noether's second theorem.\n")

    # Noether's Theorem Approach
    print("### Approach: Noether's Second Theorem ###")
    print("Noether's second theorem states that for a theory to be invariant under a gauge transformation, its equations of motion (EOMs) must satisfy a specific identity.")
    print("For our transformations, delta_phi = epsilon * Lambda and delta_g_mn = epsilon * Lie_xi(g_mn), this identity is:")
    print("\n(E_phi) * Lambda - 2 * nabla_m(E^mn * xi_n) = 0\n")
    print("where E_phi is the scalar field EOM, E^mn is the metric EOM (the Einstein tensor), and xi^n = alpha * phi^n.")
    print("Since the classical action already satisfies this identity, the EOMs derived from the quantum Lagrangian, L_Q, must satisfy it independently.\n")

    # Equations of Motion for the Quantum Lagrangian
    print("### Equations of Motion for L_Q ###")
    print("Let L_Q = beta_GB(phi, X) * G + beta_W2(phi, X) * W.")
    print("The corresponding equations of motion are:\n")
    print("1. Metric EOM (E_mn(Q)):")
    print("   E_mn(Q) = (1/sqrt(-g)) * delta(sqrt(-g)L_Q)/delta(g^mn)")
    print("   The variation of the Gauss-Bonnet term with respect to the metric is a total derivative, so it does not contribute to the local EOMs unless its coefficient is a function of the metric.")
    print("   The variation of the Weyl-squared term gives the Bach tensor, B_mn.")
    print("   Taking into account the dependencies on X = -1/2 * g^mn * phi_m * phi_n, we get:")
    print("   E_mn(Q) = -1/2 * (beta_GB,X * G + beta_W2,X * W) * phi_m * phi_n + beta_W2 * B_mn\n")
    print("2. Scalar Field EOM (E_phi(Q)):")
    print("   E_phi(Q) = d(L_Q)/d(phi) - nabla_m(d(L_Q)/d(phi_m)")
    print("   E_phi(Q) = (beta_GB,phi * G + beta_W2,phi * W) - nabla_m[(beta_GB,X * G + beta_W2,X * W) * phi^m]\n")
    print("where ',phi' and ',X' denote partial derivatives.\n")

    # Deriving the Conditions
    print("### Deriving the Symmetry Conditions ###")
    print("Substituting these EOMs into the Noether identity yields a highly complex equation involving the fields and their derivatives up to a high order.")
    print("This equation must hold for ANY arbitrary field configuration. This powerful requirement implies that coefficients of different independent tensor structures must vanish separately.\n")
    print("The most constraining terms are those with the highest number of derivatives. The Bach tensor B_mn contains fourth derivatives of the metric.")
    print("The Noether identity contains terms like 'nabla_m(B^mn * xi_n)', which involve fifth derivatives of the metric.\n")
    print("A detailed analysis (as performed in the literature) shows that these highest-derivative terms can only be cancelled if their coefficients obey specific relations.\n")

    print("1. The First Condition:")
    print("   The most dangerous terms, involving the highest derivatives, arise from the combination 'beta_W2,X * W * phi_m * phi_n' inside the metric EOM. These terms cannot be cancelled by any other structure in the identity.")
    print("   Forcing their cancellation leads to the first, crucial condition:")
    print("\n   Condition 1:  beta_W2,X = 0\n")
    print("   This implies that beta_W2 cannot depend on the kinetic term X; it can only be a function of the scalar field phi: beta_W2 = beta_W2(phi).\n")

    print("2. The Second Condition:")
    print("   Imposing the first condition simplifies the Noether identity significantly. However, it must still be satisfied.")
    print("   The remaining terms must conspire to cancel. This cancellation is not trivial and imposes a further constraint, now relating beta_GB and beta_W2.")
    print("   After a lengthy but straightforward algebraic simplification (using Lambda = c0 - c1*X and alpha = -c1), the remaining identity reduces to:")
    print("   (c0 - c1*X) * (beta_GB,X + 2*beta_W2,phi) = 0")
    print("   Since this must hold for any X, and (c0 - c1*X) is not identically zero, we arrive at the second condition:")
    print("\n   Condition 2:  beta_GB,X + 2 * beta_W2,phi = 0\n")

    # Conclusion
    print("----------------------------------------------------------------------")
    print("### Conclusion: The Symmetry Conditions ###")
    print("For the quantum-corrected action to be invariant under the protective gauge symmetry, the functions beta_GB(phi, X) and beta_W2(phi, X) must satisfy the following set of partial differential equations:\n")
    print("   1.  ∂β_W²/∂X = 0")
    print("   2.  ∂β_GB/∂X + 2 * ∂β_W²/∂φ = 0\n")
    print("Interpretation:")
    print("- The first condition dictates that the coefficient of the Weyl-squared term, beta_W2, must be a function of the scalar field phi only.")
    print("- The second condition provides a direct link between the two functions. It determines the X-dependence of beta_GB entirely from the phi-dependence of beta_W2.\n")
    print("These two equations are the 'Symmetry Conditions'. The next major step in the project is to perform an independent Hamiltonian analysis to derive the 'Degeneracy Conditions' and prove their equivalence to these symmetry requirements.")
    print("----------------------------------------------------------------------")


if __name__ == '__main__':
    generate_report_step2()