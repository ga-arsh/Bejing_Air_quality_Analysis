import pandas as pd
df = pd.read_csv("C:\\Users\\ganga\\OneDrive\\Desktop\\mlops_dvc\\Beijing_Air_Quality_Project\\data\\PRSA_Data_Aotizhongxin.csv")
summary = df.describe()
summary.to_csv("outputs/summary.csv")
print(summary)
