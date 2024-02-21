import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def generate_stock_chart(stock_name):
    # Fetch stock data from Yahoo Finance
    stock_data = fetch_stock_data(stock_name)

    # Convert the 'Period' index back to a 'Datetime' index
    stock_data.index = stock_data.index.to_timestamp()

    # Extract relevant data for plotting
    dates = stock_data.index
    prices = stock_data['Close']

    # Plot the original stock chart
    plt.plot(dates, prices, label='Original')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'Stock Chart for {stock_name}')

    # Create an ARIMA model and make predictions
    model = ARIMA(prices, order=(5,1,0))
    model_fit = model.fit()
    forecast, stderr, conf_int, _ = model_fit.forecast(steps=30)

    # Plot the forecasted stock chart
    future_dates = pd.date_range(start=dates[-1], periods=31, freq='B')[1:]
    plt.plot(future_dates, forecast, label='Forecast')
    plt.legend()

    plt.show()

def fetch_stock_data(stock_name):
    # Fetch stock data from Yahoo Finance
    stock_data = yf.download(stock_name, start='2021-01-01', end='2022-12-31')
    stock_data.index = stock_data.index.to_period('B')
    return stock_data

# Get user input for the stock name
stock_name = input('Enter the stock name: ')

# Generate the stock chart
generate_stock_chart(stock_name)