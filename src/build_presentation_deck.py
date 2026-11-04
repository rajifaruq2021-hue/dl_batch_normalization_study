# Here I import the libraries I need to generate the complete PowerPoint presentation slides.
import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Here I define the project paths where my figures are stored and where the presentation will be saved.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(BASE_DIR, 'figures')
PRES_DIR = os.path.join(BASE_DIR, 'presentation')
os.makedirs(PRES_DIR, exist_ok=True)

# Here I initialize a PowerPoint presentation object with 16:9 widescreen dimensions.
prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Here I define my consistent academic color palette matching IU presentation standards.
C_NAVY = RGBColor(15, 34, 64)       # Deep IU Navy Blue
C_WHITE = RGBColor(255, 255, 255)
C_DARK = RGBColor(40, 40, 40)
C_GRAY = RGBColor(110, 110, 110)
C_ACCENT = RGBColor(208, 56, 43)    # Red accent
C_LIGHT_BG = RGBColor(248, 249, 250)
C_CARD_BG = RGBColor(238, 242, 248)
C_BLUE_CARD = RGBColor(235, 243, 252)
C_GREEN_CARD = RGBColor(235, 247, 238)

blank_layout = prs.slide_layouts[6]

# Here I create a helper function to add a standard academic slide header.
def add_header(slide, title_text, category_text='ORAL ASSIGNMENT | DLBDSNNDL01-01'):
    top_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.9))
    tf = top_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p_cat = tf.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = 'Arial'
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = C_ACCENT
    p_cat.space_after = Pt(2)
    
    p_title = tf.add_paragraph()
    p_title.text = title_text
    p_title.font.name = 'Arial'
    p_title.font.size = Pt(20)
    p_title.font.bold = True
    p_title.font.color.rgb = C_NAVY

# Here I create a helper function to add a standard slide footer with student details and slide number.
def add_footer(slide, slide_num):
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.9), Inches(11.7), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor(220, 220, 220)
    line.line.color.rgb = RGBColor(220, 220, 220)
    
    box = slide.shapes.add_textbox(Inches(0.8), Inches(6.95), Inches(11.7), Inches(0.4))
    tf = box.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = f'Raji Faruq Ishola (Matr. 4253139) | DLBDSNNDL01-01: Neural Nets and Deep Learning | Slide {slide_num}'
    p.font.name = 'Arial'
    p.font.size = Pt(9)
    p.font.color.rgb = C_GRAY

# -------------------------------------------------------------
# Slide 1: Title Slide
# -------------------------------------------------------------
s1 = prs.slides.add_slide(blank_layout)
bg = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg.fill.solid()
bg.fill.fore_color.rgb = C_NAVY
bg.line.fill.background()

t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(4.5))
tf1 = t_box.text_frame
tf1.word_wrap = True

p = tf1.paragraphs[0]
p.text = 'IU INTERNATIONAL UNIVERSITY OF APPLIED SCIENCES'
p.font.name = 'Arial'
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = RGBColor(200, 215, 235)
p.space_after = Pt(14)

p = tf1.add_paragraph()
p.text = 'Accelerating Deep Network Training\nvia Batch Normalization'
p.font.name = 'Arial'
p.font.size = Pt(32)
p.font.bold = True
p.font.color.rgb = C_WHITE
p.space_after = Pt(20)

p = tf1.add_paragraph()
p.text = 'Oral Assignment Examination | Course Code: DLBDSNNDL01-01'
p.font.name = 'Arial'
p.font.size = Pt(15)
p.font.color.rgb = RGBColor(180, 200, 225)
p.space_after = Pt(30)

p = tf1.add_paragraph()
p.text = 'Student: Raji Faruq Ishola   |   Matriculation Number: 4253139   |   Date: November 03, 2026'
p.font.name = 'Arial'
p.font.size = Pt(12)
p.font.color.rgb = RGBColor(220, 230, 245)

# -------------------------------------------------------------
# Slide 2: Outline & Agenda
# -------------------------------------------------------------
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, 'Presentation Agenda & Roadmap')
add_footer(s2, 2)

