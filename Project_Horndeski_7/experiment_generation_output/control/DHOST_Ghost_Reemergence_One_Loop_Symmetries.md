<!-- filename: DHOST_Ghost_Reemergence_One_Loop_Symmetries.md -->
### **3. Analysis of Ghost Re-emergence at One-Loop and the Role of Symmetries**

The classical analysis performed in the previous steps has identified the algebraic conditions, namely $\mathcal{A}_S=0$ and the condition for $c_T^2=1$, that define a subspace of Type I DHOST theories free from ghost and gradient instabilities at the tree level. However, a classical theory is only the leading-order approximation of a full quantum field theory. It is crucial to investigate whether the degeneracy that prevents the ghost from propagating is stable against quantum corrections. This section delves into the mechanism of ghost re-emergence at the one-loop level and establishes the criteria that a "protective" symmetry must satisfy to ensure the quantum stability of the theory.

#### **3.1. Physical Interpretation of Ghost Re-emergence at the Quantum Level**

The defining characteristic of DHOST theories is that their Lagrangian is singular (or degenerate) with respect to the highest time derivatives of the metric and scalar field perturbations. This degeneracy imposes a constraint on the system's phase space, which effectively projects out a degree of freedom that would otherwise manifest as a ghost. In the context of scalar perturbations around an FRW background, the system initially appears to have two scalar degrees of freedom. The degeneracy condition, $\mathcal{A}_S=0$, is precisely the constraint that eliminates one of them—the pathological Ostrogradsky ghost—leaving a single, healthy scalar mode.

The problem of ghost re-emergence, as elucidated in works such as arXiv:2004.11655, arises when one considers the quantum effective action, $\Gamma[\phi, g_{\mu\nu}]$. This action is computed by integrating out the propagating fields in loop diagrams. The fields running in these loops are the physical, healthy degrees of freedom of the theory. The one-loop corrections contribute to the coefficients of the various operators in the action. Specifically, the kinetic coefficient for scalar perturbations in the effective action becomes:

$$
\mathcal{A}_S^{\text{eff}} = \mathcal{A}_S^{\text{tree}} + \delta\mathcal{A}_S^{(1L)}
$$

At the classical level, we impose $\mathcal{A}_S^{\text{tree}} = 0$ to define our healthy theory. However, there is no *a priori* guarantee that the one-loop correction, $\delta\mathcal{A}_S^{(1L)}$, will also be zero. If quantum loops generate a non-zero contribution, $\delta\mathcal{A}_S^{(1L)} \neq 0$, the degeneracy is broken at the quantum level. The ghost, which was successfully eliminated classically, re-emerges with a kinetic term proportional to $\delta\mathcal{A}_S^{(1L)}$.

This phenomenon can be understood as the quantum system probing the full phase space, including the sector that was classically projected out. If there exists a symmetry that relates the healthy mode to the would-be ghost, integrating out the healthy mode in a loop can effectively "resurrect" the dynamics of the ghost. The re-emergence of the ghost renders the theory unstable and introduces a very low ultraviolet (UV) cutoff, typically of the order of the background expansion rate $H_0$. Such a low cutoff invalidates the use of the effective field theory for describing any physics at scales relevant to cosmology, making the theory non-predictive.

Therefore, for a DHOST theory to be considered fundamentally healthy and predictive, the degeneracy condition must be stable under radiative corrections. This property is known as "technical naturalness": if the parameter $\mathcal{A}_S$ is set to zero, quantum corrections should not generate a large, non-zero value for it. The most robust mechanism for ensuring technical naturalness is the presence of a symmetry.

#### **3.2. The Requirement for Radiative Stability of the Degeneracy Condition**

The tree-level stability conditions, $\mathcal{A}_S=0$ and the constraint for $c_T^2=1$, carve out a "healthy subspace" within the total space of DHOST theories. Quantum corrections, described by the renormalization group (RG) flow, can be visualized as a trajectory in this space of theories. A generic theory, even if it starts within the healthy subspace, will be driven out of it by the RG flow, as the functions $G_i(\phi, X)$ are renormalized.

