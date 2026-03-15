# filename: codebase/visualize_solution_space.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import os


def visualize_solution_space():
    """
    Generates and saves plots illustrating the solution space of the
    derived partial differential equations for beta_GB(phi, X) and beta_W2(phi, X).

    The PDEs derived from both symmetry and degeneracy analysis are:
    1.  ∂β_W²/∂X = 0
    2.  ∂β_GB/∂X + 2 * ∂β_W²/dφ = 0

    The general solution is:
    -   β_W²(φ) = f(φ)
    -   β_GB(φ, X) = -2 * f'(φ) * X + g(φ)
    where f(φ) and g(φ) are arbitrary functions.

    This function visualizes a specific example of this solution space.
    """
    # Ensure the data directory exists
    database_path = 'data'
    if not os.path.exists(database_path):
        os.makedirs(database_path)

    # --- Parametric Analysis ---
    # Choose specific functional forms for the arbitrary functions f(phi) and g(phi)
    # Let's use a simple polynomial case for illustration.
    a = 0.1
    b = 0.5

    # f(phi) = a * phi^2
    def f(phi):
        return a * phi**2

    # f'(phi) = 2 * a * phi
    def df_dphi(phi):
        return 2 * a * phi

    # g(phi) = b * phi
    def g(phi):
        return b * phi

    # Resulting functions for beta_W2 and beta_GB
    def beta_W2(phi):
        """Calculates beta_W2(phi) = f(phi)."""
        return f(phi)

    def beta_GB(phi, X):
        """Calculates beta_GB(phi, X) = -2 * f'(phi) * X + g(phi)."""
        return -2 * df_dphi(phi) * X + g(phi)

    print("--- Visualization of the Solution Space ---")
    print("Illustrating the structure of beta_GB(phi, X) and beta_W2(phi, X) that satisfy the ghost-free and symmetry conditions.")
    print("The conditions are:")
    print("1. ∂β_W²/∂X = 0")
    print("2. ∂β_GB/∂X + 2 * ∂β_W²/dφ = 0")
    print("\nFor this visualization, we choose the following functional forms:")
    print("Arbitrary function f(φ) = " + str(a) + " * φ^2")
    print("Arbitrary function g(φ) = " + str(b) + " * φ")
    print("\nThis leads to the specific solutions:")
    print("β_W²(φ) = " + str(a) + " * φ^2")
    print("β_GB(φ, X) = " + str(-4 * a) + " * φ * X + " + str(b) + " * φ")
    print("\nGenerating plots...")

    # --- Plotting ---
    plt.rcParams['text.usetex'] = False
    plt.rcParams['figure.dpi'] = 300

    fig = plt.figure(figsize=(12, 6))
    fig.suptitle('Solution Space for Ghost-Free Quantum Corrections', fontsize=16)

    # 1. Plot for beta_W2(phi)
    ax1 = fig.add_subplot(1, 2, 1)
    phi_range_1d = np.linspace(-3, 3, 400)
    b_w2_values = beta_W2(phi_range_1d)

    ax1.plot(phi_range_1d, b_w2_values, lw=2)
    ax1.set_xlabel('Scalar Field (φ)', fontsize=12)
    ax1.set_ylabel('β_W²', fontsize=12)
    ax1.set_title('β_W² as a function of φ', fontsize=14)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.text(0.05, 0.95, 'Independent of X', transform=ax1.transAxes,
             fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round,pad=0.3', fc='wheat', alpha=0.5))


    # 2. Plot for beta_GB(phi, X)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    phi_range_2d = np.linspace(-3, 3, 50)
    X_range_2d = np.linspace(0, 10, 50)
    PHI, X = np.meshgrid(phi_range_2d, X_range_2d)
    B_GB = beta_GB(PHI, X)

    surf = ax2.plot_surface(PHI, X, B_GB, cmap='viridis', edgecolor='none')
    ax2.set_xlabel('Scalar Field (φ)', fontsize=10, labelpad=10)
    ax2.set_ylabel('Kinetic Term (X)', fontsize=10, labelpad=10)
    ax2.set_zlabel('β_GB', fontsize=10, labelpad=10)
    ax2.set_title('β_GB as a function of φ and X', fontsize=14)
    ax2.view_init(elev=20., azim=-135)
    fig.colorbar(surf, shrink=0.5, aspect=5, ax=ax2, pad=0.1)

    # Final adjustments and saving
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    timestamp = int(time.time())
    plot_filename = os.path.join(database_path, 'solution_space_visualization_1_' + str(timestamp) + '.png')
    plt.savefig(plot_filename)
    plt.close(fig)

    print("\nPlot saved successfully.")
    print("Filename: " + plot_filename)
    print("Description: The plot visualizes the structure of the coupling functions beta_W2 and beta_GB.")
    print("- The left panel shows that beta_W2 must be a function of the scalar field phi only.")
    print("- The right panel shows the resulting structure for beta_GB, which has a specific linear dependence on the kinetic term X, with a slope that varies with phi.")



if __name__ == '__main__':
    visualize_solution_space()