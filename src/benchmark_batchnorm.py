# Here I import the standard libraries I need for numerical math, deep learning, and plotting.
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

# Here I set a fixed random seed so that all my experimental results are reproducible.
torch.manual_seed(42)
np.random.seed(42)

# Here I define the file paths where my dataset is located and where I will save my figures.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'mnist_data.npz')
FIG_DIR = os.path.join(BASE_DIR, 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

# Here I load the MNIST dataset from my local pre-saved numpy file.
print('Loading dataset from local storage.')
raw_data = np.load(DATA_PATH)
X_train_raw = raw_data['X_train']
y_train_raw = raw_data['y_train']
X_test_raw = raw_data['X_test']
y_test_raw = raw_data['y_test']

# Here I take a representative subset of 10000 training images and 2000 test images for rapid, controlled benchmarking.
train_subset_size = 10000
test_subset_size = 2000

X_train = torch.tensor(X_train_raw[:train_subset_size], dtype=torch.float32).unsqueeze(1) / 255.0
y_train = torch.tensor(y_train_raw[:train_subset_size], dtype=torch.long)

X_test = torch.tensor(X_test_raw[:test_subset_size], dtype=torch.float32).unsqueeze(1) / 255.0
y_test = torch.tensor(y_test_raw[:test_subset_size], dtype=torch.long)

# Here I create PyTorch data loaders with a standard batch size of 64.
batch_size = 64
train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=batch_size, shuffle=True)
test_loader = DataLoader(TensorDataset(X_test, y_test), batch_size=batch_size, shuffle=False)

print(f'Train samples: {len(X_train)}, Test samples: {len(X_test)}')

# Here I define a modular Convolutional Neural Network architecture.
# I allow the normalization layer to be swapped between None, BatchNorm2d, LayerNorm, and GroupNorm.
class ModularCNN(nn.Module):
    def __init__(self, norm_type='none'):
        super(ModularCNN, self).__init__()
        self.norm_type = norm_type
        
        # Layer 1: Conv2d from 1 channel to 16 channels.
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        if norm_type == 'batch_norm':
            self.norm1 = nn.BatchNorm2d(16)
        elif norm_type == 'layer_norm':
            self.norm1 = nn.GroupNorm(1, 16) # LayerNorm over channels and spatial dimensions.
        elif norm_type == 'group_norm':
            self.norm1 = nn.GroupNorm(4, 16) # 4 groups of 4 channels.
        else:
            self.norm1 = nn.Identity()
            
        # Layer 2: Conv2d from 16 channels to 32 channels.
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        if norm_type == 'batch_norm':
            self.norm2 = nn.BatchNorm2d(32)
        elif norm_type == 'layer_norm':
            self.norm2 = nn.GroupNorm(1, 32)
        elif norm_type == 'group_norm':
            self.norm2 = nn.GroupNorm(4, 32)
        else:
            self.norm2 = nn.Identity()
            
        # Layer 3: Conv2d from 32 channels to 64 channels.
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        if norm_type == 'batch_norm':
            self.norm3 = nn.BatchNorm2d(64)
        elif norm_type == 'layer_norm':
            self.norm3 = nn.GroupNorm(1, 64)
        elif norm_type == 'group_norm':
            self.norm3 = nn.GroupNorm(4, 64)
        else:
            self.norm3 = nn.Identity()
            
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(2, 2)
        
        # After 3 pooling layers: 28 -> 14 -> 7 -> 3.
        self.fc = nn.Linear(64 * 3 * 3, 10)

    def forward(self, x):
        # Block 1
        x = self.conv1(x)
        x = self.norm1(x)
        x = self.relu(x)
        x = self.pool(x)
        
        # Block 2
        x = self.conv2(x)
        x = self.norm2(x)
        x = self.relu(x)
        x = self.pool(x)
        
        # Block 3
        x = self.conv3(x)
        x = self.norm3(x)
        x = self.relu(x)
        x = self.pool(x)
        
        # Flatten and classification
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# Here I write a training function that records training loss, test loss, test accuracy, and training duration per epoch.
def train_and_evaluate(norm_type, learning_rate=0.01, epochs=8):
    print(f'Starting experiment: Normalization = {norm_type}, LR = {learning_rate}')
    model = ModularCNN(norm_type=norm_type)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)
    
    train_losses = []
    test_losses = []
    test_accuracies = []
    epoch_times = []
    
    start_total_time = time.time()
    
    for epoch in range(epochs):
        epoch_start = time.time()
        model.train()
        running_loss = 0.0
        
        for batch_x, batch_y in train_loader:
            optimizer.zero_grad()
            outputs = model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * batch_x.size(0)
            
        epoch_loss = running_loss / len(train_loader.dataset)
        train_losses.append(epoch_loss)
        
        # Evaluation step
        model.eval()
        eval_loss = 0.0
        correct = 0
        with torch.no_grad():
            for batch_x, batch_y in test_loader:
                outputs = model(batch_x)
                loss = criterion(outputs, batch_y)
                eval_loss += loss.item() * batch_x.size(0)
                preds = outputs.argmax(dim=1)
                correct += (preds == batch_y).sum().item()
                
        test_loss = eval_loss / len(test_loader.dataset)
        test_acc = (correct / len(test_loader.dataset)) * 100.0
        
        test_losses.append(test_loss)
        test_accuracies.append(test_acc)
        epoch_time = time.time() - epoch_start
        epoch_times.append(epoch_time)
        
        print(f'  Epoch {epoch+1}/{epochs} - Train Loss: {epoch_loss:.4f} - Test Loss: {test_loss:.4f} - Test Acc: {test_acc:.2f}% ({epoch_time:.2f}s)')
        
    total_time = time.time() - start_total_time
    return {
        'norm_type': norm_type,
        'train_losses': train_losses,
        'test_losses': test_losses,
        'test_accuracies': test_accuracies,
        'total_time': total_time,
        'final_accuracy': test_accuracies[-1]
    }

