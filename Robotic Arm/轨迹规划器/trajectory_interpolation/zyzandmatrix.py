import numpy as np

def euler_to_rotation_matrix(phi, theta, psi):
    """
    将 ZYZ 欧拉角转换为旋转矩阵

    参数:
    phi -- 绕 Z 轴旋转的角度
    theta -- 绕 Y 轴旋转的角度
    psi -- 绕 Z 轴旋转的角度

    返回:
    3x3 旋转矩阵
    """
    # 绕 Z 轴的旋转矩阵
    Rz_phi = np.array([
        [np.cos(phi), -np.sin(phi), 0],
        [np.sin(phi), np.cos(phi), 0],
        [0, 0, 1]
    ])
    
    # 绕 Y 轴的旋转矩阵
    Ry_theta = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    
    # 绕 Z 轴的旋转矩阵
    Rz_psi = np.array([
        [np.cos(psi), -np.sin(psi), 0],
        [np.sin(psi), np.cos(psi), 0],
        [0, 0, 1]
    ])
    
    # 计算旋转矩阵： R = Rz(phi) * Ry(theta) * Rz(psi)
    R = np.dot(Rz_phi, np.dot(Ry_theta, Rz_psi))
    
    return R

# 示例
phi = np.radians(15)  # 45度
theta = np.radians(0)  # 60度
psi = np.radians(35)  # 30度

rotation_matrix = euler_to_rotation_matrix(phi, theta, psi)

print("旋转矩阵：")
print(rotation_matrix)
