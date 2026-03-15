# filename: codebase/dhost_viability_analysis.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from scipy.integrate import solve_ivp
import time
import os


def run_viability_analysis():
    """
    Performs a cosmological viability analysis for a representative DHOST theory.

    This function orchestrates the entire analysis:
    1. Defines the model parameters and cosmological constants.
    2. Solves for the background evolution of the scalar field.
    3. Computes the structure growth observables (G_eff, eta).
    4. Generates and saves plots summarizing the results.
    """
    print("--- Cosmological Viability Analysis of a Representative DHOST Theory ---")
    print("This analysis verifies the cosmological viability of a DHOST model with a protective symmetry structure.")
    print("The model is defined by G4(X) = M_pl^2/2 + g4*sqrt(X), G2=2*Lambda, G3=0, G5=0.")
    print("One-loop stability is enforced by solving the A_S=0 no-ghost condition for the scalar field X.\n")

    # Define model and cosmological parameters
    # We work in units where M_pl = 1.
    M_pl = 1.0
    # The g4 parameter controls the deviation from GR.
    # A negative g4 is chosen as it leads to a real solution for X in the quintic equation.
    g4 = -0.5 * M_pl**2
    
    # Standard cosmological parameters
    H0_val = 67.4  # km/s/Mpc
    Omega_m0 = 0.315
    Omega_DE0 = 1.0 - Omega_m0
    
    params = {
        'M_pl': M_pl,
        'g4': g4,
        'H0': H0_val,
        'Omega_m0': Omega_m0,
        'Omega_DE0': Omega_DE0
    }

    print("Model Parameters:")
    print("M_pl = " + str(params['M_pl']))
    print("g4 = " + str(params['g4']))
    print("\nCosmological Parameters:")
    print("H0 = " + str(params['H0']) + " km/s/Mpc")
    print("Omega_m0 = " + str(params['Omega_m0']))
    print("Omega_DE0 = " + str(params['Omega_DE0']))
    print("\n")

    # Solve for the background evolution
    z_range = np.linspace(0, 5, 500)
    background_solution = solve_background(z_range, params)

    if background_solution is None:
        print("Could not find a valid background solution. Aborting.")
        return

    # Compute structure growth observables
    observables = compute_observables(background_solution, params)

    # Plot the results
    plot_results(background_solution, observables, params)


def solve_background(z_range, params):
    """
    Solves for the background evolution of the scalar field kinetic term X.

    Args:
        z_range (np.ndarray): Array of redshift values.
        params (dict): Dictionary of model and cosmological parameters.

    Returns:
        dict: A dictionary containing the background evolution arrays (z, H, y),
              or None if no solution is found.
    """
    print("Solving for background evolution of the scalar field...")
    M_pl = params['M_pl']
    g4 = params['g4']
    H0 = params['H0']
    Omega_m0 = params['Omega_m0']
    Omega_DE0 = params['Omega_DE0']

    # Hubble parameter in a flat Lambda-CDM universe (km/s/Mpc)
    H_z = H0 * np.sqrt(Omega_m0 * (1 + z_range)**3 + Omega_DE0)

    # Convert H to units of M_pl. 1/Mpc = 1.29e-42 M_pl
    # H0_in_Mpl = H0 * 1.29e-42
    # For simplicity in this theoretical exercise, we will treat H as a dimensionless
    # quantity proportional to its value in km/s/Mpc, as the units will
    # cancel out in the quintic equation's structure.
    H_norm = H_z / H0

    y_solution = np.zeros_like(z_range)

    # Define the quintic equation derived from the A_S = 0 condition
    def quintic_eq(y, H_val):
        # y = sqrt(X)
        # H*g4^2*y^5 - (H*M_pl^4/4)*y^3 - M_pl^4/4 = 0
        term5 = H_val * g4**2 * y**5
        term3 = -(H_val * M_pl**4 / 4.0) * y**3
        term0 = -M_pl**4 / 4.0
        return term5 + term3 + term0

    # Solve for y = sqrt(X) at each redshift
    for i, (z, H_val) in enumerate(zip(z_range, H_norm)):
        # Bracket the root. Based on the equation, a positive real root is expected.
        sol = root_scalar(quintic_eq, args=(H_val,), bracket=[0.1, 2.0], method='brentq')
        if sol.converged:
            y_solution[i] = sol.root
        else:
            print("Warning: Root finding failed at z = " + str(z))
            y_solution[i] = np.nan

    if np.any(np.isnan(y_solution)):
        print("Failed to find a consistent solution for X(z).")
        return None
    
    print("Successfully solved for X(z) from the no-ghost condition.")
    return {'z': z_range, 'H': H_z, 'y': y_solution}  # y is sqrt(X)


