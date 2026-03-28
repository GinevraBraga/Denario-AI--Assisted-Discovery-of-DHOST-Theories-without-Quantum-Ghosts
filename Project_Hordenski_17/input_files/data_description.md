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
Employ the path integral formalism to derive the associated effective action $\Gamma^{(1)}$ and construct within it the most general Lagrangian of counter terms, $\L_{ct}$, that could
potentially be generated at the one-loop level.
Then impose the functions $\Lambda$ and $\alpha$ to take the following form:
\begin{align}
\label{eq:gauge_parameters_explicit}
\Lambda(\phi, X) &= c_0 - c_1 X\,, \\
\alpha(\phi, X) &= -c_1\,,
\end{align}
with $c_0$ and $c_1$ constants, and the free function of the theory in terms of these parameters read
\begin{align}
\label{eq:TypeI_free_functions}
F_0&=c_0\,,\\
A_1&=-A_2 = -c_1 \,,\\
A_3&=0\,,\\
A_4 &= \frac{-16Xc_1^3 + 12c_0c_1^2}{8(c_0 - Xc_1)^2}\,, \\
A_5 &= \frac{4c_1^3}{8(c_0 - Xc_1)^2}\,.
\end{align}
Insert these into the counter term Lagrangian and show explicitly the final form of the counter term lagrangian. Particularly try to identify corrections proportional to the Gauss-Bonnet scalar 
\begin{equation}
\label{eq:gauss_bonnet_scalar}
G = R^2 - 4R_{\mu\nu}R^{\mu\nu} + R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}\,,
\end{equation} and the Weyl tensor
\begin{equation}
\label{eq:Weyl_scalar}
W = C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma} = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} - 2R_{\mu\nu}R^{\mu\nu} + \frac{1}{3}R^2\,.
\end{equation}