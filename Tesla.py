# Install necessary libraries
!pip install yfinance requests beautifulsoup4 plotly

# Import necessary libraries
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.graph_objects as go

# Question 1: Extracting Tesla Stock Data Using yfinance
# Download Tesla stock data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print("Tesla Stock Data:")
print(tesla_data.head())

# Question 2: Extracting Tesla Revenue Data Using Web Scraping
# Scrape Tesla revenue data
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

tables = soup.find_all('table')
tesla_revenue = pd.read_html(str(tables))[1]
tesla_revenue.columns = ['Date', 'Revenue']
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',', '').str.replace('$', '')
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].astype('int64')
print("\nTesla Revenue Data:")
print(tesla_revenue.head())

# Question 3: Extracting GameStop Stock Data Using yfinance
# Download GameStop stock data
gamestop = yf.Ticker("GME")
gamestop_data = gamestop.history(period="max")
gamestop_data.reset_index(inplace=True)
print("\nGameStop Stock Data:")
print(gamestop_data.head())

# Question 4: Extracting GameStop Revenue Data Using Web Scraping
# Scrape GameStop revenue data
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

tables = soup.find_all('table')
gamestop_revenue = pd.read_html(str(tables))[1]
gamestop_revenue.columns = ['Date', 'Revenue']
gamestop_revenue['Revenue'] = gamestop_revenue['Revenue'].str.replace(',', '').str.replace('$', '')
gamestop_revenue.dropna(inplace=True)
gamestop_revenue = gamestop_revenue[gamestop_revenue['Revenue'] != ""]
gamestop_revenue['Revenue'] = gamestop_revenue['Revenue'].astype('int64')
print("\nGameStop Revenue Data:")
print(gamestop_revenue.head())

# Question 5: Tesla Stock and Revenue Dashboard
fig_tesla = go.Figure()
fig_tesla.add_trace(go.Scatter(x=tesla_data['Date'], y=tesla_data['Close'], name='Tesla Stock Price'))
fig_tesla.add_trace(go.Scatter(x=tesla_revenue['Date'], y=tesla_revenue['Revenue'], name='Tesla Revenue', yaxis='y2'))

fig_tesla.update_layout(
    title="Tesla Stock Price and Revenue",
    xaxis_title="Date",
    yaxis_title="Stock Price",
    yaxis2=dict(
        title="Revenue",
        overlaying='y',
        side='right'
    )
)

fig_tesla.show()

# Question 6: GameStop Stock and Revenue Dashboard
fig_gamestop = go.Figure()
fig_gamestop.add_trace(go.Scatter(x=gamestop_data['Date'], y=gamestop_data['Close'], name='GameStop Stock Price'))
fig_gamestop.add_trace(go.Scatter(x=gamestop_revenue['Date'], y=gamestop_revenue['Revenue'], name='GameStop Revenue', yaxis='y2'))

fig_gamestop.update_layout(
    title="GameStop Stock Price and Revenue",
    xaxis_title="Date",
    yaxis_title="Stock Price",
    yaxis2=dict(
        title="Revenue",
        overlaying='y',
        side='right'
    )
)

fig_gamestop.show()
