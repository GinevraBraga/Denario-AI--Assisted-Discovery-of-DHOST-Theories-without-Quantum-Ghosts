Starting from the scalar--tensor action
\begin{align}
S[g_{\mu\nu},\phi]=& \int d^4x\,\sqrt{-g}\Big[F\left(X,\phi\right)R+C^{\mu\nu\rho\sigma}\nabla_\mu\nabla_\nu \phi\nabla_\rho\nabla_\sigma \phi\Big]
\end{align}
where 
\begin{equation}
X \equiv g^{\mu\nu}\nabla_\mu\phi\,\nabla_\nu\phi ,
\end{equation}
and 
\begin{align}
C^{\mu\nu,\rho\sigma}
&=\frac{1}{2} A_1\left(g^{\mu\rho} g^{\nu\sigma}+ g^{\mu\sigma} g^{\nu\rho}\right)+ A_2\, g^{\mu\nu}g^{\rho\sigma}\nonumber\\
&+ \frac{1}{2} A_3\left(\phi^\mu \phi^\nu g^{\rho\sigma}+ \phi^\rho \phi^\sigma g^{\mu\nu}\right)\nonumber\\
&+ \frac{1}{4} A_4\left(\phi^\mu \phi^\rho g^{\nu\sigma}+ \phi^\nu \phi^\rho g^{\mu\sigma}+ \phi^\mu\phi^\sigma g^{\nu\rho}+ \phi^\nu \phi^\sigma g^{\mu\rho}\right)+ A_5\, \phi^\mu \phi^\nu \phi^\rho \phi^\sigma \,,
\end{align}
with $\phi^\mu=g^{\mu\nu}\nabla_\mu\phi$,
Focus on the Type $Ia$ class, namely the ones such that the degeneracy condition gives:
\begin{equation}
    \left\{
    \begin{aligned}
        &A_1=-A_2\\
        &F+XA_2\neq 0\\
        &A_4=\frac{1}{8\,(F - X A_1)^2}\Big[-16 X A_1^3+ 4\bigl(3F + 16 X F_X\bigr) A_1^2- X^2 F\, A_3^2\nonumber\\
        &\qquad- \bigl(16 X^2 F_X - 12 X F\bigr) A_3 A_1- 16 F_X \bigl(3F + 4 X F_X\bigr) A_1\nonumber\\
        &\qquad+ 8 F \bigl(X F_X - F\bigr) A_3+ 48 F\, F_X^2\Big] ,\\
        &A_5=\frac{\bigl(4 F_X - 2 A_1 + X A_3\bigr)\bigl(-2 A_1^2 - 3 X A_1 A_3 + 4 F_X A_1 + 4 F A_3\bigr)}{8\,(F - X A_1)^2}\,,
    \end{aligned}\right.
\end{equation}
where $F_X=\partial_X F$ and $F,A_1,A_3$ free functions depending only on $\phi$ and $X$. 
Then implement the following gauge transformations on the fields: 
$$\delta_\epsilon \phi(x) = \epsilon(x) \Lambda(\phi, X)$$
and 
$$\delta_\epsilon g_{\mu\nu}(x) = \epsilon(x) \mathcal{L}_{\xi} g_{\mu\nu}$$
where $\mathcal{L}_{\xi}$ denotes the Lie derivative along a vector field $\xi^\mu$. This vector field is constructed from the scalar field itself, $\xi^\mu = \alpha(\phi, X) \phi^\mu$, with $\phi^\mu = g^{\mu\nu}\partial_\nu\phi$. Here, $\epsilon(x)$ is an arbitrary spacetime-dependent function, acting as the gauge parameter, while $\Lambda(\phi, X)$ and $\alpha(\phi, X)$ are functions of the scalar field and its kinetic term, which are to be determined through the requirement of action invariance.
Show that requiring the Type $Ia$ action to be invariant under these transformations give a set of partial differential equations for the parameters $\Lambda$ and $\alpha$ which are mathematically equivalent to the solutions of the degeneracy conditions.