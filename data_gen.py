import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("--- Mock Trading Data Generator ---")
print("Generating 30 days of simulated market data...")

# 1. Generate 30 days of dates (counting backward from today)
dates = [datetime.today() - timedelta(days=x) for x in range(30)]
dates.reverse() # Put them in chronological order

# 2. Generate random daily price movements (volatility)
np.random.seed(42) # Ensures we get the same "random" numbers every time
daily_returns = np.random.normal(loc=0.001, scale=0.02, size=30)

# 3. Calculate actual prices (Starting at $150.00)
prices = 150.0 * np.cumprod(1 + daily_returns)

# 4. Organize into a Pandas DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Close_Price': prices
})

# 5. Calculate a 5-Day Simple Moving Average (SMA)
df['5_Day_SMA'] = df['Close_Price'].rolling(window=5).mean()

# 6. Save the data to a CSV file
filename = "simulated_portfolio.csv"
df.to_csv(filename, index=False)

print(f"\nSuccess! Data saved locally to '{filename}'.")
print("\nHere is a sneak peek at the last 5 days:")
print(df.tail())