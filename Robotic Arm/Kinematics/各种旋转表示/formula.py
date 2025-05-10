import sympy as sp

# 定义符号
theta_x, theta_y, theta_z = sp.symbols('theta_x theta_y theta_z')

# 绕x轴旋转矩阵
R_x = sp.Matrix([
    [1, 0, 0],
    [0, sp.cos(theta_x), -sp.sin(theta_x)],
    [0, sp.sin(theta_x), sp.cos(theta_x)]
])

# 绕y轴旋转矩阵
R_y = sp.Matrix([
    [sp.cos(theta_y), 0, sp.sin(theta_y)],
    [0, 1, 0],
    [-sp.sin(theta_y), 0, sp.cos(theta_y)]
])

# 绕z轴旋转矩阵
R_z = sp.Matrix([
    [sp.cos(theta_z), -sp.sin(theta_z), 0],
    [sp.sin(theta_z), sp.cos(theta_z), 0],
    [0, 0, 1]
])

# 计算旋转矩阵的乘积
R_total = R_z* R_y * R_x

# 展示结果
# sp.pprint(R_total)

def quaternion_multiply_symbolic(q1, q2):
    """
    进行符号计算的四元数乘积，q1 和 q2 是四元数，表示为 (w, x, y, z)
    """
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    
    # 计算四元数乘积的各个分量
    w3 = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x3 = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y3 = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
    z3 = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
    
    return sp.Matrix([w3, x3, y3, z3])

# 示例：定义四元数的符号变量
theta_x, theta_y, theta_z = sp.symbols('theta_x theta_y theta_z')

q1 = sp.Matrix([sp.cos(theta_x/2), sp.sin(theta_x/2), 0, 0])  # 第一个四元数
q2 = sp.Matrix([sp.cos(theta_y/2), 0, sp.sin(theta_y/2), 0])  # 第二个四元数
q3 = sp.Matrix([sp.cos(theta_z/2), 0, 0, sp.sin(theta_z/2)])  # 第二个四元数

# 计算符号四元数乘积
q_product = quaternion_multiply_symbolic(q2, q1)
q_product = quaternion_multiply_symbolic(q3, q_product)

# 显示结果
sp.pprint(q_product)

# 真实数值代替符号变量
# 假设角度值为 30 度，45 度，60 度
substitutions = {
    theta_x: sp.pi/6,  # 30度
    theta_y: sp.pi/4,  # 45度
    theta_z: sp.pi/3   # 60度
}

# 使用 subs 方法替换符号变量为数值
q_product_numeric = q_product.subs(substitutions)

q_product_numeric_float = q_product_numeric.evalf()
# 显示数值结果
print("\n替换符号后的数值结果:")
sp.pprint(q_product_numeric_float)

def elller_to_quaternion_symbolic(roll, pitch, yaw):
    """
    将欧拉角转换为四元数表示
    """
    # 计算旋转矩阵
    # R = R_z.subs({theta_z: yaw}) * R_y.subs({theta_y: pitch}) * R_x.subs({theta_x: roll})
    
    # 从旋转矩阵中提取四元数
    # q = sp.Matrix([
    #     sp.sqrt(1 + R[0, 0] + R[1, 1] + R[2, 2]) / 2,
    #     (R[2, 1] - R[1, 2]) / (4 * sp.sqrt(1 + R[0, 0] + R[1, 1] + R[2, 2])),
    #     (R[0, 2] - R[2, 0]) / (4 * sp.sqrt(1 + R[0, 0] + R[1, 1] + R[2, 2])),
    #     (R[1, 0] - R[0, 1]) / (4 * sp.sqrt(1 + R[0, 0] + R[1, 1] + R[2, 2]))
    # ])
    # 另一种方法直接计算四元数，不使用旋转矩阵
    q = sp.Matrix([
        sp.cos(roll/2) * sp.cos(pitch/2) * sp.cos(yaw/2) + sp.sin(roll/2) * sp.sin(pitch/2) * sp.sin(yaw/2),
        sp.sin(roll/2) * sp.cos(pitch/2) * sp.cos(yaw/2) - sp.cos(roll/2) * sp.sin(pitch/2) * sp.sin(yaw/2),
        sp.cos(roll/2) * sp.sin(pitch/2) * sp.cos(yaw/2) + sp.sin(roll/2) * sp.cos(pitch/2) * sp.sin(yaw/2),
        sp.cos(roll/2) * sp.cos(pitch/2) * sp.sin(yaw/2) - sp.sin(roll/2) * sp.sin(pitch/2) * sp.cos(yaw/2)
    ])
    return q
def quaternion_to_euler_symbolic(q):
    """
    将四元数转换为欧拉角表示
    """
    w, x, y, z = q
    
    # 计算旋转矩阵
    # R = sp.Matrix([
    #     [1 - 2*y**2 - 2*z**2, 2*x*y - 2*z*w, 2*x*z + 2*y*w],
    #     [2*x*y + 2*z*w, 1 - 2*x**2 - 2*z**2, 2*y*z - 2*x*w],
    #     [2*x*z - 2*y*w, 2*y*z + 2*x*w, 1 - 2*x**2 - 2*y**2]
    # ])
    
    # 计算欧拉角，这里是XYZ固定角，ZYX欧拉角
    # roll = sp.atan2(R[2, 1], R[2, 2])
    # pitch = sp.asin(-R[2, 0])
    # yaw = sp.atan2(R[1, 0], R[0, 0])
    # 另一种方法直接计算欧拉角，不使用旋转矩阵
    roll = sp.atan2(2*(w*x + y*z), 1 - 2*(x**2 + y**2))
    pitch = sp.asin(2*(w*y - z*x))
    yaw = sp.atan2(2*(w*z + x*y), 1 - 2*(y**2 + z**2))
    return sp.Matrix([roll, pitch, yaw])