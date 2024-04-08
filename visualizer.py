# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 14:54:33 2023

@author: marko
"""
import matplotlib.pyplot as plt
import numpy as np

class Visualizer(object):
    def PlotSeries(series, title, xlabel, ylabel):
        plt.show()
        plt.plot(series)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.tight_layout()
        plt.show()
    def PredActual(y_test, y_pred):
       # Calculate the coefficients of the linear regression line
        coefficients = np.polyfit(y_test, y_pred, 1)
        regression_line = np.polyval(coefficients, y_test)
        
        # Plot predicted vs. actual values with regression line
        plt.scatter(y_test, y_pred, label='Actual vs. Predicted')
        plt.plot(y_test, regression_line, color='red', label='Regression Line')
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')
        plt.title('SVR: Predicted vs. Actual Values with Regression Line')
        plt.legend()
        plt.show()
    def PlotROCCurve(fpr, tpr, roc_auc, title):
        plt.figure(figsize=(8, 8))
        plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'AUC = {roc_auc:.2f}')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(title + ' ROC Curve for SVC')
        plt.legend(loc='lower right')
        plt.show()
    def PlotMeanROCCurve(mean_fpr, mean_tpr, mean_auc, std_auc, title):
        plt.figure(figsize=(8, 8))
        print(mean_auc, std_auc)
        plt.plot(mean_fpr, mean_tpr, color='darkorange', lw=2, label=f'Mean AUC = {mean_auc:.2f} ± {std_auc:.2f}')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(title + ' Mean ROC Curve with Cross-Validation')
        plt.legend(loc='lower right')
        plt.show()
    def PlotAccuracy(accuracy_values, title, xlabel, ylabel):
        epochs = np.arange(1, len(accuracy_values) + 1)
        coefficients = np.polyfit(epochs, accuracy_values, deg=1)
        poly_function = np.poly1d(coefficients)
        y_line = poly_function(epochs)
        plt.plot(epochs, y_line, color='red', label='Regression line')
        plt.scatter(epochs, accuracy_values, marker='o', linestyle='-', color='b')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
    