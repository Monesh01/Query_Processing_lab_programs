import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), columns=["B", "C", "D", "E"])

df.loc[0, "C"] = np.nan
df.loc[4, "B"] = np.nan
df.loc[9, "E"] = np.nan

def highlight(x):
    return "background-color: red" if pd.isna(x) else ""

df.style.map(highlight)
