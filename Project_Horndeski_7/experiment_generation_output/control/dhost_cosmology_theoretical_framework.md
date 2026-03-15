<!-- filename: dhost_cosmology_theoretical_framework.md -->
### **1. Theoretical Framework and Background Cosmology**

This section establishes the theoretical foundation for the analysis of Type I Degenerate Higher-Order Scalar-Tensor (DHOST) theories. We introduce the action, specify the cosmological background, derive the equations of motion governing the background evolution, and outline the fundamental conditions required for the classical stability of the theory.

#### **1.1. The Cosmological Background: Friedmann-Robertson-Walker Metric**

The analysis of cosmological dynamics and the evolution of structure within the Universe is predicated on the Cosmological Principle, which posits that on sufficiently large scales, the Universe is homogeneous and isotropic. The metric that embodies these symmetries is the Friedmann-Robertson-Walker (FRW) metric. For a spatially flat universe, consistent with modern cosmological observations (e.g., from the Planck satellite), the line element is given by:

$$
 ds^2 = g_{\mu\nu} dx^\mu dx^\nu = -N(t)^2 dt^2 + a(t)^2 \delta_{ij} dx^i dx^j
$$

Here, $a(t)$ is the scale factor, which describes the expansion of the spatial sections of the spacetime, and $N(t)$ is the lapse function. For a comoving observer, physical time corresponds to the case $N(t)=1$, which we will assume after deriving the equations of motion. The Hubble parameter, which measures the rate of expansion, is defined as $H(t) = \dot{a}(t)/a(t)$, where the overdot denotes a derivative with respect to cosmic time $t$.

The choice of the FRW metric is not merely one of convenience; it is a physical necessity for constructing a background that aligns with our observed Universe. The high degree of symmetry simplifies the field equations immensely, allowing for an analytical and numerical treatment of the cosmological evolution. Furthermore, it provides the natural vacuum state upon which to study linear perturbations, which correspond to the seeds of cosmic structure (e.g., galaxies and clusters) and propagating gravitational waves.

In this background, a scalar field $\phi$ consistent with the symmetries of the metric must be homogeneous, i.e., $\phi = \phi_0(t)$. Its kinetic energy is thus given by $X = -g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi = \dot{\phi}_0(t)^2$.

#### **1.2. The Action for Type I DHOST Theories**

We consider the class of Type I DHOST theories, which are a subset of the most general scalar-tensor theories with second-order equations of motion. The action for these theories can be expressed in terms of five arbitrary functions $G_i(\phi, X)$ of the scalar field $\phi$ and its kinetic term $X$. Following the formulation in arXiv:2012.10218, the action is:

$$
 S = \int d^4x \sqrt{-g} \left[ G_2(\phi, X) - G_3(\phi, X)\Box\phi + G_4(\phi, X)R - 2G_{4X}(\phi, X)((\Box\phi)^2 - \phi_{;\mu\nu}\phi^{;\mu\nu}) + G_5(\phi, X)G_{\mu\nu}\phi^{;\mu\nu} - \frac{G_{5X}(\phi,X)}{6}((\Box\phi)^3 - 3\Box\phi \phi_{;\mu\nu}\phi^{;\mu\nu} + 2\phi_{;\mu\nu}\phi^{;\nu\sigma}\phi_{;\sigma}^{\;\mu}) \right]
$$

where:
*   $g$ is the determinant of the metric $g_{\mu\nu}$.
*   $R$ is the Ricci scalar.
*   $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R$ is the Einstein tensor.
*   $\phi_{;\mu\nu} = \nabla_\nu \nabla_\mu \phi$ is the second covariant derivative of the scalar field.
*   $\Box\phi = g^{\mu\nu}\phi_{;\mu\nu}$.
*   $G_{iX} \equiv \partial G_i / \partial X$.

This action is a subclass of the full DHOST Lagrangian, specifically chosen to be "Type I," which implies certain relations among the more general $A_i$ functions that define the complete DHOST theory space. This specific structure is essential for the degeneracy mechanism that we will investigate.

