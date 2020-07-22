import pandas as pd
dataset = pd.read_csv("general_data.csv")


dataset["Attrition"]=dataset["Attrition"].astype('category')
dataset["Attrition"]= dataset["Attrition"].cat.codes


from scipy.stats import pearsonr

dataset1=dataset[["Age","Attrition"]]
stats,p1=pearsonr(dataset1.Attrition,dataset1.Age)
print("Correlation of Age and Attrition is ",stats,p1)

dataset2=dataset[["DistanceFromHome","Attrition"]]
stats,p2=pearsonr(dataset2.Attrition,dataset2.DistanceFromHome)
print("Correlation of Age and Attrition is ",stats,p2)

dataset3=dataset[["Education","Attrition"]]
stats,p3=pearsonr(dataset3.Attrition,dataset3.Education)
print("Correlation of DistanceFromHome and Attrition is ",stats,p3)

dataset4=dataset[["MonthlyIncome","Attrition"]]
stats,p4=pearsonr(dataset4.Attrition,dataset4.MonthlyIncome)
print("Correlation of MonthlyIncome and Attrition is ",stats,p4)

dataset5=dataset[["TrainingTimesLastYear","Attrition"]]
stats,p5=pearsonr(dataset5.Attrition,dataset5.TrainingTimesLastYear)
print("Correlation of Training and Attrition is ",stats,p5)

dataset6=dataset[["YearsWithCurrManager","Attrition"]]
stats,p6=pearsonr(dataset6.Attrition,dataset6.YearsWithCurrManager)
print("Correlation of YearsWithCurrManager and Attrition is ",stats,p6)

dataset7=dataset[["PercentSalaryHike","Attrition"]]
stats,p7=pearsonr(dataset7.Attrition,dataset7.PercentSalaryHike)
print("Correlation of PercentSalaryHike and Attrition is ",stats,p7) 

dataset8=dataset[["YearsAtCompany","Attrition"]]
stats,p8=pearsonr(dataset8.Attrition,dataset8.YearsAtCompany)
print("Correlation of YearsAtCompany and Attrition is ",stats,p8)