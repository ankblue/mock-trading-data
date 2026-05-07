import pandas as pd
import matplotlib.pyplot as plt

print("--- Data Visualization Script ---")
print("Reading simulated_portfolio.csv...")

# 1. Load the data
df = pd.DataFrame()
try:
    df = pd.read_csv("simulated_portfolio.csv")
    # Convert the Date column from text back into actual datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
except FileNotFoundError:
    print("Error: Could not find the CSV file. Did you run data_gen.py first?")
    exit()

# 2. Set up the "Canvas"
plt.figure(figsize=(10, 6)) # Width: 10 inches, Height: 6 inches

# 3. Plot the lines
# Plot the daily closing price
plt.plot(df['Date'], df['Close_Price'], label='Daily Close Price', color='blue', linewidth=2)

# Plot the 5-Day Simple Moving Average
plt.plot(df['Date'], df['5_Day_SMA'], label='5-Day SMA', color='orange', linestyle='--', linewidth=2)

# 4. Add labels and title
plt.title('Simulated Portfolio Performance (30 Days)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)

# 5. Make it pretty
plt.grid(True, linestyle=':', alpha=0.6) # Add a faint grid
plt.legend() # Show the legend (matches lines to labels)
plt.xticks(rotation=45) # Tilt the dates so they don't overlap
plt.tight_layout() # Ensure everything fits perfectly in the frame

# 6. Save the chart as an image
filename = "portfolio_chart.png"
plt.savefig(filename)
print(f"Success! Chart saved locally as '{filename}'")