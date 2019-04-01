import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r'C:\Users\student\Desktop\python\FinalDataset.csv',header='infer')

x=df['BabyId']
y=df['FirsttimeParent']
plt.plot(x,y)
plt.xlabel('BabyId')
plt.ylabel('FirsttimeParent')
plt.legend()
plt.show()
