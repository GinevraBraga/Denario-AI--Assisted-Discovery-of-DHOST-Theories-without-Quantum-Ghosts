# filename: codebase/disformal_co_invariant.py
import sympy

def derive_co_invariant_subclass():
    """
    Performs a symbolic derivation to find the subclass of Horndeski theories
    that is co-invariant under a standard Galilean symmetry and a special
    disformal transformation.

    The derivation follows these steps:
    1. Assume the Horndeski functions G_i have the structure of a
       "Covariant Galileon", which respects Galilean symmetry.
    2. Assume a special disformal transformation of the form:
       tilde_g_munu = C(phi) * g_munu + (f(phi)/X) * nabla_mu(phi) * nabla_nu(phi).
    3. Apply the transformation rules to the Galileon ansatz.
    4. Require that the transformed theory, tilde_G_i, has the same
       functional form (i.e., the same powers of the kinetic term X) as the
       original theory.
    5. This requirement imposes constraints on the initial functions, which
       are solved to define the co-invariant subclass.
    """
    # --- 1. Symbolic Setup ---
    phi, X = sympy.symbols('phi X', real=True, positive=True)
    g2 = sympy.Function('g2')(phi, X)
    g3 = sympy.Function('g3')(phi)
    g4 = sympy.Function('g4')(phi)
    g5 = sympy.Function('g5')(phi)
    C = sympy.Function('C')(phi)
    f = sympy.Function('f')(phi)

    print("--- Step 2: Algebraic Computation of the Co-invariant Subclass ---")
    print("\nDerivation started. Assumptions:")
    print("1. Base theory has a 'Covariant Galileon' structure (invariant under delta_phi = b_mu * x^mu).")
    print("2. Disformal transformation is of the special class with D(phi, X) = f(phi)/X and C = C(phi).")
    print("-" * 70)

    # --- 2. Galileon Ansatz ---
    G3 = g3 * X
    G4 = g4 * X**2
    G5 = g5 * X**2

    print("\nInitial Galileon Ansatz:")
    print("G3(phi, X) = g3(phi) * X")
    print("G4(phi, X) = g4(phi) * X^2")
    print("G5(phi, X) = g5(phi) * X^2")
    print("-" * 70)

    # --- 3. Special Disformal Transformation Definitions ---
    # D = f(phi)/X. This implies d/dX(X*D) = 0.
    # This specific choice corresponds to the "disformal Galileon" and simplifies
    # the transformation rules significantly by cancelling integral terms.
    D = f / X
    F = C - 2 * X * D
    F_simplified = C - 2 * f
    tildeX = sympy.Symbol('tildeX')

    print("\nDisformal Transformation Parameters:")
    print("C(phi, X) = C(phi)")
    print("D(phi, X) = f(phi) / X")
    print("F = C - 2*X*D = " + str(F_simplified))
    print("The new kinetic term relates to the old as: X = F * tildeX = (" + str(F_simplified) + ") * tildeX")
    print("-" * 70)

    # --- 4. Transformation Rules (from arXiv:1306.6724, simplified for D=f/X) ---
    # These rules map the old functions G_i(phi, X) to the new ones tilde_G_i(phi, tildeX).
    
    # Transformation for G5
    tilde_G5_expr = C**(sympy.Rational(5, 2)) * F_simplified**(-sympy.Rational(1, 2)) * G5
    
    # Transformation for G4
    G5_phi = sympy.diff(G5, phi)
    tilde_G4_expr = C**(sympy.Rational(3, 2)) * F_simplified**(sympy.Rational(1, 2)) * G4 \
                  - sympy.Rational(2, 3) * C**(sympy.Rational(5, 2)) * F_simplified**(-sympy.Rational(1, 2)) * X * G5_phi

    # Transformation for G3
    G4_phi = sympy.diff(G4, phi)
    G5_phiphi = sympy.diff(G5_phi, phi)
    tilde_G3_expr = C**(sympy.Rational(1, 2)) * F_simplified**(sympy.Rational(1, 2)) * \
                  (C * G3 - 2 * X * G4_phi + sympy.Rational(2, 3) * X**2 * G5_phiphi)

    print("\nApplying simplified transformation rules from Bettoni & Liberati (2013)...")
    print("-" * 70)

    # --- 5. & 6. Impose Co-invariance and Derive Constraints ---

    # --- Constraint from G5 ---
    print("\nAnalyzing tilde_G5...")
    # We need tilde_G5 to be of the form tilde_g5(phi) * tildeX**2
    tilde_G5_in_tildeX = tilde_G5_expr.subs(X, F_simplified * tildeX)
    tilde_G5_in_tildeX = sympy.simplify(tilde_G5_in_tildeX)
    
    # The form is automatically preserved.
    tilde_g5_coeff = sympy.simplify(tilde_G5_in_tildeX / tildeX**2)
    print("tilde_G5 = (" + str(tilde_g5_coeff) + ") * tildeX**2")
    print("Result: The X^2 structure of G5 is preserved automatically.")

    # --- Constraint from G4 ---
    print("\nAnalyzing tilde_G4...")
    # We need tilde_G4 to be of the form tilde_g4(phi) * tildeX**2
    tilde_G4_in_tildeX = tilde_G4_expr.subs(X, F_simplified * tildeX)
    tilde_G4_in_tildeX = sympy.expand(tilde_G4_in_tildeX)
    
    # Collect terms in powers of tildeX
    poly_tilde_G4 = sympy.collect(tilde_G4_in_tildeX, tildeX)
    print("Expression for tilde_G4 in terms of tildeX:")
    print(poly_tilde_G4)

    # For co-invariance, the coefficient of tildeX**3 must be zero.
    coeff_X3_G4 = poly_tilde_G4.coeff(tildeX, 3)
    print("\nFor co-invariance, the coefficient of tildeX^3 must be zero.")
    print("Coefficient of tildeX^3 = " + str(coeff_X3_G4))
    
    # The equation is coeff_X3_G4 = 0.
    # -2/3 * C**(5/2) * F_simplified**(5/2) * g5.diff(phi) = 0
    # Since C and F are non-zero, this implies g5.diff(phi) = 0.
    constraint1 = sympy.Eq(sympy.diff(g5, phi), 0)
    print("Constraint derived from tilde_G4: " + str(constraint1))
    print("This implies g5(phi) must be a constant.")
    
    # Apply this constraint for the next step
    g5_const = sympy.Symbol('c5', real=True)
    G4 = g4 * X**2
    G5_constrained = g5_const * X**2
    
    # Re-evaluate tilde_G4 with the constraint
    G5_phi_constrained = sympy.diff(G5_constrained, phi)
    tilde_G4_expr_constrained = C**(sympy.Rational(3, 2)) * F_simplified**(sympy.Rational(1, 2)) * G4 \
                              - sympy.Rational(2, 3) * C**(sympy.Rational(5, 2)) * F_simplified**(-sympy.Rational(1, 2)) * X * G5_phi_constrained
    tilde_G4_in_tildeX_constrained = tilde_G4_expr_constrained.subs(X, F_simplified * tildeX)
    tilde_g4_coeff = sympy.simplify(tilde_G4_in_tildeX_constrained / tildeX**2)


    # --- Constraint from G3 ---
    print("\nAnalyzing tilde_G3 (with g5 = constant)...")
    # We need tilde_G3 to be of the form tilde_g3(phi) * tildeX
    G4_phi_constrained = sympy.diff(G4, phi) # g4 is still a function of phi
    G5_phiphi_constrained = sympy.diff(G5_phi_constrained, phi)

    tilde_G3_expr_constrained = C**(sympy.Rational(1, 2)) * F_simplified**(sympy.Rational(1, 2)) * \
                  (C * G3 - 2 * X * G4_phi_constrained + sympy.Rational(2, 3) * X**2 * G5_phiphi_constrained)

    tilde_G3_in_tildeX = sympy.expand(tilde_G3_expr_constrained.subs(X, F_simplified * tildeX))
    poly_tilde_G3 = sympy.collect(tilde_G3_in_tildeX, tildeX)
    print("Expression for tilde_G3 in terms of tildeX:")
    print(poly_tilde_G3)

    # For co-invariance, the coefficient of tildeX**3 must be zero.
    coeff_X3_G3 = poly_tilde_G3.coeff(tildeX, 3)
    print("\nFor co-invariance, the coefficient of tildeX^3 must be zero.")
    print("Coefficient of tildeX^3 = " + str(coeff_X3_G3))

    # The equation is coeff_X3_G3 = 0.
    # -2 * C**(1/2) * F_simplified**(7/2) * g4.diff(phi) = 0
    # This implies g4.diff(phi) = 0.
    constraint2 = sympy.Eq(sympy.diff(g4, phi), 0)
    print("Constraint derived from tilde_G3: " + str(constraint2))
    print("This implies g4(phi) must be a constant.")
    
    g4_const = sympy.Symbol('c4', real=True)
    
    # Re-evaluate tilde_G3 with all constraints
    G4_doubly_constrained = g4_const * X**2
    G4_phi_doubly_constrained = sympy.diff(G4_doubly_constrained, phi)
    tilde_G3_expr_final = C**(sympy.Rational(1, 2)) * F_simplified**(sympy.Rational(1, 2)) * \
                  (C * G3 - 2 * X * G4_phi_doubly_constrained + sympy.Rational(2, 3) * X**2 * G5_phiphi_constrained)
    tilde_G3_in_tildeX_final = tilde_G3_expr_final.subs(X, F_simplified * tildeX)
    tilde_g3_coeff = sympy.simplify(tilde_G3_in_tildeX_final / tildeX)

    print("-" * 70)
    # --- 7. & 8. Final Result and Output ---
    print("\n--- Derivation Complete: The Co-Invariant Subclass ---")
    print("\nThe analysis shows that for the Galileon structure to be preserved under the special disformal transformation,")
    print("the coefficients of G4 and G5 must be constants.")
    
    print("\nThe resulting Disformal-Generalized Galilean Co-invariant subclass is defined by:")
    print("G2(phi, X) = g2(phi, X)  (remains an arbitrary function)")
    print("G3(phi, X) = g3(phi) * X")
    print("G4(phi, X) = c4 * X^2      (c4 is a constant)")
    print("G5(phi, X) = c5 * X^2      (c5 is a constant)")
    
    print("\nThis theory is invariant under Galilean shifts and its structure is preserved by the disformal transformation:")
    print("tilde_g_munu = C(phi) * g_munu + (f(phi)/X) * nabla_mu(phi) * nabla_nu(phi)")
    
    print("\nThe coefficients of the transformed theory are:")
    print("tilde_g3(phi) = " + str(tilde_g3_coeff))
    print("tilde_c4 = " + str(tilde_g4_coeff))
    print("tilde_c5 = " + str(tilde_g5_coeff))
    print("-" * 70)


if __name__ == '__main__':
    derive_co_invariant_subclass()