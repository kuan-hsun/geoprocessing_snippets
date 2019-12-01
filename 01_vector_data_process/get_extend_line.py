import matplotlib.pyplot as plt
import cmath, math 
import numpy as np

# 原始線段
x1, y1 = 4.0, 8.0
x2, y2 = 10.0, 15.0
line_x, line_y = [x1, x2], [y1, y2]


# 計算斜率
m = float(y2-y1)/float(x2-x1)
print 'm: ',m


# 計算角度
angle_rad = np.arctan(m)
angle_deg = np.rad2deg(angle_rad)
print 'angle_rad: ', angle_rad
print 'angle_deg: ', angle_deg


# 指定延伸長度
d = 20

# 計算延伸線(x2, y2) > (x3, y3) -- 延伸10個單位長
x3 = x2 + (d * math.cos(angle_rad))
y3 = y2 + (d * math.sin(angle_rad))
print 'x3: ',x3
print 'y3: ',y3


# 計算延伸線(x1, y1) > (x4, y4) -- 延伸10個單位長
x4 = x1 - (d * math.cos(angle_rad))
y4 = y1 - (d * math.sin(angle_rad))
print 'x4: ',x4
print 'y4: ',y4



# 檢驗線段長度是否為d
print 'check_d1 = ', cmath.sqrt((x3-x2)**2 + (y3-y2)**2)
print 'check_d2 = ', cmath.sqrt((x4-x1)**2 + (y4-y1)**2)

# 延伸線段 (x1, y1) -> (x3, y3)
lined1_x, lined1_y = [x3, x2], [y3, y2]
lined2_x, lined2_y = [x4, x1], [y4, y1]

plt.plot(line_x, line_y, marker = 'o') # 原線段
plt.plot(lined1_x, lined1_y, marker = 'o') # 延伸線段1
plt.plot(lined2_x, lined2_y, marker = 'o') # 延伸線段2
plt.grid(True)
plt.axis('equal')
plt.show()
