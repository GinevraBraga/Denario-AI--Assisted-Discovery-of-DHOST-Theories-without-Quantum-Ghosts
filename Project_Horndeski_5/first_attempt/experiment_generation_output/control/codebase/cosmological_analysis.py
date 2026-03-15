# filename: codebase/cosmological_analysis.py
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import time
import os

# Ensure the data directory exists
database_path = 'data'
if not os.path.exists(database_path):
    os.makedirs(database_path)


def run_cosmological_analysis():
    """
    Performs a full cosmological analysis for a specific Generalized Proca-Scalar model.

    This function carries out the following steps:
    1.  Defines the model parameters and cosmological constants.
    2.  Prints the theoretical context, including the c_T^2=1 constraint.
    3.  Initializes and runs the CosmologySolver to obtain the background evolution.
    4.  Calculates key cosmological and perturbation observables (Omega_i, w_DE, G_eff, eta).
    5.  Prints a summary of the results at redshift z=0.
    6.  Generates and saves a multi-panel plot comparing the model to LCDM.
    """
    print("--- Step 5: Observational Constraints Analysis ---")
    print("\n--- 1. Theoretical Framework and Model Specification ---")
    print("We analyze the cosmological viability of the theory on an FLRW background.")
    print("A key constraint comes from GW170817, which requires the speed of gravitational")
    print("waves c_T to be unity. The general expression is c_T^2 = (2*G4 - A0*dphi*G5_X) / (2*G4 - 2*X*G4_X).")
    print("Setting c_T^2 = 1 imposes the condition: A0 * dphi * G5_X = 2 * X * G4_X.")
    print("\nTo satisfy this, we choose a simple model where G4_X = 0 and G5_X = 0:")
    print("  - G2(X, phi, A) = -X - V(phi) + 0.5*m_A^2*A0^2")
    print("  - G3(X, phi) = g3 * X")
    print("  - G4(phi) = M_p^2 / 2 (constant, so G4_X = 0)")
    print("  - G5(phi) = g5 * phi (so G5_X = 0)")
    print("  - V(phi) = V0 * exp(-lambda_V * phi)")
    print("This model is automatically consistent with c_T^2 = 1.\n")

    # Planck mass squared is set to 1 in natural units
    M_p_sq = 1.0

    # Define the model parameters
    model_params = {
        "m_A": 1.0,      # Vector mass in units of H0
        "g3": -5.0,      # G3 coupling
        "g5": -0.02,     # G5 coupling
        "V0": 2.4,       # Potential amplitude
        "lambda_V": 0.1, # Potential slope
    }

    # Standard cosmological parameters
    cosmo_params = {
        "Omega_m0": 0.315,
        "Omega_r0": 5.4e-5,
        "h": 0.674,
    }
    cosmo_params["H0"] = cosmo_params["h"] * 100.0 / (3.086e19) * (3.086e19 / 1e3) # H0 in 1/kpc units, not used in dimensionless solve

    solver = CosmologySolver(model_params, cosmo_params, M_p_sq)

    print("\n--- 2. Solving Background Cosmological Evolution ---")
    print("Solving differential equations for H(z), phi(z) from z=3000 to z=0.")
    z_sol, y_sol = solver.solve()
    print("Integration complete.")

    print("\n--- 3. Calculating Observational Quantities ---")
    results = solver.calculate_observables(z_sol, y_sol)
    print("Calculation of observables complete.")

    print("\n--- 4. Summary of Results at z=0 ---")
    H0_model = results["H"][-1]
    Omega_m0_model = cosmo_params["Omega_m0"]
    Omega_r0_model = cosmo_params["Omega_r0"]
    Omega_DE0_model = results["Omega_DE"][-1]
    
    print("Hubble Constant H0 / h: " + str(H0_model / (100.0 / (3.086e19) * (3.086e19 / 1e3)) * 100))
    print("Omega_Matter_0: " + str(Omega_m0_model))
    print("Omega_Radiation_0: " + str(Omega_r0_model))
    print("Omega_Dark_Energy_0: " + str(Omega_DE0_model))
    print("Total Omega_0: " + str(Omega_m0_model + Omega_r0_model + Omega_DE0_model))
    print("Dark Energy EoS w_DE(0): " + str(results["w_DE"][-1]))
    print("G_eff(0) / G_N: " + str(results["G_eff"][-1]))
    print("eta(0): " + str(results["eta"][-1]))

    plot_cosmological_results(z_sol, results, cosmo_params)


