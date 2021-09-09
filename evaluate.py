import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats

from env import user, host, password
import explore
import acquire

import os
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")

from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 
from math import sqrt


def plot_residuals():
    plt.figure(figsize = (11,5))

    plt.subplot(121)
    plt.scatter(df.total_bill, df.baseline_residual)
    plt.axhline(y = 0, ls = ':')
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.title('Baseline Residuals')

    plt.subplot(122)
    plt.scatter(df.total_bill, df.residual)
    plt.axhline(y = 0, ls = ':')
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.title('OLS model residuals');
    return plt.show()

def regression_errors():
    SSE = df['residual^2'].sum()
    ESS = ((df.yhat - df.tip_baseline)**2).sum()
    TSS = ((df.tip - df.tip_baseline)**2).sum()
    MSE = SSE/len(df)
    RMSE = sqrt(MSE)
    return print(f" SSE = {SSE}\n ESS = {ESS}\n TSS = {TSS}\n MSE = {MSE}\n RMSE = {RMSE}")
    

def baseline_mean_errors():
    SSE_baseline = df['baseline_residual^2'].sum()
    MSE_baseline = SSE_baseline/len(df)
    RMSE_baseline =  sqrt(MSE_baseline)
    return print(f" SSE_baseline = {SSE_baseline}\n MSE_baseline = {MSE_baseline}\n RMSE_baseline = {RMSE_baseline}")


def better_than_baseline():
    if SSE < SSE_baseline:
        print("My model performs better than baseline.")
        x = True
    else:
        print("My model does NOT perform better than baseline.")
        x = False
    return x


##############Copied from GitHUb ###################

import math
import sklearn.metrics
import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt

def residuals(actual, predicted):
    return actual - predicted

def sse(actual, predicted):
    return (residuals(actual, predicted) **2).sum()

def mse(actual, predicted):
    n = actual.shape[0]
    return sse(actual, predicted) / n

def rmse(actual, predicted):
    return math.sqrt(mse(actual, predicted))

def ess(actual, predicted):
    return ((predicted - actual.mean()) ** 2).sum()

def tss(actual):
    return ((actual - actual.mean()) ** 2).sum()

def regression_errors(actual, predicted):
    return pd.Series({
        'sse': sse(actual, predicted),
        'ess': ess(actual, predicted),
        'tss': tss(actual),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    })

def baseline_mean_errors(actual):
    predicted = actual.mean()
    return {
        'sse': sse(actual, predicted),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    }

def better_than_baseline(actual, predicted):
    rmse_baseline = rmse(actual, actual.mean())
    rmse_model = rmse(actual, predicted)
    return rmse_model < rmse_baseline

def r2_score(actual, predicted):
    return ess(actual, predicted) / tss(actual)
    
# def model_significance(ols_model):
#     return {
#         'r^2 -- variance explained': ols_model.rsquared,
#         'p-value -- P(data|model == baseline)': ols_model.f_pvalue,
#     }
def plot_residuals(actual, predicted):
    residuals = actual - predicted
    plt.hlines(0, actual.min(), actual.max(), ls=':')
    plt.scatter(actual, residuals)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title('Actual vs Residual')
    plt.show()