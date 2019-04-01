import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r'C:\Users\student\Desktop\python\FinalDataset.csv',header='infer')

#2 rows 2 cols
#first row, first col
n=17
index=np.arange(n)
bar_width = 0.45
opacity = 0.8
b=[8959.15,6402.90,10690,12836.66,15292,9464.15,15300,860.42,1699.78,9652.26,6664.66,10665.55,9202.19,13813.63,10584.69,8842.44,12532.75] 
rects2 = plt.bar(index, b, bar_width, 
                 alpha=opacity,
                 color='g',
                 label='Sleeping')
plt.xlabel('BabyId')
plt.ylabel('Average Sleeping rate(in seconds)')
plt.title('Sleeping details of all babies')
plt.xticks(index, ('16', '17', '18', '19','20','21','22','23','24','25','26','27','28','29','30','31','33'))
plt.legend()
plt.show()