cards_data = [
    ('1. Optimization Foundations & The Problem', '• Deep neural network training via gradient descent\n• Backpropagation dynamics and Jacobian multiplication\n• The vanishing gradient and internal covariate shift bottlenecks'),
    ('2. Mathematical Formulation & Architecture', '• Mini-batch mean and variance calculations\n• Standardization and learnable scale and shift (gamma, beta)\n• Spatial Batch Normalization across convolutional feature maps (N x H x W)'),
    ('3. Empirical Evaluation & Acceleration Metrics', '• Measuring training acceleration: Loss curves and epoch reduction\n• High learning rate tolerance without numerical divergence\n• Comparative evaluation against Layer Normalization and Group Normalization'),
    ('4. Practical Adoption & Critical Reflection', '• Placement guidelines: Convolution, BatchNorm, and non-linearities\n• Architectural impact: Enabling ResNet and deep vision backbones\n• Failure modes and limitations: Small mini-batch sensitivity and distributed overhead')
]

for idx, (title, content) in enumerate(cards_data):
    row = idx // 2
    col = idx % 2
    left = Inches(0.8 + col * 5.95)
    top = Inches(1.5 + row * 2.5)
    
    card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(5.7), Inches(2.3))
    card.fill.solid()
    card.fill.fore_color.rgb = C_CARD_BG
    card.line.color.rgb = RGBColor(200, 215, 235)
    
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.18)
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = 'Arial'
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    p2 = tf.add_paragraph()
    p2.text = content
    p2.font.name = 'Arial'
    p2.font.size = Pt(11)
    p2.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 3: Deep Neural Network Training Fundamentals
# -------------------------------------------------------------
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, 'Deep Neural Network Training Fundamentals')
add_footer(s3, 3)

c1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.1))
c1.fill.solid()
c1.fill.fore_color.rgb = C_LIGHT_BG
c1.line.color.rgb = RGBColor(215, 225, 235)
tf1 = c1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = Inches(0.25)

p = tf1.paragraphs[0]
p.text = 'Forward Pass & Objective Function'
p.font.name = 'Arial'
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(8)

p = tf1.add_paragraph()
p.text = '• Sequential Function Composition:\n  A deep network transforms inputs x through multiple non-linear layers: h_l = f(W_l * h_{l-1} + b_l).\n\n• Loss Evaluation:\n  A scalar objective function evaluates prediction error against true targets (e.g., Cross-Entropy Loss for multi-class classification).\n\n• Gradient Descent Optimization:\n  Parameters are iteratively updated in the direction of steepest loss descent:\n  Theta_{t+1} = Theta_t - eta * Grad_Theta(L).'
p.font.name = 'Arial'
p.font.size = Pt(11.5)
p.font.color.rgb = C_DARK

c2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.1))
c2.fill.solid()
c2.fill.fore_color.rgb = C_LIGHT_BG
c2.line.color.rgb = RGBColor(215, 225, 235)
tf2 = c2.text_frame
tf2.word_wrap = True
tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = Inches(0.25)

p = tf2.paragraphs[0]
p.text = 'Backpropagation & Gradient Instability'
p.font.name = 'Arial'
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(8)

p = tf2.add_paragraph()
p.text = '• The Chain Rule of Calculus:\n  Error gradients propagate backwards layer by layer through successive Jacobian matrix multiplications.\n\n• The Vanishing Gradient Dilemma:\n  When weight matrices have singular values less than 1, gradients decay exponentially as they travel toward early layers:\n  Grad_{W_1}(L) = Grad_{h_L}(L) * Product_{k=2}^L (J_k) -> 0.\n\n• Saturating Activation Traps:\n  Sigmoid and tanh non-linearities saturate easily when inputs have large variance, setting derivatives to zero and stalling optimization.'
p.font.name = 'Arial'
p.font.size = Pt(11.5)
p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 4: Internal Covariate Shift & Optimization Challenges
# -------------------------------------------------------------
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, 'The Core Bottleneck: Internal Covariate Shift')
add_footer(s4, 4)

t4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.2))
tf4 = t4.text_frame
tf4.word_wrap = True
tf4.margin_left = tf4.margin_top = tf4.margin_right = tf4.margin_bottom = 0

p = tf4.paragraphs[0]
p.text = 'The Moving Target Problem in Deep Learning'
p.font.name = 'Arial'
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(6)

