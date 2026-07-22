import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Date": ["2024-01-01","2024-01-02","2024-01-03","2024-01-04"],
    "Close": [140, 145, 143, 148]
})

df["Date"] = pd.to_datetime(df["Date"])

plt.plot(df["Date"], df["Close"])
plt.title("Alphabet Stock Price")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.show()
