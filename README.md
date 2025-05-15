# Quantitative Strategy – Live Performance Tracking

This repository hosts a market-neutral quantitative portfolio management strategy that has been running live in the cryptocurrency market since **January 31, 2025**. The portfolio is rebalanced once per day, and all performance metrics and visualizations are updated automatically on a daily cadence.

---

## Key Considerations

- **Sharpe Ratio**  
  Calculated assuming a zero risk-free rate and annualized by a factor of $\sqrt{365}$.

- **Model Version**  
  Version 2 of the strategy was deployed on **May 15, 2025 00:00:00 UTC**, superseding the original implementation.

- **Net Performance**  
  All metrics reflect returns net of transaction costs and slippage.

- **Leverage & Scaling**  
  While the strategy may employ dynamic leverage and capital adjustments, all return series are reported on a zero-leverage basis for comparability.

---

## Interactive Dashboard

Interactive performance statistics and visualizations via the [Quant Strategy Dashboard](https://quant-strat-live-performance-daqdrmca2knbflylgh7vxh.streamlit.app/).

---

## Daily Metrics

- **`evaluation_summary.csv`**  
  End-of-day summary of key performance and risk metrics (e.g., Sharpe ratio, maximum drawdown, volatility).

---

## Performance Visualizations

- **`cumulative_return.png`**  
  Cumulative portfolio return over time.

- **`drawdown.png`**  
  Drawdown curve illustrating peak-to-trough declines.

- **`monthly_returns_heatmap.png`**  
  Heatmap displaying monthly return performance.
