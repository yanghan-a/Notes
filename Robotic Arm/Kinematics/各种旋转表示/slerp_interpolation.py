import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

# 将欧拉角转换为四元数
def euler_to_quaternion(roll, pitch, yaw):
    r = R.from_euler('xyz', [roll, pitch, yaw], degrees=True)
    # print(r.as_quat())
    
    # r0 = R.from_quat(r.as_quat())
    # print(r0.as_euler('xyz', degrees=True))
    
    return r.as_quat()

# 计算两个四元数之间的SLERP插值
def slerp(q0, q1, t):
    # 转换为scipy的旋转对象
    r0 = R.from_quat(q0)
    r1 = R.from_quat(q1)

    # 计算夹角
    if np.dot(r0.as_quat(), r1.as_quat()) < 0:
        r1 = -r1
    
    dot_product = np.clip(np.dot(r0.as_quat(), r1.as_quat()), -1.0, 1.0)
    omega = np.arccos(dot_product)

    # 特殊情况：如果夹角为0，返回 q0 或 q1
    if omega == 0:
        return q0

    # 计算插值的四元数
    sin_omega = np.sin(omega)
    q_interpolated = (
        np.sin((1 - t) * omega) / sin_omega * r0.as_quat() +
        np.sin(t * omega) / sin_omega * r1.as_quat()
    )

    return q_interpolated

# 可视化函数
def plot_interpolated_poses(q0, q1, num_steps=10):
    t_vals = np.linspace(0, 1, num_steps)  # 从0到1的插值
    interpolated_quats = [slerp(q0, q1, t) for t in t_vals]
    
    # 转换四元数为欧拉角
    interpolated_eulers = [R.from_quat(q).as_euler('xyz', degrees=True) for q in interpolated_quats]
    
    # 可视化
    fig, ax = plt.subplots(3, 1, figsize=(10, 12))

    # 绘制每个欧拉角的插值轨迹
    ax[0].plot(t_vals, [e[0] for e in interpolated_eulers], label="Roll")
    ax[1].plot(t_vals, [e[1] for e in interpolated_eulers], label="Pitch")
    ax[2].plot(t_vals, [e[2] for e in interpolated_eulers], label="Yaw")

    for a in ax:
        a.set_xlabel('Interpolation Factor t')
        a.set_ylabel('Angle (degrees)')
        a.legend()

    plt.tight_layout()
    plt.show()

# 示例：给定两个欧拉角姿态（roll, pitch, yaw）
euler_angles_1 = [30, 45, 60]  # 姿态 1
euler_angles_2 = [60, 90, 120]  # 姿态 2

# 转换为四元数
q1 = euler_to_quaternion(*euler_angles_1)
q2 = euler_to_quaternion(*euler_angles_2)

# 可视化插值结果
plot_interpolated_poses(q1, q2, num_steps=50)
