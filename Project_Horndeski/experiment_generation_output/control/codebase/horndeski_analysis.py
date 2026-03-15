# filename: codebase/horndeski_analysis.py
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import matplotlib

# Set backend to Agg to avoid display issues in environments without a GUI
matplotlib.use('Agg')

def analyze_qskp_model(c_B, w0, z_range, H0, Omega_m0):
    """
    Analyzes a QKSP-symmetric Horndeski model for a given set of parameters.

    This function calculates the evolution of the effective gravitational constant (G_eff)
    and the gravitational slip (eta) for a model defined by a wCDM background and
    a specific parameterization of the Horndeski 'alpha_B' parameter.

    Args:
        c_B (float): The coupling constant for the braiding parameter alpha_B.
        w0 (float): The equation of state parameter for dark energy.
        z_range (np.ndarray): An array of redshift values for the calculation.
        H0 (float): The Hubble constant at z=0, in km/s/Mpc.
        Omega_m0 (float): The matter density parameter at z=0.

    Returns:
        tuple: A tuple containing arrays for redshift, G_eff/G_N, and eta.
    """
    a_range = 1.0 / (1.0 + z_range)
    Omega_DE0 = 1.0 - Omega_m0
    
    # Calculate Hubble parameter H(a)
    H_a = H0 * np.sqrt(Omega_m0 * a_range**(-3) + Omega_DE0 * a_range**(-3.0 * (1.0 + w0)))
    
    # Calculate dark energy density fraction Omega_DE(a)
    Omega_DE_a = (Omega_DE0 * a_range**(-3.0 * (1.0 + w0))) / (H_a / H0)**2
    
    # Parameterize the braiding alpha_B
    alpha_B_a = c_B * Omega_DE_a
    
    # In the quasi-static, sub-horizon limit for this class of models (G4=const, G5=0),
    # the effective gravitational constant and slip parameter have simple forms.
    g_eff_over_gn = 1.0 / (1.0 - alpha_B_a)
    eta_a = np.ones_like(a_range)
    
    return z_range, g_eff_over_gn, eta_a

def main():
    """
    Main function to run the phenomenological analysis, generate plots, and print results.
    """
    # --- Cosmological and Model Parameters ---
    H0 = 67.4  # Hubble constant in km/s/Mpc (Planck 2018)
    Omega_m0 = 0.315 # Matter density parameter at z=0 (Planck 2018)
    w0 = -1.0 # Equation of state for the background (LCDM)

    # Sensitivity analysis for the braiding coupling constant c_B
    cB_values = [0.05, 0.1, -0.05, -0.1]
    
    # Redshift range for analysis
    z_range = np.linspace(0, 3, 200)
    
    results = {}
    
    print("--- Phenomenological Viability Analysis of QKSP-Symmetric Model ---")
    print("Cosmological Parameters:")
    print("H0 = " + str(H0) + " km/s/Mpc")
    print("Omega_m0 = " + str(Omega_m0))
    print("Background w_DE = " + str(w0))
    print("\nModel Assumptions:")
    print("c_T^2 = 1 (G4=const, G5=0)")
    print("c_s^2 = 1 (QKSP condition)")
    print("alpha_B = c_B * Omega_DE(a)")
    print("Analysis in Quasi-Static limit.")
    print("-" * 60)

    for c_B in cB_values:
        z, g_eff, eta = analyze_qskp_model(c_B, w0, z_range, H0, Omega_m0)
        results[c_B] = {'z': z, 'g_eff': g_eff, 'eta': eta}

    # --- Plotting Results ---
    fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True)
    fig.suptitle('Phenomenological Viability of QKSP-Symmetric Horndeski Model', fontsize=16)

    # Plot w_DE
    axes[0].axhline(w0, color='k', linestyle='--', label='LCDM (w_DE = -1)')
    axes[0].set_ylim(-1.2, -0.8)
    axes[0].set_ylabel('w_DE(z)')
    axes[0].set_title('Dark Energy Equation of State (Background)')
    axes[0].legend()
    axes[0].grid(True)

    # Plot G_eff
    axes[1].axhline(1.0, color='k', linestyle='--', label='General Relativity')
    for c_B, res in results.items():
        label_str = 'c_B = ' + str(c_B)
        axes[1].plot(res['z'], res['g_eff'], label=label_str)
    axes[1].set_ylabel('G_eff(z) / G_N')
    axes[1].set_title('Effective Gravitational Constant')
    axes[1].legend()
    axes[1].grid(True)

    # Plot eta
    axes[2].axhline(1.0, color='k', linestyle='--', label='General Relativity')
    for c_B, res in results.items():
        # All models have eta=1 in this subclass
        if c_B == cB_values[0]: # Plot only once to avoid overlap
             axes[2].plot(res['z'], res['eta'], color='r', label='QKSP Model (G5=0)')
    axes[2].set_ylim(0.95, 1.05)
    axes[2].set_xlabel('Redshift (z)')
    axes[2].set_ylabel('eta(z)')
    axes[2].set_title('Gravitational Slip Parameter')
    axes[2].legend()
    axes[2].grid(True)
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.96])

    # --- Saving Plot ---
    database_path = 'data'
    if not os.path.exists(database_path):
        os.makedirs(database_path)
        
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    plot_filename = os.path.join(database_path, 'horndeski_phenomenology_plot_1_' + timestamp + '.png')
    plt.savefig(plot_filename, dpi=300)
    plt.close(fig)
    
    print("\nPlot saved to: " + plot_filename)
    print("Plot Description: Evolution of the dark energy equation of state (w_DE),")
    print("the effective gravitational constant (G_eff), and the gravitational slip (eta)")
    print("as a function of redshift for several QKSP-symmetric models with varying")
    print("braiding parameter coupling c_B.")
    print("-" * 60)

    # --- Printing Key Statistics ---
    print("Key Numerical Results (G_eff / G_N):")
    z_points = [0.0, 1.0]
    for c_B, res in results.items():
        print("\nModel: c_B = " + str(c_B))
        for z_val in z_points:
            idx = np.argmin(np.abs(res['z'] - z_val))
            g_eff_val = res['g_eff'][idx]
            print("  at z = " + str(z_val) + ": G_eff / G_N = " + str(round(g_eff_val, 4)))


if __name__ == '__main__':
    main()
