import pandas as pd
import numpy as np

df1 = pd.read_csv("shared_articles.csv")

df2 = pd.read_csv("users_interactions.csv")

df1.head()

df2.head()

df1 = df1[df1["eventType"] == "CONTENT SHARED"]

df1.head()