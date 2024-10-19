import pandas as pd
import yfinance as yf
import ta

# Fetch historical silver price data
data = yf.download('SI=F', start='2020-01-01', end='2024-01-01')

# Calculate technical indicators
data['SMA50'] = ta.trend.sma_indicator(data['Close'], window=50)
data['SMA200'] = ta.trend.sma_indicator(data['Close'], window=200)
data['RSI'] = ta.momentum.rsi(data['Close'], window=14)

# Generate buy/sell signals
data['Signal'] = 0
data['Signal'][50:] = np.where(data['SMA50'][50:] > data['SMA200'][50:], 1, 0)
data['Position'] = data['Signal'].diff()

# Backtest the strategy
initial_capital = 10000
data['Portfolio Value'] = initial_capital + (data['Position'] * data['Close']).cumsum()

# Print the final portfolio value
print(data['Portfolio Value'].iloc[-1])