p = tf4.add_paragraph()
p.text = '• Defining Internal Covariate Shift (Ioffe & Szegedy, 2015):\n  As training progresses, updating the parameters of early layers constantly shifts the distribution of inputs to deeper layers. Each layer must continually readapt to an unstable input distribution.\n\n• Consequences for Training:\n  - Demands tiny learning rates to avoid sudden divergence.\n  - Extreme sensitivity to weight initialization (e.g., Xavier/He).\n  - Drastically slows down overall convergence speed.\n\n• Loss Landscape Smoothing (Santurkar et al., 2018):\n  Modern analysis demonstrates that normalization makes the loss surface significantly smoother and Lipschitz-continuous, enabling stable gradient steps.'
p.font.name = 'Arial'
p.font.size = Pt(11)
p.font.color.rgb = C_DARK

fig1_p = os.path.join(FIG_DIR, 'figure1_training_challenges_and_internal_covariate_shift.png')
if os.path.exists(fig1_p):
    s4.shapes.add_picture(fig1_p, Inches(6.6), Inches(1.6), width=Inches(5.9))

# -------------------------------------------------------------
# Slide 5: Batch Normalization: Core Mathematical Formulation
# -------------------------------------------------------------
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, 'Batch Normalization: Mathematical Principles')
add_footer(s5, 5)

steps = [
    ('Step 1: Mini-Batch Mean', 'Calculate the empirical average across the current mini-batch B of size N:', 'μ_B = (1 / N) * Σ_{i=1}^N (x_i)', '#E3F2FD', '#1976D2'),
    ('Step 2: Mini-Batch Variance', 'Compute the sample dispersion around the calculated mini-batch mean:', 'σ_B^2 = (1 / N) * Σ_{i=1}^N (x_i - μ_B)^2', '#FFF9C4', '#F57F17'),
    ('Step 3: Standardization', 'Normalize activations to achieve zero mean and unit variance (ε prevents division by zero):', 'x̂_i = (x_i - μ_B) / √(σ_B^2 + ε)', '#FFEBEE', '#D32F2F'),
    ('Step 4: Scale and Shift', 'Restore representational power via learnable parameters γ (scale) and β (shift):', 'y_i = γ * x̂_i + β', '#E8F5E9', '#388E3C')
]

for idx, (title, desc, formula, bg_col, border_col) in enumerate(steps):
    left = Inches(0.8 + idx * 2.95)
    top = Inches(1.6)
    
    card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(2.8), Inches(4.2))
    card.fill.solid()
    card.fill.fore_color.rgb = C_CARD_BG
    card.line.color.rgb = RGBColor(180, 205, 230)
    
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.15)
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = 'Arial'
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    p = tf.add_paragraph()
    p.text = desc
    p.font.name = 'Arial'
    p.font.size = Pt(10)
    p.font.color.rgb = C_DARK
    p.space_after = Pt(8)
    
    p = tf.add_paragraph()
    p.text = formula
    p.font.name = 'Arial'
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(20, 60, 120)

b_note = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.0), Inches(11.7), Inches(0.7))
b_note.fill.solid()
b_note.fill.fore_color.rgb = C_LIGHT_BG
b_note.line.color.rgb = RGBColor(210, 220, 235)
tf_b = b_note.text_frame
tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = Inches(0.1)
p = tf_b.paragraphs[0]
p.text = 'Identity Recovery Property: If optimal for the network, the optimization can learn γ = √(σ_B^2 + ε) and β = μ_B, perfectly recovering the original input activation y_i = x_i without loss of capacity.'
p.font.name = 'Arial'
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = C_NAVY

# -------------------------------------------------------------
# Slide 6: Spatial Batch Normalization in CNNs (REDESIGNED FOR MAXIMUM VISIBILITY)
# -------------------------------------------------------------
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, 'Batch Normalization in Convolutional Networks')
add_footer(s6, 6)

# Left Card: Fully Connected Normalization
c_fc = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.45), Inches(5.7), Inches(4.3))
c_fc.fill.solid()
c_fc.fill.fore_color.rgb = C_BLUE_CARD
c_fc.line.color.rgb = RGBColor(30, 136, 229)
c_fc.line.width = Pt(2)
tf_fc = c_fc.text_frame
tf_fc.word_wrap = True
tf_fc.margin_left = tf_fc.margin_top = tf_fc.margin_right = tf_fc.margin_bottom = Inches(0.22)

p = tf_fc.paragraphs[0]
p.text = 'Fully Connected Layers (1D / 2D)'
p.font.name = 'Arial'
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = RGBColor(13, 71, 161)
p.space_after = Pt(4)

