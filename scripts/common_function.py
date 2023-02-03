#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from cProfile import label
import os
from random import random
import sys
import numpy as np
import matplotlib.pyplot as plt

class TestFunction():

    code_only = False
    def pose_filter(self,pose_fiterred, new_pose, cnt):
        """[summary]

        Args:
            pose_fiterred (PoseStamped): pose fiterred
            new_pose (PoseStamped): new pose
            cnt (int): number of pose fiterred

        Returns:
            (pose_filtered, cnt)
        """
        if self.code_only:
            pose_fiterred = float()
            new_pose = float()
        pose_fiterred = (pose_fiterred* cnt + new_pose)/(cnt + 1)
        return pose_fiterred, cnt+1

class KalmanFilter(object):
    def __init__(self, F = None, B = None, H = None, Q = None, R = None, P = None, x0 = None):
        """
        F: state transition matrix
        B: control matrix
        H: observation matrix
        Q: covariance of the process noise matrix
        R: covariance of the observation noise
        P: covariance matrix of estimate
        x0: init value
        """

        if(F is None or H is None):
            raise ValueError("Set proper system dynamics.")

        self.n = F.shape[1]
        self.m = H.shape[1]

        self.F = F
        self.H = H
        self.B = 0 if B is None else B
        self.Q = np.eye(self.n) if Q is None else Q
        self.R = np.eye(self.n) if R is None else R
        self.P = np.eye(self.n) if P is None else P
        self.x = np.zeros((self.n, 1)) if x0 is None else x0

    def predict(self, u = 0):
        """
        x(k|k-1) = F*x(k-1) + B*u(k)
        P(k|k-1) = F*P(k-1)*F_T + Q
        """
        self.x = np.dot(self.F, self.x) + np.dot(self.B, u)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
        # print("\nMatrix P : \n", self.P)
        return self.x

    def update(self, z):
        """
        z(k) = H*x(k) + v(k)
        R = E[v(k)*v(k)_T] = [sigma(z)^2]
        """
        y = z - np.dot(self.H, self.x)
        S = self.R + np.dot(self.H, np.dot(self.P, self.H.T))
        # print("\nMatrix S : \n", S)
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        # print("\nMatrix K : \n", K)
        self.x = self.x + np.dot(K, y)
        I = np.eye(self.n)
        self.P = np.dot(np.dot(I - np.dot(K, self.H), self.P),
        	(I - np.dot(K, self.H)).T) + np.dot(np.dot(K, self.R), K.T)
        return self.x

class KalmanFilterSimple(object):
    _current_estimate = float()
    _last_estimate = float()
    _kalman_gain = float()
    def __init__(self,  mea_e,  est_e,  q):
        """
        e_mea: Độ không chắc chắn của phép đo.
        e_est: Độ không chắc chắn của ước tính
        q    : Phương sai quá trình
        """
        self._err_measure = mea_e
        self._err_estimate = est_e
        self._q = q

    def updateEstimate(self, mea):
        self._kalman_gain = self._err_estimate/(self._err_estimate + self._err_measure)
        self._current_estimate = self._last_estimate + self._kalman_gain * (mea - self._last_estimate)
        self._err_estimate =  (1.0 - self._kalman_gain)*self._err_estimate + abs(self._last_estimate-self._current_estimate)*self._q
        self._last_estimate= self._current_estimate

        return self._current_estimate


if __name__ == '__main__':
    pose_test = TestFunction()
    kalman_test = KalmanFilterSimple(2,5,0.01)
    dock_pose_filtered = float()
    icp_filtered_cnt = 0
    average_arr = list()
    kalman_arr = list()
    plt.title("Graph test")
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    num = 50
    value = 10
    _index = np.arange(num)
    mea_value = np.random.normal(value,1,num)
    for new_pose in mea_value:
        (dock_pose_filtered, icp_filtered_cnt) = pose_test.pose_filter(dock_pose_filtered, new_pose, icp_filtered_cnt)
        # print("result {}: {}".format(icp_filtered_cnt, dock_pose_filtered))
        average_arr.append(dock_pose_filtered)
        # print("kalman {}: {}".format(icp_filtered_cnt,kalman_test.updateEstimate(new_pose)))
        kalman_arr.append(kalman_test.updateEstimate(new_pose))
    print(average_arr[-1])
    print(kalman_arr[-1])
    mean_value = np.ones(num) * value
    plt.plot(_index, mea_value, 'c+')
    plt.plot(_index, mean_value, 'b')
    plt.plot(_index, average_arr, 'g*', label="average")
    plt.plot(_index, kalman_arr, 'ro', label="kalman")
    plt.legend()
    plt.show()