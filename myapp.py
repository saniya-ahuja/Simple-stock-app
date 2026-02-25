import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!
""")

# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get historical prices
tickerDf = tickerData.history(
    start='2010-05-31',
    end='2020-05-31'
)

# Display closing price
st.write("""
## Closing Price
""")
st.line_chart(tickerDf['Close'])

# Display volume
st.write("""
## Volume
""")
st.line_chart(tickerDf['Volume'])
