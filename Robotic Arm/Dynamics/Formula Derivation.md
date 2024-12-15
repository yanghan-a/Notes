# 机械臂动力学推导

该文档主要记录机械臂动力学推导过程，包括基本公式推导和牛顿-欧拉法推导。

## 基础公式推导

内容主要分为两块，第一部分是普通坐标系下公式的推导，第二部分是将公式应用到机械臂中建立的坐标系上。

### 速度和角速度相关

#### 普通坐标系下

考虑坐标系A，坐标系B以及坐标系C

角速度

$^A\Omega_C = {^A\Omega}_B + {^A_BR}^B\Omega_C$

线速度

$^AV_C = {^AV}_B + {^A\Omega_B\times{^A}P_B}+ {^A_B}R ^BV_C$

#### 机械臂坐标系下

角速度

$^{j}\omega_{j+1} = {^j\omega}_j + ^j_{j+1}R\dot{\theta}_{j+1}{^{j+1}\hat{Z}_{j+1}}$

$^{j+1}\omega_{j+1} = ^{j+1}_{j}R{^j\omega}_j + \dot{\theta}_{j+1}{^{j+1}\hat{Z}_{j+1}}$

线速度

$^{j}v_{j+1} = {^jv}_j + ^j\omega_{j}\times^jP_{j+1}$

$^{j+1}v_{j+1} = ^{j+1}_{j}R{^jv}_j + ^{j+1}_{j}R^j\omega_{j}\times^jP_{j+1}$

### 加速度和角加速度相关

首先考虑一些基本的结论，从$^AV_C = {^AV}_B + {^A\Omega_B\times{^A}P_B}+ {^A_B}R ^BV_C${1.2.1}出发，把C当成B中一点Q。这里**仅考虑${^AV}_B$ = 0**，非0情况有问题后面再解决。

上式可写成

$\frac{d}{dt}(^A_BR{^BQ}) = {^A\Omega_B\times^A_BR{^B}Q}+ {^A_B}R ^BV_Q$

这里我们会得到一个很重要的结论就是矩阵与向量乘积的微分$\frac{d}{dt}(^A_BR{^BQ})$可以写成${^AV}_B + {^A\Omega_B\times^A_BR{^B}Q}+ {^A_B}R ^BV_Q$的形式。

进而我们可以推出下面的结论

$\frac{d}{dt}(^A_BR{^BV_Q}) = {^A\Omega_B\times^A_BR{^B}V_Q}+ {^A_B}R ^B\dot{V}_Q$

$\frac{d}{dt}(^A_BR{^B\Omega_Q}) = {^A\Omega_B\times^A_BR{^B}\Omega_Q}+ {^A_B}R ^B\dot{\Omega}_Q$



#### 普通坐标系下

线加速度

对式1.2.1两边微分得到右式为

$^A\dot{V}_Q = \frac{d}{dt}(^A_BR{^BV_Q}) + {^A\dot\Omega_B\times^A_BR{^B}Q} + {^A\Omega_B\times\frac{d}{dt}(^A_BR{^BQ})}$ 

对两个微分项带入上面的式子并化简得

$^A\dot{V}_Q = {^A\Omega_B\times^A_BR{^B}V_Q}+ {^A_B}R ^B\dot{V}_Q + {^A\dot\Omega_B\times^A_BR{^B}Q} + {^A\Omega_B\times\frac{d}{dt}(^A_BR{^BQ})}$

$^A\dot{V}_Q = 2*{^A\Omega_B\times^A_BR{^B}V_Q}+ {^A_B}R ^B\dot{V}_Q + {^A\dot\Omega_B\times^A_BR{^B}Q} + {^A\Omega_B\times({^A\Omega_B\times^A_BR{^B}Q}})$

值得注意得是$^B\dot{V}_Q$ = 0，$^B{V}_Q$ =0，并且引入$^A\dot{V}_{BORG}$因此有

$^A\dot{V}_Q = ^A\dot{V}_{BORG} + {^A\dot\Omega_B\times^A_BR{^B}Q} + {^A\Omega_B\times({^A\Omega_B\times^A_BR{^B}Q}})$

角加速度

由$^A\Omega_C = {^A\Omega}_B + {^A_BR}^B\Omega_C$两边微分得

$^A\dot\Omega_C = {^A\dot\Omega}_B + \frac{d}{dt}({^A_BR}^B\Omega_C)$

再次带入上面得结论得

$^A\dot\Omega_C = {^A\dot\Omega}_B + {^A\Omega_B\times^A_BR{^B}\Omega_C}+ {^A_B}R ^B\dot{\Omega}_C$

#### 机械臂坐标系下

从普通坐标系转到机械臂坐标系下的一些想法，把A当成上一时刻j坐标系，B当成当前时刻j坐标系，C为j+1坐标系。那么我们有如下结论

线加速度

$^j\dot{v}_{j+1} = ^j\dot{v}_j + {^j\dot\omega_j\times^jP_{j+1}} + {^j\omega_j\times({^j\omega_j\times^jP_{j+1}}})$

