import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from docutils.nodes import figure
# from mpmath import arange

df=pd.read_csv("/Users/phantom/District/PhantomLab/CodeSpace/ZPrac/IOC (20250819000000000 _20240807000000000).csv");

print(df.info())
print(df.describe())
print(df["close"].head())
print(df[df["Close"]>385.2])
df["Double"] = df['Close'] * 2
print(df.head())
df["Date"] = df["Date"].str.replace(r"\s*\(.*\)$","", regex=True)
df["Date"] = df["Date"].str.replace(r"\s*GMT[+-]\d{4}","", regex=True)
df["Date"] = df["Date"].str.replace(r"\s*\{GMT+0530}$","", regex=True)
print(df.head())
df["Date"]=pd.to_datetime(df["Date"],format="%a %b %d %Y %H:%M:%S")
print(df.dtypes)
print(df[["Date"]])
df["Range"] = df["High"] - df["Low"]
plt.plot(df["Range"], label="Range",color='green')
plt.legend();
plt.xlabel("Date");
plt.ylabel("Price(INR)");
plt.show();
import plotly.graph_objects as go
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close']
)])

fig.update_layout(
    title='Interactive Candlestick Chart',
    xaxis_rangeslider_visible=False
)
fig.show()