p = tf_fc.add_paragraph()
p.text = 'Activation Tensor: (N, D)  |  N = Mini-batch size, D = Feature dimension'
p.font.name = 'Arial'
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = RGBColor(21, 101, 192)
p.space_after = Pt(8)

p = tf_fc.add_paragraph()
p.text = '1. Mini-Batch Statistics (calculated independently per feature d):'
p.font.name = 'Arial'
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = C_NAVY

p = tf_fc.add_paragraph()
p.text = '   μ_d = (1 / N) * Σ_{i=1}^N x_{i,d}        σ_d^2 = (1 / N) * Σ_{i=1}^N (x_{i,d} - μ_d)^2'
p.font.name = 'Arial'
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = RGBColor(13, 71, 161)
p.space_after = Pt(6)

p = tf_fc.add_paragraph()
p.text = '2. Standardization & Learned Scaling:'
p.font.name = 'Arial'
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = C_NAVY

p = tf_fc.add_paragraph()
p.text = '   x̂_{i,d} = (x_{i,d} - μ_d) / √(σ_d^2 + ε)       y_{i,d} = γ_d * x̂_{i,d} + β_d'
p.font.name = 'Arial'
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = RGBColor(13, 71, 161)
p.space_after = Pt(8)

p = tf_fc.add_paragraph()
p.text = '• Normalization Domain: Along batch dimension N independently\n• Effective Sample Size: m = N samples per feature\n• Learnable Parameters: 2 * D parameters (γ_d, β_d per feature)'
p.font.name = 'Arial'
p.font.size = Pt(10)
p.font.color.rgb = C_DARK

# Right Card: Convolutional Spatial Normalization
c_cnn = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.45), Inches(5.7), Inches(4.3))
c_cnn.fill.solid()
c_cnn.fill.fore_color.rgb = C_GREEN_CARD
c_cnn.line.color.rgb = RGBColor(46, 125, 50)
c_cnn.line.width = Pt(2)
tf_cnn = c_cnn.text_frame
tf_cnn.word_wrap = True
tf_cnn.margin_left = tf_cnn.margin_top = tf_cnn.margin_right = tf_cnn.margin_bottom = Inches(0.22)

p = tf_cnn.paragraphs[0]
p.text = 'Convolutional Layers (Spatial 4D)'
p.font.name = 'Arial'
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = RGBColor(27, 94, 32)
p.space_after = Pt(4)

p = tf_cnn.add_paragraph()
p.text = 'Activation Tensor: (N, C, H, W)  |  N = Batch, C = Channels, H, W = Grid'
p.font.name = 'Arial'
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = RGBColor(46, 125, 50)
p.space_after = Pt(8)

p = tf_cnn.add_paragraph()
p.text = '1. Spatial Statistics (pooled across batch and spatial grid H x W):'
p.font.name = 'Arial'
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = C_NAVY

p = tf_cnn.add_paragraph()
p.text = '   μ_c = (1 / m) * Σ_{i,h,w} x_{i,c,h,w}     σ_c^2 = (1 / m) * Σ_{i,h,w} (x_{i,c,h,w} - μ_c)^2'
p.font.name = 'Arial'
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = RGBColor(27, 94, 32)
p.space_after = Pt(6)

p = tf_cnn.add_paragraph()
p.text = '2. Standardization & Shared Feature Map Shift:'
p.font.name = 'Arial'
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = C_NAVY

p = tf_cnn.add_paragraph()
p.text = '   x̂_{i,c,h,w} = (x_{i,c,h,w} - μ_c) / √(σ_c^2 + ε)   y_{i,c,h,w} = γ_c * x̂_{i,c,h,w} + β_c'
p.font.name = 'Arial'
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = RGBColor(27, 94, 32)
p.space_after = Pt(8)

p = tf_cnn.add_paragraph()
p.text = '• Normalization Domain: Jointly across (N, H, W) per feature map\n• Effective Sample Size: m = N * H * W (e.g., 64 * 14 * 14 = 12,544 elements)\n• Learnable Parameters: Only 2 * C parameters (γ_c, β_c per channel)'
p.font.name = 'Arial'
p.font.size = Pt(10)
p.font.color.rgb = C_DARK

