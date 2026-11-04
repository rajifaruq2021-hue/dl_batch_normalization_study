# Here I import the libraries I need to generate clear conceptual diagrams for my presentation slides.
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Here I define the directory where all output figures will be stored.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(BASE_DIR, 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

# -------------------------------------------------------------
# Figure 1: Deep Network Training Challenges & Internal Covariate Shift
# -------------------------------------------------------------
# Here I create Figure 1 to illustrate the forward and backward pass, and how parameter updates cause distribution shifts.
fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis('off')

# Box 1: Input Layer
ax.add_patch(patches.FancyBboxPatch((0.5, 1.8), 2.0, 1.4, boxstyle='round,pad=0.2', facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2))
ax.text(1.5, 2.5, 'Input Data (X)\nDistribution P(X)', ha='center', va='center', fontsize=11, fontweight='bold', color='#0D47A1')

# Arrow 1: Forward W1
ax.annotate('', xy=(3.6, 2.7), xytext=(2.7, 2.7), arrowprops=dict(facecolor='#1976D2', edgecolor='#1976D2', width=2, headwidth=8))
ax.text(3.15, 3.0, 'W1, b1', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#1976D2')

# Box 2: Hidden Layer 1
ax.add_patch(patches.FancyBboxPatch((3.8, 1.8), 2.0, 1.4, boxstyle='round,pad=0.2', facecolor='#FFF9C4', edgecolor='#FBC02D', linewidth=2))
ax.text(4.8, 2.5, 'Layer 1 Activations\nDistribution P(h1|X)', ha='center', va='center', fontsize=11, fontweight='bold', color='#F57F17')

# Arrow 2: Forward W2
ax.annotate('', xy=(6.9, 2.7), xytext=(6.0, 2.7), arrowprops=dict(facecolor='#1976D2', edgecolor='#1976D2', width=2, headwidth=8))
ax.text(6.45, 3.0, 'W2, b2', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#1976D2')

# Box 3: Hidden Layer 2
ax.add_patch(patches.FancyBboxPatch((7.1, 1.8), 2.0, 1.4, boxstyle='round,pad=0.2', facecolor='#FFEBEE', edgecolor='#D32F2F', linewidth=2))
ax.text(8.1, 2.5, 'Layer 2 Activations\nDistribution P(h2|h1)', ha='center', va='center', fontsize=11, fontweight='bold', color='#B71C1C')

# Arrow 3: Forward W3
ax.annotate('', xy=(10.2, 2.7), xytext=(9.3, 2.7), arrowprops=dict(facecolor='#1976D2', edgecolor='#1976D2', width=2, headwidth=8))
ax.text(9.75, 3.0, 'W3, b3', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#1976D2')

# Box 4: Output & Loss
ax.add_patch(patches.FancyBboxPatch((10.4, 1.8), 1.4, 1.4, boxstyle='round,pad=0.2', facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=2))
ax.text(11.1, 2.5, 'Loss L\nCross-Entropy', ha='center', va='center', fontsize=10, fontweight='bold', color='#1B5E20')

# Backward Pass Arrows
ax.annotate('', xy=(8.1, 1.5), xytext=(10.4, 1.5), arrowprops=dict(facecolor='#D32F2F', edgecolor='#D32F2F', width=2, headwidth=8, linestyle='dashed'))
ax.annotate('', xy=(4.8, 1.5), xytext=(7.1, 1.5), arrowprops=dict(facecolor='#D32F2F', edgecolor='#D32F2F', width=2, headwidth=8, linestyle='dashed'))
ax.annotate('', xy=(1.5, 1.5), xytext=(3.8, 1.5), arrowprops=dict(facecolor='#D32F2F', edgecolor='#D32F2F', width=2, headwidth=8, linestyle='dashed'))
ax.text(6.0, 1.1, 'Backward Pass: Gradients Propagate Reverse', ha='center', va='top', fontsize=11, fontweight='bold', color='#D32F2F')

# Callout banner at top explaining Internal Covariate Shift
ax.add_patch(patches.Rectangle((0.5, 3.9), 11.3, 0.8, facecolor='#ECEFF1', edgecolor='#90A4AE', linewidth=1.5))
ax.text(6.15, 4.3, 'Internal Covariate Shift: Updating W1 continuously changes the distribution of h1, forcing W2 to adapt to a moving target.', ha='center', va='center', fontsize=10.5, color='#263238', style='italic')

plt.title('Deep Neural Network Optimization Challenge: Forward Dynamics, Backpropagation, and Covariate Shift', fontsize=12, fontweight='bold', pad=15)
plt.tight_layout()
fig1_path = os.path.join(FIG_DIR, 'figure1_training_challenges_and_internal_covariate_shift.png')
plt.savefig(fig1_path, dpi=300)
plt.close()
print(f'Saved Figure 1 to: {fig1_path}')

# -------------------------------------------------------------
# Figure 2: Batch Normalization in Fully Connected vs CNN Layers
# -------------------------------------------------------------
# Here I create Figure 2 comparing normalization across dimensions in FC versus Convolutional layers.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5), dpi=300)

# FC BatchNorm
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.add_patch(patches.FancyBboxPatch((1, 2), 8, 6, boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#757575', linewidth=1.5))
ax1.text(5, 7.3, 'Fully Connected Layer: Batch Normalization', ha='center', va='center', fontsize=12, fontweight='bold', color='#212121')
ax1.text(5, 6.2, 'Input Tensor Dimensions: (N, D)', ha='center', va='center', fontsize=11, color='#424242')
ax1.text(5, 5.2, 'N = Batch Size (e.g., 64) | D = Feature Dimension', ha='center', va='center', fontsize=10, color='#616161')

# Formula box
ax1.add_patch(patches.Rectangle((1.5, 2.5), 7, 2.2, facecolor='#E3F2FD', edgecolor='#1E88E5', linewidth=1.5))
ax1.text(5, 4.0, 'Mean and Variance calculated across N for each feature d:', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0D47A1')
ax1.text(5, 3.3, r'mu_d = (1/N) * sum(x_{i,d})   |   sigma_d^2 = (1/N) * sum((x_{i,d} - mu_d)^2)', ha='center', va='center', fontsize=9, color='#1565C0')
ax1.text(5, 2.7, r'Learned Parameters per feature: gamma_d (scale), beta_d (shift)', ha='center', va='center', fontsize=9, color='#0D47A1')

# CNN BatchNorm
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.add_patch(patches.FancyBboxPatch((1, 2), 8, 6, boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#757575', linewidth=1.5))
ax2.text(5, 7.3, 'Convolutional Layer: Spatial Batch Normalization', ha='center', va='center', fontsize=12, fontweight='bold', color='#212121')
ax2.text(5, 6.2, 'Input Tensor Dimensions: (N, C, H, W)', ha='center', va='center', fontsize=11, color='#424242')
ax2.text(5, 5.2, 'N = Batch Size | C = Channels | H, W = Spatial Grid', ha='center', va='center', fontsize=10, color='#616161')

# Formula box
ax2.add_patch(patches.Rectangle((1.5, 2.5), 7, 2.2, facecolor='#E8F5E9', edgecolor='#43A047', linewidth=1.5))
ax2.text(5, 4.0, 'Mean and Variance calculated across (N, H, W) for each channel c:', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1B5E20')
ax2.text(5, 3.3, r'Effective Sample Size m = N * H * W elements per channel', ha='center', va='center', fontsize=9, color='#2E7D32')
ax2.text(5, 2.7, r'Preserves translation equivariance: 1 pair (gamma_c, beta_c) per channel', ha='center', va='center', fontsize=9, color='#1B5E20')

plt.tight_layout()
fig2_path = os.path.join(FIG_DIR, 'figure2_batchnorm_cnn_formulation.png')
plt.savefig(fig2_path, dpi=300)
plt.close()
print(f'Saved Figure 2 to: {fig2_path}')

# -------------------------------------------------------------
# Figure 5: Normalization Taxonomy Comparison
# -------------------------------------------------------------
# Here I create Figure 5 illustrating how BatchNorm, LayerNorm, InstanceNorm, and GroupNorm slice the 4D tensor (N, C, H, W).
fig, axes = plt.subplots(1, 4, figsize=(14, 4), dpi=300)
methods = [
    ('Batch Normalization (BN)', 'Across (N, H, W)\nPer Channel C', '#1E88E5', 'Sensitive to small N'),
    ('Layer Normalization (LN)', 'Across (C, H, W)\nPer Sample N', '#43A047', 'Ideal for RNN / NLP'),
    ('Instance Normalization (IN)', 'Across (H, W)\nPer Sample N & Channel C', '#FB8C00', 'Used in Style Transfer'),
    ('Group Normalization (GN)', 'Across (G, H, W)\nPer Sample N & Group G', '#8E24AA', 'Batch-size independent')
]

for ax, (title, norm_slice, color, note) in zip(axes, methods):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.add_patch(patches.FancyBboxPatch((0.5, 0.5), 9, 9, boxstyle='round,pad=0.2', facecolor='#FAFAFA', edgecolor=color, linewidth=2))
    ax.text(5, 8.5, title, ha='center', va='center', fontsize=10, fontweight='bold', color=color)
    
    # Inner box representing normalization domain
    ax.add_patch(patches.Rectangle((1.5, 4.0), 7, 3.5, facecolor=color, alpha=0.2, edgecolor=color, linewidth=1.5))
    ax.text(5, 5.8, norm_slice, ha='center', va='center', fontsize=10, fontweight='bold', color='#212121')
    
    # Note at bottom
    ax.text(5, 2.0, f'Key Property:\n{note}', ha='center', va='center', fontsize=9, color='#424242', style='italic')

plt.tight_layout()
fig5_path = os.path.join(FIG_DIR, 'figure5_normalization_taxonomy_comparison.png')
plt.savefig(fig5_path, dpi=300)
plt.close()
print(f'Saved Figure 5 to: {fig5_path}')
print('All conceptual figures generated successfully.')
