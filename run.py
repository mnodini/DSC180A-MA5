import pandas as pd
import io
import os
import gzip
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import sys

def main(targets):

    if 'test' in targets:
        merged = pd.read_csv('DSC180A-MA5/test/testdata/test_data.csv',index_col='Unnamed: 0')
        #Use matched expressions and alleles
        X = sm.add_constant(merged['expression'].values)
        est = sm.OLS(merged['allele'].values.astype(float),X.astype(float))
        est2 = est.fit()
        print(est2.summary())

if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