# Bottom Full-Width Banner: Architectural Principle
b_cnn = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.9), Inches(11.7), Inches(0.85))
b_cnn.fill.solid()
b_cnn.fill.fore_color.rgb = C_LIGHT_BG
b_cnn.line.color.rgb = RGBColor(180, 205, 230)
b_cnn.line.width = Pt(1.5)
tf_bcnn = b_cnn.text_frame
tf_bcnn.word_wrap = True
tf_bcnn.margin_left = tf_bcnn.margin_top = tf_bcnn.margin_right = tf_bcnn.margin_bottom = Inches(0.12)

p = tf_bcnn.paragraphs[0]
p.text = 'Core Architectural Principle: Spatial Weight Sharing & Translation Equivariance'
p.font.name = 'Arial'
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(2)

p = tf_bcnn.add_paragraph()
p.text = 'In CNNs, convolutional kernels share weights across all spatial locations (H, W). To preserve translation equivariance, activations at different spatial locations are normalized identically using one shared pair (γ_c, β_c) per channel. This expands the sample size to m = N * H * W, yielding exceptionally stable variance estimates with minimal parameter overhead.'
p.font.name = 'Arial'
p.font.size = Pt(9.5)
p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 7: Training vs. Evaluation Mechanics
# -------------------------------------------------------------
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, 'Operational Mechanics: Training vs. Inference Mode')
add_footer(s7, 7)

c_tr = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.1))
c_tr.fill.solid()
c_tr.fill.fore_color.rgb = C_CARD_BG
c_tr.line.color.rgb = RGBColor(190, 215, 240)
tf_tr = c_tr.text_frame
tf_tr.word_wrap = True
tf_tr.margin_left = tf_tr.margin_top = tf_tr.margin_right = tf_tr.margin_bottom = Inches(0.25)

p = tf_tr.paragraphs[0]
p.text = 'Training Phase (model.train())'
p.font.name = 'Arial'
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(8)

p = tf_tr.add_paragraph()
p.text = '• Mini-Batch Statistics:\n  Mean and variance are computed dynamically from the current training mini-batch B.\n\n• Stochastic Regularization Effect:\n  Because statistics depend on random mini-batch groupings, each sample receives slight stochastic perturbation. This acts as an implicit regularizer, decreasing reliance on dropout.\n\n• Tracking Running Population Statistics:\n  Maintains exponential moving averages throughout training:\n  mu_{run} = (1 - p) * mu_{run} + p * mu_B\n  sigma_{run}^2 = (1 - p) * sigma_{run}^2 + p * sigma_B^2\n  where p is the momentum parameter (typically 0.1).'
p.font.name = 'Arial'
p.font.size = Pt(11.5)
p.font.color.rgb = C_DARK

c_inf = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.1))
c_inf.fill.solid()
c_inf.fill.fore_color.rgb = C_LIGHT_BG
c_inf.line.color.rgb = RGBColor(215, 225, 235)
tf_inf = c_inf.text_frame
tf_inf.word_wrap = True
tf_inf.margin_left = tf_inf.margin_top = tf_inf.margin_right = tf_inf.margin_bottom = Inches(0.25)

p = tf_inf.paragraphs[0]
p.text = 'Inference Phase (model.eval())'
p.font.name = 'Arial'
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(8)

p = tf_inf.add_paragraph()
p.text = '• Deterministic Evaluation:\n  Individual samples must produce identical predictions regardless of batch composition or single-sample serving.\n\n• Fixed Population Parameters:\n  Frozen running statistics (mu_{run}, sigma_{run}^2) are used in place of mini-batch statistics.\n\n• Linear Operator Folding:\n  At test time, the normalization transformation simplifies to an affine mapping:\n  y = W_{folded} * x + b_{folded}\n  This allows BatchNorm to be folded directly into preceding convolutional weights, resulting in zero additional inference latency.'
p.font.name = 'Arial'
p.font.size = Pt(11.5)
p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 8: Empirical Training Acceleration
# -------------------------------------------------------------
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, 'Empirical Measurement of Training Acceleration')
add_footer(s8, 8)

fig3_p = os.path.join(FIG_DIR, 'figure3_empirical_training_acceleration.png')
if os.path.exists(fig3_p):
    s8.shapes.add_picture(fig3_p, Inches(0.8), Inches(1.5), width=Inches(11.7))

b_exp = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.3), Inches(11.7), Inches(1.4))
b_exp.fill.solid()
b_exp.fill.fore_color.rgb = C_CARD_BG
b_exp.line.color.rgb = RGBColor(190, 215, 240)
tf_e = b_exp.text_frame
tf_e.word_wrap = True
tf_e.margin_left = tf_e.margin_top = tf_e.margin_right = tf_e.margin_bottom = Inches(0.15)