$^{j+1}\dot{v}_{j+1} = ^{j+1}_jR(^j\dot{v}_j + {^j\dot\omega_j\times^jP_{j+1}} + {^j\omega_j\times({^j\omega_j\times^jP_{j+1}}}))$

将上式中的位置$^jP_{j+1}$更改为质心得位置可得

$^j\dot{v}_{C_j} = ^j\dot{v}_j + {^j\dot\omega_j\times^jP_{C_j}} + {^j\omega_j\times({^j\omega_j\times^jP_{C_j}}})$

角加速度

$^j\dot\omega_{j+1} = {^j\dot\omega}_j + {^j\omega_j\times\dot\theta_{j+1}{^{j+1}\hat Z_{j+1}}}+ ^{j}_{j+1}R\ddot\theta_{j+1}{^{j+1}\hat Z_{j+1}}$

$^{j+1}\dot\omega_{j+1} = ^{j+1}_jR{^j\dot\omega}_j + ^{j+1}_jR{^j\omega_j\times\dot\theta_{j+1}{^{j+1}\hat Z_{j+1}}}+ \ddot\theta_{j+1}{^{j+1}\hat Z_{j+1}}$

### 力矩平衡方程引入

#### 欧拉方程

##### 形式

参考：GPT

刚体力矩的欧拉方程

$I_1\dotω_1+(I_3−I_2)ω_2ω_3=M_1 $

$I_2\dotω_2+(I_1−I_3)ω_3ω_1=M_2$

$I_3\dotω_3+(I_2−I_1)ω_1ω_2=M_3$

写成一个方程就是

$I\dotω+ω×(Iω)=M$

$I$是一个对角矩阵 $I=diag(I_1,I_2,I_3)$

##### 理解

参考：[(16 封私信 / 81 条消息) 请教：刚体动力学中的欧拉方程是如何推导出来的？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/327324524/answers/updated)

该方程可以理解为在动系中力矩与惯性常量和角速度以及角加速度的关系。由于考虑了坐标系的变换，因此**惯性矩阵始终是一个常量**。

从一般出发，我们有力矩等于角动量的微分，即

$^ON_B = \frac{d}{dt}(^OI_B\cdot{^O\omega_B})$

按照链式法则求导有

$^ON_B = \frac{d}{dt}(^OI_B)\cdot{^O\omega_B} + ^OI_B\cdot\frac{d}{dt}({^O\omega_B})$

我们只需关心$\frac{d}{dt}(^OI_B)$，由科里奥利公式即

$\frac{d}{dt}(^AQ) = {^A\Omega_B\times{^A}Q}+ {^A_B}R \frac{d}{dt}(^BQ)$

因此有

$\frac{d}{dt}(^OI_B) = {^O_B}R\cdot\frac{d}{dt}(^BI_B) + ^O\omega_B\times^OI_B$

其中$\frac{d}{dt}(^BI_B) = 0$

因此$^ON_B = ^O\omega_B\times^OI_B\cdot{^O\omega_B} + ^OI_B\cdot{^O\dot\omega_B}$

### 牛顿-欧拉递推动力学方程

递推动力学方程主要涉及线速度、角速度关系，线加速度、角加速度关系，牛顿方程、欧拉方程，力平衡、力矩平衡。

#### 推导算法流程

算法分为两部分：外推和内推

外推涉及线速度、角速度关系，线加速度、角加速度关系，牛顿方程、欧拉方程。计算各个关节的速度、加速度和力

内推涉及利用外推得到的速度、加速度和力结合力平衡和力矩平衡得到关节力矩计算值。

#### 考虑重力因素

考虑重力只需要令$^o\dot v_0 = G$即可，这等价于机器人正以1g的加速度向上做加速度运动。

#### 实际例子

在Craig书中有一个两连杆质量分布集中的例子，见书189页

从该例子可以引出对动力学方程结构的讨论

##### 状态空间方程

动力学方程可以写成如下形式

$\tau = M(\Theta)\ddot \Theta +V(\Theta,\dot\Theta)+G(\Theta)$

$M(\Theta)$为nxn阶质量矩阵，对称且正定

$V(\Theta)$为nx1阶的离心力和哥氏力矢量，离心力矢量就是形如$\dot\Theta^2$的项，哥氏力矢量就是形如$\dot\Theta_i\dot\Theta_j(i\ne j)$的项

$G(\Theta)$为nx1阶重力矢量

##### 位形状态空间方程

将$V(\Theta,\dot\Theta )$拆分，动力学方程可以写成如下形式

$\tau = M(\Theta)\ddot \Theta +B(\Theta)(\dot\Theta\dot\Theta)+C(\Theta)(\dot\Theta^2)+G(\Theta)$

$B(\Theta)$是nxn(n-1)/2阶的哥氏力系数矩阵，$(\dot\Theta\dot\Theta)$是n(n-1)/2x1阶的关节速度积矢量

$C(\Theta)$是nxn阶离心力系数矩阵，$(\dot\Theta^2)$是nx1阶矢量

### 操作臂动力学的拉格朗日方程



