import numpy as np
import math
# 定义旋转矩阵从欧拉角到旋转矩阵的转换
def euler_to_rotation_matrix(roll, pitch, yaw):
    # Roll - 绕X轴旋转角度
    # Pitch - 绕Y轴旋转角度
    # Yaw - 绕Z轴旋转角度
    roll = np.radians(roll)
    pitch = np.radians(pitch)
    yaw = np.radians(yaw)
    # 计算旋转矩阵
    R_x = np.array([[1, 0, 0],
                    [0, np.cos(roll), -np.sin(roll)],
                    [0, np.sin(roll), np.cos(roll)]])
    
    R_y = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                    [0, 1, 0],
                    [-np.sin(pitch), 0, np.cos(pitch)]])
    
    R_z = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                    [np.sin(yaw), np.cos(yaw), 0],
                    [0, 0, 1]])

    # 综合旋转矩阵
    R = R_z @ R_y @ R_x
    return R

# 定义旋转矩阵到欧拉角的转换
def rotation_matrix_to_euler(R):
    if np.isclose(R[2, 0], 1):
        # Gimbal lock condition (pitch = ±90 degrees)
        pitch = np.pi / 2
        roll = 0
        yaw = np.arctan2(R[0, 1], R[0, 2])
    elif np.isclose(R[2, 0], -1):
        pitch = -np.pi / 2
        roll = 0
        yaw = np.arctan2(-R[0, 1], -R[0, 2])
    else:
        pitch = -np.arcsin(R[2, 0])
        roll = np.arctan2(R[2, 1] / np.cos(pitch), R[2, 2] / np.cos(pitch))
        yaw = np.arctan2(R[1, 0] / np.cos(pitch), R[0, 0] / np.cos(pitch))

    return roll, pitch, yaw

# 欧拉角 (roll, pitch, yaw) 转 四元数 (q_w, q_x, q_y, q_z)
def euler_to_quaternion_degrees(roll_deg, pitch_deg, yaw_deg):
    # 将角度转为弧度
    roll = math.radians(roll_deg)
    pitch = math.radians(pitch_deg)
    yaw = math.radians(yaw_deg)
    
    # 计算四元数
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    q_w = cr * cp * cy + sr * sp * sy
    q_x = sr * cp * cy - cr * sp * sy
    q_y = cr * sp * cy + sr * cp * sy
    q_z = cr * cp * sy - sr * sp * cy

    return [q_w, q_x, q_y, q_z]

# 四元数 (q_w, q_x, q_y, q_z) 转 欧拉角 (roll, pitch, yaw)
def quaternion_to_euler(q):
    q_w, q_x, q_y, q_z = q

    # 计算欧拉角
    roll = math.atan2(2 * (q_w * q_x + q_y * q_z), 1 - 2 * (q_x**2 + q_y**2))
    pitch = math.asin(2 * (q_w * q_y - q_z * q_x))
    yaw = math.atan2(2 * (q_w * q_z + q_x * q_y), 1 - 2 * (q_y**2 + q_z**2))

    roll = math.degrees(roll)
    pitch = math.degrees(pitch)
    yaw = math.degrees(yaw)
    return [roll, pitch, yaw]

# 测试示例
if __name__ == "__main__":
    # 示例欧拉角
    # roll = np.radians(0)  # 绕X轴旋转30度
    # pitch = np.radians(135)  # 绕Y轴旋转45度
    # yaw = np.radians(0)  # 绕Z轴旋转60度

    # # 从欧拉角生成旋转矩阵
    # R = euler_to_rotation_matrix(roll, pitch, yaw)
    # print("旋转矩阵：")
    # print(R)

    # # 从旋转矩阵恢复欧拉角
    # roll_, pitch_, yaw_ = rotation_matrix_to_euler(R)
    # print("\n恢复的欧拉角（弧度）：")
    # print(f"roll: {roll_}, pitch: {pitch_}, yaw: {yaw_}")
    # print("\n恢复的欧拉角（度）：")
    # print(f"roll: {np.degrees(roll_)}, pitch: {np.degrees(pitch_)}, yaw: {np.degrees(yaw_)}")
    q = euler_to_quaternion_degrees(-120, 90, 0)
    print(q)
    
    q = euler_to_quaternion_degrees(180, 90, 0)
    print(q)
    
    q = [0.7071,0.5,0,-0.5]
    e = quaternion_to_euler(q)
    print(e)

    m = euler_to_rotation_matrix(0,-60,0)
    print(m)
    m = euler_to_rotation_matrix(180,60,180)
    print(m)