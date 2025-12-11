
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
df = pd.read_csv(filename)
df.head()
a = df[["OrderID"]]
b = df[[""]]
print(df)
print(a)