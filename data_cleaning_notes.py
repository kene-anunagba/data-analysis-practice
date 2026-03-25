# Basic data cleaning steps using pandas
import pandas as pd
# load dataset
df = pd.read_csv("data.csv")
# remove duplicates
df = df.drop_duplicates()
# handle missing values
df = df.fillna(0)
# view summary
print(df.describe())
