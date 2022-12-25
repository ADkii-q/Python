#1.	Загрузить данные из файла “insurance.csv”
import pandas as pd

#'age,sex,bmi,children,smoker,region,charges'

def getData():
    data = pd.read_csv("insurance.csv", sep=',')

    return data

print(getData())

#2.	С помощью метода describe() посмотреть статистику по данным. Сделать выводы. 
from firstTask import getData

inshuranceData = getData()

print(inshuranceData.describe())

#3.	Построить гистограммы для числовых показателей. Сделать выводы. 
import seaborn as sns
import matplotlib.pyplot as plt
import firstTask

inshuranceData = firstTask.getData()

#sns.histplot(data=inshuranceData['age'])
#sns.histplot(data=inshuranceData['bmi'])
#sns.histplot(data=inshuranceData['children'])
sns.histplot(data=inshuranceData['charges'])

plt.show()

#4.	Найти меры центральной̆ тенденции и меры разброса для индекса массы тела (bmi) и расходов (charges).
import matplotlib.pyplot as plt
import firstTask

#'age,sex,bmi,children,smoker,region,charges'
inshuranceData = firstTask.getData()

def bmiInfo(inshuranceData):
    print("mean, median, mode: ", inshuranceData['bmi'].mean(),inshuranceData['bmi'].median(), inshuranceData['bmi'].mode()

    plt.bar(1, inshuranceData['bmi'].mean(), color='red', label='mean')
    plt.bar(2, inshuranceData['bmi'].median(), color='blue', label='median')
    plt.bar(3, inshuranceData['bmi'].mode(), color='green', label='mode')

def chargesInfo(inshuranceData):
    print("mean, median, mode: ", inshuranceData['charges'].mean(),inshuranceData['charges'].median(), inshuranceData['charges'].mode()

    plt.bar(1, inshuranceData['charges'].mean(), color='cyan', label='mean')
    plt.bar(2, inshuranceData['charges'].median(), color='magenta',label='median')
    plt.bar(3, nshuranceData['charges'].mode(), color='yellow', label='mode')

bmiInfo(inshuranceData)
#chargesInfo(inshuranceData)

plt.legend()
plt.grid()
plt.show()

#5.	Построить box-plot для числовых показателей. Названия графиков должны соответствовать названиям признаков.
import firstTask
import matplotlib.pyplot as plt

#'age,sex,bmi,children,smoker,region,charges'
inshuranceData = firstTask.getData()

plt.figure(figsize=(5, 7))

#inshuranceData.boxplot()

#plt.boxplot(inshuranceData['age'], labels=['age'], vert=True)
#plt.boxplot(inshuranceData['bmi'], labels=['bmi'], vert=True)
#plt.boxplot(inshuranceData['children'], labels=['children'], vert=True)
plt.boxplot(inshuranceData['charges'], labels=['charges'], vert=True)

plt.grid()

plt.show()

          
