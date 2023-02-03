#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import *
def angle_from_coordinates(a,b):
    angle = atan2(b[1]-a[1],b[0]-a[0])
    # print("angle rad: {}".format(angle))
    # print("angle deg: {}".format(degrees(angle)))
    return angle

# Create an array
# a1 = [0.777,-1.088]
# b1 = [1.8,6.06]

a1 = [0.865,-0.891]
b1 = [1.805,6.330]

a2= [ -0.242 ,-2.188]
b2 = [ 1.477 , 4.606]

a3 = [ 1.491,  -0.493 ]
b3 =  [2.250  , 6.943]

# a4 = [ 2.262 ,  3.402    ]
# b4 = [ 3.67769165 ,  0.3435749 ]
a4 = [ -0.403 , -3.499   ]
b4 = [ 1.893 , 3.391]

a5 = [-0.621 , -4.779]
b5 = [ 2.266 , 2.222]

X = [a1,a2,a3,a4,a5]
Y = [b1,b2,b3,b4,b5]
theta_list = []
x_offset_list = []
y_offset_list = []
k = 0
for i in range(1,len(X)):
    for j in range(i):
        if i!=j:
            theta1 = angle_from_coordinates(X[j],X[i])
            theta2 = angle_from_coordinates(Y[j],Y[i])
            theta = degrees(theta1 - theta2)
            theta_list.append(float(format(theta,".2f")))
            k +=1
            print("theta from point {} to {} is deg: {}".format(j+1,i+1,theta))
print(theta_list)
theta_ave = np.average(theta_list)

# array1 = np.asarray(a)
# print(array1)

R_a_b = [  [cos(radians(theta_ave)),  -sin(radians(theta_ave))],
                    [sin(radians(theta_ave)), cos(radians(theta_ave))]]

print(R_a_b)
I_R_a_b = np.asmatrix(np.linalg.inv(R_a_b))
# print(I_R_a_b)
for jj in range(len(X)):

    A_x = np.asmatrix(X[jj]).reshape((2,1))
    B_x = np.asmatrix(Y[jj]).reshape((2,1))
    # print(A_x)
    C = R_a_b * B_x
    # print(C)
    D = A_x - C
    # print(D)
    x_offset_list.append(float(format(float(D[0][0]),".4f")))
    y_offset_list.append(float(format(float(D[1][0]),".4f")))
print(x_offset_list)
print(y_offset_list)
print("average: ")
print(format(radians(theta_ave),".5f"))
print(np.average(x_offset_list))
print(np.average(y_offset_list))
