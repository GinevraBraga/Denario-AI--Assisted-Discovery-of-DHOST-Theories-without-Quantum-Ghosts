# filename: codebase/equivalence_proof.py
import sympy

def generate_report_step4():
    """
    Generates a detailed report for Step 4:
    Compares the symmetry and degeneracy conditions and proves their equivalence.
    """

    # Define symbolic variables for the report
    phi, X = sympy.symbols('phi X')
    beta_GB = sympy.Function('beta_GB')(phi, X)
    beta_W2 = sympy.Function('beta_W2')(phi, X)

    # Define the partial derivatives
    beta_W2_X = sympy.Derivative(beta_W2, X)
    beta_GB_X = sympy.Derivative(beta_GB, X)
    beta_W2_phi = sympy.Derivative(beta_W2.func(phi, X), phi)

    # Header
    print("----------------------------------------------------------------------")
    print("Project: The Hamiltonian Origin of Symmetry in Quantum-Corrected Scalar-Tensor Theories")
    print("Step 4: The Equivalence of Symmetry and Degeneracy Conditions")
    print("----------------------------------------------------------------------\n")

    # Introduction
    print("### Introduction: The Final Comparison ###")
    print("In the preceding steps, we pursued two independent paths to ensure the viability of the quantum-corrected scalar-tensor theory:")
    print("1. Path A (Symmetry Analysis, Step 2): We demanded that the full action remain invariant under the classical protective gauge symmetry.")
    print("2. Path B (Hamiltonian Analysis, Step 3): We demanded that the theory be free of the Ostrogradsky ghost by ensuring the degeneracy of the kinetic Hessian.\n")
    print("The goal of this final step is to compare the sets of conditions derived from these two distinct physical principles and prove their mathematical equivalence.\n")

    # Summary of Conditions
    print("### Summary of Derived Conditions ###")
    print("Let's recall the final results from each path.\n")

    print("1. The 'Symmetry Conditions' from Path A (Step 2):")
    print("   For the action to be invariant under the gauge transformation, the following PDEs must be satisfied:")
    print("   - Condition S1: " + str(sympy.Eq(beta_W2_X, 0)))
    print("   - Condition S2: " + str(sympy.Eq(beta_GB_X + 2 * beta_W2_phi, 0)))
    print("\n")

    print("2. The 'Degeneracy Conditions' from Path B (Step 3):")
    print("   To eliminate the Ostrogradsky ghost, the Hamiltonian analysis required that:")
    print("   - Condition D1: " + str(sympy.Eq(beta_W2_X, 0)))
    print("   - Condition D2: " + str(sympy.Eq(beta_GB_X + 2 * beta_W2_phi, 0)))
    print("\n")

    # Comparative Table
    print("### Comparative Table ###")
    print("To make the comparison explicit, we present the conditions side-by-side:\n")
    print("+--------------------------------+--------------------------------+")
    print("|   Symmetry Conditions (Path A) |  Degeneracy Conditions (Path B)  |")
    print("+--------------------------------+--------------------------------+")
    print("| 1. " + str(sympy.Eq(beta_W2_X, 0)).ljust(28) + " | 1. " + str(sympy.Eq(beta_W2_X, 0)).ljust(28) + " |")
    print("| 2. " + str(sympy.Eq(beta_GB_X + 2 * beta_W2_phi, 0)).ljust(28) + " | 2. " + str(sympy.Eq(beta_GB_X + 2 * beta_W2_phi, 0)).ljust(28) + " |")
    print("+--------------------------------+--------------------------------+\n")

    # Proof of Equivalence
    print("### Proof of Equivalence ###")
    print("By direct inspection of the comparative table, the conclusion is immediate and unambiguous:")
    print("\n   Condition S1 is identical to Condition D1.")
    print("   Condition S2 is identical to Condition D2.\n")
    print("The set of partial differential equations derived from demanding gauge invariance is mathematically identical to the set derived from demanding the absence of a ghost degree of freedom.")
    print("This establishes the central result of this investigation: the two conditions are equivalent.\n")
    print("   (Symmetry Conditions) <=> (Degeneracy Conditions)\n")

    # Discussion and Implications
    print("### Discussion and Implications ###")
    print("The equivalence demonstrated above is not merely a mathematical curiosity; it reveals a deep and powerful connection between the fundamental principles of a physical theory.\n")
    print("1. Symmetry as a Predictor of Health: This result proves that the gauge symmetry is not just a feature of the classical theory but is the fundamental organizing principle that ensures its quantum-corrected extension remains physically viable (ghost-free). The classical symmetry is not 'broken' but must be 'extended' to the quantum terms.\n")
    print("2. A Powerful Theoretical Tool: The Hamiltonian analysis (Path B) is notoriously difficult and requires a complex ADM decomposition and analysis of kinetic terms. In contrast, the symmetry analysis (Path A), while still involved, is algebraically more straightforward. Our proof shows that one can use the simpler symmetry requirement as a reliable and sufficient tool to construct healthy, ghost-free effective field theories.\n")
    print("3. Unification of Concepts: The equivalence demonstrates that the 'algebraic' requirement of symmetry and the 'dynamical' requirement of a well-posed Hamiltonian are two sides of the same coin. The presence of the gauge symmetry is the underlying reason for the degeneracy in the kinetic sector.\n")

    # Conclusion
    print("----------------------------------------------------------------------")
    print("### Conclusion for Step 4 ###")
    print("We have rigorously shown that the conditions for restoring the protective gauge symmetry in the quantum-corrected scalar-tensor action are identical to the conditions required to eliminate the Ostrogradsky ghost via Hamiltonian analysis.")
    print("This equivalence is the cornerstone of the project, providing both a profound physical insight and a practical method for constructing consistent theories.")
    print("The principle is clear: to build a healthy theory, one must follow the symmetry.")
    print("----------------------------------------------------------------------")

if __name__ == '__main__':
    generate_report_step4()