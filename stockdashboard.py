import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# Page config
st.set_page_config(page_title="Stock Dashboard", layout="wide")

# Title
st.title("📊 Stock Market Dashboard")

# Sidebar inputs
ticker = st.sidebar.text_input("Enter Stock Ticker", "TSLA")
period = st.sidebar.selectbox("Select Period", ["1mo", "3mo", "6mo", "1y", "5y", "max"])

# Fetch data
stock = yf.Ticker(ticker)
data = stock.history(period=period)

# Reset index so Date becomes column
data.reset_index(inplace=True)

# Check data
if not data.empty:

    st.subheader(f"{ticker} Stock Data")
    st.write(data.tail())

    # 📈 Closing Price Chart
    fig1 = px.line(data, x="Date", y="Close", title="Closing Price")
    st.plotly_chart(fig1, use_container_width=True)

    # 📊 Volume Chart
    fig2 = px.bar(data, x="Date", y="Volume", title="Trading Volume")
    st.plotly_chart(fig2, use_container_width=True)

    # 📉 Moving Average
    data["MA50"] = data["Close"].rolling(50).mean()

    fig3 = px.line(data, x="Date", y=["Close", "MA50"], title="Moving Average (50 Days)")
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.error("No data found. Please check the ticker symbol.")
