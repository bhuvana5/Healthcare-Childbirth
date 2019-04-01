import numpy as  np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r'C:\Users\student\Desktop\FinalDataset.csv',header='infer')

n=17

a=[175.80,128.125,144.66,68.67,110.20,140.35,76,101.66,109.88,140,174.64,160.30,123,174.03,116.45,104.61,0]
bar_width = 0.35
opacity = 0.8
index = np.arange(n) 
rects1 = plt.bar(index, a, bar_width,
                 alpha=opacity,
                 color='b' ,
                 label='Feeding')
plt.xlabel('BabyId')
plt.ylabel('Feeding rate(in milli litres)')
plt.title('Feeding data details of all babies')
plt.xticks(index, ('16', '17', '18', '19','20','21','22','23','24','25','26','27','28','29','30','31','33'))
 

plt.legend()
plt.show()
