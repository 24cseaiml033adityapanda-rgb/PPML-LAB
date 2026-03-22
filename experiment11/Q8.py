import pandas as pd
df_csv =pd.read_csv("sample.csv")
print("Dataframe from csv: ")
print(df_csv)
df_json=pd.read_json("sample.json")
print("data from json: ")
print(df_json)