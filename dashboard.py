import streamlit as st
import pandas as pd
import os
from PIL import Image

st.title('Quant Strategy Performance Dashboard')

def load_metrics():
    df = pd.read_csv('metrics/evaluation_summary.csv')
    return df

metrics_df = load_metrics()

st.header('📊 Performance Metrics')
st.dataframe(metrics_df, use_container_width=True)

st.sidebar.header('Available Plots')
plot_choices = [
    'Cumulative Return',
    'Monthly Returns Heatmap',
    'Rolling Metrics',
    'Returns Distribution',
    'Drawdown',
    'Scatter vs BTC/ETH',

]

plot_files = {
    'Cumulative Return': 'cumulative_return.png',
    'Monthly Returns Heatmap': 'monthly_returns_heatmap.png',
    'Rolling Metrics': 'rolling_metrics_30_days.png',
    'Returns Distribution': 'distribution_returns.png',
    'Drawdown Over Time': 'drawdown.png',
    'Scatter vs BTC/ETH': 'scatter_strategy_vs_btc_eth.png',

}

selected_plot = st.sidebar.selectbox('Select Plot to View:', list(plot_files.keys()))

selected_plot_file = plot_files[selected_plot]

full_plot_path = os.path.join("metrics", selected_plot_file)

st.subheader(selected_plot)
img = Image.open(full_plot_path)
st.image(img, use_container_width=True)


st.sidebar.header('Strategy Information')
st.sidebar.info("""
This dashboard presents **live**, deployed performance metrics and visualizations for the quantitative market-neutral portfolio strategy. Deployed in the cryptocurrency market since January 31, 2025, the strategy's metrics and visualizations are automatically updated daily to reflect the most recent market performance.

Key analytics provided include cumulative returns, Sharpe ratios, drawdown analyses, monthly returns heatmaps, rolling performance metrics, returns distribution, and comparative scatter plots against benchmark cryptocurrencies such as BTC and ETH.
""")
