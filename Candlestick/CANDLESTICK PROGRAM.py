#GURLEEN 12514824
import subprocess, sys

for p in ["pandas", "matplotlib", "mplfinance"]:
    try:
        __import__(p)
    except:
        subprocess.call([sys.executable, "-m", "pip", "install", p])
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\DELL\Downloads\Quote-Equity-PSB-EQ-16-03-2026-16-04-2026.csv")
df.columns = df.columns.str.strip().str.capitalize()
date_col = [c for c in df.columns if 'date' in c.lower() or 'time' in c.lower()][0]
df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
df.set_index(date_col, inplace=True)
for c in ['Open', 'High', 'Low', 'Close', 'Volume']:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c].astype(str).str.replace(',', ''), errors='coerce')
mpf.plot(df, type='candle', style='yahoo', volume=False)
plt.show()