p = tf_e.paragraphs[0]
p.text = 'Key Empirical Insights from Benchmarking:'
p.font.name = 'Arial'
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(2)

p = tf_e.add_paragraph()
p.text = '• (A) Rapid Loss Reduction: BatchNorm drops training loss to under 0.1 within 2 epochs, while the unnormalized baseline requires extensive iterations.\n• (B) Superior Test Accuracy: BatchNorm reaches 97.45% validation accuracy, outperforming models without normalization by a wide margin.\n• (C) High Learning Rate Resilience: At lr = 0.15, the baseline fails to optimize due to gradient explosion, whereas BatchNorm trains smoothly without divergence.'
p.font.name = 'Arial'
p.font.size = Pt(10.5)
p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 9: Hidden Activations & Gradient Dynamics
# -------------------------------------------------------------
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, 'Internal Dynamics: Activation Distributions & Gradient Norms')
add_footer(s9, 9)

fig4_p = os.path.join(FIG_DIR, 'figure4_gradient_stability_and_internal_distribution.png')
if os.path.exists(fig4_p):
    s9.shapes.add_picture(fig4_p, Inches(0.8), Inches(1.5), width=Inches(7.2))

t9 = s9.shapes.add_textbox(Inches(8.2), Inches(1.5), Inches(4.3), Inches(5.1))
tf9 = t9.text_frame
tf9.word_wrap = True
tf9.margin_left = tf9.margin_top = tf9.margin_right = tf9.margin_bottom = 0

p = tf9.paragraphs[0]
p.text = 'Preventing Saturation & Smoothing Gradients'
p.font.name = 'Arial'
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(6)

p = tf9.add_paragraph()
p.text = '• Activation Distribution Control:\n  Without normalization, deep activations spread widely and drift, causing neurons to saturate or output near-zero gradients.\n\n• Zero-Centered Standard Normalization:\n  BatchNorm centers hidden activations with mean 0.00 and standard deviation 1.00, keeping activations in the most sensitive, dynamic range of non-linearities.\n\n• Stable Gradient Backpropagation:\n  Gradient norms remain well-conditioned across all layers. This eliminates the need for complex warm-up schedules and delicate parameter initializations.'
p.font.name = 'Arial'
p.font.size = Pt(11)
p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 10: Comparative Analysis: Alternative Normalization Methods
# -------------------------------------------------------------
s10 = prs.slides.add_slide(blank_layout)
add_header(s10, 'Comparative Analysis: Alternative Normalization Methods')
add_footer(s10, 10)

fig5_p = os.path.join(FIG_DIR, 'figure5_normalization_taxonomy_comparison.png')
if os.path.exists(fig5_p):
    s10.shapes.add_picture(fig5_p, Inches(0.8), Inches(1.5), width=Inches(11.7))

c10 = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.0), Inches(11.7), Inches(1.7))
c10.fill.solid()
c10.fill.fore_color.rgb = C_LIGHT_BG
c10.line.color.rgb = RGBColor(210, 220, 235)
tf10 = c10.text_frame
tf10.word_wrap = True
tf10.margin_left = tf10.margin_top = tf10.margin_right = tf10.margin_bottom = Inches(0.15)

p = tf10.paragraphs[0]
p.text = 'Comparative Assessment Across Deep Learning Paradigms:'
p.font.name = 'Arial'
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(2)

p = tf10.add_paragraph()
p.text = '• Batch Normalization (BN): Optimal for Computer Vision with moderate-to-large mini-batches. Degrades when N < 8.\n• Layer Normalization (LN, Ba et al. 2016): Normalizes across channels per sample. Standard for RNNs and Transformers (BERT, GPT, ViT).\n• Group Normalization (GN, Wu & He 2018): Normalizes groups of channels. Completely independent of batch size; ideal for high-res vision tasks.\n• Weight Normalization (WN, Salimans & Kingma 2016): Re-parameterizes weight vectors directly; low memory overhead but less stabilization.'
p.font.name = 'Arial'
p.font.size = Pt(10.5)
p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 11: Real-World Architectural Adoption
# -------------------------------------------------------------
s11 = prs.slides.add_slide(blank_layout)
add_header(s11, 'Practical Implementation & Architectural Impact')
add_footer(s11, 11)

