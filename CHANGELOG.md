# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-11-17

### 🎉 Major Modernization Release

This release represents a complete upgrade of the 4+ year old codebase to modern standards.

### Added

- ✨ **requirements.txt** - Comprehensive dependency management with latest versions
- ✨ **pyproject.toml** - Modern Python project configuration
- ✨ **config.yaml** - Centralized configuration management for all hyperparameters
- ✨ **UPGRADE_NOTES.md** - Detailed documentation of all changes and migration guide
- ✨ **test_upgrade.py** - Automated test suite to verify the upgrade
- ✨ **CHANGELOG.md** - This file
- ✨ **.gitignore** - Comprehensive gitignore for Python projects
- ✨ Type hints in a1_sim.py for better code quality
- ✨ Improved README with badges, better documentation, and usage examples

### Changed

- 🔄 **PyBullet**: Upgraded from ~2.x to `>=3.2.6`
  - Improved physics simulation stability
  - Better rendering performance
  - Enhanced collision detection

- 🔄 **gym → gymnasium**: Complete migration from deprecated gym to gymnasium
  - Updated `CustomGymEnv` to use gymnasium API
  - `reset()` now returns `(observation, info)` tuple
  - `step()` now returns `(obs, reward, terminated, truncated, info)` with separated done conditions
  - Updated metadata format to gymnasium standards
  - Improved render mode handling

- 🔄 **Stable-Baselines3**: Updated from ~1.5 to `>=2.4.0`
  - Full gymnasium compatibility
  - Improved PPO implementation
  - Better type hints and documentation
  - Enhanced callback system

- 🔄 **PyTorch**: Updated from ~1.x to `>=2.1.0`
  - Better performance on modern hardware
  - Improved memory efficiency
  - Enhanced distributed training support

- 🔄 **NumPy**: Updated to `>=1.24.0, <2.0.0`
  - Maintained backward compatibility
  - Performance improvements

- 🔄 **SciPy**: Updated to `>=1.11.0`
  - Better optimization algorithms
  - Improved interpolation methods

### Fixed

- 🐛 **a1_sim.py:114** - Fixed deprecated `collections.Sequence`
  - Changed from `collections.Sequence` to `collections.abc.Sequence`
  - Prevents DeprecationWarning in Python 3.9+

- 🐛 **exc_mpc.ipynb** - Updated all cells for gymnasium compatibility
  - Fixed environment reset/step API
  - Updated seeding mechanism
  - Improved render mode handling
  - Better error handling in training loop

- 🐛 **VideoRecorderCallback** - Updated for gymnasium compatibility
  - Fixed render method calls
  - Better screen capture handling
  - Null-safe video recording

### Removed

- ❌ **motion-imitation dependency** - Package is no longer maintained
  - Removed from requirements
  - MPC controller imports remain for compatibility

### Security

- 🔒 Updated all dependencies to latest versions with security patches
- 🔒 Added .gitignore to prevent accidental commits of model files and credentials

## [1.0.0] - ~2020

### Initial Release

- Initial implementation of MPC + RL hybrid control
- PyBullet simulation environment
- PPO training with Stable-Baselines3
- Google Colab support
- Basic trotting gait implementation

---

## Upgrade Path from v1.0 to v2.0

For users with existing v1.0 installations:

1. **Update Python** to 3.9 or higher if needed
2. **Backup your models** - Old models may need retraining
3. **Install new dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Update your code** following UPGRADE_NOTES.md
5. **Test** with `python test_upgrade.py`

### Breaking Changes

- **gym is no longer supported** - Must use gymnasium
- **Environment API changed** - reset() and step() have new signatures
- **Python 3.8 and below are not supported** - Minimum Python 3.9

### Deprecation Warnings

None - all deprecated code has been updated.

---

**For detailed migration instructions, see [UPGRADE_NOTES.md](UPGRADE_NOTES.md)**