#### **1.3. Background Friedmann Equations**

To derive the equations governing the cosmological background, we evaluate the DHOST action on the FRW metric with $N(t)$ and a homogeneous scalar field $\phi_0(t)$. The relevant geometric and scalar quantities are:

*   $X = \dot{\phi}_0^2$
*   $\Box\phi_0 = - (\ddot{\phi}_0 + 3H\dot{\phi}_0)$
*   $R = 6(\dot{H} + 2H^2)$
*   $G_{00} = 3H^2$
*   $\phi_{;00} = -\ddot{\phi}_0$, $\phi_{;ij} = -a^2 H \dot{\phi}_0 \delta_{ij}$
*   $\phi_{;\mu\nu}\phi^{;\mu\nu} = \ddot{\phi}_0^2 + 3H^2\dot{\phi}_0^2$
*   $G_{\mu\nu}\phi^{;\mu\nu} = -3H^2\ddot{\phi}_0 - 3H\dot{\phi}_0(\dot{H} + 3H^2)$

Substituting these into the action and integrating over spatial dimensions yields the effective Lagrangian for the background:
$S = \int dt \, a^3 \mathcal{L}_{\text{bg}}$, where $\mathcal{L}_{\text{bg}}$ is a function of $a, \dot{a}, \phi_0, \dot{\phi}_0, \ddot{\phi}_0$.

Varying the action with respect to the lapse function $N$ and then setting $N=1$ gives the first Friedmann equation (the Hamiltonian constraint):

$$
 \mathcal{E} \equiv 2X G_{2X} - G_2 + 2X G_{3\phi} - 6H\dot{\phi}_0 G_{3X} X + 6H^2 G_4 - 12 H^2 X G_{4X} - 12 H \dot{\phi}_0 G_{4\phi} + 24 H^2 X^2 G_{4XX} + 24 H^2 X G_{4X} + 24 H \dot{\phi}_0 X G_{4\phi X} - 6H^2 X G_{5\phi} - 6H^3 \dot{\phi}_0 G_5 + 6H^3 \dot{\phi}_0 X G_{5X} - 18 H^2 X^2 G_{5\phi X} - 6 H \dot{\phi}_0 X^2 G_{5\phi\phi} = 0
$$

Varying with respect to the scale factor $a(t)$ gives the second Friedmann equation (the evolution equation):

$$
 \mathcal{P} \equiv G_2 - 2X G_{3\phi} - 2\ddot{\phi}_0 G_{3X} X - 2(\dot{H} + 3H^2)G_4 + 4H\dot{\phi}_0 G_{4\phi} + 4\dot{H}X G_{4X} + 8H^2 X G_{4X} - 8H\dot{\phi}_0 X G_{4\phi X} - 4\ddot{\phi}_0 X G_{4X} - 4\dot{\phi}_0^2 X G_{4XX} + 2H^2 X G_{5\phi} + 2H\dot{\phi}_0 G_{5\phi} + 2\ddot{\phi}_0 X G_{5\phi} + 2\dot{\phi}_0^2 G_{5\phi\phi} X + 4H\dot{\phi}_0 X^2 G_{5\phi X} + 2H\dot{\phi}_0 X G_{5\phi} + (2\dot{H} + 3H^2) \dot{\phi}_0 H G_5 - H\dot{\phi}_0 X(2\dot{H}+3H^2)G_{5X} + 2H^2\ddot{\phi}_0 X G_{5X} + 2H^2\dot{\phi}_0^2 X G_{5XX} = 0
$$

The scalar field equation of motion is obtained by varying with respect to $\phi_0(t)$. These three equations (with one being redundant due to the Bianchi identity) fully determine the dynamics of the FRW background $(\phi_0(t), a(t))$.

#### **1.4. Classical Stability: Degeneracy and Observational Constraints**