arch_cards = [
    ('ResNet & Deep Residual Networks', '• Foundational enabler of 50 to 152 layer networks (He et al., 2016).\n• Placed within residual blocks after convolution.\n• Guarantees that identity shortcuts receive well-scaled gradient signals.'),
    ('Inception & Modern Vision CNNs', '• Replaced aggressive dropout in Inception-v2 and Inception-v3 (Ioffe & Szegedy, 2015).\n• Enables 14x fewer training steps to reach ImageNet state-of-the-art accuracy.'),
    ('Architectural Best Practice: Bias Omission', '• In layers preceding BatchNorm: Conv2d(in_channels, out_channels, bias=False).\n• Because BatchNorm subtracts the mini-batch mean, any additive bias b is exactly canceled out:\n  BN(W * x + b) = BN(W * x).\n• Omitting bias saves memory and parameters without any loss of accuracy.')
]

for idx, (title, content) in enumerate(arch_cards):
    left = Inches(0.8 + idx * 3.95)
    card = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.6), Inches(3.8), Inches(5.0))
    card.fill.solid()
    card.fill.fore_color.rgb = C_CARD_BG
    card.line.color.rgb = RGBColor(190, 215, 240)
    
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.2)
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = 'Arial'
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(8)
    
    p = tf.add_paragraph()
    p.text = content
    p.font.name = 'Arial'
    p.font.size = Pt(11)
    p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 12: Critical Reflection, Limitations & Failure Modes
# -------------------------------------------------------------
s12 = prs.slides.add_slide(blank_layout)
add_header(s12, 'Critical Reflection: Limitations & Failure Modes')
add_footer(s12, 12)

limits = [
    ('1. Mini-Batch Size Sensitivity', '• When batch size is very small (N = 2, 4), sample mean and variance become noisy and inaccurate.\n• Error rate increases dramatically in memory-intensive tasks such as 3D medical segmentation and object detection.\n• Group Normalization is strongly preferred in small-batch domains.'),
    ('2. Distributed Training Synchronization', '• Standard BatchNorm calculates statistics per GPU worker, reducing the effective batch size.\n• Synchronized BatchNorm (SyncBN) shares statistics across nodes but introduces network latency and synchronization bottlenecks.'),
    ('3. Incompatibility with Recurrent Networks', '• In RNNs, sequence lengths vary dynamically across time steps.\n• Maintaining separate running statistics per time step leads to exploding estimation errors; Layer Normalization is strictly superior.')
]

for idx, (title, content) in enumerate(limits):
    top = Inches(1.6 + idx * 1.7)
    card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(11.7), Inches(1.5))
    card.fill.solid()
    card.fill.fore_color.rgb = C_LIGHT_BG
    card.line.color.rgb = RGBColor(220, 220, 230)
    
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.18)
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = 'Arial'
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_ACCENT
    p.space_after = Pt(4)
    
    p = tf.add_paragraph()
    p.text = content
    p.font.name = 'Arial'
    p.font.size = Pt(11)
    p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 13: Summary & Conclusion
# -------------------------------------------------------------
s13 = prs.slides.add_slide(blank_layout)
add_header(s13, 'Summary & Concluding Synthesis')
add_footer(s13, 13)

concl_box = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.1))
concl_box.fill.solid()
concl_box.fill.fore_color.rgb = C_CARD_BG
concl_box.line.color.rgb = RGBColor(190, 215, 240)
tf13 = concl_box.text_frame
tf13.word_wrap = True
tf13.margin_left = tf13.margin_top = tf13.margin_right = tf13.margin_bottom = Inches(0.3)

p = tf13.paragraphs[0]
p.text = 'Core Takeaways of the Oral Assignment:'
p.font.name = 'Arial'
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)

p = tf13.add_paragraph()
p.text = '1. Resolution of Optimization Bottlenecks:\n   Batch Normalization mitigates internal covariate shift, bounds activation distributions, and prevents vanishing/exploding gradients in deep networks.\n\n2. Exceptional Training Acceleration:\n   By smoothing the optimization landscape, BatchNorm allows learning rates up to an order of magnitude higher, accelerating convergence by 3x to 10x.\n\n3. Spatial Equivariance in CNNs:\n   Jointly normalizing over batch and spatial dimensions (N x H x W) preserves convolutional properties with minimal parameter overhead.\n\n4. Architectural Foundation:\n   BatchNorm is an indispensable building block for deep vision architectures (ResNet, Inception), while LayerNorm and GroupNorm complement it in sequence and small-batch domains.'
p.font.name = 'Arial'
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 14: List of Figures
# -------------------------------------------------------------
s14 = prs.slides.add_slide(blank_layout)
add_header(s14, 'List of Figures')
add_footer(s14, 14)

