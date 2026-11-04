# Here I import the libraries I need to build the interactive HTML5 presentation rehearsal studio.
import os
import json
import wave

# Here I define the directory paths for the project.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(BASE_DIR, 'audio')
SLIDES_IMG_DIR = os.path.join(BASE_DIR, 'slide_images')
PRES_DIR = os.path.join(BASE_DIR, 'presentation')
SUBMISSION_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'submission')

slides = [
    {
        'id': 1,
        'title': 'Slide 1: Title Slide (Welcome and Topic Introduction)',
        'target_time': '0:00 - 1:00 (1.0 min)',
        'duration_sec': 78,
        'img': '../slide_images/slide_1.png',
        'audio': '../audio/slide_1.wav',
        'script': 'Good day, esteemed examiner. My name is Raji Faruq Ishola, matriculation number 4253139. Today, I am presenting my Oral Assignment for the module Neural Nets and Deep Learning, with course code DLBDSNNDL01-01. The topic of my presentation is Accelerating Deep Network Training via Batch Normalization.\n\nIn deep learning, training deep neural networks has historically been difficult. As networks grow deeper, training often becomes unstable, slow, or fails entirely. In 2015, Sergey Ioffe and Christian Szegedy introduced Batch Normalization, which fundamentally transformed deep learning practice. Today, Batch Normalization is a core architectural component across modern computer vision and deep learning models. In this presentation, I explain the foundational challenges of deep network optimization, the mathematical formulation of Batch Normalization, its extension to convolutional architectures, and an empirical evaluation comparing it with alternative normalization methods.',
        'qa': 'Q: Why is Batch Normalization considered a breakthrough in deep learning?\nA: It addressed foundational optimization barriers by stabilizing internal activation distributions, smoothing the optimization landscape, and allowing networks like ResNet to train deeper than 100 layers without divergence.'
    },
    {
        'id': 2,
        'title': 'Slide 2: Agenda and Presentation Roadmap',
        'target_time': '1:00 - 2:00 (1.0 min)',
        'duration_sec': 65,
        'img': '../slide_images/slide_2.png',
        'audio': '../audio/slide_2.wav',
        'script': 'Let us look at the agenda for our 15 minutes together. I have structured this presentation into four major parts.\n\nFirst, I will explain how deep neural networks are trained through gradient descent and backpropagation. I will discuss the core optimization challenges, specifically vanishing gradients and internal covariate shift.\n\nSecond, I will present the mathematical formulation of Batch Normalization, showing how mini-batch statistics are calculated and how learnable scale and shift parameters restore representational capacity. I will also detail its implementation in convolutional neural networks.\n\nThird, I will explain how training acceleration is measured empirically. I will share experimental results comparing Batch Normalization with Layer Normalization and Group Normalization.\n\nFinally, I will discuss practical implementation guidelines, critical limitations, and conclude with key takeaways.',
        'qa': 'Q: How does your presentation adhere to the IU task sheet requirements?\nA: It directly maps to the three questions of Task 1: deep training foundations, mathematical/CNN formulation, and empirical acceleration metrics with comparative literature evaluation.'
    },
    {
        'id': 3,
        'title': 'Slide 3: Deep Neural Network Training Fundamentals',
        'target_time': '2:00 - 3:30 (1.5 min)',
        'duration_sec': 90,
        'img': '../slide_images/slide_3.png',
        'audio': '../audio/slide_3.wav',
        'script': 'To understand why Batch Normalization is needed, we must first look at how deep neural networks are trained. A neural network is a composition of non-linear functions arranged in sequential layers. In the forward pass, input data passes through weight matrices, bias vectors, and activation functions to produce a final prediction. A loss function, such as cross-entropy for classification, measures the discrepancy between predicted outputs and ground truth labels.\n\nTraining proceeds through gradient-based optimization, typically mini-batch Stochastic Gradient Descent or its adaptive variants. The central engine of this process is backpropagation, which uses the mathematical chain rule of calculus. Backpropagation computes the partial derivative of the scalar loss with respect to each weight and bias parameter in the network.\n\nHowever, in deep architectures with many layers, backpropagation requires multiplying many Jacobian matrices together. When these gradients are repeatedly multiplied across layers, their magnitudes can either shrink exponentially toward zero or grow exponentially toward infinity. This is the well-known vanishing and exploding gradient problem, which historically prevented researchers from training networks deeper than a few layers without severe numerical instabilities.',
        'qa': 'Q: What mathematical mechanism causes vanishing gradients in deep networks?\nA: Repeated Jacobian matrix multiplication across L layers via the chain rule. When singular values of weight matrices or activation derivatives are less than 1, gradients decay exponentially toward zero.'
    },
    {
        'id': 4,
        'title': 'Slide 4: The Internal Covariate Shift Bottleneck',
        'target_time': '3:30 - 5:00 (1.5 min)',
        'duration_sec': 92,
        'img': '../slide_images/slide_4.png',
        'audio': '../audio/slide_4.wav',
        'script': 'In their 2015 seminal paper, Ioffe and Szegedy identified a major challenge which they termed Internal Covariate Shift. In classical machine learning, covariate shift refers to a situation where the input data distribution changes between training and testing. Internal Covariate Shift describes a similar phenomenon occurring inside the hidden layers of a deep network during training.\n\nDuring gradient descent, all network parameters update simultaneously. When early layers update their weights, the distribution of inputs feeding into later layers changes continuously. As a result, subsequent layers must constantly adapt to a moving target. This instability forces practitioners to use very small learning rates and careful parameter initialization, which severely slows down convergence.\n\nIn addition, when using saturating activation functions such as the sigmoid or hyperbolic tangent, shifting inputs easily push activations into regions where the derivative is close to zero. Once activations saturate, gradients vanish, and learning halts. Later work by Santurkar and colleagues in 2018 provided an additional perspective: Batch Normalization accelerates training primarily by smoothing the optimization landscape, making gradients more predictable and Lipschitz-continuous.',
        'qa': 'Q: How did Santurkar et al. (2018) refine our understanding of Batch Normalization beyond internal covariate shift?\nA: They demonstrated through perturbation experiments that BatchNorm works primarily by smoothing the loss landscape and ensuring Lipschitz continuity of gradients, rather than solely reducing covariate shift.'
    },
    {
        'id': 5,
        'title': 'Slide 5: Batch Normalization: Core Mathematical Principles',
        'target_time': '5:00 - 6:30 (1.5 min)',
        'duration_sec': 96,
        'img': '../slide_images/slide_5.png',
        'audio': '../audio/slide_5.wav',
        'script': 'Now let us examine the mathematical formulation of Batch Normalization. For a given mini-batch of activations, the transformation operates across four distinct steps.\n\nFirst, we compute the mini-batch mean by summing the activation values across all samples in the batch and dividing by the batch size N. Second, we compute the mini-batch variance by calculating the average squared deviation of each sample from the mean.\n\nThird, each activation is standardized by subtracting the mini-batch mean and dividing by the standard deviation. A small positive constant, epsilon, is added to the variance to ensure numerical stability and avoid division by zero. This step produces standardized activations with zero mean and unit variance.\n\nHowever, simply forcing activations to have zero mean and unit variance can limit what the layer can represent. For example, if a sigmoid activation is constrained to zero mean, it is forced to operate entirely in its linear regime. To solve this, Ioffe and Szegedy introduced two learnable parameters: gamma, which scales the normalized value, and beta, which shifts it. These parameters are updated through backpropagation alongside the network weights. If optimal, the network can even recover the identity mapping by learning gamma equal to standard deviation and beta equal to mean.',
        'qa': 'Q: Why are gamma and beta essential parameters?\nA: Pure standardization restricts activations to zero mean and unit variance, which removes non-linear expressiveness. Learnable gamma and beta allow the network to scale and shift activations flexibly, preserving representation capacity.'
    },
    {
        'id': 6,
        'title': 'Slide 6: Batch Normalization in Convolutional Architectures',
        'target_time': '6:30 - 8:00 (1.5 min)',
        'duration_sec': 91,
        'img': '../slide_images/slide_6.png',
        'audio': '../audio/slide_6.wav',
        'script': 'In convolutional neural networks, Batch Normalization requires a specialized spatial formulation to respect the translation equivariance of convolution operations. In a fully connected layer, activations form a two-dimensional matrix of size N by D, and normalization occurs independently across each feature dimension.\n\nIn contrast, a convolutional feature map has four dimensions: batch size N, channel count C, height H, and width W. Because convolutional filters slide across spatial positions and share weights, all locations within a single feature map must be treated equally. Therefore, spatial Batch Normalization pools statistics over both the mini-batch dimension and all spatial coordinates H and W simultaneously.\n\nFor each channel, the effective sample size is N multiplied by H and W. For instance, with a batch size of 64 and a 14 by 14 feature map, the mean and variance for a single channel are calculated across 12,544 individual values. Importantly, each feature map learns only a single pair of gamma and beta parameters across the entire spatial grid. This parameter efficiency preserves the structural properties of convolution while providing robust stabilization.',
        'qa': 'Q: Why must convolutional BatchNorm pool over spatial dimensions H and W?\nA: Convolutional kernels share weights across all spatial coordinates. To preserve translation equivariance, activations at different spatial locations must be normalized identically with one shared pair of (gamma, beta) per channel.'
    },
    {
        'id': 7,
        'title': 'Slide 7: Training Mode vs. Inference Mode Mechanics',
        'target_time': '8:00 - 9:00 (1.0 min)',
        'duration_sec': 73,
        'img': '../slide_images/slide_7.png',
        'audio': '../audio/slide_7.wav',
        'script': 'An essential operational detail of Batch Normalization is the distinction between training mode and evaluation mode. During training, normalization relies on the current mini-batch statistics. This introduces stochasticity into each sample activation, which acts as a gentle regularizer and reduces the need for heavy dropout.\n\nHowever, at test time, predictions must be deterministic and independent of other samples. An image classification result should not depend on what other images happen to be evaluated in the same batch. Also, during real-world production deployment, models often process single instances one at a time.\n\nTo achieve deterministic inference, Batch Normalization tracks running exponential moving averages of the mean and variance during training with a momentum parameter. During testing, the moving average mean and variance are used as fixed parameters. The normalization step becomes a simple linear transformation that can even be mathematically folded into the convolutional weights for zero-cost inference.',
        'qa': 'Q: How does weight folding work during inference?\nA: Since BatchNorm at test time is a linear affine mapping y = gamma*(x-mu)/sigma + beta, it can be mathematically merged into the convolutional weights W_folded = W * (gamma/sigma) and bias b_folded = beta - (gamma*mu)/sigma, resulting in zero extra inference time.'
    },
    {
        'id': 8,
        'title': 'Slide 8: Empirical Measurement of Training Acceleration',
        'target_time': '9:00 - 10:30 (1.5 min)',
        'duration_sec': 92,
        'img': '../slide_images/slide_8.png',
        'audio': '../audio/slide_8.wav',
        'script': 'To verify theoretical claims, we must measure training acceleration using objective empirical metrics. Acceleration is evaluated through three key indicators: epochs to reach a target validation accuracy, wall-clock training time, and learning rate tolerance.\n\nOn Slide 8, I present empirical results from controlled experiments I conducted using a convolutional architecture. In Panel A, we observe the training loss curves. The baseline network without normalization requires significantly more epochs to decrease its loss. In contrast, the network with Batch Normalization achieves rapid loss reduction within the very first two epochs.\n\nIn Panel B, we look at validation accuracy progression. Batch Normalization achieves over 97 percent accuracy in four epochs, whereas the baseline requires twice as many epochs to reach comparable accuracy.\n\nPanel C illustrates learning rate stability. When the learning rate is raised to 0.15, the unnormalized baseline experiences unstable gradients and diverges completely. The network with Batch Normalization remains stable, optimizes smoothly, and converges without issue. This ability to use large learning rates is the single most significant factor behind the wall-clock speedup observed in practice.',
        'qa': 'Q: What is the primary empirical evidence for training acceleration?\nA: Achieving target accuracy in 3x to 5x fewer epochs and allowing learning rates up to an order of magnitude larger without gradient divergence.'
    },
    {
        'id': 9,
        'title': 'Slide 9: Hidden Activation Distributions and Gradient Stability',
        'target_time': '10:30 - 11:30 (1.0 min)',
        'duration_sec': 61,
        'img': '../slide_images/slide_9.png',
        'audio': '../audio/slide_9.wav',
        'script': 'Slide 9 illustrates the internal mechanism behind this stability. Here, I examined the distribution of activations in deep layers before non-linear activation.\n\nIn Panel A, the unnormalized network displays an uncontrolled activation distribution with high variance and drifting mean values. As these wide activations pass through non-linearities, many values fall into saturated saturation regimes, leading to gradient dampening.\n\nIn Panel B, Batch Normalization centers the activation distribution cleanly around zero with unit variance. Every neuron operates in its most active, responsive regime, preventing saturation. At the same time, gradient norms during the backward pass remain bounded and stable across all layers. This confirms that Batch Normalization controls gradient scaling throughout the network depth.',
        'qa': 'Q: How does zero-centered standardization prevent gradient saturation?\nA: Most activation functions (tanh, sigmoid, even leaky ReLU) have their highest derivative and dynamic sensitivity near zero. Keeping inputs zero-centered ensures neurons operate in their non-saturating regime.'
    },
    {
        'id': 10,
        'title': 'Slide 10: Comparative Analysis: Alternative Normalization Methods',
        'target_time': '11:30 - 13:00 (1.5 min)',
        'duration_sec': 98,
        'img': '../slide_images/slide_10.png',
        'audio': '../audio/slide_10.wav',
        'script': 'While Batch Normalization is dominant in computer vision, it is not the only normalization technique in modern deep learning. The academic literature offers three major competing approaches, illustrated on Slide 10.\n\nFirst, Layer Normalization, introduced by Jimmy Ba, Ryan Kiros, and Geoffrey Hinton in 2016, computes normalization statistics across all channels and features for a single sample, rather than across the batch. Because Layer Normalization does not depend on batch size, it is the standard normalization method in natural language processing and Transformer architectures.\n\nSecond, Instance Normalization, proposed by Ulyanov and colleagues, normalizes across spatial dimensions for each channel individually. It is widely used in style transfer and generative adversarial networks where contrast normalization is beneficial.\n\nThird, Group Normalization, introduced by Yuxin Wu and Kaiming He in 2018, divides channels into distinct groups and normalizes across the channels in each group and spatial dimensions. Group Normalization matches Batch Normalization performance on visual recognition tasks while remaining completely invariant to mini-batch size. In our empirical benchmark, Group Normalization performed closely behind Batch Normalization, proving to be an excellent alternative when batch sizes must be small.',
        'qa': 'Q: Why is Layer Normalization preferred in Transformers and RNNs over BatchNorm?\nA: Sequence lengths vary dynamically across samples and time steps. LayerNorm normalizes across the feature dimension within each individual sample, making it invariant to batch size and sequence length.'
    },
    {
        'id': 11,
        'title': 'Slide 11: Practical Implementation and Architectural Impact',
        'target_time': '13:00 - 14:00 (1.0 min)',
        'duration_sec': 68,
        'img': '../slide_images/slide_11.png',
        'audio': '../audio/slide_11.wav',
        'script': 'The practical impact of Batch Normalization on modern deep learning cannot be overstated. When Kaiming He and colleagues designed the Deep Residual Network, or ResNet, in 2015, Batch Normalization was essential to successfully training networks with 50, 101, and 152 layers.\n\nIn terms of architectural guidelines, Batch Normalization is conventionally placed immediately after the linear convolution operation and before the non-linear activation function. Because the normalization step subtracts the mini-batch mean, any additive bias term in the preceding convolutional layer is completely canceled out. Therefore, when using Batch Normalization, convolutional layers should be configured without bias parameters, saving memory and compute.\n\nIn addition, Batch Normalization reduces the need for aggressive weight decay or dropout, because mini-batch statistics introduce slight regularizing noise during training.',
        'qa': 'Q: Why should Conv2d have bias=False when followed by BatchNorm?\nA: BatchNorm explicitly subtracts the batch mean mu_B during standardization. Any constant bias b added prior to BatchNorm is mathematically canceled out: (x + b) - (mu + b) = x - mu.'
    },
    {
        'id': 12,
        'title': 'Slide 12: Critical Reflection, Limitations, and Failure Modes',
        'target_time': '14:00 - 14:30 (0.5 min)',
        'duration_sec': 41,
        'img': '../slide_images/slide_12.png',
        'audio': '../audio/slide_12.wav',
        'script': 'A critical academic evaluation requires acknowledging limitations. Batch Normalization has three known weaknesses. First, it degrades significantly when mini-batch sizes are very small, such as batches of 2 or 4 used in dense object detection and high-resolution medical imaging. Second, in distributed training across multiple GPUs, synchronizing batch statistics requires communication overhead. Third, Batch Normalization is unsuitable for variable-length sequence modeling and recurrent networks, where Layer Normalization remains superior.',
        'qa': 'Q: What happens to BatchNorm when batch size N=2?\nA: The sample mean and variance estimates become highly stochastic and inaccurate, introducing excessive noise that severely degrades model convergence and test accuracy.'
    },
    {
        'id': 13,
        'title': 'Slide 13: Summary and Concluding Synthesis',
        'target_time': '14:30 - 15:00 (0.5 min)',
        'duration_sec': 42,
        'img': '../slide_images/slide_13.png',
        'audio': '../audio/slide_13.wav',
        'script': 'In summary, Batch Normalization resolves foundational optimization challenges in deep networks by standardizing internal activations and smoothing the loss landscape. It enables substantially higher learning rates, accelerates training convergence by factors of three to ten, and provides mild regularization.\n\nWhile alternative methods like Layer Normalization and Group Normalization are preferable for sequence processing and small-batch regimes, Batch Normalization remains a cornerstone technique in deep learning. Thank you very much for your time and attention. I am now pleased to answer any questions.',
        'qa': 'Q: How would you conclude the debate between BatchNorm and competing methods?\nA: BatchNorm is unmatched in large-batch computer vision; GroupNorm is superior for small batches/high-resolution vision; and LayerNorm is the definitive standard for sequence and attention models.'
    },
    {
        'id': 14,
        'title': 'Slide 14: List of Figures',
        'target_time': 'Reference',
        'duration_sec': 14,
        'img': '../slide_images/slide_14.png',
        'audio': '../audio/slide_14.wav',
        'script': 'On this slide, I provide the formal list of figures included in the presentation, detailing the conceptual diagrams, mathematical formulations, and empirical benchmarking plots.',
        'qa': 'Reference slide listing all academic figures.'
    },
    {
        'id': 15,
        'title': 'Slide 15: Academic References',
        'target_time': 'Reference',
        'duration_sec': 16,
        'img': '../slide_images/slide_15.png',
        'audio': '../audio/slide_15.wav',
        'script': 'Here are the primary academic references supporting this presentation, including foundational papers by Ioffe and Szegedy, Balestriero and Baraniuk, and competing normalization literature. Thank you for your attention.',
        'qa': 'Reference slide citing Ioffe & Szegedy (2015), Ba et al. (2016), Wu & He (2018), and He et al. (2016).'
    }
]

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IU Oral Assignment - 15-Minute Presentation Rehearsal Studio</title>
<style>
  :root {
    --iu-navy: #0F2240;
    --iu-accent: #D0382B;
    --iu-blue: #1E88E5;
    --iu-light: #F8FAFC;
    --iu-border: #E2E8F0;
    --text-dark: #1E293B;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: #0B1526;
    color: #F8FAFC;
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  header {
    background: var(--iu-navy);
    padding: 10px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(255,255,255,0.1);
  }
  .header-title h1 { font-size: 16px; font-weight: 700; color: #FFF; letter-spacing: 0.5px; }
  .header-title p { font-size: 12px; color: #94A3B8; }
  .timekeeper {
    display: flex;
    align-items: center;
    gap: 16px;
    background: rgba(0,0,0,0.3);
    padding: 6px 16px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.1);
  }
  .clock-display { font-family: monospace; font-size: 20px; font-weight: bold; color: #38BDF8; }
  .badge-pacing {
    font-size: 11px;
    font-weight: bold;
    padding: 4px 8px;
    border-radius: 4px;
    background: #10B981;
    color: #FFF;
  }
  main {
    flex: 1;
    display: flex;
    padding: 16px;
    gap: 16px;
    overflow: hidden;
  }
  .slide-stage {
    flex: 65;
    display: flex;
    flex-direction: column;
    background: #000;
    border-radius: 12px;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(255,255,255,0.1);
  }
  .slide-stage img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    background: #000;
  }
  .slide-overlay-info {
    position: absolute;
    top: 12px;
    left: 12px;
    background: rgba(15, 34, 64, 0.85);
    backdrop-filter: blur(4px);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
  }
  .teleprompter-pane {
    flex: 35;
    background: #1E293B;
    border-radius: 12px;
    border: 1px solid var(--iu-border);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .teleprompter-header {
    background: #0F172A;
    padding: 12px 16px;
    border-bottom: 1px solid #334155;
  }
  .teleprompter-header h2 { font-size: 14px; font-weight: 700; color: #38BDF8; margin-bottom: 4px; }
  .teleprompter-header .target-badge {
    font-size: 11px;
    color: #94A3B8;
  }
  .teleprompter-body {
    flex: 1;
    padding: 16px;
    overflow-y: auto;
    font-size: 15px;
    line-height: 1.6;
    color: #E2E8F0;
  }
  .teleprompter-body p { margin-bottom: 12px; }
  .qa-box {
    background: rgba(30, 136, 229, 0.1);
    border-left: 3px solid var(--iu-blue);
    padding: 10px 12px;
    border-radius: 4px;
    margin-top: 16px;
    font-size: 13px;
  }
  .qa-box strong { color: #60A5FA; display: block; margin-bottom: 4px; }
  footer {
    background: var(--iu-navy);
    padding: 12px 24px;
    border-top: 1px solid rgba(255,255,255,0.1);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .controls-left, .controls-center, .controls-right {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  button {
    background: #334155;
    border: none;
    color: #FFF;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 13px;
    font-weight: 600;
    transition: all 0.2s;
  }
  button:hover { background: #475569; }
  button.btn-primary { background: var(--iu-accent); }
  button.btn-primary:hover { background: #E04030; }
  .slide-counter { font-size: 13px; color: #94A3B8; font-weight: 600; }
  .auto-toggle {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    color: #94A3B8;
  }
  audio { display: none; }
</style>
</head>
<body>

<header>
  <div class="header-title">
    <h1>IU ORAL ASSIGNMENT: ACCELERATING DEEP NETWORK TRAINING VIA BATCH NORMALIZATION</h1>
    <p>Student: Raji Faruq Ishola (Matr. 4253139) | Course: DLBDSNNDL01-01 | Rehearsal Simulator</p>
  </div>
  <div class="timekeeper">
    <div>
      <span style="font-size: 11px; color: #94A3B8; display: block;">OVERALL ELAPSED</span>
      <span class="clock-display" id="totalClock">00:00 / 15:00</span>
    </div>
    <div class="badge-pacing" id="pacingBadge">PACING: ON TRACK</div>
  </div>
</header>

<main>
  <div class="slide-stage">
    <div class="slide-overlay-info" id="slideOverlay">Slide 1 of 15</div>
    <img id="slideImg" src="../slide_images/slide_1.png" alt="Slide Display">
  </div>
  
  <div class="teleprompter-pane">
    <div class="teleprompter-header">
      <h2 id="slideTitle">Slide 1: Title Slide (Welcome and Topic Introduction)</h2>
      <div class="target-badge" id="slideTarget">Target Time: 0:00 - 1:00 (1.0 min)</div>
    </div>
    <div class="teleprompter-body">
      <p id="scriptText"></p>
      <div class="qa-box">
        <strong>Examiner Potential Question & Model Answer:</strong>
        <p id="qaText"></p>
      </div>
    </div>
  </div>
</main>

<footer>
  <div class="controls-left">
    <button id="prevBtn" onclick="prevSlide()">&larr; Previous Slide</button>
    <button class="btn-primary" id="playBtn" onclick="togglePlay()">Play Narration</button>
    <button id="nextBtn" onclick="nextSlide()">Next Slide &rarr;</button>
    <span class="slide-counter" id="slideCounter">Slide 1 / 15</span>
  </div>
  
  <div class="controls-right">
    <label class="auto-toggle">
      <input type="checkbox" id="autoAdvance" checked> Auto-advance when speech ends
    </label>
    <button onclick="resetRehearsal()">Reset Timer</button>
  </div>
</footer>

<audio id="audioPlayer"></audio>

<script>
const slidesData = ''' + json.dumps(slides, indent=2) + ''';

let currentIndex = 0;
let isPlaying = false;
let elapsedSeconds = 0;
let timerInterval = null;

const audioPlayer = document.getElementById("audioPlayer");
const slideImg = document.getElementById("slideImg");
const slideOverlay = document.getElementById("slideOverlay");
const slideTitle = document.getElementById("slideTitle");
const slideTarget = document.getElementById("slideTarget");
const scriptText = document.getElementById("scriptText");
const qaText = document.getElementById("qaText");
const slideCounter = document.getElementById("slideCounter");
const playBtn = document.getElementById("playBtn");
const totalClock = document.getElementById("totalClock");
const pacingBadge = document.getElementById("pacingBadge");

function loadSlide(index) {
  currentIndex = index;
  const slide = slidesData[index];
  
  slideImg.src = slide.img;
  slideOverlay.textContent = `Slide ${slide.id} of ${slidesData.length}`;
  slideTitle.textContent = slide.title;
  slideTarget.textContent = `Target Window: ${slide.target_time} | Spoken Duration: ${slide.duration_sec}s`;
  scriptText.textContent = slide.script;
  qaText.textContent = slide.qa;
  slideCounter.textContent = `Slide ${slide.id} / ${slidesData.length}`;
  
  audioPlayer.src = slide.audio;
  if (isPlaying) {
    audioPlayer.play();
  }
}

function togglePlay() {
  if (isPlaying) {
    pauseNarration();
  } else {
    startNarration();
  }
}

function startNarration() {
  isPlaying = true;
  playBtn.textContent = "Pause Narration";
  playBtn.style.background = "#EAB308";
  audioPlayer.play();
  
  if (!timerInterval) {
    timerInterval = setInterval(() => {
      elapsedSeconds++;
      updateClock();
    }, 1000);
  }
}

function pauseNarration() {
  isPlaying = false;
  playBtn.textContent = "Resume Narration";
  playBtn.style.background = "#D0382B";
  audioPlayer.pause();
  clearInterval(timerInterval);
  timerInterval = null;
}

function nextSlide() {
  if (currentIndex < slidesData.length - 1) {
    loadSlide(currentIndex + 1);
  }
}

function prevSlide() {
  if (currentIndex > 0) {
    loadSlide(currentIndex - 1);
  }
}

function resetRehearsal() {
  pauseNarration();
  elapsedSeconds = 0;
  updateClock();
  loadSlide(0);
}

function updateClock() {
  const mins = Math.floor(elapsedSeconds / 60);
  const secs = elapsedSeconds % 60;
  const fmt = (mins < 10 ? "0" : "") + mins + ":" + (secs < 10 ? "0" : "") + secs;
  totalClock.textContent = fmt + " / 15:00";
  
  if (elapsedSeconds <= 900) {
    pacingBadge.textContent = "PACING: ON TRACK";
    pacingBadge.style.background = "#10B981";
  } else if (elapsedSeconds <= 960) {
    pacingBadge.textContent = "PACING: SLIGHTLY OVER (REFINING)";
    pacingBadge.style.background = "#F59E0B";
  } else {
    pacingBadge.textContent = "PACING: TIME LIMIT EXCEEDED";
    pacingBadge.style.background = "#EF4444";
  }
}

audioPlayer.addEventListener("ended", () => {
  const auto = document.getElementById("autoAdvance").checked;
  if (auto && currentIndex < slidesData.length - 1) {
    nextSlide();
  } else {
    pauseNarration();
  }
});

// Initialize first slide
loadSlide(0);
</script>

</body>
</html>
'''

out_html_solution = os.path.join(PRES_DIR, '20261103_Raji_FaruqIshola_4253139_DLBDSNNDL01_Rehearsal_Studio.html')
with open(out_html_solution, 'w', encoding='utf-8') as f:
    f.write(html_template)

out_html_submission = os.path.join(SUBMISSION_DIR, '20261103_Raji_FaruqIshola_4253139_DLBDSNNDL01_Rehearsal_Studio.html')
with open(out_html_submission, 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Successfully generated Rehearsal Studio HTML in solution and submission folders.')
