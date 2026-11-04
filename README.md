# Accelerating Deep Network Training via Batch Normalization

Oral Assignment Examination for Course **DLBDSNNDL01-01: Neural Nets and Deep Learning**  
IU International University of Applied Sciences  
Student: **Raji Faruq Ishola** (Matriculation Number: **4253139**)  
Date: November 03, 2026  

---

## 1. Project Overview

This repository contains the complete empirical code, visualizations, presentation slides, and spoken speech script for the Oral Assignment examination on Task 1: **Accelerating Deep Network Training via Batch Normalization**.

The project investigates:
1. The mathematical mechanics of gradient descent, backpropagation, and internal covariate shift in deep neural networks.
2. The formulation and implementation of Batch Normalization in fully connected and 2D convolutional architectures.
3. Quantitative empirical benchmarking measuring training loss reduction, validation accuracy progression, gradient stability, and high learning rate resilience.
4. Comparative analysis with competing normalization techniques from academic literature, including Layer Normalization and Group Normalization.

---

## 2. Directory Structure

`	ext
Oral Assignment - Batch Normalization/
├── data/
│   └── mnist_data.npz                  # Benchmark dataset
├── figures/
│   ├── figure1_training_challenges_and_internal_covariate_shift.png
│   ├── figure2_batchnorm_cnn_formulation.png
│   ├── figure3_empirical_training_acceleration.png
│   ├── figure4_gradient_stability_and_internal_distribution.png
│   └── figure5_normalization_taxonomy_comparison.png
├── presentation/
│   ├── 20261103_Raji_FaruqIshola_4253139_DLBDSNNDL01.pdf
│   └── 20261103_Raji_FaruqIshola_4253139_DLBDSNNDL01_Presentation.pptx
├── script/
│   ├── 20261103_Raji_FaruqIshola_4253139_DLBDSNNDL01_Speech_Script.docx
│   └── 20261103_Raji_FaruqIshola_4253139_DLBDSNNDL01_Speech_Script.pdf
├── src/
│   ├── benchmark_batchnorm.py          # PyTorch benchmarking pipeline
│   └── generate_conceptual_diagrams.py # Publication-quality figures generator
└── requirements.txt
`

---

## 3. How to Reproduce

### Step 1: Install Requirements
`ash
pip install torch torchvision numpy matplotlib python-pptx python-docx
`

### Step 2: Generate Conceptual Architecture Figures
`ash
python src/generate_conceptual_diagrams.py
`

### Step 3: Run Empirical Benchmark and Generate Acceleration Plots
`ash
python src/benchmark_batchnorm.py
`

---

## 4. Academic References

- Ba, J. L., Kiros, J. R., & Hinton, G. E. (2016). Layer normalization. *arXiv preprint arXiv:1607.06450*.
- Balestriero, R., & Baraniuk, R. G. (2022). Batch normalization explained. *arXiv preprint arXiv:2209.14778*.
- He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 770-778).
- Ioffe, S., & Szegedy, C. (2015). Batch normalization: Accelerating deep network training by reducing internal covariate shift. In *International Conference on Machine Learning (ICML)* (pp. 448-456). PMLR.
- Salimans, T., & Kingma, D. P. (2016). Weight normalization: A simple reparameterization to accelerate training of deep neural networks. *Advances in Neural Information Processing Systems (NeurIPS)*, 29.
- Santurkar, S., Tsipras, D., Ilyas, A., & Madry, A. (2018). How does batch normalization help optimization? *Advances in Neural Information Processing Systems (NeurIPS)*, 31.
- Wu, Y., & He, K. (2018). Group normalization. In *Proceedings of the European Conference on Computer Vision (ECCV)* (pp. 3-19).

