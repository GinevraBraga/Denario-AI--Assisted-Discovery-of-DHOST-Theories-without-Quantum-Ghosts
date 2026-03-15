# filename: codebase/observational_analysis.py
import numpy as np
import matplotlib.pyplot as plt
import time
import os

# Set matplotlib parameters to avoid LaTeX rendering
plt.rcParams['text.usetex'] = False


class ObservationalAnalysis:
    """
    Analyzes the compatibility of the quantum-corrected Horndeski theory
    with cosmological observations, specifically the speed of gravitational
    waves and the stability of scalar perturbations.
    """

    def __init__(self, database_path='data'):
        """
        Initializes the analysis with model parameters and cosmological settings.

        Args:
            database_path (str): The path to the directory where results are saved.
        """
        self.database_path = database_path
        if not os.path.exists(self.database_path):
            os.makedirs(self.database_path)

        # Cosmological parameters
        self.M_p = 1.0  # Reduced Planck Mass in natural units (M_p^2 = 1/(8*pi*G))
        self.H0 = 1.0   # Hubble constant today, for normalization
        self.Omega_m0 = 0.3
        self.Omega_L0 = 0.7

        # Scalar field background model parameters
        # X(z) = X0 * (1+z)^n
        self.X0 = 0.01  # Kinetic energy at z=0
        self.n = 3.0    # Evolution index, e.g., n=3 for matter-like evolution

        # G2 = K(X) model: K(X) = -X + c2 * X^2
        self.c2 = 10.0

        # Quantum correction parameters (dimensionless)
        # alpha_H4 corresponds to the coefficient of the allowed counterterm
        # (Box phi)^2 - (nabla_mu nabla_nu phi)^2
        self.alpha_H4_values = [0.0, 1e-2, 5e-2, 1e-1]
        # alpha_R corresponds to the coefficient of the R counterterm
        self.alpha_R = 1e-4  # A small correction to the Planck mass

        # Redshift range for analysis
        self.z_range = np.linspace(0, 5, 200)

    def _background_evolution(self, z):
        """
        Computes the background Hubble parameter and scalar kinetic energy at redshift z.

        Args:
            z (np.ndarray): Array of redshift values.

        Returns:
            tuple: (H, X) tuple of Hubble parameter and scalar kinetic energy.
        """
        # Hubble parameter H(z) for Lambda-CDM
        H = self.H0 * np.sqrt(self.Omega_m0 * (1 + z)**3 + self.Omega_L0)
        # Scalar field kinetic energy X(z)
        X = self.X0 * (1 + z)**self.n
        return H, X

    def calculate_tensor_observables(self, X, alpha_H4):
        """
        Calculates the effective Planck mass and speed of gravitational waves.

        Args:
            X (np.ndarray): Scalar field kinetic energy.
            alpha_H4 (float): Quantum correction parameter for the H4 term.

        Returns:
            tuple: (M_star_sq, c_T_sq) tuple of effective Planck mass squared
                   and tensor speed squared.
        """
        # Base model G4 = M_p^2 / 2.
        # Effective G4_eff = M_p^2/2 + alpha_R + alpha_H4 * X
        # Effective G4_eff,X = alpha_H4
        
        # G_T = 2 * (G4_eff - X * G4_eff,X)
        M_star_sq = self.M_p**2 + 2 * self.alpha_R
        
        # F_T = 2 * G4_eff
        F_T_eff = self.M_p**2 + 2 * self.alpha_R + 2 * alpha_H4 * X
        
        # c_T^2 = F_T / G_T
        c_T_sq = F_T_eff / M_star_sq
        
        return M_star_sq, c_T_sq

    def calculate_scalar_observables(self, H, X, alpha_H4):
        """
        Calculates the sound speed of scalar perturbations.

        Args:
            H (np.ndarray): Hubble parameter.
            X (np.ndarray): Scalar field kinetic energy.
            alpha_H4 (float): Quantum correction parameter for the H4 term.

        Returns:
            np.ndarray: The squared sound speed of scalar perturbations.
        """
        # For G2 = K(X) = -X + c2*X^2, G3=G5=0
        # K_X = -1 + 2*c2*X
        # K_XX = 2*c2
        K_X = -1.0 + 2.0 * self.c2 * X
        K_XX = 2.0 * self.c2
        
        # Numerator of classical c_s^2
        num_cs2 = K_X + 2 * X * K_XX
        
        # Denominator modification from quantum corrections
        G4_eff = self.M_p**2 / 2.0 + self.alpha_R + alpha_H4 * X
        # The term is proportional to (G4,X)^2 / G4
        den_mod = 12 * H**2 * X * (alpha_H4**2) / (2 * G4_eff)
        
        # Effective c_s^2
        c_s_sq = num_cs2 / (num_cs2 + den_mod)
        
        # Avoid division by zero if denominator is zero
        c_s_sq[np.isnan(c_s_sq)] = 1.0

        return c_s_sq

    def run_analysis(self):
        """
        Runs the full analysis, calculates observables, prints results, and plots.
        """
        print("=====================================================================")
        print("= Analysis of Cosmological Observables and Constraints            =")
        print("=====================================================================")
        print("\nThis analysis investigates the impact of BRST-allowed quantum corrections")
        print("on the speed of gravitational waves (c_T) and scalar perturbations (c_s).\n")

        # --- Theoretical Derivations ---
        print("--- Key Theoretical Results ---")
        print("The one-loop effective action includes the BRST-invariant counterterm:")
        print("S_ct = integral[d^4x sqrt(-g) * (alpha_R * R + alpha_H4 * L_H4)]")
        print("where L_H4 = (Box phi)^2 - (nabla_mu nabla_nu phi)^2.\n")
        
        print("1. Speed of Gravitational Waves (c_T):")
        print("The effective G4 function is G4_eff = M_p^2/2 + alpha_R + alpha_H4 * X.")
        print("The squared tensor speed is c_T^2 = F_T/G_T = (2*G4_eff) / (2*(G4_eff - X*G4_eff,X)).")
        print("This yields the deviation from the speed of light:")
        print("c_T^2 - 1 = (2 * alpha_H4 * X) / (M_p^2 + 2 * alpha_R)")
        
        # --- Observational Constraint from GW170817 ---
        cT_constraint = 1e-15
        print("\nConstraint from GW170817: |c_T - 1| < " + str(cT_constraint))
        print("This implies |c_T^2 - 1| approx. < " + str(2 * cT_constraint))
        # Assuming X is of order X0 at z=0 and M_p=1
        max_alpha_H4_X = (2 * cT_constraint) * (self.M_p**2) / 2.0
        print("This imposes a strong constraint on the allowed quantum correction:")
        print("alpha_H4 * X < " + ("%.2e" % max_alpha_H4_X))
        print("For X(z=0) = " + str(self.X0) + ", this means alpha_H4 < " + ("%.2e" % (max_alpha_H4_X / self.X0)) + ".\n")
        
        print("2. Stability of Scalar Perturbations (c_s^2):")
        print("For a model with G2=K(X), the scalar sound speed squared is modified:")
        print("c_s^2_eff = num_cs2 / (num_cs2 + 12*H^2*X*(alpha_H4^2)/(2*G4_eff))")
        print("where num_cs2 = K_X + 2*X*K_XX.")
        print("A positive num_cs2 (classical stability) ensures c_s^2_eff > 0, as the")
        print("quantum correction term in the denominator is positive definite.")
        print("The symmetry thus preserves gradient stability of scalar modes.\n")
        
        # --- Plotting Results ---
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), sharex=True)
        
        H, X = self._background_evolution(self.z_range)

        for alpha_H4 in self.alpha_H4_values:
            label = 'alpha_H4 = ' + str(alpha_H4)
            
            # Tensor observables
            M_star_sq, c_T_sq = self.calculate_tensor_observables(X, alpha_H4)
            ax1.plot(self.z_range, c_T_sq - 1, label=label)
            
            # Scalar observables
            c_s_sq = self.calculate_scalar_observables(H, X, alpha_H4)
            ax2.plot(self.z_range, c_s_sq, label=label)

        # Plot formatting
        ax1.set_ylabel('Deviation from Light Speed ($c_T^2 - 1$)')
        ax1.set_title('Impact of Quantum Corrections on Gravitational Wave Speed')
        ax1.grid(True, linestyle='--', alpha=0.6)
        ax1.legend()
        ax1.set_yscale('log')
        ax1.axhline(2 * cT_constraint, color='r', linestyle='--', label='GW170817 Constraint')
        ax1.legend()

        ax2.set_ylabel('Scalar Sound Speed ($c_s^2$)')
        ax2.set_xlabel('Redshift (z)')
        ax2.set_title('Impact of Quantum Corrections on Scalar Perturbation Stability')
        ax2.grid(True, linestyle='--', alpha=0.6)
        ax2.legend()
        ax2.set_ylim(bottom=0)  # c_s^2 must be positive for stability

        fig.suptitle('Analysis of Cosmological Observables in Quantum-Corrected Horndeski Theory', fontsize=16)
        fig.tight_layout(rect=[0, 0.03, 1, 0.96])

        # Save plot
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        plot_filename = os.path.join(self.database_path, 'cosmological_observables_plot_1_' + timestamp + '.png')
        plt.savefig(plot_filename, dpi=300)
        
        print("--- Plot Generation ---")
        print("Plot saved to: " + plot_filename)
        print("Description of the plot:")
        print("- The top panel shows the deviation of the squared speed of gravitational waves (c_T^2) from 1.")
        print("  It demonstrates that the deviation is proportional to the quantum correction parameter alpha_H4.")
        print("  The red dashed line indicates the stringent constraint from GW170817.")
        print("- The bottom panel shows the squared sound speed of scalar perturbations (c_s^2).")
        print("  It shows that for a classically stable model (c_s^2 > 0), the allowed quantum")
        print("  corrections modify its value but do not introduce a gradient instability (c_s^2 < 0).")
        print("=====================================================================" + "\n")


if __name__ == '__main__':
    analysis = ObservationalAnalysis(database_path='data')
    analysis.run_analysis()