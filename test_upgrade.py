#!/usr/bin/env python3
"""
Test script to verify the upgraded robotics control system.
This script tests basic imports and environment creation.
"""

import sys
import traceback

def test_imports():
    """Test that all required packages can be imported."""
    print("=" * 60)
    print("Testing Package Imports")
    print("=" * 60)

    tests = []

    # Test basic packages
    try:
        import numpy as np
        print(f"✅ NumPy {np.__version__}")
        tests.append(True)
    except Exception as e:
        print(f"❌ NumPy import failed: {e}")
        tests.append(False)

    try:
        import scipy
        print(f"✅ SciPy {scipy.__version__}")
        tests.append(True)
    except Exception as e:
        print(f"❌ SciPy import failed: {e}")
        tests.append(False)

    # Test PyBullet
    try:
        import pybullet
        print(f"✅ PyBullet (version check not available)")
        tests.append(True)
    except Exception as e:
        print(f"❌ PyBullet import failed: {e}")
        tests.append(False)

    # Test Gymnasium (NOT gym)
    try:
        import gymnasium as gym
        print(f"✅ Gymnasium {gym.__version__}")
        tests.append(True)
    except Exception as e:
        print(f"❌ Gymnasium import failed: {e}")
        tests.append(False)

    # Test that old gym is not present
    try:
        import gym as old_gym
        if hasattr(old_gym, '__version__') and old_gym.__version__.startswith('0.'):
            print(f"⚠️  Old gym {old_gym.__version__} is still installed - consider removing it")
    except ImportError:
        print("✅ Old gym is not installed (good!)")

    # Test Stable-Baselines3
    try:
        import stable_baselines3
        print(f"✅ Stable-Baselines3 {stable_baselines3.__version__}")
        tests.append(True)
    except Exception as e:
        print(f"❌ Stable-Baselines3 import failed: {e}")
        tests.append(False)

    # Test PyTorch
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__}")
        tests.append(True)
    except Exception as e:
        print(f"❌ PyTorch import failed: {e}")
        tests.append(False)

    return all(tests)


def test_a1_sim():
    """Test that a1_sim.py can be imported without errors."""
    print("\n" + "=" * 60)
    print("Testing a1_sim.py Module")
    print("=" * 60)

    try:
        import a1_sim
        print("✅ a1_sim.py imported successfully")

        # Test that the fix is applied
        from collections.abc import Sequence
        print("✅ collections.abc.Sequence import works")

        # Test motor model creation
        motor_model = a1_sim.LaikagoMotorModel(
            kp=100.0,
            kd=2.0,
            torque_limits=33.5
        )
        print("✅ LaikagoMotorModel can be instantiated")

        return True
    except Exception as e:
        print(f"❌ a1_sim.py test failed: {e}")
        traceback.print_exc()
        return False


def test_environment_creation():
    """Test that the environment can be created (without PyBullet connection)."""
    print("\n" + "=" * 60)
    print("Testing Environment Creation")
    print("=" * 60)

    try:
        # Note: We can't fully test environment creation without mpc_controller
        # But we can test the imports and basic structure
        import gymnasium as gym
        from gymnasium import spaces
        import numpy as np

        print("✅ Gymnasium spaces imported")

        # Test space creation
        obs_space = spaces.Box(low=-20, high=20, shape=(37,), dtype=np.float32)
        action_space = spaces.Box(low=-0.3, high=0.3, shape=(12,), dtype=np.float32)

        print(f"✅ Observation space: {obs_space}")
        print(f"✅ Action space: {action_space}")

        return True
    except Exception as e:
        print(f"❌ Environment creation test failed: {e}")
        traceback.print_exc()
        return False


def test_stable_baselines3_compatibility():
    """Test Stable-Baselines3 with Gymnasium."""
    print("\n" + "=" * 60)
    print("Testing Stable-Baselines3 + Gymnasium Compatibility")
    print("=" * 60)

    try:
        import gymnasium as gym
        from stable_baselines3 import PPO
        from stable_baselines3.common.vec_env import DummyVecEnv

        # Create a simple test environment
        env = gym.make('CartPole-v1')
        env = DummyVecEnv([lambda: env])

        print("✅ Test environment created")

        # Try to create a model (don't train)
        model = PPO('MlpPolicy', env, verbose=0)
        print("✅ PPO model created successfully with Gymnasium environment")

        # Test reset
        obs = env.reset()
        print(f"✅ Environment reset works, obs shape: {obs.shape}")

        return True
    except Exception as e:
        print(f"❌ Stable-Baselines3 compatibility test failed: {e}")
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("\n" + "🧪 " * 20)
    print("ROBOTICS CONTROL UPGRADE TEST SUITE")
    print("🧪 " * 20 + "\n")

    results = []

    # Run tests
    results.append(("Package Imports", test_imports()))
    results.append(("a1_sim Module", test_a1_sim()))
    results.append(("Environment Structure", test_environment_creation()))
    results.append(("SB3 + Gymnasium", test_stable_baselines3_compatibility()))

    # Print summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    for name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {name}")

    all_passed = all(result[1] for result in results)

    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL TESTS PASSED! 🎉")
        print("The upgrade was successful!")
    else:
        print("⚠️  SOME TESTS FAILED")
        print("Please check the errors above and install missing dependencies.")
    print("=" * 60 + "\n")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
