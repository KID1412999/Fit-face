#二次曲面拟合/leastsq库的使用
###最小二乘法试验###
#error是自定义计算误差的函数，k,b也就是p0是计算初始化值，args是error其余的参数，该函数返回2个值，第一个是k,b的值
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
###采样点(Xi,Yi)###
Xi=np.random.randint(100,size=1000)
Yi=np.random.randint(100,size=1000)
noise=np.random.randint(20,size=1000)
Zi=3*Xi**2+4*Yi**2+1*Yi*Xi+5*Yi+4*Xi+1

###需要拟合的函数func及误差error###
def func(p,x,y):
	a,b,c,d,e,f=p
	return a*x**2+b*y**2+c*x*y+d*x+e*y+f

def error(p,x,y,z):
	return abs(p[0]*x**2+p[1]*y**2+p[2]*x*y+p[3]*x+p[4]*y+p[5]-z) #x、y都是列表，故返回值也是个列表

#TEST
p0=[1,1,1,1,1,1]
#print( error(p0,Xi,Yi) )

###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
Para=leastsq(error,p0,args=(Xi,Yi,Zi)) #把error函数中除了p以外的参数打包到args中
a,b,c,d,e,f=Para[0]
print('根据数据点，得到函数f(x,y)=ax^2+by^2+cxy+dx+ey+f的拟合系数依次为：')
print(Para[0])

###绘图，看拟合效果###



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(Xi, Yi, Zi, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
 
plt.show()
