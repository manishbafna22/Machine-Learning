# -*- coding: utf-8 -*-
"""linearmodel.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bk8fsEq6kt-8b3wVkkBrVZN6uRtThd1R
"""

import numpy as np
import pandas as pd


from google.colab import files
uploaded  = files.upload()

import io
abalone = pd.read_csv(
    io.BytesIO(uploaded['abalone_train.csv']),
    names=["Length", "Diameter", "Height", "Whole weight", "Shucked weight",
           "Viscera weight", "Shell weight", "Age"])

X1 = abalone["Length"]


X2 = np.array(X1)


X = X2.reshape(-1, 1)

y1 = abalone["Height"]
y2 = np.array(y1)
y = y2.reshape(len(y2), 1)