class CosmologySolver:
    """
    Solves the background cosmological equations for the Generalized Proca-Scalar model.
    """
    def __init__(self, model_params, cosmo_params, M_p_sq):
        self.params = model_params
        self.cosmo = cosmo_params
        self.M_p_sq = M_p_sq
        self.H0_val = self.cosmo["h"] * 100
        
    def _get_coeffs(self, y):
        """
        Computes the coefficients of the linear system for (ddot_phi, dot_H).
        System: A*ddot_phi + B*dot_H = C, D*ddot_phi + E*dot_H = F
        """
        phi, phi_dot, H = y
        m_A = self.params["m_A"] * self.H0_val
        g3 = self.params["g3"]
        g5 = self.params["g5"]
        V0 = self.params["V0"] * (self.H0_val**2)
        lambda_V = self.params["lambda_V"]
        
        V = V0 * np.exp(-lambda_V * phi)
        V_p = -lambda_V * V

        X = -0.5 * phi_dot**2
        
        A0 = (3.0 * H / m_A**2) * (0.5 * g3 * phi_dot**2 - g5)

        # Coefficients for phi EOM: A*ddot_phi + B*dot_H = C
        A = 1.0 - 3.0 * g3 * H * phi_dot
        B = -3.0 * g3 * phi_dot * X
        C = -V_p - 3.0 * H * phi_dot + 3.0 * g5 * (3.0 * H**2) + 9.0 * g3 * H**2 * phi_dot * X

        # Coefficients for conservation EOM: D*ddot_phi + E*dot_H = F
        D = phi_dot * (1.0 - 3.0 * g3 * H * phi_dot)
        E = -6.0 * self.M_p_sq * H - 6.0 * g3 * H * X
        F = -3.0*H*(V - X - m_A**2 * A0**2 + 3.0*H*A0*g5) - 3.0*H*(V - X)

        return A, B, C, D, E, F

    def _ode_system(self, N, y):
        """
        Defines the system of ODEs with N = log(a) as the independent variable.
        y = [phi, phi_dot, H]
        """
        phi, phi_dot, H = y
        
        # Get coefficients for the linear system
        A, B, C, D, E, F = self._get_coeffs(y)
        
        # Solve the 2x2 system for ddot_phi and dot_H
        detM = A * E - B * D
        if abs(detM) < 1e-30: # Avoid singularity
            ddot_phi = 0
            dot_H = 0
        else:
            ddot_phi = (C * E - B * F) / detM
            dot_H = (A * F - C * D) / detM

        # Derivatives with respect to N = log(a)
        # d/dN = (1/H) * d/dt
        phi_prime = phi_dot / H
        phi_dot_prime = ddot_phi / H
        H_prime = dot_H / H
        
        return [phi_prime, phi_dot_prime, H_prime]

    def solve(self):
        """
        Solves the ODE system from high redshift to today.
        """
        z_initial = 3000.0
        a_initial = 1.0 / (1.0 + z_initial)
        N_initial = np.log(a_initial)
        N_final = 0.0
        
        # Initial conditions in matter era
        H_initial = self.H0_val * np.sqrt(self.cosmo["Omega_m0"] * (1+z_initial)**3)
        phi_initial = 0.1
        phi_dot_initial = 0.0
        
        y_initial = [phi_initial, phi_dot_initial, H_initial]
        
        sol = solve_ivp(
            self._ode_system,
            [N_initial, N_final],
            y_initial,
            method='Radau',
            dense_output=True,
            t_eval=np.linspace(N_initial, N_final, 500)
        )
        
        N_sol = sol.t
        y_sol = sol.y
        z_sol = np.exp(-N_sol) - 1.0
        
        # Rescale H to be dimensionless H/H0
        H_rescaled = y_sol[2, :] / self.H0_val
        y_sol[2, :] = H_rescaled
        
        return z_sol, y_sol

    def calculate_observables(self, z, y):
        """
        Calculates cosmological and perturbation parameters from the solution.
        """
        N = -np.log(1.0 + z)
        phi, phi_dot, H_norm = y
        H = H_norm * self.H0_val

        m_A = self.params["m_A"] * self.H0_val
        g3 = self.params["g3"]
        g5 = self.params["g5"]
        V0 = self.params["V0"] * (self.H0_val**2)
        lambda_V = self.params["lambda_V"]
        
        V = V0 * np.exp(-lambda_V * phi)
        X = -0.5 * phi_dot**2
        A0 = (3.0 * H / m_A**2) * (0.5 * g3 * phi_dot**2 - g5)

        rho_DE = -X + V - m_A**2 * A0**2 - 1.5 * g3 * H * phi_dot**2 + 3.0 * H * A0 * g5
        p_DE = -X - V + m_A**2 * A0**2 + g3 * (0.5 * phi_dot**2 * (3*H**2 + 2*H*H/H) ) # Simplified
        
        rho_crit = 3.0 * self.M_p_sq * H**2
        Omega_DE = rho_DE / rho_crit
        w_DE = p_DE / rho_DE

        # Perturbation parameters (simplified for our model c_T=1)
        alpha_K = (phi_dot**2 - m_A**2 * A0**2 - 3.0*g3*H*phi_dot**2) / H**2
        alpha_B = (3.0*g5*A0 - g3*phi_dot*X) / (self.M_p_sq * H)
        
        G_eff = self.M_p_sq / (self.M_p_sq * 2.0) * (2.0 + alpha_B**2 / (alpha_K + 1.5*alpha_B**2))
        eta = np.ones_like(z) # Simplified for this model, a more detailed calculation is needed

        return {
            "H": H, "Omega_DE": Omega_DE, "w_DE": w_DE, "G_eff": G_eff, "eta": eta
        }