figs_info = [
    ('Figure 1: Deep Network Training Dynamics, Backpropagation, and Internal Covariate Shift', 'Slide 4. Conceptual diagram illustrating forward activations, loss evaluation, reverse gradient flow, and the parameter update shift mechanism.'),
    ('Figure 2: Batch Normalization in Fully Connected vs. Convolutional Architectures', 'Slide 6. Mathematical comparison of normalization over feature dimensions (N, D) versus 4D spatial tensors (N x H x W, C).'),
    ('Figure 3: Empirical Training Acceleration, Accuracy Progression, and Learning Rate Stability', 'Slide 8. Multi-panel empirical evaluation showing training loss convergence, test accuracy progression, and high learning rate stability.'),
    ('Figure 4: Hidden Layer Activation Distributions and Gradient Norm Conditioning', 'Slide 9. Histogram analysis of deep layer activations before and after Batch Normalization, showing zero-centered standardization.'),
    ('Figure 5: Normalization Taxonomy Comparison Across Tensor Dimensions (N, C, H, W)', 'Slide 10. Architectural comparison of Batch Normalization, Layer Normalization, Instance Normalization, and Group Normalization.')
]

for idx, (title, desc) in enumerate(figs_info):
    top = Inches(1.5 + idx * 1.0)
    box = s14.shapes.add_textbox(Inches(0.8), top, Inches(11.7), Inches(0.9))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = 'Arial'
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    
    p = tf.add_paragraph()
    p.text = desc
    p.font.name = 'Arial'
    p.font.size = Pt(10)
    p.font.color.rgb = C_DARK

# -------------------------------------------------------------
# Slide 15: Academic References
# -------------------------------------------------------------
s15 = prs.slides.add_slide(blank_layout)
add_header(s15, 'References (APA 7th Edition)')
add_footer(s15, 15)

refs = [
    '• Ba, J. L., Kiros, J. R., & Hinton, G. E. (2016). Layer normalization. arXiv preprint arXiv:1607.06450.',
    '• Balestriero, R., & Baraniuk, R. G. (2022). Batch normalization explained. arXiv preprint arXiv:2209.14778.',
    '• He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (pp. 770-778).',
    '• Ioffe, S., & Szegedy, C. (2015). Batch normalization: Accelerating deep network training by reducing internal covariate shift. In International Conference on Machine Learning (ICML) (pp. 448-456). PMLR.',
    '• Salimans, T., & Kingma, D. P. (2016). Weight normalization: A simple reparameterization to accelerate training of deep neural networks. Advances in Neural Information Processing Systems (NeurIPS), 29.',
    '• Santurkar, S., Tsipras, D., Ilyas, A., & Madry, A. (2018). How does batch normalization help optimization? Advances in Neural Information Processing Systems (NeurIPS), 31.',
    '• Ulyanov, D., Vedaldi, A., & Lempitsky, V. (2016). Instance normalization: The missing ingredient for fast stylization. arXiv preprint arXiv:1607.08022.',
    '• Wu, Y., & He, K. (2018). Group normalization. In Proceedings of the European Conference on Computer Vision (ECCV) (pp. 3-19).'
]

box_ref = s15.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.1))
tf_ref = box_ref.text_frame
tf_ref.word_wrap = True
tf_ref.margin_left = tf_ref.margin_top = tf_ref.margin_right = tf_ref.margin_bottom = 0

for idx, r in enumerate(refs):
    p = tf_ref.paragraphs[0] if idx == 0 else tf_ref.add_paragraph()
    p.text = r
    p.font.name = 'Arial'
    p.font.size = Pt(10.5)
    p.font.color.rgb = C_DARK
    p.space_after = Pt(6)

# Save presentation PPTX
pptx_path = os.path.join(PRES_DIR, '20261103_Raji_FaruqIshola_4253139_DLBDSNNDL01_Presentation.pptx')
prs.save(pptx_path)
print('Successfully generated presentation PPTX:', pptx_path)

if __name__ == '__main__':
    print('Finished executing presentation builder script.')