# Here I run the benchmarks across the four configurations.
experiments = ['none', 'batch_norm', 'layer_norm', 'group_norm']
results = {}

for exp in experiments:
    results[exp] = train_and_evaluate(exp, learning_rate=0.02, epochs=8)

# Here I also test high learning rate stability (LR = 0.15) to demonstrate how Batch Normalization prevents divergence.
print('Testing high learning rate stability (LR = 0.15).')
res_high_lr_none = train_and_evaluate('none', learning_rate=0.15, epochs=6)
res_high_lr_bn = train_and_evaluate('batch_norm', learning_rate=0.15, epochs=6)

# Here I plot Figure 3: Empirical Training Acceleration and Comparison.
plt.figure(figsize=(15, 4.5), dpi=300)

# Subplot 1: Training Loss Convergence
plt.subplot(1, 3, 1)
colors = {'none': '#D9534F', 'batch_norm': '#0275D8', 'layer_norm': '#5CB85C', 'group_norm': '#F0AD4E'}
labels = {'none': 'No Normalization', 'batch_norm': 'Batch Normalization', 'layer_norm': 'Layer Normalization', 'group_norm': 'Group Normalization'}

for exp in experiments:
    plt.plot(range(1, 9), results[exp]['train_losses'], marker='o', linewidth=2, color=colors[exp], label=labels[exp])
plt.title('(A) Training Loss Convergence', fontsize=12, fontweight='bold')
plt.xlabel('Training Epochs', fontsize=10)
plt.ylabel('Cross-Entropy Loss', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=8)

# Subplot 2: Validation Accuracy Progression
plt.subplot(1, 3, 2)
for exp in experiments:
    plt.plot(range(1, 9), results[exp]['test_accuracies'], marker='s', linewidth=2, color=colors[exp], label=labels[exp])
plt.title('(B) Test Accuracy Progression (%)', fontsize=12, fontweight='bold')
plt.xlabel('Training Epochs', fontsize=10)
plt.ylabel('Test Accuracy (%)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=8)

# Subplot 3: High Learning Rate Stability (LR = 0.15)
plt.subplot(1, 3, 3)
plt.plot(range(1, 7), res_high_lr_none['train_losses'], marker='^', linewidth=2, color='#D9534F', label='No Norm (LR=0.15)')
plt.plot(range(1, 7), res_high_lr_bn['train_losses'], marker='v', linewidth=2, color='#0275D8', label='BatchNorm (LR=0.15)')
plt.title('(C) High Learning Rate Stability (LR=0.15)', fontsize=12, fontweight='bold')
plt.xlabel('Training Epochs', fontsize=10)
plt.ylabel('Cross-Entropy Loss', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=8)

plt.tight_layout()
fig3_path = os.path.join(FIG_DIR, 'figure3_empirical_training_acceleration.png')
plt.savefig(fig3_path, dpi=300)
plt.close()
print(f'Saved Figure 3 to: {fig3_path}')

# Here I plot Figure 4: Activation Statistics and Gradient Dynamics.
# I measure the internal activations of Conv3 before and after Batch Normalization.
m_none = ModularCNN('none')
m_bn = ModularCNN('batch_norm')

sample_x = X_train[:256]

# Extract Conv3 raw activations
with torch.no_grad():
    # Forward through block 1 and block 2 for m_none
    h1_none = m_none.pool(m_none.relu(m_none.conv1(sample_x)))
    h2_none = m_none.pool(m_none.relu(m_none.conv2(h1_none)))
    act_none = m_none.conv3(h2_none).flatten().numpy()
    
    # Forward for m_bn
    h1_bn = m_bn.pool(m_bn.relu(m_bn.norm1(m_bn.conv1(sample_x))))
    h2_bn = m_bn.pool(m_bn.relu(m_bn.norm2(m_bn.conv2(h1_bn))))
    act_bn = m_bn.norm3(m_bn.conv3(h2_bn)).flatten().numpy()

plt.figure(figsize=(12, 4.5), dpi=300)

plt.subplot(1, 2, 1)
plt.hist(act_none, bins=50, color='#D9534F', alpha=0.6, density=True, label=f'No Norm (Mean={np.mean(act_none):.2f}, Std={np.std(act_none):.2f})')
plt.title('(A) Deep Hidden Activation Distribution (No Norm)', fontsize=11, fontweight='bold')
plt.xlabel('Activation Value', fontsize=10)
plt.ylabel('Probability Density', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=8)

plt.subplot(1, 2, 2)
plt.hist(act_bn, bins=50, color='#0275D8', alpha=0.6, density=True, label=f'With BatchNorm (Mean={np.mean(act_bn):.2f}, Std={np.std(act_bn):.2f})')
plt.title('(B) Deep Hidden Activation Distribution (BatchNorm)', fontsize=11, fontweight='bold')
plt.xlabel('Activation Value', fontsize=10)
plt.ylabel('Probability Density', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=8)

plt.tight_layout()
fig4_path = os.path.join(FIG_DIR, 'figure4_gradient_stability_and_internal_distribution.png')
plt.savefig(fig4_path, dpi=300)
plt.close()
print(f'Saved Figure 4 to: {fig4_path}')

print('Benchmark and empirical plots finished successfully.')
