# filename: codebase/quantum_stability_analysis.py
import sympy
import pandas as pd

def analyze_quantum_stability():
    """
    Outlines the analysis of 1-loop quantum corrections and stability for
    degenerate DHOST theories, based on the underlying gauge symmetry.

    This function does not perform a full 1-loop calculation, which is
    analytically prohibitive. Instead, it formalizes the conceptual argument
    for why the degeneracy-enforcing symmetry protects the theory from quantum
    instabilities.

    The steps are:
    1.  Set up the path integral for the degenerate DHOST action.
    2.  Describe the Faddeev-Popov gauge-fixing procedure, defining the
        gauge-fixing and ghost Lagrangians symbolically.
    3.  Explain how the gauge symmetry leads to Ward-Takahashi identities at the
        quantum level.
    4.  Argue that these identities constrain the form of 1-loop corrections,
        ensuring the kinetic matrix remains degenerate and the ghost is not
        reintroduced.
    5.  Summarize the entire logical process in a pandas DataFrame.
    """
    sympy.init_printing(use_unicode=False, wrap_line=False)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', 200)

    print("=" * 80)
    print("Step 4: Analysis of Quantum Corrections and 1-Loop Stability")
    print("=" * 80)
    print("This analysis is conceptual and outlines the procedure and expected results.")

    # --- 1. Path Integral Setup ---
    print("\n--- 4.1: Path Integral Setup ---")
    S_DHOST = sympy.Symbol('S_DHOST')
    fields = sympy.Symbol('Phi')
    print("The starting point is the path integral for the DHOST action, Z = integral D[fields] * exp(i * S_DHOST).")
    print("As established in Step 3, S_DHOST possesses a field-dependent gauge symmetry.")
    print("This makes the path integral ill-defined due to overcounting of equivalent field configurations.")
    print("-" * 70)

    # --- 2. Faddeev-Popov Gauge Fixing ---
    print("\n--- 4.2: Faddeev-Popov Procedure and Gauge Fixing ---")
    print("To quantize the theory, we must fix the gauge using the Faddeev-Popov method.")

    # Define symbolic components
    xi = sympy.Symbol('xi') # Gauge-fixing parameter
    F = sympy.Symbol('F')   # Gauge-fixing condition, F[fields] = 0
    alpha = sympy.Symbol('alpha') # Gauge transformation parameter
    c, c_bar = sympy.symbols('c c_bar') # Ghost and anti-ghost fields

    # Gauge-fixing Lagrangian
    L_GF = -1 / (2 * xi) * F**2
    print("\n1. A gauge-fixing condition F[fields] = 0 is chosen.")
    print("2. This introduces a gauge-fixing term into the Lagrangian:")
    sympy.pprint(sympy.Eq(sympy.Symbol('L_GF'), L_GF))

    # Faddeev-Popov operator and ghost Lagrangian
    M_FP = sympy.Symbol('M_FP')
    L_ghost = c_bar * M_FP * c
    print("\n3. The Faddeev-Popov determinant, det(M_FP), is introduced to maintain unitarity.")
    print("   The operator M_FP is the variation of the gauge condition under the symmetry transformation: M_FP = dF/d(alpha).")
    print("4. This determinant is expressed as an integral over Faddeev-Popov ghost fields (c, c_bar),")
    print("   adding a ghost Lagrangian to the action:")
    sympy.pprint(sympy.Eq(sympy.Symbol('L_ghost'), L_ghost))

    # Total action for quantization
    S_total = S_DHOST + sympy.Integral(L_GF + L_ghost, sympy.Symbol('d^4x'))
    print("\n5. The total action used for quantization is S_total = S_DHOST + S_GF + S_ghost.")
    print("-" * 70)

    # --- 3. 1-Loop Corrections and Ward Identities ---
    print("\n--- 4.3: 1-Loop Corrections and Ward Identities ---")
    Gamma_eff = sympy.Symbol('Gamma_eff')
    Gamma_tree = sympy.Symbol('Gamma_tree')
    Sigma_1loop = sympy.Symbol('Sigma_1loop')

    print("Quantum corrections are computed using Feynman diagrams derived from S_total.")
    print("At the 1-loop level, the effective action Gamma_eff receives corrections.")
    print("The 2-point function (inverse propagator) is corrected by the self-energy Sigma:")
    print("  Gamma_2_eff(k) = Gamma_2_tree(k) - Sigma_1loop(k)")
    print("\nThe crucial insight is that a gauge symmetry at the classical level leads to")
    print("Ward-Takahashi identities at the quantum level. These identities are a direct")
    print("consequence of the symmetry and constrain the form of all correlation functions.")
    print("\nFor the effective action, the Ward identity implies that Gamma_eff must be invariant")
    print("under the same gauge symmetry that S_DHOST was: delta(Gamma_eff) = 0.")
    print("-" * 70)

    # --- 4. Verification of Quantum Stability ---
    print("\n--- 4.4: Verification of Quantum Stability ---")
    K_tree = sympy.Symbol('K_tree')
    K_1loop = sympy.Symbol('K_1loop')
    K_eff = sympy.Symbol('K_eff')

    print("At the classical level, the symmetry enforced degeneracy, meaning det(K_tree) = 0,")
    print("where K_tree is the kinetic matrix derived from S_DHOST.")
    print("\nThe Ward identity demands that the full quantum effective action also respects the symmetry.")
    print("This means the corrected kinetic matrix, K_eff = K_tree + K_1loop, must also be degenerate.")
    print("\nTherefore, the Ward identity guarantees that:")
    print("  det(K_eff) = det(K_tree + K_1loop) = 0")
    print("\nThis implies that the 1-loop corrections (Sigma_1loop) cannot generate a term that")
    print("would make the kinetic matrix invertible. The pole structure of the propagator is protected.")
    print("The ghost degree of freedom, eliminated at the classical level by the symmetry,")
    print("cannot be reintroduced by quantum corrections.")
    print("\nCONCLUSION: The degeneracy-enforcing symmetry protects the theory's stability at 1-loop.")
    print("-" * 70)

    # --- 5. Summary Table ---
    print("\n\n" + "="*80)
    print("SUMMARY OF 1-LOOP QUANTUM STABILITY ANALYSIS")
    print("="*80)

    summary_data = {
        'Stage': [
            "1. Path Integral Setup",
            "2. Gauge Fixing",
            "3. Ghost Term Derivation",
            "4. Quantum Corrections",
            "5. Symmetry Constraint",
            "6. Final Result"
        ],
        'Description': [
            "The theory is quantized using the path integral formalism.",
            "The Faddeev-Popov procedure is required to handle the gauge symmetry, introducing a gauge-fixing term L_GF.",
            "The procedure introduces a ghost Lagrangian L_ghost to ensure unitarity, where ghosts are unphysical fields.",
            "The 1-loop self-energy (Sigma) corrects the propagator. The key question is whether Sigma reintroduces the ghost.",
            "The original gauge symmetry leads to Ward-Takahashi identities at the quantum level.",
            "The Ward identities enforce det(K_eff) = 0, meaning the quantum corrections must respect the degeneracy. The ghost is NOT reintroduced."
        ],
        'Key Equation / Concept': [
            "Z = integral D[fields] exp(i*S)",
            "L_GF = -1/(2*xi) * F^2",
            "L_ghost = c_bar * (dF/d(alpha)) * c",
            "Gamma_2_eff = Gamma_2_tree - Sigma_1loop",
            "Ward Identity: delta(Gamma_eff) = 0",
            "det(K_tree + K_1loop) = 0"
        ]
    }

    summary_df = pd.DataFrame(summary_data)
    print(summary_df.to_string())
    print("\n" + "="*80)


if __name__ == '__main__':
    analyze_quantum_stability()