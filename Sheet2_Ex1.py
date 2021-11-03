import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Name':['A','B','C','D','E','F'], 'x_1':[1.0,2.0,1.0,3.0,5.5,5.5], 'x_2':[1.0,0.5,2.5,3.5,3.5,2.5], 'class':[1,1,1,2,2,2]})
print(df)

plt.scatter(df['x_1'], df['x_2'])
plt.show()

def l1norm(x1,y1,x2,y2):
    return abs((x2-x1)+(y2-y1))
    
def l2norm(x1,y1,x2,y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)
    
"""
def nearestneighbors(df):
    for i0 in range(len(df)):
        df["Nearest_Neighbor"] = ''
        df["Distance"] = np.nan
        indexnn = 0
        df1 = df
        df1 = df.drop(i0)
        d0 = l1norm(df.x_1.to_numpy()[i0], df.x_2.to_numpy()[i0], df1.x_1.to_numpy()[0], df1.x_2.to_numpy()[0])
        for i1 in range(len(df1)):
            d = l1norm(df.x_1.to_numpy()[i0], df.x_2.to_numpy()[i0], df1.x_1.to_numpy()[i1], df1.x_2.to_numpy()[i1])
            if d < d0:
                df.loc["Nearest_Neighbor"][i0] = df1.Name[i1]
                df.loc["Distance"][i0] = d
            else:
                df.loc["Nearest_Neighbor"][i0] = df.Name[i0]
                df.loc["Distance"][i0] = d0
    return df

"""
    
print("L1 Norm: \n\n")
for i in range(len(df)):
    for j in range(len(df)):
        if i != j:
            print("P1: ", df.Name[i], "P2: ", df.Name[j], "d = ", l1norm(df.x_1[i],df.x_2[i],df.x_1[j],df.x_2[j]))

print("\n\n L2 Norm: \n\n")
for i in range(len(df)):
    for j in range(len(df)):
        if i != j:
            print("P1: ", df.Name[i], "P2: ", df.Name[j], "d = ", l2norm(df.x_1[i],df.x_2[i],df.x_1[j],df.x_2[j]))
