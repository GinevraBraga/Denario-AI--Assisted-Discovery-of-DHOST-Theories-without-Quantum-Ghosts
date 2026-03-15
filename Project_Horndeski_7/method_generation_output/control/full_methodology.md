<!-- filename: full_methodology.md -->

# Methodology

This section details the step-by-step methodology for analyzing hidden symmetries and stability in Type I DHOST theories with massless gravity, as formulated in arXiv:2012.10218. The approach is designed to ensure the absence of ghost and tachyonic instabilities at both the classical and quantum (one-loop) levels, while maintaining compatibility with observational constraints. All calculations are performed on a spatially flat Friedmann-Robertson-Walker (FRW) background.

---

## 1. Lagrangian Construction and Specialization

- **General Action:**  
  Begin with the general Type I DHOST action:
  <code>
  S = ∫ d⁴x √(-g) [f(X) R + Σ_{i=1}^5 A_i(X) L_i]
  </code>
  where \( X = -\frac{1}{2} g^{μν} ∂_μϕ ∂_νϕ \), \( R \) is the Ricci scalar, and \( L_i \) are quadratic in second derivatives of ϕ. The coupling functions \( f \) and \( A_i \) are taken to depend only on \( X \) to ensure shift symmetry.

- **FRW Background:**  
  Specialize to the spatially flat FRW metric:
  <code>
  ds² = -dt² + a(t)² d\vec{x}²
  </code>
  Express all geometric and scalar quantities in terms of \( a(t) \), \( H(t) \), and \( ϕ(t) \).

- **Degeneracy and Massless Gravity:**  
  Impose the degeneracy conditions for Type I DHOST theories (see arXiv:2012.10218, Table 1) to ensure only two tensor and one scalar degree of freedom propagate, and that the graviton remains massless.

---

## 2. Symmetry Identification and Explicit Construction

- **Shift Symmetry:**  
  Impose the shift symmetry transformation:
  <code>
  ϕ → ϕ + c
  </code>
  This restricts all coupling functions to depend solely on \( X \). Explicitly verify that under this transformation, the Lagrangian changes at most by a total derivative.

- **Generalized Symmetries:**  
  Explore possible extensions, such as Galileon-like symmetries:
  <code>
  ϕ → ϕ + b_μ x^μ
  </code>
  For each candidate symmetry, write the explicit transformation rules for all fields and substitute into the Lagrangian to check invariance.

- **Variable Redefinitions:**  
  Document all field redefinitions and ensure invertibility, maintaining a clear mapping for reproducibility.

---

## 3. Classical Stability Analysis

- **Perturbative Expansion:**  
  Expand the metric and scalar field around the FRW background:
  <code>
  ϕ(t, x) = ϕ₀(t) + δϕ(t, x)
  g_{μν} = g^{(0)}_{μν} + h_{μν}
  </code>
  Derive the quadratic action for perturbations.

- **Hamiltonian and Kinetic Matrix:**  
  Construct the Hamiltonian for perturbations and extract the kinetic and mass matrices for scalar and tensor modes. Check for negative eigenvalues (ghosts) and negative mass-squared terms (tachyons).

- **Ostrogradsky Instability:**  
  Verify that the degeneracy conditions eliminate higher-derivative (Ostrogradsky) instabilities by ensuring the equations of motion for propagating degrees of freedom are second order.

---

## 4. Quantum (One-Loop) Stability Analysis

- **Quadratic Action and Path Integral:**  
  Use the quadratic action to compute the one-loop effective action via the path integral formalism.

- **Ghost Analysis at One-Loop:**  
  Analyze whether quantum corrections generate higher-derivative operators or destabilize the kinetic structure. Explicitly check if the imposed symmetries forbid the generation of dangerous operators at one-loop.

- **Symmetry Breaking and Ghost Reappearance:**  
  Introduce small symmetry-breaking deformations (e.g., weak ϕ-dependence in couplings) and repeat the stability analysis, referencing the mechanisms in arXiv:2004.11655 to identify conditions under which ghosts may reappear.

---

## 5. Observational Constraints

- **Gravitational Wave Speed:**  
  Derive the dispersion relation for tensor modes and ensure the propagation speed matches the speed of light, as required by multi-messenger observations.

- **Cosmological Expansion:**  
  Solve the background equations for \( a(t) \) and \( ϕ(t) \) and compare with observational data on the expansion history.

- **Structure Growth:**  
  Analyze the evolution of linear scalar perturbations and compare with large-scale structure observations.

---

## 6. Cross-Checks and Validation

- **Literature Consistency:**  
  Benchmark all calculations against established results in the literature (e.g., Horndeski, beyond-Horndeski limits).

- **Explicit Symmetry Verification:**  
  For each symmetry, substitute the transformation into the Lagrangian and demonstrate invariance (up to total derivatives).

- **Documentation:**  
  Record all intermediate steps, field redefinitions, and checks in detail to ensure full reproducibility.

---

This methodology ensures a systematic, transparent, and reproducible analysis of hidden symmetries and stability in Type I DHOST theories with massless gravity, fully compatible with both theoretical and observational constraints.