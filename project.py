import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\student\Desktop\FinalDataset.csv',header='infer')
df.info()
print("The average of crying data in seconds is",df['Crying seconds'].mean())
print("The median of crying data in seconds is",df['Crying seconds'].median())
print("The mode of crying data in seconds is",df['Crying seconds'].mode())
print("The varience of crying data in seconds is",df['Crying seconds'].var())
print("The standard of crying data in seconds is",df['Crying seconds'].std())
print("The maximum value of crying data in seconds is",df['Crying seconds'].max())

print("The average of feeding data is",df['Bottle amount'].mean())
print("The median of feeding data in seconds is",df['Bottle amount'].median())
print("The mode of feeding data in seconds is",df['Bottle amount'].mode())
print("The varience of feeding data in seconds is",df['Bottle amount'].var())
print("The standard of feeding data in seconds is",df['Bottle amount'].std())
print("The maximum value of feeding data in seconds is",df['Bottle amount'].max())


print("The mean of sleeping data is",df['SleepingSecond'].mean())
print("The median of sleeping data in seconds is",df['SleepingSecond'].median())
print("The mode of sleeping data in seconds is",df['SleepingSecond'].mode())
print("The varience of sleeping data in seconds is",df['SleepingSecond'].var())
print("The standard of sleeping data in seconds is",df['SleepingSecond'].std())
print("The maximum value of sleeping data in seconds is",df['SleepingSecond'].max())

print("The average pumping rate of children is",df['Pumping Left'].mean())
print("The median of pumping data in seconds is",df['Pumping Left'].median())
print("The mode of pumping data in seconds is",df['Pumping Left'].mode())
print("The varience of pumping data in seconds is",df['Pumping Left'].var())
print("The standard of pumping data in seconds is",df['Pumping Left'].std())
print("The maximum value of pumping data in seconds is",df['Pumping Left'].max())
print("**********************************************")
print("mean of subset that is baby id_16 out of 17 babies in dataset")
print(df.iloc[1:92,8].mean())
print(df.iloc[1:92,15].mean())
print(df.iloc[1:92,5].mean())

print(df.iloc[1:92,8].mode())
print(df.iloc[1:92,15].mode())
print(df.iloc[1:92,5].mode())

print(df.iloc[1:92,5].median())
print(df.iloc[1:92,15].median())
print(df.iloc[1:92,5].median())

print(df.iloc[1:92,8].var())
print(df.iloc[1:92,15].var())
print(df.iloc[1:92,5].var())

print(df.iloc[1:92,8].std())
print(df.iloc[1:92,15].std())
print(df.iloc[1:92,5].std())
print("mean of second subset that is baby id_17 out of 17 babies in dataset")
print(df.iloc[92:118,8].mean())
print(df.iloc[92:118,15].mean())
print(df.iloc[92:118,5].mean())

print(df.iloc[92:118,8].mode())
print(df.iloc[92:118,15].mode())
print(df.iloc[92:118,5].mode())

print(df.iloc[92:118,5].median())
print(df.iloc[92:118,15].median())
print(df.iloc[92:118,5].median())

print(df.iloc[92:118,8].var())
print(df.iloc[92:118,15].var())
print(df.iloc[92:118,5].var())

print(df.iloc[92:118,8].std())
print(df.iloc[92:118,15].std())
print(df.iloc[92:118,5].std())

print("mean of third subset that is baby id_18 out of 17 babies in dataset")
print(df.iloc[118:207,8].mean())   #8th column gives bottle amount details
print(df.iloc[118:207,15].mean())#15th column gives sleeping data details
print(df.iloc[118:207,5].mean())  #5th column gives crying data details

print(df.iloc[118:207,8].std())   #8th column gives bottle amount details
print(df.iloc[118:207,15].std())#15th column gives sleeping data details
print(df.iloc[118:207,5].std())  #5th column gives crying data details

print("mean of fourth subset that is baby id_19 out of 17 babies in dataset")
print(df.iloc[207:367,8].mean())   #8th column gives bottle amount details
print(df.iloc[207:367,15].mean())#15th column gives sleeping data details
print(df.iloc[207:367,5].mean())  #5th column gives crying data details

print(df.iloc[207:367,8].std())   #8th column gives bottle amount details
print(df.iloc[207:367,15].std())#15th column gives sleeping data details
print(df.iloc[207:367,5].std())  #5th column gives crying data details

print("mean of fifth subset that is baby id_20 out of 17 babies in dataset")
print(df.iloc[367:537,8].mean())   #8th column gives bottle amount details
print(df.iloc[367:537,15].mean())#15th column gives sleeping data details
print(df.iloc[367:537,5].mean())  #5th column gives crying data details

print(df.iloc[367:537,8].std())   #8th column gives bottle amount details
print(df.iloc[367:537,15].std())#15th column gives sleeping data details
print(df.iloc[367:537,5].std())  #5th column gives crying data details

print("mean of sixth subset that is baby id_21 out of 17 babies in dataset")
print(df.iloc[537:691,8].mean())   #8th column gives bottle amount details
print(df.iloc[537:691,15].mean())#15th column gives sleeping data details
print(df.iloc[537:691,5].mean())  #5th column gives crying data details

print(df.iloc[537:691,8].std())   #8th column gives bottle amount details
print(df.iloc[537:691,15].std())#15th column gives sleeping data details
print(df.iloc[537:691,5].std())  #5th column gives crying data details

print("mean of seventh subset that is baby id_22 out of 17 babies in dataset")
print(df.iloc[691:764,8].mean())   #8th column gives bottle amount details
print(df.iloc[691:764,15].mean())#15th column gives sleeping data details
print(df.iloc[691:764,5].mean())  #5th column gives crying data details

