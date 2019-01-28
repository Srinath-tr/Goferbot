import pandas as pd
import Quandl

df = Quandl.get("WIKI/GOOGL")

print(df.head())
