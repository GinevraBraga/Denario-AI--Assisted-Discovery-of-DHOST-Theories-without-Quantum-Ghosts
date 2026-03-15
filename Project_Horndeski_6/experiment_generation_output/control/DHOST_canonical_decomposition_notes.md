<!-- filename: DHOST_canonical_decomposition_notes.md -->
### **Part I: Classification and Identification of Minimal Conditions**

#### **2. Canonical DHOST Decomposition and Functional Identification**

To classify the theory presented in DHOSTS.pdf within the canonical DHOST framework of Langlois et al. (2016) [arXiv:1608.08135], we must map the provided Lagrangian onto the general DHOST form. The canonical DHOST Lagrangian, excluding the Ricci scalar term, is expressed as:

<code>L_{DHOST} = P(\phi, X) + Q(\phi, X) \Box\phi + \sum_{i=1}^{5} A_i(\phi, X) L_i^{(2)} + B_1(\phi, X) L_1^{(3)}</code>

where the basis Lagrangians are <code>L_1^{(2)} = \phi_{\mu\nu}\phi^{\mu\nu}</code>, <code>L_2^{(2)} = (\Box\phi)^2</code>, <code>L_3^{(2)} = (\Box\phi) \phi^\mu \phi_{\mu\nu} \phi^\nu</code>, <code>L_4^{(2)} = \phi^\mu \phi_{\mu\rho} \phi^{\rho\nu} \phi_\nu</code>, <code>L_5^{(2)} = (\phi^\mu \phi_{\mu\nu} \phi^\nu)^2</code>, and <code>L_1^{(3)} = \phi^\mu \phi_{\mu\nu} \phi^{\nu\rho} \phi_\rho</code>.

The Lagrangian extracted from DHOSTS.pdf is constructed from the Horndeski and "beyond Horndeski" functions:

<code>L_{DHOST} = G_2(\phi, X) - G_3(\phi, X) \Box\phi + G_4(\phi, X) R - 2G_{4,X}[(\Box\phi)^2 - \phi_{\mu\nu}\phi^{\mu\nu}] + F_4(\phi, X) L_{bH4}</code>

where <code>G_5=0</code>, <code>F_5=0</code>, and the beyond-Horndeski term is given by:

<code>L_{bH4} = X ((\Box\phi)^2 - \phi_{\mu\nu}\phi^{\mu\nu}) - 2 \phi^{\mu\nu}\phi_{\mu\rho}\phi^{\rho}_{\nu} + 2 (\Box\phi) \phi^\mu \phi^\nu \phi_{\mu\nu}</code>

By comparing the terms in this Lagrangian with the canonical DHOST basis, we can establish a direct mapping. The functions <code>P</code> and <code>Q</code> correspond to the terms with at most first derivatives of <code>\phi</code>, while the <code>A_i</code> and <code>B_1</code> functions are the coefficients of the terms quadratic and cubic in the second derivatives of <code>\phi</code>, respectively. This yields the following general relations:
*   <code>P(\phi, X) = G_2(\phi, X)</code>
*   <code>Q(\phi, X) = -G_3(\phi, X)</code>
*   <code>A_1(\phi, X) = 2G_{4,X} - XF_4(\phi, X)</code>
*   <code>A_2(\phi, X) = -2G_{4,X} + XF_4(\phi, X)</code>
*   <code>A_3(\phi, X) = 2F_4(\phi, X)</code>
*   <code>A_4(\phi, X) = 0</code>
*   <code>A_5(\phi, X) = 0</code>
*   <code>B_1(\phi, X) = -2F_4(\phi, X)</code>
*   The coefficient of the Ricci scalar is <code>F(\phi, X) = G_4(\phi, X)</code>.

Now, we substitute the specific forms of the functions for the "all-order stable" theory from DHOSTS.pdf:
*   <code>G_2(\phi, X) = G_{2_0}(\phi) - G_{3_0,\phi} X + \frac{c_4}{2} X^2</code>
*   <code>G_3(\phi, X) = G_{3_0}(\phi) - c_4 X</code>
*   <code>G_4(\phi, X) = M_P^2 / 2</code> (constant)
*   <code>F_4(\phi, X) = c_4 / X</code>

Since <code>G_4</code> is a constant, its derivative with respect to <code>X</code>, <code>G_{4,X}</code>, is zero. This significantly simplifies the expressions for <code>A_1</code> and <code>A_2</code>.

*   <code>A_1 = 2(0) - X(c_4/X) = -c_4</code>
*   <code>A_2 = -2(0) + X(c_4/X) = c_4</code>
*   <code>A_3 = 2(c_4/X) = 2c_4/X</code>
*   <code>B_1 = -2(c_4/X) = -2c_4/X</code>

These results are consolidated in the functional identification table below.

#### **3. Functional Identification Table**