print(df.iloc[691:764,8].std())   #8th column gives bottle amount details
print(df.iloc[691:764,15].std())#15th column gives sleeping data details
print(df.iloc[691:764,5].std())  #5th column gives crying data details

print("mean of eight subset that is baby id_23 out of 17 babies in dataset")
print(df.iloc[764:822,8].mean())   #8th column gives bottle amount details
print(df.iloc[764:822,15].mean())#15th column gives sleeping data details
print(df.iloc[764:822,5].mean())  #5th column gives crying data details

print(df.iloc[764:822,8].std())   #8th column gives bottle amount details
print(df.iloc[764:822,15].std())#15th column gives sleeping data details
print(df.iloc[764:822,5].std())  #5th column gives crying data details

print("mean of ninth subset that is baby id_24 out of 17 babies in dataset")
print(df.iloc[822:913,8].mean())   #8th column gives bottle amount details
print(df.iloc[822:913,15].mean())#15th column gives sleeping data details
print(df.iloc[822:913,5].mean())  #5th column gives crying data details

print(df.iloc[822:913,8].std())   #8th column gives bottle amount details
print(df.iloc[822:913,15].std())#15th column gives sleeping data details
print(df.iloc[822:913,5].std())  #5th column gives crying data details

print("mean of tenth subset that is baby id_25 out of 17 babies in dataset")
print(df.iloc[913:1039,8].mean())   #8th column gives bottle amount details
print(df.iloc[913:1039,15].mean())#15th column gives sleeping data details
print(df.iloc[913:1039,5].mean())  #5th column gives crying data details

print(df.iloc[913:1039,8].std())   #8th column gives bottle amount details
print(df.iloc[913:1039,15].std())#15th column gives sleeping data details
print(df.iloc[913:1039,5].std())  #5th column gives crying data details


print("mean of eleventh subset that is baby id_26 out of 17 babies in dataset")
print(df.iloc[1039:1053,8].mean())   #8th column gives bottle amount details
print(df.iloc[1039:1053,15].mean())#15th column gives sleeping data details
print(df.iloc[1039:1053,5].mean())  #5th column gives crying data details

print(df.iloc[1039:1053,8].std())   #8th column gives bottle amount details
print(df.iloc[1039:1053,15].std())#15th column gives sleeping data details
print(df.iloc[1039:1053,5].std())  #5th column gives crying data details

print("mean of twelve subset that is baby id_27 out of 17 babies in dataset")
print(df.iloc[1053:1136,8].mean())   #8th column gives bottle amount details
print(df.iloc[1053:1136,15].mean())
print(df.iloc[1053:1136,5].mean())

print(df.iloc[1053:1136,8].std())
print(df.iloc[1053:1136,15].std())
print(df.iloc[1053:1136,5].std())

print("mean of thirteenth subset that is baby id_28 out of 17 babies in dataset")
print(df.iloc[1136:1243,8].mean())
print(df.iloc[1136:1243,15].mean())

print(df.iloc[1136:1243,5].mean())
print(df.iloc[1136:1243,8].std())
print(df.iloc[1136:1243,15].std())
print(df.iloc[1136:1243,5].std())

print("mean of forteenth subset that is baby id_29 out of 17 babies in dataset")
print(df.iloc[1243:1347,8].mean())   #8th column gives bottle amount details
print(df.iloc[1243:1347,15].mean())#15th column gives sleeping data details
print(df.iloc[1243:1347,5].mean())  #5th column gives crying data details

print(df.iloc[1243:1347,8].std())   #8th column gives bottle amount details
print(df.iloc[1243:1347,15].std())#15th column gives sleeping data details
print(df.iloc[1243:1347,5].std())  #5th column gives crying data details

print("mean of fifteenth subset that is baby id_30 out of 17 babies in dataset")
print(df.iloc[1347:1546,8].mean())   #8th column gives bottle amount details
print(df.iloc[1347:1546,15].mean())#15th column gives sleeping data details
print(df.iloc[1347:1546,5].mean())  #5th column gives crying data details

print(df.iloc[1347:1546,8].std())   #8th column gives bottle amount details
print(df.iloc[1347:1546,15].std())#15th column gives sleeping data details
print(df.iloc[1347:1546,5].std())  #5th column gives crying data details


print("mean of sixteenth subset that is baby id_31 out of 17 babies in dataset")
print(df.iloc[1546:1715,8].mean())   #8th column gives bottle amount details
print(df.iloc[1546:1715,15].mean())#15th column gives sleeping data details
print(df.iloc[1546:1715,5].mean())  #5th column gives crying data details

print(df.iloc[1546:1715,8].std())   #8th column gives bottle amount details
print(df.iloc[1546:1715,15].std())#15th column gives sleeping data details
print(df.iloc[1546:1715,5].std())  #5th column gives crying data details

print("mean of seventeenth subset that is baby id_33 out of 17 babies in dataset")
print(df.iloc[1715:1775,8].mean())   #8th column gives bottle amount details
print(df.iloc[1715:1775,15].mean())#15th column gives sleeping data details
print(df.iloc[1715:1775,5].mean())  #5th column gives crying data details

print(df.iloc[1715:1775,8].std())   #8th column gives bottle amount details
print(df.iloc[1715:1775,15].std())#15th column gives sleeping data details
print(df.iloc[1715:1775,5].std())  #5th column gives crying data details

print("Total count of babies in dataset")
a=df['BabyId'].nunique()
print(a)
print("Counting how many records are collected for each baby in terms of feeding, sleeping crying, pumping")
print(df['BabyId'].value_counts())










