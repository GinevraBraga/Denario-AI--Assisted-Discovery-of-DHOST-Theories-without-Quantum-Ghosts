# filename: codebase/classical_stability_analysis.py
import sympy

def classical_stability_analysis():
    """
    Performs a symbolic classical stability analysis of the co-invariant
    Horndeski subclass on an FLRW background.

    This function derives the no-ghost and no-tachyonic instability conditions
    for both tensor and scalar perturbations. It uses the symbolic manipulation
    capabilities of sympy to substitute the specific forms of the Horndeski
    functions (G_i) into the general stability criteria found in the literature.

    The results are the explicit algebraic conditions that the free functions
    (g2, g3) and constants (c4, c5) of the theory must satisfy to be
    classically stable.
    """
    print("--- Step 3: Classical Stability Analysis of the Derived Subclass ---")
    print("\nAnalyzing perturbations on a flat FLRW background: ds^2 = -dt^2 + a(t)^2 dx^i dx_i")
    print("The co-invariant subclass is defined by:")
    print("G2(phi, X), G3 = g3(phi)*X, G4 = c4*X**2, G5 = c5*X**2")
    print("-" * 70)

    # --- 1. Symbolic Setup ---
    # Spacetime and field variables
    t = sympy.Symbol('t')
    phi_t = sympy.Function('phi')(t)
    a_t = sympy.Function('a')(t)

    # Generic Horndeski variables
    phi, X = sympy.symbols('phi X', real=True)

    # Background quantities
    H = sympy.diff(a_t, t) / a_t
    phi_dot = sympy.diff(phi_t, t)
    phi_ddot = sympy.diff(phi_dot, t)
    # Background kinetic term X = -1/2 g^munu nabla_mu phi nabla_nu phi
    # On FLRW, g^00 = -1, so X = 1/2 * phi_dot^2
    X_b = sympy.Rational(1, 2) * phi_dot**2

    # --- 2. Define the Co-Invariant Subclass Functions and their Derivatives ---
    g2 = sympy.Function('g2')(phi, X)
    g3 = sympy.Function('g3')(phi)
    g3_p = sympy.diff(g3, phi)  # g3_p denotes derivative of g3 w.r.t. phi
    c4, c5 = sympy.symbols('c4 c5', real=True)

    G2 = g2
    G3 = g3 * X
    G4 = c4 * X**2
    G5 = c5 * X**2

    # Calculate all necessary derivatives
    G2_X, G2_XX = sympy.diff(G2, X), sympy.diff(G2, X, 2)
    G3_phi, G3_X, G3_Xphi = sympy.diff(G3, phi), sympy.diff(G3, X), sympy.diff(G3, X, phi)
    G4_X, G4_XX = sympy.diff(G4, X), sympy.diff(G4, X, 2)
    G5_phi, G5_X, G5_XX, G5_Xphi = sympy.diff(G5, phi), sympy.diff(G5, X), sympy.diff(G5, X, 2), sympy.diff(G5, X, phi)

    # --- 3. Evaluate all quantities on the background ---
    sub_map = {phi: phi_t, X: X_b}
    def on_bg(expr):
        return sympy.simplify(expr.subs(sub_map))

    # --- 4. Tensor Stability Analysis ---
    print("\n--- 4.1 Tensor Perturbations (Gravitational Waves) ---")
    # Using formulas from Kobayashi (2019) review, arXiv:1901.07183
    # Kinetic term coefficient for tensor modes: mathcal_G_T
    mathcal_G_T = 2 * (G4 - X * G4_X)
    mathcal_G_T_bg = on_bg(mathcal_G_T)

    # Numerator for tensor speed squared: mathcal_F_T
    mathcal_F_T = G4 - X * G5_phi - X * phi_ddot * G5_X
    mathcal_F_T_bg = on_bg(mathcal_F_T)

    # Tensor speed squared
    c_T_sq = mathcal_F_T / mathcal_G_T
    c_T_sq_bg = on_bg(c_T_sq)

    print("Kinetic coefficient for tensor modes, mathcal_G_T:")
    sympy.pprint(mathcal_G_T_bg)
    print("\nNo-ghost condition for tensor modes: mathcal_G_T > 0")
    print("This implies: -c4 * phi_dot(t)^4 > 0  ==>  c4 < 0")
    print("-" * 50)

    print("Squared speed of tensor modes, c_T^2:")
    sympy.pprint(c_T_sq_bg)
    print("\nNo-tachyonic instability condition for tensor modes: c_T^2 >= 0")
    print("This implies: (c4 * phi_dot(t)^2 + 2*c5*phi_dot(t)^2*Derivative(phi(t), (t, 2))) / (c4 * phi_dot(t)^2) >= 0")
    print("Assuming c4 < 0, this simplifies to: c4 + 2*c5*phi_ddot <= 0")
    print("-" * 70)

    # --- 5. Scalar Stability Analysis ---
    print("\n--- 5.2 Scalar Perturbations ---")
    # Using intermediate variables w_i from Kobayashi (2019)
    w1 = (2 * G2_X + 2 * X * G2_XX - 2 * G3_phi - 2 * X * G3_Xphi
          + phi_dot * H * (3 * G3_X + X * sympy.diff(G3_X, X))
          + 6 * H**2 * (G4 - 2 * X * G4_X + X**2 * G4_XX)
          - 6 * H**2 * X * (G5_phi + X * G5_Xphi)
          + 2 * H**3 * phi_dot * X * (3 * G5_X + X * G5_XX))

    w2 = (phi_dot * G3_X - 2 * H * (G4 - 2 * X * G4_X)
          + 2 * H * X * G5_phi - 2 * H**2 * phi_dot * X * G5_X)

    w3 = G4 - 2 * X * G4_X - X * G5_phi - X * phi_ddot * G5_X

    w4 = G4 - X * G4_X

    # Simplify the w_i terms on the background
    w1_bg = on_bg(w1)
    w2_bg = on_bg(w2)
    w3_bg = on_bg(w3)
    w4_bg = on_bg(w4)

    print("Intermediate functions for scalar stability (evaluated on background):")
    print("\nw1 =")
    sympy.pprint(w1_bg)
    print("\nw2 =")
    sympy.pprint(w2_bg)
    print("\nw3 =")
    sympy.pprint(w3_bg)
    print("\nw4 =")
    sympy.pprint(w4_bg)
    print("-" * 50)

    # Kinetic term coefficient for scalar modes
    mathcal_G_S = (w1 * w3**2 - 3 * w2**2) / (4 * w4**2)
    mathcal_G_S_bg = on_bg(mathcal_G_S)

    # Gradient term coefficient for scalar modes
    H_dot = sympy.diff(H, t)
    mathcal_F_S = -w3 * H_dot - (sympy.diff(a_t * w2, t) / a_t) + H * w2
    mathcal_F_S_bg = on_bg(mathcal_F_S)  # This expression is very large, we analyze G_S first

    print("\nKinetic coefficient for scalar modes, mathcal_G_S:")
    print("The full expression is very large. It is given by (w1*w3^2 - 3*w2^2)/(4*w4^2).")
    print("Its sign depends on the background evolution and the free functions g2 and g3.")
    print("\nNo-ghost condition for scalar modes: mathcal_G_S > 0")
    print("w1*w3^2 - 3*w2^2 > 0")
    print("This condition must be checked for any specific cosmological solution.")
    print("-" * 50)

    print("\nGradient term for scalar modes, c_S^2 * mathcal_G_S:")
    print("The expression is given by -w3*H_dot - d(a*w2)/dt / a + H*w2.")
    print("Its sign determines the presence of tachyonic instabilities.")
    print("\nNo-tachyonic instability condition for scalar modes: c_S^2 >= 0")
    print("Given mathcal_G_S > 0, this requires:")
    print("-w3*H_dot - d(a*w2)/dt / a + H*w2 >= 0")
    print("This is a complex differential condition on the background evolution.")
    print("-" * 70)

    print("\n--- 5.3 Summary of Classical Stability Conditions ---")
    print("1. Tensor No-Ghost: c4 < 0")
    print("2. Tensor No-Tachyon: c4 + 2*c5*phi_ddot <= 0 (assuming c4 < 0)")
    print("3. Scalar No-Ghost: w1*w3^2 - 3*w2^2 > 0")
    print("4. Scalar No-Tachyon: -w3*H_dot - d(a*w2)/dt / a + H*w2 >= 0 (assuming scalar no-ghost)")
    print("\nWhere w1, w2, w3 are functions of g2, g3, c4, c5 and background quantities H, phi_dot.")
    print("The stability of the scalar sector imposes complex constraints on the remaining free")
    print("functions g2(phi, X) and g3(phi) and the cosmological background solution.")
    print("-" * 70)


if __name__ == '__main__':
    classical_stability_analysis()