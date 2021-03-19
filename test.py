import plotly.figure_factory as ff
import statistics
import csv
import pandas as pd
import random
import plotly.graph_objects as go

dataset1 = []
def random_set(counter):
  
  df = pd.read_csv("data.csv")
  data = df["Math_score"].tolist()
  for i in range(0,counter):
    randomindex1 = random.randint(0,len(data)-1)
    value1 = data[randomindex1]
    dataset1.append(value1)
    
  mean1 = statistics.mean(dataset1)
  return mean1

  meanList = []
  for i in range(0,1000):
    setofmeans = randomMean(100)
    meanList.append(setofmeans)


  

# def setup():
#   meanList = []
#   for i in range(0,1000):
#     setofmeans = randomMean(100)
#     meanList.append(setofmeans)
  
#   showfig(meanList)
random_set(100)

  
fig1 = ff.create_distplot([dataset1],["Math_score"],show_hist=False)
fig1.show()
mean = statistics.mean(dataset1)
sd = statistics.stdev(dataset1)
print("Mean is: ",mean)

print("SD is: ",sd)

firstSDStart,firstSDEnd = mean-sd,mean+sd
secondSDStart,secondSDEnd = mean-(2*sd),mean+(2*sd)
thirdSDStart,thirdSDEnd = mean-(3*sd),mean+(3*sd)

print("std1",firstSDStart,firstSDEnd)
print("std2",secondSDStart,secondSDEnd)
print("std3",thirdSDStart,thirdSDEnd)

fig1.add_trace(go.Scatter( 
    x = [mean,mean],
    y = [0,0.17],
    mode = "lines",
    name = "MEAN"
))

fig1.add_trace(go.Scatter(
    x = [firstSDStart,firstSDStart],
    y = [0,0.17],
    mode = "lines",
    name = "Standed Daveation1 Start"
))

fig1.add_trace(go.Scatter(
    x = [firstSDEnd,firstSDEnd],
    y = [0,0.17],
    mode = "lines",
    name = "Standed Daveation1 End"
))

fig1.add_trace(go.Scatter(
    x = [secondSDStart,secondSDStart],
    y = [0,0.17],
    mode = "lines",
    name = "Standed Daveation2 Start"
))

fig1.add_trace(go.Scatter(
    x = [secondSDEnd,secondSDEnd],
    y = [0,0.17],
    mode = "lines",
    name = "Standed Daveatione2 End"
))

fig1.add_trace(go.Scatter(
    x = [thirdSDStart,thirdSDStart],
    y = [0,0.17],
    mode = "lines",
    name = "Standed Daveatione3 Start"
))

fig1.add_trace(go.Scatter(
    x = [thirdSDEnd,thirdSDEnd],
    y = [0,0.17],
    mode = "lines",
    name = "Standed Daveatione3 End"
))