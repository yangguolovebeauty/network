import numpy
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model,discriminant_analysis,cross_decomposition

def load_data():
    diabetes = datasets.load_diabetes()
    return cross_decomposition.train_test_split(datasets.data,diabetes.target,test_size=0.25,random_state=0)


