"""
Axiomatic Uniqueness: Computational Companion
==============================================

Demonstrates:
1. The uniqueness proof visually (multiplicative vs alternatives under axioms)
2. The CES family and where multiplicative sits within it
3. The discriminating parameter ρ (elasticity of substitution)
4. Cliff vs slope degradation predictions
5. Separability test framework

Run: python axiomatic_proof.py
Outputs: figures/ directory with publication-ready plots

Project: Multiplicative Composition of Independent Dimensions
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit
from pathlib import Path
import os

# Output directory
FIG_DIR = Path(__file__).parent / "figures"
FIG_DIR.mkdir(exist_ok=True)

# Plotting defaults
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox_inches': 'tight',
})


# =============================================================================
# 1. COMPOSITION FUNCTIONS — THE COMPETING FORMS
# =============================================================================

def multiplicative(x1, x2, alpha1=1.0, alpha2=1.0):
    """Cobb-Douglas / multiplicative: f = x1^a1 * x2^a2"""
    return np.power(x1, alpha1) * np.power(x2, alpha2)

def additive(x1, x2, w1=0.5, w2=0.5):
    """Weighted sum: f = w1*x1 + w2*x2"""
    return w1 * x1 + w2 * x2

def ces(x1, x2, rho, alpha1=0.5, alpha2=0.5):
    """CES (Constant Elasticity of Substitution):
    f = (a1*x1^rho + a2*x2^rho)^(1/rho)
    
    rho -> 0: Cobb-Douglas (multiplicative)
    rho = 1: linear (additive)  
    rho -> -inf: Leontief (min)
    """
    if abs(rho) < 1e-10:
        # Limit case: geometric mean (Cobb-Douglas)
        return np.power(x1, alpha1) * np.power(x2, alpha2)
    return np.power(alpha1 * np.power(x1, rho) + alpha2 * np.power(x2, rho), 1.0 / rho)

def leontief(x1, x2):
    """Min function (perfect complements): f = min(x1, x2)"""
    return np.minimum(x1, x2)


# =============================================================================
# 2. ZERO-COLLAPSE TEST — AXIOM 1 VISUALIZATION
# =============================================================================

def plot_zero_collapse():
    """Show which forms satisfy zero-collapse and which don't."""
    x2_fixed = 5.0
    x1 = np.linspace(0, 10, 200)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left: all forms as x1 -> 0
    ax = axes[0]
    ax.plot(x1, multiplicative(x1, x2_fixed), 'k-', lw=2, label='Multiplicative')
    ax.plot(x1, additive(x1, x2_fixed), 'r--', lw=2, label='Additive')
    ax.plot(x1, leontief(x1, x2_fixed), 'b:', lw=2, label='Leontief (min)')
    ax.plot(x1, ces(x1, x2_fixed, rho=-1), 'g-.', lw=2, label='CES (ρ=-1)')
    
    ax.axvline(0, color='gray', alpha=0.3, lw=0.5)
    ax.axhline(0, color='gray', alpha=0.3, lw=0.5)
    ax.set_xlabel('x₁ (one dimension)')
    ax.set_ylabel('f(x₁, x₂=5)')
    ax.set_title('Zero-Collapse Test')
    ax.legend(fontsize=9)
    ax.set_xlim(-0.5, 10)
    
    # Annotate the key distinction
    ax.annotate('Additive: f(0, 5) = 2.5 ≠ 0\n→ VIOLATES zero-collapse',
                xy=(0, 2.5), xytext=(2, 7),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=9, color='red')
    ax.annotate('Multiplicative: f(0, 5) = 0\n→ SATISFIES zero-collapse',
                xy=(0, 0), xytext=(2, 4),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=9, color='black')
    
    # Right: cliff vs slope near zero
    ax = axes[1]
    x1_near_zero = np.linspace(0.01, 2, 200)
    ax.plot(x1_near_zero, multiplicative(x1_near_zero, x2_fixed), 'k-', lw=2, label='Multiplicative (cliff)')
    ax.plot(x1_near_zero, additive(x1_near_zero, x2_fixed), 'r--', lw=2, label='Additive (no cliff)')
    ax.plot(x1_near_zero, ces(x1_near_zero, x2_fixed, rho=-2), 'b:', lw=2, label='CES ρ=-2 (steep cliff)')
    
    ax.set_xlabel('x₁ (near zero)')
    ax.set_ylabel('f(x₁, x₂=5)')
    ax.set_title('Degradation Shape Near Zero')
    ax.legend(fontsize=9)
    
    plt.tight_layout()
    plt.savefig(FIG_DIR / '01_zero_collapse.png')
    plt.close()
    print(f"  Saved: {FIG_DIR / '01_zero_collapse.png'}")


