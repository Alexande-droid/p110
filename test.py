import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import csv
import scipy
import random

df = pd.read_csv("newdata.csv")
data = df["average"].tolist() 
fig = ff.create_distplot([data],["average"],show_hist=False)
fig.show()
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
meanlist = []
def setup():
    for i in range(0,1000):
        setofmeans=random_set_of_mean(100)
        meanlist.append(setofmeans)
setup()
fig = ff.create_distplot([meanlist],["average"],show_hist=False)
fig.show()