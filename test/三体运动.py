import numpy as np
from matplotlib import pyplot as plt 
import time

#三个星球的初始化
G=1 #万有引力常数
t=1 #步长
m1=10000 #星球一的质量
m2=10000
m3=10000
#位置初始化
x1=0
y1=3
x2=3/2*np.sqrt(3)
y2=-3/2
x3=-3/2*np.sqrt(3)
y3=-3/2
#速度初始化
v1_x=v1_y=0.1
v2_x=v2_y=0.2
v3_x=v3_y=0.3
x1_all=[]
y1_all=[]
x2_all=[]
y2_all=[]
x3_all=[]
y3_all=[]

plt.ion()
plt.figure(1)
for i in range(5000):  # while True:  # 无限循环用这个
    distance12 = np.sqrt((x1-x2)**2+(y1-y2)**2)   # 物体1和物体2之间的距离
    distance13 = np.sqrt((x1-x3)**2+(y1-y3)**2)   # 物体1和物体3之间的距离
    distance23 = np.sqrt((x2-x3)**2+(y2-y3)**2)   # 物体2和物体3之间的距离
    # 对物体1的计算
    a1_2 = G*m2/distance12**2  # 物体2对物体1的加速度（用上万有引力公式）
    a1_3 = G*m3/distance13**2  # 物体3对物体1的加速度
    a1_x = a1_2*(x2-x1)/distance12 + a1_3*(x3-x1)/distance13  # 物体1受到的水平加速度
    a1_y = a1_2*(y2-y1)/distance12 + a1_3*(y3-y1)/distance13  # 物体1受到的垂直加速度
    v1_x = v1_x + a1_x*t  # 物体1的速度
    v1_y = v1_y + a1_y*t  # 物体1的速度
    x1 = x1 + v1_x*t  # 物体1的水平位置
    y1 = y1 + v1_y*t  # 物体1的垂直位置
    x1_all = np.append(x1_all, x1)  # 记录轨迹
    y1_all = np.append(y1_all, y1)  # 记录轨迹
    # 对物体2的计算
    a2_1 = G*m1/distance12
    a2_3 = G*m3/distance23
    a2_x = a2_1*(x1-x2)/distance12 + a2_3*(x3-x2)/distance23
    a2_y = a2_1*(y1-y2)/distance12 + a2_3*(y3-y2)/distance23
    v2_x = v2_x + a2_x*t
    v2_y = v2_y + a2_y*t
    x2 = x2 + v2_x*t
    y2 = y2 + v2_y*t
    x2_all = np.append(x2_all, x2)
    y2_all = np.append(y2_all, y2)
    # 对物体3的计算
    a3_1 = G*m1/distance13
    a3_2 = G*m2/distance23
    a3_x = a3_1*(x1-x3)/distance13 + a3_2*(x2-x3)/distance23
    a3_y = a3_1*(y1-y3)/distance13 + a3_2*(y2-y3)/distance23
    v3_x = v3_x + a3_x*t
    v3_y = v3_y + a3_y*t
    x3 = x3 + v3_x*t
    y3 = y3 + v3_y*t
    x3_all = np.append(x3_all, x3)
    y3_all = np.append(y3_all, y3)
 
    plt.clf()
    plt.plot(x1, y1, 'og', markersize=m1)  # 默认密度相同，质量越大的，画出来的面积越大
    plt.plot(x2, y2, 'or', markersize=m2)    
    plt.plot(x3, y3, 'ob', markersize=m3)
    plt.plot(x1_all, y1_all, '-g')  # 画轨迹
    plt.plot(x2_all, y2_all, '-r')
    plt.plot(x3_all, y3_all, '-b')    
    plt.draw()
    time.sleep(0.01)
    plt.show()
#plt.show()
