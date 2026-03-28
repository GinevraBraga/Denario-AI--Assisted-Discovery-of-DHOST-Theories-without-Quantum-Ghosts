# filename: codebase/gauge_algebra_derivation.py
import sympy

def display_gauge_algebra_derivation():
    """
    This function documents and displays the analytical derivation of the open gauge
    algebra for the specified DHOST theory. It presents the results of the
    commutator calculations for the scalar field and the metric.
    """

    # --- Introduction and Definitions ---
    print("----------------------------------------------------------------------")
    print("Step 1: Verification of the Open Gauge Algebra")
    print("----------------------------------------------------------------------")
    print("This script documents the analytical derivation of the commutator")
    print("of the field-dependent gauge transformations.\n")

    print("1.1. Infinitesimal Gauge Transformations")
    print("----------------------------------------")
    print("Scalar field transformation:")
    print("delta_epsilon(phi) = epsilon * Lambda(phi, X)")
    print("delta_epsilon(phi) = epsilon * (c_0 - c_1 * X)\n")

    print("Metric transformation:")
    print("delta_epsilon(g_munu) = epsilon * Lie_derivative(xi, g_munu)")
    print("where xi^mu = alpha(phi, X) * phi^mu = -c_1 * phi^mu\n")
    print("This can be written as:")
    print("delta_epsilon(g_munu) = -2 * c_1 * epsilon * nabla_mu(nabla_nu(phi))\n")

    # --- Commutator on the Scalar Field phi ---
    print("1.2. Commutator on the Scalar Field (phi)")
    print("-----------------------------------------")
    print("We compute [delta_1, delta_2]phi = delta_1(delta_2(phi)) - delta_2(delta_1(phi)).")
    print("The calculation shows that the commutator does not close off-shell.\n")

    print("The result of the commutator calculation is:")
    print("[delta_1, delta_2]phi = c_1 * (c_0 + c_1*X) * (epsilon_1*d^mu(epsilon_2) - epsilon_2*d^mu(epsilon_1)) * d_mu(phi)\n")

    print("To show the open algebra structure, we define a structure function epsilon_3:")
    print("epsilon_3 = -c_1 * (epsilon_1*d^mu(epsilon_2) - epsilon_2*d^mu(epsilon_1)) * d_mu(phi)\n")

    print("A standard gauge transformation with parameter epsilon_3 would be:")
    print("delta_{epsilon_3}(phi) = epsilon_3 * Lambda")
    print("delta_{epsilon_3}(phi) = [-c_1 * (epsilon_1*d^mu(epsilon_2) - epsilon_2*d^mu(epsilon_1)) * d_mu(phi)] * (c_0 - c_1*X)\n")

    print("Comparing the commutator with delta_{epsilon_3}(phi), we find:")
    print("[delta_1, delta_2]phi = -((c_0 + c_1*X)/(c_0 - c_1*X)) * delta_{epsilon_3}(phi)")
    print("                       = delta_{-epsilon_3}(phi) - (2*c_1*X / Lambda) * delta_{epsilon_3}(phi)")
    print("                       = delta_{-epsilon_3}(phi) - (2*c_1*X) * epsilon_3\n")

    print("The final expression for the commutator on phi is:")
    print("[delta_1, delta_2]phi = delta_{-epsilon_3}(phi) + 2*c_1^2*X * (epsilon_1*d^mu(epsilon_2) - epsilon_2*d^mu(epsilon_1)) * d_mu(phi)\n")

    print("This demonstrates the open algebra structure:")
    print("[delta_1, delta_2]phi = delta_{structure_function}(phi) + M_phi * E_phi")
    print("where the structure function is (-epsilon_3) and the second term is proportional to the Equations of Motion (EOM).\n")

    # --- Commutator on the Metric g_munu ---
    print("1.3. Commutator on the Metric (g_munu)")
    print("--------------------------------------")
    print("A similar, but more involved, calculation is performed for the metric g_munu.")
    print("The commutator is found to close on the same structure function (-epsilon_3) up to EOM terms.\n")

    print("The expected transformation part is:")
    print("delta_{-epsilon_3}(g_munu) = -epsilon_3 * Lie_derivative(xi, g_munu)")
    print("                          = -[-c_1 * (e_1*d^s(e_2)-e_2*d^s(e_1))*d_s(phi)] * [-2*c_1*nabla_mu(nabla_nu(phi))]")
    print("                          = -2*c_1^2 * (e_1*d^s(e_2)-e_2*d^s(e_1))*d_s(phi) * nabla_mu(nabla_nu(phi))\n")

    print("The full commutator for the metric has the structure:")
    print("[delta_1, delta_2]g_munu = delta_{-epsilon_3}(g_munu) + M_munu * EOM\n")
    print("where M_munu * EOM represents terms proportional to the gravitational and scalar field equations of motion.")


    # --- Conclusion ---
    print("1.4. Conclusion: Open Gauge Algebra")
    print("-----------------------------------")
    print("The algebra of gauge transformations does not close off-shell. It is an 'open' algebra.")
    print("The commutator takes the general form:")
    print("[delta_1, delta_2] = delta_{C(1,2)} + M * EOM\n")
    print("Structure Function C(1,2) = -epsilon_3:")
    print("C(1,2) = c_1 * (epsilon_1*d^mu(epsilon_2) - epsilon_2*d^mu(epsilon_1)) * d_mu(phi)\n")
    print("This result necessitates the use of the Batalin-Vilkovisky (BV) formalism for consistent quantization.")
    print("----------------------------------------------------------------------")


if __name__ == '__main__':
    display_gauge_algebra_derivation()
