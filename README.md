# 🤖 Robotics Control: MPC + Reinforcement Learning

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyBullet](https://img.shields.io/badge/PyBullet-3.2.6+-green.svg)](https://pybullet.org/)
[![Gymnasium](https://img.shields.io/badge/Gymnasium-0.29.1+-orange.svg)](https://gymnasium.farama.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Version 2.0** - Fully modernized for 2025 with latest dependencies

A hybrid control system combining **Model Predictive Control (MPC)** with **Reinforcement Learning (PPO)** for quadrupedal robot locomotion.

## 🎯 Project Overview

This project demonstrates how to combine conventional model predictive control with reinforcement learning to control a quadrupedal robot (A1/Laikago) in PyBullet simulation.

### Key Concepts

**MPC (Model Predictive Control)**:
- Optimization-based control with constraints
- Uses physical models and system dynamics
- Handles friction, motor limits, etc.

**RL (Reinforcement Learning)**:
- Data-driven optimization
- Learns through trial and error
- Requires less mathematical modeling

### Goals of Combining MPC + RL

1. **RL as residual controller** - Compensates for MPC errors
2. **Extreme scenarios handling** - Helps with high-speed starts and difficult maneuvers
3. **Gait improvement** - Makes locomotion more natural
4. **Energy efficiency** - Optimizes power consumption

## 🏗️ Architecture

```
Base State (estimated) ────────►  Swing Leg Control  ──► Inverse Kinematics ──┐
                                   (foot position)                             │
Desired State          ┌────────► Stance Leg Control ──► Jacobian Transform ──┼──► Motor Torque
(forward speed)        │           (foot force)                                │
                       │                                                        │
Trotting Gait (fixed) ─┘           + RL Residual ───────────────────────────►─┘
```

## 🆕 What's New in v2.0

This version represents a **complete modernization** of the 4+ year old codebase:

### Major Updates

- ✅ **PyBullet** upgraded to `3.2.6+` (latest stable)
- ✅ **gym → gymnasium** migration (gym is deprecated)
- ✅ **Stable-Baselines3** updated to `2.4.0+`
- ✅ **PyTorch** updated to `2.1.0+`
- ✅ Fixed deprecated `collections.Sequence` → `collections.abc.Sequence`
- ✅ Updated all APIs to latest standards
- ✅ Added type hints and modern Python practices
- ✅ Improved code organization and documentation
- ✅ Added configuration management (YAML)
- ✅ Better error handling and logging

See [UPGRADE_NOTES.md](UPGRADE_NOTES.md) for detailed migration information.

## 📦 Installation

### Prerequisites

- Python 3.9 or higher
- pip or conda
- (Optional) CUDA for GPU acceleration

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/robotics_control.git
cd robotics_control

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Or use pyproject.toml
pip install -e .
```

### Google Colab

The project is designed to work seamlessly in Google Colab:

1. Upload `exc_mpc.ipynb` to Colab
2. Run the first cell to install dependencies
3. Mount your Google Drive for model storage
4. Run training cells

## 🚀 Usage

### Training a New Model

```python
# In Jupyter notebook or Colab
from stable_baselines3 import PPO
import gymnasium as gym

# Create environment
env = CustomGymEnv()

# Create PPO model
model = PPO('MlpPolicy', env, verbose=1)

# Train
model.learn(total_timesteps=1000000)

# Save
model.save("my_quadruped_model")
```

### Loading and Testing

```python
# Load trained model
model = PPO.load("my_quadruped_model")

# Test
obs, info = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()
```

### Configuration

Edit `config.yaml` to customize:
- Robot parameters (mass, inertia, dimensions)
- Training hyperparameters
- Reward function weights
- Callback settings

## 📁 Project Structure

```
robotics_control/
├── a1_sim.py              # Robot model and motor control
├── exc_mpc.ipynb          # Main training notebook
├── config.yaml            # Configuration file
├── requirements.txt       # Dependencies
├── pyproject.toml         # Modern Python project config
├── UPGRADE_NOTES.md       # Detailed upgrade documentation
├── README.md              # This file
├── .gitignore            # Git ignore rules
│
├── best_model414a.zip    # Pretrained model (old version)
├── mpc_ppo0410.zip       # Pretrained model (old version)
│
└── mpc_controller/       # MPC implementation (external)
    ├── com_velocity_estimator.py
    ├── gait_generator.py
    ├── locomotion_controller.py
    ├── openloop_gait_generator.py
    ├── raibert_swing_leg_controller.py
    └── torque_stance_leg_controller.py
```

## 🎮 Control Flow

1. **MPC Controller** generates base actions for swing and stance legs
2. **RL Policy** (PPO) learns residual corrections
3. **Combined action** sent to robot motors via hybrid control
4. **Reward** based on:
   - Forward velocity tracking
   - Stability (orientation)
   - Energy efficiency (action penalties)
   - Not falling

## 📊 Training

Default training configuration:
- **Algorithm**: PPO (Proximal Policy Optimization)
- **Total timesteps**: 6,000,000
- **Parallel environments**: 4
- **Network architecture**: [256, 256] for both policy and value networks
- **Observation space**: 37-dimensional (joint states, velocities, orientation, etc.)
- **Action space**: 12-dimensional (motor position/torque adjustments)

Training progress can be monitored with TensorBoard:
```bash
tensorboard --logdir ./logs/tensorboard/
```

## 🔧 Troubleshooting

### Common Issues

**1. Import errors with gym**
```
ModuleNotFoundError: No module named 'gym'
```
**Solution**: This is expected! We now use `gymnasium`. Make sure you installed the latest requirements.

**2. Stable-Baselines3 compatibility**
```
AttributeError: 'DummyVecEnv' object has no attribute...
```
**Solution**: Ensure you have `stable-baselines3>=2.4.0` installed.

**3. PyBullet rendering issues**
```
Error: GLX initialization failed
```
**Solution**: In headless environments (servers, Colab), use `render_mode=None` or `"rgb_array"`.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- [ ] Add more terrain types (stairs, slopes, obstacles)
- [ ] Implement domain randomization
- [ ] Add sim-to-real transfer capabilities
- [ ] Support for other quadruped models
- [ ] Better visualization and analysis tools
- [ ] Wandb integration for experiment tracking

## 📚 References

- [Motion Imitation](https://github.com/erwincoumans/motion_imitation)
- [PyBullet Examples](https://github.com/bulletphysics/bullet3/tree/master/examples/pybullet)
- [Stable-Baselines3](https://stable-baselines3.readthedocs.io/)
- [Gymnasium Documentation](https://gymnasium.farama.org/)

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Original MPC implementation based on motion_imitation
- PyBullet physics simulation
- Stable-Baselines3 RL algorithms

## 📧 Contact

For questions or issues, please open a GitHub issue or contact the maintainers.

---

**Status**: ✅ Fully upgraded and tested for 2025

**Last Updated**: 2025-11-17
