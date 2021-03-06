from __future__ import division, print_function

from typing import List

import numpy as np
import scipy


############################################################################
# DO NOT MODIFY ABOVE CODES
############################################################################

class LinearRegression:
    def __init__(self, nb_features: int):
        self.nb_features = nb_features
    def train(self, features: List[List[float]], values: List[float]):
        """TODO : Complete this function"""
        x = np.c_[np.ones(len(features)), np.array(features)]
        y = np.reshape(values,(len(values),1))
        inv = np.linalg.pinv(np.dot(np.transpose(x),x))
        self.w = np.dot(np.dot(inv,np.transpose(x)),y)
        
        #raise NotImplementedError

    def predict(self, features: List[List[float]]) -> List[float]:
        x = np.c_[np.ones(len(features)), np.array(features)]
        preds = np.dot(x,self.w)
        return preds
        #raise NotImplementedError

    def get_weights(self) -> List[float]:
        """TODO : Complete this function"""
        return self.w
        """
        for a model y = 1 + 3 * x_0 - 2 * x_1,
        the return value should be [1, 3, -2].
        """
        raise NotImplementedError


class LinearRegressionWithL2Loss:
    '''Use L2 loss for weight regularization'''
    def __init__(self, nb_features: int, alpha: float):
        self.alpha = alpha
        self.nb_features = nb_features

    def train(self, features: List[List[float]], values: List[float]):
        """TODO : Complete this function"""
        x = np.c_[np.ones(len(features)), np.array(features)]
        y = np.reshape(values,(len(values),1))
        inv = np.linalg.pinv(np.dot(np.transpose(x),x) + self.alpha*np.identity(x.shape[1]))
        self.w = np.dot(np.dot(inv,np.transpose(x)),y)
        # raise NotImplementedError

    def predict(self, features: List[List[float]]) -> List[float]:
        """TODO : Complete this function"""
        x = np.c_[np.ones(len(features)), np.array(features)]
        preds = np.dot(x,self.w)
        return preds
        raise NotImplementedError

    def get_weights(self) -> List[float]:
        """TODO : Complete this function"""
        
        return self.w
        """
        for a model y = 1 + 3 * x_0 - 2 * x_1,
        the return value should be [1, 3, -2].
        """
        raise NotImplementedError


if __name__ == '__main__':
    print(numpy.__version__)
    print(scipy.__version__)
