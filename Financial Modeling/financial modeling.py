#GURLEEN 12514824
import pandas as pd
import numpy as np
import numpy_financial as npf

file_path = r"C:\Users\DELL\Downloads\PUNJAB AND SIND NEW xlsx.xlsx"
f = pd.ExcelFile(file_path)
s = f.sheet_names[0]

d = pd.read_excel(f, sheet_name=s, header=None)

def find_any(keywords):
    for i, v in d[0].items():
        if isinstance(v, str):
            txt = v.lower().strip()
            for k in keywords:
                if k in txt:
                    return i
    return None

rv = find_any(["revenue"])
if rv is None:
    rv = find_any(["revenue +"])

ex = find_any(["expense", "expenses"])

if None in [rv, ex]:
    raise SystemExit("Revenue/Expense row not found")

start_col = 1
while pd.isna(d.iloc[rv, start_col]):
    start_col += 1

YH = d.iloc[rv - 1, start_col:].dropna().values

R = pd.to_numeric(d.iloc[rv, start_col:start_col+len(YH)], errors="coerce").fillna(0).values.astype(float)
C = pd.to_numeric(d.iloc[ex, start_col:start_col+len(YH)], errors="coerce").fillna(0).values.astype(float)

inv = float(input())
yrs = int(input())
disc = float(input()) / 100

def growth(arr):
    if len(arr) >= 2 and arr[-2] != 0:
        return (arr[-1] - arr[-2]) / arr[-2]
    return 0.0

gR = growth(R)
gC = growth(C)

S1 = R[-1] * (1 + gR)
C1 = C[-1] * (1 + gC)

Y = np.arange(1, yrs + 1)

SF = S1 * (1 + gR) ** (Y - 1)
CF = C1 * (1 + gC) ** (Y - 1)

PF = SF - CF
CF_money = PF * 1e7

DF = 1 / ((1 + disc) ** Y)
PV = CF_money * DF

if disc > gR:
    TV = (CF_money[-1] * (1 + gR)) / (disc - gR)
    TV_PV = TV / ((1 + disc) ** yrs)
else:
    TV = 0
    TV_PV = 0

NPV = -inv + PV.sum() + TV_PV

try:
    cashflows = np.concatenate((np.array([-inv], float), CF_money.astype(float), np.array([TV], float)))
    irr_val = npf.irr(cashflows)
    IRR = float(irr_val) * 100 if np.isfinite(irr_val) else np.nan
except:
    IRR = np.nan

cum = np.cumsum(CF_money)
PB = None

for i, v in enumerate(cum):
    if v >= 0:
        PB = 0.0 if i == 0 else (i - 1) + (-cum[i - 1] / CF_money[i])
        break

ROI = (CF_money.sum() - inv) / inv * 100

proj = []
for i in range(len(Y)):
    proj.append([
        Y[i],
        SF[i],
        CF[i],
        PF[i],
        CF_money[i],
        DF[i],
        PV[i]
    ])

proj_df = pd.DataFrame(proj)

DCF = pd.DataFrame([
    ["DCF Calculations including Terminal Value", ""],
    ["", "RESULT", ""],
    ["ROI %", ROI],
    ["NPV incl. TV (₹ Cr)", NPV / 1e7],
    ["IRR %", IRR],
    ["Payback (Years)", PB]
])

E = pd.concat([proj_df, DCF], ignore_index=True)

import time
output_file = f"financial_output_{int(time.time())}.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as w:
    E.to_excel(w, sheet_name=s, index=False, header=False)

print(output_file)