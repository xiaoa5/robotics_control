# robotics_control
robotics with mpc wbc and rl

code can be excuted in colab


in this repo, i try to make a simple example to combine the conventional model predictive control (mpc) with reinforcement learning (rl) to control the quadrupedal.
mpc is just an optimization, to find the optimal solution with various constraints, includes dynamic function of the sysytem (physical model) and others (fictions, motor, etc.).
rl is also an optimization, but required few mathmatics and physics as mpc, rl is mainly data driven, the parameter of the rl trained with trail and error.

combine mpc and rl, i hope:

1 rl works as a residium of the mpc control.

2 rl helps mpc control in extrem senarios (high speed starting).

3 rl improves gaits, maybe looks more naturely.

4 rl improves energy effiency.

details:

Base State (estimated) --------->.............................swing leg control (desired foot position)....-----> inversed kinematics 

Desired State (forward speed) -->swing or stance -->..........................................................................----> motor torgue  

trotting Gait (fixed) ---------->.............................stance leg control (desired foot force)......-----> jacobian





simulation enviroment: pybullet 

ref: https://github.com/erwincoumans/motion_imitation  https://github.com/erwincoumans/bullet3/tree/master/examples/pybullet/gym/pybullet_envs