| Canonical Function | Derived Form from DHOSTS.pdf |
| :--- | :--- |
| <code>P(\phi,X)</code> | <code>G_{2_0}(\phi) - \frac{dG_{3_0}}{d\phi} X + \frac{c_4}{2} X^2</code> |
| <code>Q(\phi,X)</code> | <code>-G_{3_0}(\phi) + c_4 X</code> |
| <code>A_1(\phi,X)</code> | <code>-c_4</code> |
| <code>A_2(\phi,X)</code> | <code>c_4</code> |
| <code>A_3(\phi,X)</code> | <code>2c_4/X</code> |
| <code>A_4(\phi,X)</code> | <code>0</code> |
| <code>A_5(\phi,X)</code> | <code>0</code> |
| <code>B_1(\phi,X)</code> | <code>-2c_4/X</code> |

Additionally, the coefficient of the Ricci scalar is <code>F(\phi,X) = G_4 = M_P^2/2</code>.

#### **4. Formal Classification**

The classification of DHOST theories is determined by the degeneracy conditions satisfied by the kinetic part of the Lagrangian. These conditions ensure the elimination of the ghost-like Boulware-Deser mode. Following Langlois et al. (2016), we define four key quantities based on the canonical functions:
*   <code>\mathcal{F}_A = A_1 + A_2</code>
*   <code>\mathcal{G}_A = A_3 + X B_{1,X}</code>
*   <code>\mathcal{H}_A = A_4 + B_1/2</code>
*   <code>\mathcal{K}_A = A_5</code>

We compute these quantities for the theory under investigation, assuming <code>c_4 \neq 0</code> (as <code>c_4=0</code> would reduce the theory to Horndeski):

*   <code>\mathcal{F}_A = (-c_4) + (c_4) = 0</code>
*   To compute <code>\mathcal{G}_A</code>, we first find the derivative of <code>B_1</code>: <code>B_{1,X} = \frac{\partial}{\partial X}(-2c_4/X) = 2c_4/X^2</code>.
    Then, <code>\mathcal{G}_A = (2c_4/X) + X(2c_4/X^2) = 2c_4/X + 2c_4/X = 4c_4/X \neq 0</code>.
*   <code>\mathcal{H}_A = 0 + (-2c_4/X)/2 = -c_4/X \neq 0</code>.
*   <code>\mathcal{K}_A = A_5 = 0</code>.

The DHOST classes are defined by which of these quantities vanish:
*   **Quadratic DHOST**: Requires <code>B_1=0</code>. Our theory has <code>B_1 \neq 0</code>, so it is a **cubic DHOST theory**.
*   **Class N-I**: Requires <code>\mathcal{F}_A = 0</code>. This condition is satisfied.
*   **Class N-II**: Requires <code>\mathcal{F}_A = 0</code> and <code>\mathcal{G}_A = 0</code>. Our theory has <code>\mathcal{G}_A \neq 0</code>.
*   **Class M-II**: Requires <code>\mathcal{F}_A = 0</code> and <code>\mathcal{H}_A = 0</code>. Our theory has <code>\mathcal{H}_A \neq 0</code>.

Since the theory satisfies the condition for Class N-I but fails to meet the additional constraints for more restrictive classes like N-II or M-II, we conclude that the kinetic structure of the theory from DHOSTS.pdf belongs to **Class N-I**. This is the most general class of degenerate cubic DHOST theories.

#### **5. Isolation of Minimal Stability Conditions**

The classification as N-I stems from the condition <code>A_1+A_2=0</code>. For any theory constructed from the sum of the Horndeski <code>L_4^H</code> and beyond-Horndeski <code>L_4^{bH}</code> Lagrangians, we have <code>A_1 = 2G_{4,X} - XF_4</code> and <code>A_2 = -2G_{4,X} + XF_4</code>, which means <code>A_1+A_2=0</code> is a structural identity. Therefore, simply being in Class N-I is not a particularly restrictive condition.

The "all-order stability" claimed in DHOSTS.pdf arises not from this general classification alone, but from a more specific and finely-tuned structure. The minimal set of algebraic relations that define the kinetic part of this specific "cornerstone" model are:
1.  **Constant Gravitational Coupling:** <code>G_4(\phi, X) = \text{constant}</code> (specifically <code>M_P^2/2</code>). This implies <code>G_{4,X}=0</code>.
2.  **Specific "Beyond Horndeski" Form:** <code>F_4(\phi, X) = c_4/X</code>. This specific dependence on the kinetic term <code>X</code> is crucial.
3.  **Internal Symmetry Relation:** The functions <code>G_2</code> and <code>G_3</code> are not independent but are linked by the relation <code>G_{2,X} + G_{3,\phi} = c_4 X</code>. This can be seen by taking the derivatives of the forms given in the paper: <code>G_{2,X} = -G_{3_0,\phi} + c_4 X</code> and <code>G_{3,\phi} = G_{3_0,\phi}</code>.

These three conditions are the minimal requirements imposed on the kinetic Lagrangian in DHOSTS.pdf. While they place the theory in the broad DHOST Class N-I, it is this precise combination of constraints that, when coupled with a specific massive graviton potential, is argued to eliminate pathologies and ensure stability. The subsequent analysis of quantum stability and symmetries will rely critically on this specific structure, which goes beyond the general N-I classification.