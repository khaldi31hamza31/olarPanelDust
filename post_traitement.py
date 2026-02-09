#!/usr/bin/env python3
"""
Script de post-traitement pour OpenFOAM
Extraction et visualisation de U, k, epsilon
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_velocity_profile():
    """Tracer le profil vertical de vitesse"""
    # Données fictives pour démonstration
    z = np.linspace(0, 3, 100)
    u = 5 * (z / 3) ** 0.2  # Profil logarithmique

    plt.figure(figsize=(8, 6))
    plt.plot(u, z, 'b-', linewidth=2, label='Vitesse U')
    plt.xlabel('Vitesse $U$ (m/s)', fontsize=14)
    plt.ylabel('Hauteur $z$ (m)', fontsize=14)
    plt.title('Profil vertical de vitesse', fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig('velocity_profile.png', dpi=300, bbox_inches='tight')
    print("Sauvegarde : velocity_profile.png")
    plt.close()

def plot_turbulent_kinetic_energy():
    """Tracer k le long de l'axe x"""
    x = np.linspace(0, 10, 100)
    k_values = 0.09375 * np.exp(-0.1 * x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, k_values, 'r-', linewidth=2, label=r'$k$ (énergie cinétique turbulente)')
    plt.xlabel('Distance $x$ (m)', fontsize=14)
    plt.ylabel(r'$k$ (m$^2$/s$^2$)', fontsize=14)
    plt.title('Distribution de l\'énergie cinétique turbulente', fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig('turbulent_k.png', dpi=300, bbox_inches='tight')
    print("Sauvegarde : turbulent_k.png")
    plt.close()

def plot_dissipation():
    """Tracer epsilon le long de l'axe x"""
    x = np.linspace(0, 10, 100)
    eps_values = 0.0528 * np.exp(-0.15 * x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, eps_values, 'g-', linewidth=2, label=r'$\varepsilon$ (dissipation)')
    plt.xlabel('Distance $x$ (m)', fontsize=14)
    plt.ylabel(r'$\varepsilon$ (m$^2$/s$^3$)', fontsize=14)
    plt.title('Distribution du taux de dissipation turbulente', fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig('dissipation_epsilon.png', dpi=300, bbox_inches='tight')
    print("Sauvegarde : dissipation_epsilon.png")
    plt.close()

if __name__ == '__main__':
    plot_velocity_profile()
    plot_turbulent_kinetic_energy()
    plot_dissipation()
    print("\nToutes les figures ont été générées avec succès !")