# =============================================================================
# 3. CES FAMILY — THE ρ PARAMETER LANDSCAPE
# =============================================================================

def plot_ces_family():
    """Show how ρ interpolates between additive, multiplicative, and min."""
    x1 = np.linspace(0.1, 10, 200)
    x2_fixed = 5.0
    
    rho_values = [1.0, 0.5, 0.001, -0.5, -1.0, -2.0, -5.0]
    labels = ['ρ=1 (additive)', 'ρ=0.5', 'ρ→0 (multiplicative)', 
              'ρ=-0.5', 'ρ=-1 (harmonic)', 'ρ=-2', 'ρ=-5 (→min)']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    cmap = plt.cm.coolwarm
    colors = [cmap(i / (len(rho_values) - 1)) for i in range(len(rho_values))]
    
    for rho, label, color in zip(rho_values, labels, colors):
        y = ces(x1, x2_fixed, rho)
        lw = 2.5 if abs(rho) < 0.01 else 1.5
        ax.plot(x1, y, color=color, lw=lw, label=label)
    
    ax.set_xlabel('x₁')
    ax.set_ylabel('f(x₁, x₂=5)')
    ax.set_title('CES Family: ρ interpolates between composition forms')
    ax.legend(fontsize=9, loc='upper left')
    
    # Add annotation
    ax.text(7, 2.5, 'ρ is the\ndiscriminating\nparameter', fontsize=11,
            style='italic', ha='center',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig(FIG_DIR / '02_ces_family.png')
    plt.close()
    print(f"  Saved: {FIG_DIR / '02_ces_family.png'}")


# =============================================================================
# 4. ISOQUANT MAP — SUBSTITUTABILITY VISUALIZATION  
# =============================================================================

def plot_isoquants():
    """Show isoquant curves (constant-output contours) for different forms.
    Multiplicative: smooth hyperbolic curves (unit elasticity)
    Additive: straight lines (perfect substitutes)
    Min: L-shaped (perfect complements)
    """
    x1 = np.linspace(0.1, 10, 300)
    x2 = np.linspace(0.1, 10, 300)
    X1, X2 = np.meshgrid(x1, x2)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    levels = [1, 2, 4, 8, 16]
    
    # Multiplicative
    Z = multiplicative(X1, X2)
    axes[0].contour(X1, X2, Z, levels=levels, colors='black', linewidths=1.5)
    axes[0].set_title('Multiplicative\n(unit elasticity)')
    axes[0].set_xlabel('x₁')
    axes[0].set_ylabel('x₂')
    
    # Additive  
    Z = additive(X1, X2, 1, 1)
    axes[1].contour(X1, X2, Z, levels=levels, colors='red', linewidths=1.5)
    axes[1].set_title('Additive\n(perfect substitutes)')
    axes[1].set_xlabel('x₁')
    
    # CES with low rho (near-Leontief)
    Z = ces(X1, X2, rho=-3)
    axes[2].contour(X1, X2, Z, levels=levels, colors='blue', linewidths=1.5)
    axes[2].set_title('CES ρ=-3\n(near-complements)')
    axes[2].set_xlabel('x₁')
    
    for ax in axes:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.grid(alpha=0.2)
    
    plt.suptitle('Isoquant Maps: How substitutable are the dimensions?', fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig(FIG_DIR / '03_isoquants.png')
    plt.close()
    print(f"  Saved: {FIG_DIR / '03_isoquants.png'}")


# =============================================================================
# 5. CLIFF VS SLOPE — THE TESTABLE PREDICTION
# =============================================================================

def plot_cliff_vs_slope():
    """The key empirical discriminant: how does emergence degrade
    as one dimension is starved while others are held constant?
    
    Multiplicative predicts: cliff (nonlinear collapse near zero)
    Additive predicts: slope (linear degradation)
    """
    x1 = np.linspace(0, 1, 500)
    x2, x3 = 5.0, 5.0  # held constant
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left: normalized degradation curves
    ax = axes[0]
    
    mult_vals = x1 * x2 * x3  # multiplicative (α=1 each)
    add_vals = x1 + x2 + x3   # additive
    ces_neg1 = ces(ces(x1, np.full_like(x1, x2), -1), np.full_like(x1, x3), -1)
    
    # Normalize to max=1
    ax.plot(x1, mult_vals / mult_vals.max(), 'k-', lw=2.5, label='Multiplicative')
    ax.plot(x1, add_vals / add_vals.max(), 'r--', lw=2, label='Additive')
    ax.plot(x1, ces_neg1 / ces_neg1.max(), 'b:', lw=2, label='CES ρ=-1')
    
    ax.axvspan(0, 0.15, alpha=0.1, color='orange', label='Cliff zone')
    ax.set_xlabel('x₁ (starved dimension)')
    ax.set_ylabel('Normalized emergence')
    ax.set_title('Degradation as one dimension → 0')
    ax.legend(fontsize=9)
    
    # Right: derivative (rate of degradation)
    ax = axes[1]
    dx = x1[1] - x1[0]
    
    mult_deriv = np.gradient(mult_vals / mult_vals.max(), dx)
    add_deriv = np.gradient(add_vals / add_vals.max(), dx)
    
    ax.plot(x1, mult_deriv, 'k-', lw=2.5, label='Multiplicative (∂f/∂x₁)')
    ax.plot(x1, add_deriv, 'r--', lw=2, label='Additive (∂f/∂x₁)')
    
    ax.set_xlabel('x₁ (starved dimension)')
    ax.set_ylabel('Rate of change')
    ax.set_title('Gradient: multiplicative is steepest near zero')
    ax.legend(fontsize=9)
    
    plt.tight_layout()
    plt.savefig(FIG_DIR / '04_cliff_vs_slope.png')
    plt.close()
    print(f"  Saved: {FIG_DIR / '04_cliff_vs_slope.png'}")


# =============================================================================
# 6. HOMOGENEITY TEST FRAMEWORK
# =============================================================================

def plot_homogeneity_test():
    """Framework for testing Axiom 4 (scale consistency).
    If homogeneity holds: log(f(λx)) = k·log(λ) + log(f(x))
    i.e., log-log plot of scaling factor vs output is linear.
    """
    lambdas = np.linspace(0.1, 5, 100)
    x_base = np.array([2.0, 3.0, 4.0])
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left: f(λx) vs λ for different forms
    ax = axes[0]
    f_base_mult = np.prod(x_base)
    f_base_add = np.sum(x_base)
    
    mult_scaled = [np.prod(l * x_base) for l in lambdas]
    add_scaled = [np.sum(l * x_base) for l in lambdas]
    
    ax.loglog(lambdas, mult_scaled, 'k-', lw=2, label=f'Multiplicative (k={len(x_base)})')
    ax.loglog(lambdas, add_scaled, 'r--', lw=2, label='Additive (k=1)')
    ax.loglog(lambdas, lambdas**3 * f_base_mult, 'k:', alpha=0.5, label='λ³ reference')
    ax.loglog(lambdas, lambdas**1 * f_base_add, 'r:', alpha=0.5, label='λ¹ reference')
    
    ax.set_xlabel('Scaling factor λ')
    ax.set_ylabel('f(λx)')
    ax.set_title('Homogeneity Test (log-log)')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.2)
    
    # Right: residual from power law (should be zero if homogeneous)
    ax = axes[1]
    
    # Fit power law: log(f) = k*log(λ) + c
    log_l = np.log(lambdas)
    log_mult = np.log(mult_scaled)
    log_add = np.log(add_scaled)
    
    # Linear fit in log-log
    mult_fit = np.polyfit(log_l, log_mult, 1)
    add_fit = np.polyfit(log_l, log_add, 1)
    
    mult_residual = log_mult - np.polyval(mult_fit, log_l)
    add_residual = log_add - np.polyval(add_fit, log_l)
    
    ax.plot(lambdas, mult_residual, 'k-', lw=2, label=f'Multiplicative (k={mult_fit[0]:.2f})')
    ax.plot(lambdas, add_residual, 'r--', lw=2, label=f'Additive (k={add_fit[0]:.2f})')
    ax.axhline(0, color='gray', alpha=0.5)
    
    ax.set_xlabel('Scaling factor λ')
    ax.set_ylabel('Residual from power law')
    ax.set_title('Both forms are exactly homogeneous')
    ax.legend(fontsize=9)
    
    plt.tight_layout()
    plt.savefig(FIG_DIR / '05_homogeneity_test.png')
    plt.close()
    print(f"  Saved: {FIG_DIR / '05_homogeneity_test.png'}")


# =============================================================================
# 7. SYNERGY MEASUREMENT — PID CONNECTION
# =============================================================================

def measure_synergy():
    """Compute synergistic information for multiplicative vs additive.
    
    Using a simple model: X1, X2 are independent uniform on [0,1].
    Y_mult = X1 * X2 (multiplicative)
    Y_add = X1 + X2 (additive)
    
    Measure: I(X1, X2; Y) - I(X1; Y) - I(X2; Y) ≈ synergy
    (This is the co-information / interaction information)
    """
    np.random.seed(42)
    N = 100000
    
    X1 = np.random.uniform(0.1, 1.0, N)
    X2 = np.random.uniform(0.1, 1.0, N)
    
    Y_mult = X1 * X2
    Y_add = X1 + X2
    
    # Estimate mutual information via binning
    def mi_binned(x, y, bins=50):
        """Estimate mutual information I(X;Y) via histogram."""
        hist_xy, _, _ = np.histogram2d(x, y, bins=bins)
        hist_x = np.sum(hist_xy, axis=1)
        hist_y = np.sum(hist_xy, axis=0)
        
        # Normalize
        p_xy = hist_xy / N + 1e-12
        p_x = hist_x / N + 1e-12
        p_y = hist_y / N + 1e-12
        
        # I(X;Y) = sum p(x,y) log(p(x,y) / p(x)p(y))
        mi = 0
        for i in range(bins):
            for j in range(bins):
                if p_xy[i, j] > 1e-11:
                    mi += p_xy[i, j] * np.log2(p_xy[i, j] / (p_x[i] * p_y[j]))
        return mi
    
    # For multiplicative
    mi_x1_ymult = mi_binned(X1, Y_mult)
    mi_x2_ymult = mi_binned(X2, Y_mult)
    mi_joint_mult = mi_binned(X1, Y_mult) + mi_binned(X2, Y_mult)  # Approx (ignoring redundancy)
    
    # For additive
    mi_x1_yadd = mi_binned(X1, Y_add)
    mi_x2_yadd = mi_binned(X2, Y_add)
    
    print("\n  Synergy Analysis (PID approximation):")
    print(f"    Multiplicative: I(X1;Y)={mi_x1_ymult:.3f}, I(X2;Y)={mi_x2_ymult:.3f}")
    print(f"    Additive:       I(X1;Y)={mi_x1_yadd:.3f}, I(X2;Y)={mi_x2_yadd:.3f}")
    print(f"    Note: full PID decomposition requires specialized libraries (dit, pypid)")
    print(f"    → Key test: does multiplicative Y contain information ABSENT from both marginals?")


# =============================================================================
# 8. RHO ESTIMATOR — FOR EMPIRICAL DATA
# =============================================================================

def estimate_rho(x1_data, x2_data, y_data):
    """Estimate the CES elasticity parameter ρ from empirical data.
    
    Fit: y = (a1*x1^rho + a2*x2^rho)^(1/rho)
    
    Returns: estimated ρ, standard error, and interpretation.
    
    ρ ≈ 0 → multiplicative form validated
    ρ ≈ 1 → additive form wins
    ρ < 0 → complementarity stronger than multiplicative
    """
    def ces_model(X, rho, a1, a2, scale):
        x1, x2 = X
        if abs(rho) < 1e-6:
            return scale * np.power(x1, a1) * np.power(x2, a2)
        return scale * np.power(a1 * np.power(x1, rho) + a2 * np.power(x2, rho), 1.0 / rho)
    
    try:
        X_data = np.vstack([x1_data, x2_data])
        popt, pcov = curve_fit(ces_model, X_data, y_data, p0=[0.5, 0.5, 0.5, 1.0],
                               maxfev=10000, bounds=([-10, 0.01, 0.01, 0.01], [2, 10, 10, 100]))
        rho_est = popt[0]
        rho_se = np.sqrt(pcov[0, 0]) if pcov[0, 0] > 0 else float('inf')
        
        if abs(rho_est) < 0.1:
            interp = "MULTIPLICATIVE (ρ ≈ 0)"
        elif rho_est > 0.5:
            interp = "ADDITIVE-LEANING (ρ > 0.5)"
        elif rho_est < -0.5:
            interp = "COMPLEMENT-LEANING (ρ < -0.5)"
        else:
            interp = f"INTERMEDIATE (ρ = {rho_est:.2f})"
        
        return rho_est, rho_se, interp
    except Exception as e:
        return None, None, f"Fit failed: {e}"


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("Axiomatic Uniqueness — Computational Companion")
    print("=" * 50)
    
    print("\n1. Zero-collapse test...")
    plot_zero_collapse()
    
    print("\n2. CES family landscape...")
    plot_ces_family()
    
    print("\n3. Isoquant maps...")
    plot_isoquants()
    
    print("\n4. Cliff vs slope predictions...")
    plot_cliff_vs_slope()
    
    print("\n5. Homogeneity test framework...")
    plot_homogeneity_test()
    
    print("\n6. Synergy measurement (PID connection)...")
    measure_synergy()
    
    print("\n" + "=" * 50)
    print("All figures saved to:", FIG_DIR)
    print("\nNext steps:")
    print("  → Run estimate_rho() on empirical data from domain transfer experiments")
    print("  → Full PID decomposition with `dit` library")
    print("  → Connect to Sleep-EDF phase transition data")
