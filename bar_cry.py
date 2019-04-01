import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r'C:\Users\student\Desktop\python\FinalDataset.csv',header='infer')

n=17
index=np.arange(n)
bar_width = 0.35
opacity = 0.8
c=[604,1800,1975,1080,0,0,1260,60,76.68,300,0,0,660,351.42,8010,2166.31,1400] 
rects3 = plt.bar(index, c, bar_width,
                 alpha=opacity,
                 color='b' ,
                 label='Crying')
 
plt.xlabel('BabyId')
plt.ylabel('Average Crying rate(in seconds)')
plt.title('Crying details of all babies')
plt.xticks(index, ('16', '17', '18', '19','20','21','22','23','24','25','26','27','28','29','30','31','33'))
plt.legend()
plt.show()