For a modified gravity theory to be physically viable, it must be free from pathologies such as ghost and gradient instabilities. Furthermore, it must comply with stringent observational constraints.

**1. Tensor Perturbations and the Speed of Gravitational Waves**

The first crucial test comes from tensor perturbations, $h_{ij}$, which represent gravitational waves. The quadratic action for these modes takes the generic form:

$$
 S_T^{(2)} = \frac{1}{8} \int dt d^3x \, a^3 \mathcal{G}_T \left[ \dot{h}_{ij}^2 - \frac{c_T^2}{a^2} (\partial_k h_{ij})^2 \right]
$$

A healthy theory requires a positive kinetic term, $\mathcal{G}_T > 0$, to avoid ghosts, and a non-negative squared propagation speed, $c_T^2 \ge 0$, to avoid gradient instabilities.

The detection of the binary neutron star merger GW170817 and its electromagnetic counterpart GRB 170817A placed an extraordinary constraint on the speed of gravitational waves, requiring it to be equal to the speed of light to high precision: $|c_T - 1| \lesssim 10^{-15}$. Therefore, any viable cosmological model must enforce $c_T^2 = 1$.

For the DHOST action under consideration, the explicit derivation (to be performed in Step 2) yields the following condition for massless gravity:

$$
 G_4 - X G_{5\phi} - X G_{5X} \ddot{\phi}_0 = G_{4, \text{eff}}
$$
where $G_{4, \text{eff}}$ is the effective Planck mass term appearing in the kinetic part of the tensor action. The condition $c_T^2=1$ imposes a direct algebraic relation between the functions $G_4$ and $G_5$ and their derivatives, evaluated on the background solution:

$$
 \boxed{
 X(G_{5\phi} + \ddot{\phi}_0 G_{5X}) = 0
 }
$$
Since we are interested in non-trivial scalar field dynamics where $X \neq 0$, this simplifies to:
$$
 G_{5\phi} + \ddot{\phi}_0 G_{5X} = 0
$$
This constraint must be imposed on the theory from the outset. It represents a powerful restriction, significantly reducing the available parameter space of DHOST theories.

**2. Scalar Perturbations and the No-Ghost Condition**

DHOST theories are defined by the property of "degeneracy." A generic higher-order theory contains more degrees of freedom than General Relativity, one of which is typically an Ostrogradsky ghost—a mode with negative kinetic energy that leads to catastrophic vacuum instability. DHOST theories evade this by possessing a Lagrangian that is singular (degenerate) with respect to the highest derivatives, effectively projecting out the ghost.

When analyzing scalar perturbations around the FRW background, this degeneracy manifests in the quadratic action for the perturbations. After integrating out auxiliary fields, the action for the physical scalar mode (e.g., the curvature perturbation $\psi$) must not contain terms proportional to its second time derivative, $\ddot{\psi}^2$. The quadratic action for scalar modes schematically takes the form:

$$
 S_S^{(2)} = \int dt d^3x \, a^3 \left[ \mathcal{A}_S \dot{\psi}^2 + \mathcal{B}_S \frac{(\partial_i \psi)^2}{a^2} + \dots \right]
$$
The coefficient $\mathcal{A}_S$ is a complicated function of the background quantities ($H, \dot{H}, \phi_0, \dot{\phi}_0, \dots$) and the DHOST functions ($G_i$ and their derivatives). The defining condition of a DHOST theory is that this kinetic coefficient vanishes identically:

$$
 \boxed{
 \mathcal{A}_S = 0
 }
$$

This is the tree-level no-ghost condition. It is an algebraic constraint on the functions $G_i$ that ensures the theory propagates only one scalar degree of freedom, which is healthy. The explicit derivation of the full expression for $\mathcal{A}_S$ is a primary task for the subsequent analysis. The core of our investigation will be to find theories where this condition, along with the $c_T^2=1$ condition, is protected by a symmetry, ensuring stability not only at the classical level but also against quantum corrections.