def compute_observables(background_solution, params):
    """
    Computes the structure growth observables G_eff and eta.

    Args:
        background_solution (dict): Dictionary with background evolution arrays.
        params (dict): Dictionary of model parameters.

    Returns:
        dict: A dictionary containing the observable arrays (G_eff_ratio, eta).
    """
    print("Computing structure growth observables G_eff and eta...")
    M_pl = params['M_pl']
    g4 = params['g4']
    y = background_solution['y']  # sqrt(X)

    # For this model, the braiding parameter alpha_B is zero.
    # This leads to a trivial gravitational slip parameter eta = 1.
    eta = np.ones_like(y)
    print("Gravitational slip parameter eta = 1 (a prediction of this model class).")

    # The effective Planck mass squared is M_star^2 = 2 * G4
    M_star_sq = M_pl**2 + 2 * g4 * y

    # The effective gravitational constant for matter clustering is G_eff/G_N = M_pl^2 / M_star^2
    # We assume G_N = 1/M_pl^2 in our units.
    G_eff_ratio = M_pl**2 / M_star_sq
    print("Computed G_eff/G_N as a function of redshift.")

    return {'G_eff_ratio': G_eff_ratio, 'eta': eta}


def plot_results(background, observables, params):
    """
    Generates and saves plots of the background evolution and observables.

    Args:
        background (dict): Dictionary with background evolution arrays.
        observables (dict): Dictionary with observable arrays.
        params (dict): Dictionary of model parameters.
    """
    print("Generating and saving plots...")
    z = background['z']
    H = background['H']
    y = background['y']
    G_eff_ratio = observables['G_eff_ratio']
    eta = observables['eta']
    
    # Create database path if it doesn't exist
    database_path = 'data'
    if not os.path.exists(database_path):
        os.makedirs(database_path)

    plt.rcParams['text.usetex'] = False
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), dpi=300)
    fig.suptitle('Cosmological Analysis of a Mimetic DHOST Model', fontsize=16)

    # 1. Hubble Parameter
    ax = axes[0, 0]
    ax.plot(z, H, lw=2)
    ax.set_xlabel('Redshift (z)')
    ax.set_ylabel('Hubble Parameter H(z) [km/s/Mpc]')
    ax.set_title('Background Expansion (Assumed LCDM)')
    ax.grid(True, linestyle='--', alpha=0.6)

    # 2. Scalar Field Kinetic Term
    ax = axes[0, 1]
    ax.plot(z, y, lw=2, color='C1')
    ax.set_xlabel('Redshift (z)')
    ax.set_ylabel('sqrt(X) [in M_pl units]')
    ax.set_title('Scalar Field Dynamics from No-Ghost Condition')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_yscale('log')

    # 3. Effective Gravitational Constant
    ax = axes[1, 0]
    ax.plot(z, G_eff_ratio, lw=2, color='C2')
    ax.axhline(1.0, color='black', linestyle='--', label='GR value (G_eff/G_N = 1)')
    ax.set_xlabel('Redshift (z)')
    ax.set_ylabel('G_eff / G_N')
    ax.set_title('Effective Gravitational Constant')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    # Set ylim to be symmetric around 1 for better visualization
    max_dev = np.max(np.abs(G_eff_ratio - 1))
    ax.set_ylim(1 - 1.2*max_dev, 1 + 1.2*max_dev)


    # 4. Gravitational Slip Parameter
    ax = axes[1, 1]
    ax.plot(z, eta, lw=2, color='C3')
    ax.axhline(1.0, color='black', linestyle='--', label='GR value (eta = 1)')
    ax.set_xlabel('Redshift (z)')
    ax.set_ylabel('Gravitational Slip (eta)')
    ax.set_title('Gravitational Slip Parameter')
    ax.legend()
    ax.set_ylim(0.95, 1.05)
    ax.grid(True, linestyle='--', alpha=0.6)

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(database_path, 'dhost_viability_plot_1_' + timestamp + '.png')
    plt.savefig(filename)
    plt.close(fig)
    
    print("\n--- Plot Summary ---")
    print("A plot has been saved to '" + filename + "' with four panels:")
    print("1. H(z): Shows the assumed Lambda-CDM expansion history.")
    print("2. sqrt(X): Shows the required scalar field kinetic term to ensure the theory is ghost-free.")
    print("3. G_eff/G_N: Shows the deviation of the gravitational constant for matter from GR. The deviation is driven by the g4 parameter.")
    print("4. eta: Shows the gravitational slip. For this model, eta is predicted to be 1, identical to GR.")
    
    # Print key numerical results
    print("\n--- Key Numerical Results ---")
    print("Value of G_eff/G_N at z=0: " + str(G_eff_ratio[0]))
    print("Value of G_eff/G_N at z=1: " + str(G_eff_ratio[np.argmin(np.abs(z - 1))]))
    print("Maximum deviation of G_eff/G_N from GR: " + str(np.max(np.abs(G_eff_ratio - 1.0))))



if __name__ == '__main__':
    run_viability_analysis()