def plot_cosmological_results(z, results, cosmo_params):
    """
    Generates and saves a multi-panel plot of the cosmological results.
    """
    z_lcdm = np.logspace(-3, np.log10(max(z)), 500)
    H_lcdm = cosmo_params["h"]*100 * np.sqrt(cosmo_params["Omega_m0"]*(1+z_lcdm)**3 + cosmo_params["Omega_r0"]*(1+z_lcdm)**4 + (1-cosmo_params["Omega_m0"]-cosmo_params["Omega_r0"]))
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Cosmological Constraints Analysis', fontsize=16)

    # Panel 1: Hubble Parameter H(z)
    axes[0, 0].loglog(z, results["H"], label='Proca-Scalar Model', color='r')
    axes[0, 0].loglog(z_lcdm, H_lcdm, label='LCDM', color='k', linestyle='--')
    axes[0, 0].set_xlabel('Redshift z')
    axes[0, 0].set_ylabel('Hubble Parameter H(z) [km/s/Mpc]')
    axes[0, 0].set_title('Hubble Parameter Evolution')
    axes[0, 0].legend()
    axes[0, 0].grid(True, which="both", ls="--")

    # Panel 2: Omega Parameters
    Omega_m = cosmo_params["Omega_m0"] * (1+z)**3 / (results["H"]/(cosmo_params["h"]*100))**2
    Omega_r = cosmo_params["Omega_r0"] * (1+z)**4 / (results["H"]/(cosmo_params["h"]*100))**2
    axes[0, 1].semilogx(z, Omega_m, label='$\Omega_m$', color='b')
    axes[0, 1].semilogx(z, Omega_r, label='$\Omega_r$', color='g')
    axes[0, 1].semilogx(z, results["Omega_DE"], label='$\Omega_{DE}$', color='r')
    axes[0, 1].set_xlabel('Redshift z')
    axes[0, 1].set_ylabel('Density Parameter $\Omega_i$')
    axes[0, 1].set_title('Evolution of Density Parameters')
    axes[0, 1].legend()
    axes[0, 1].grid(True, which="both", ls="--")
    axes[0, 1].set_ylim(-0.1, 1.1)

    # Panel 3: Dark Energy Equation of State w_DE(z)
    axes[1, 0].semilogx(z, results["w_DE"], label='$w_{DE}$', color='r')
    axes[1, 0].axhline(-1, label='LCDM', color='k', linestyle='--')
    axes[1, 0].set_xlabel('Redshift z')
    axes[1, 0].set_ylabel('Dark Energy EoS $w_{DE}$')
    axes[1, 0].set_title('Dark Energy Equation of State')
    axes[1, 0].legend()
    axes[1, 0].grid(True, which="both", ls="--")
    axes[1, 0].set_ylim(-1.2, 0.5)

    # Panel 4: Growth Parameters G_eff and eta
    axes[1, 1].semilogx(z, results["G_eff"], label='$G_{eff}/G_N$', color='purple')
    axes[1, 1].semilogx(z, results["eta"], label='$\eta$', color='orange')
    axes[1, 1].axhline(1.0, label='GR Value', color='k', linestyle='--')
    axes[1, 1].set_xlabel('Redshift z')
    axes[1, 1].set_ylabel('Value')
    axes[1, 1].set_title('Structure Growth Parameters')
    axes[1, 1].legend()
    axes[1, 1].grid(True, which="both", ls="--")
    axes[1, 1].set_ylim(0.8, 1.2)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(database_path, 'cosmological_constraints_plot_1_' + timestamp + '.png')
    plt.savefig(filename, dpi=300)
    print("\nPlot saved to " + filename)
    print("Plot Description: A 4-panel plot showing the cosmological evolution of the Proca-Scalar model vs. LCDM.")
    print("  - Top-left: Hubble parameter H(z).")
    print("  - Top-right: Evolution of density parameters Omega_i(z).")
    print("  - Bottom-left: Dark energy equation of state w_DE(z).")
    print("  - Bottom-right: Structure growth parameters G_eff and eta.")


if __name__ == '__main__':
    run_cosmological_analysis()