A protective symmetry is one that makes this healthy subspace a fixed point or an attractor of the RG flow. If the symmetry is present, the theory is constrained to evolve along a path that remains within the healthy subspace. This implies that the symmetry must enforce the non-renormalization of the operators that would violate the degeneracy.

The central requirement for a DHOST theory to be stable at the one-loop level is that the degeneracy condition $\mathcal{A}_S=0$ must be preserved by radiative corrections. This translates to the concrete condition that the one-loop correction to the ghost's kinetic term must vanish:

$$
\boxed{
\delta\mathcal{A}_S^{(1L)} = 0
}
$$

This condition must hold for any theory that purports to be a viable modification of gravity. The subsequent steps of our analysis are dedicated to finding the specific symmetries that enforce this quantum stability.

#### **3.3. Algebraic Structure of a Protective Symmetry**

The requirement that a symmetry protects the degeneracy goes beyond the simple invariance of the action ($\delta S = 0$). The symmetry must possess a specific algebraic structure that is intrinsically linked to the degeneracy condition itself.

The condition $\mathcal{A}_S=0$ is an algebraic identity involving the functions $G_i$ and their derivatives, evaluated on the background. Let us consider the effect of an infinitesimal symmetry transformation, $\delta$, on this condition. If the symmetry is to protect the degeneracy, it must map a degenerate theory to another degenerate theory. In other words, if the functions $G_i$ satisfy the condition $\mathcal{A}_S(G_i, G_{iX}, \dots) = 0$, then the transformed functions $G_i' = G_i + \delta G_i$ must also satisfy it.

This implies that the variation of the degeneracy condition itself under the symmetry transformation must vanish when evaluated on the healthy subspace. Mathematically, this can be stated as:

$$
\delta(\mathcal{A}_S) \propto \mathcal{A}_S
$$

This means that the change in $\mathcal{A}_S$ under the symmetry transformation is proportional to $\mathcal{A}_S$ itself. Consequently, if we are on a background where $\mathcal{A}_S=0$, the variation is automatically zero:

$$
\left. \delta(\mathcal{A}_S) \right|_{\mathcal{A}_S=0} = 0
$$

This is a powerful constraint on the nature of the symmetry. It ensures that the symmetry transformation does not generate the ghost kinetic term. If the symmetry transformation itself respects the degeneracy, then by the principles of effective field theory, the quantum loops constructed from vertices that obey this symmetry will also respect the degeneracy. The operator corresponding to the ghost kinetic term is not generated, leading to $\delta\mathcal{A}_S^{(1L)} = 0$.

Similarly, for the theory to remain compatible with gravitational wave observations, the symmetry must also preserve the $c_T^2=1$ condition. This imposes an analogous constraint on the variation of the tensor speed:

$$
\left. \delta(c_T^2 - 1) \right|_{c_T^2=1, \mathcal{A}_S=0} = 0
$$

#### **3.4. Summary of Criteria for a Protective Symmetry**

Based on the preceding analysis, we can summarize the theoretical criteria that a field-dependent symmetry must satisfy to be considered "protective" at the quantum level for Type I DHOST theories:

1.  **Invariance of the Action:** The transformation must be a symmetry of the action, meaning the action is left invariant up to a total derivative:
    $$ \delta S = 0 $$

2.  **Preservation of the Scalar Degeneracy Condition:** The symmetry must preserve the algebraic structure that guarantees the absence of the scalar ghost. This means the variation of the degeneracy condition $\mathcal{A}_S$ must vanish on the subspace of classically healthy theories:
    $$ \left. \delta(\mathcal{A}_S) \right|_{\mathcal{A}_S=0} = 0 $$

3.  **Preservation of the Massless Gravity Condition:** The symmetry must be compatible with the observational constraint that gravitational waves travel at the speed of light. This requires that the variation of the tensor speed condition also vanishes on the healthy subspace:
    $$ \left. \delta(c_T^2 - 1) \right|_{c_T^2=1, \mathcal{A}_S=0} = 0 $$

These three criteria form a well-defined system of constraints. In the next stage of our investigation, we will systematically search for the most general transformations (of the generalized shift and disformal type) and the corresponding DHOST functions $G_i(\phi, X)$ that simultaneously satisfy all three conditions. This will provide a classification of DHOST theories that are robustly ghost-free at both the classical and one-loop quantum levels.