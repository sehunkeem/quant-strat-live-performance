# Quantitative Strategy – Live Performance Tracking

This repository hosts a market-neutral quantitative portfolio management strategy that has been running live in the cryptocurrency market since **January 31, 2025**. The portfolio is rebalanced once per day, and all performance metrics and visualizations are updated automatically on a daily cadence.

---

## Key Considerations

- **Sharpe Ratio**  
  Computed assuming a zero risk-free rate and annualized by $\sqrt{365}$.

- **Net Performance**  
  All returns are reported net of transaction costs and slippage.

- **Leverage & Scaling**  
  While leverage and capital may be adjusted dynamically at my discretion, all returns are normalized to a zero-leverage basis for consistency.

---

## Model Version & History

**Current:** v2 (deployed **2025-05-15 00:00 UTC**)  
**Previous:** v1 (2025-01-31 → 2025-05-14)

| Version | Effective Dates           | Notes                      |
| ------- | ------------------------- | -------------------------- |
| **v1**  | 2025-01-31 to 2025-05-14  | initial deployment         |
| **v2**  | 2025-05-15 to present     | model improvement          |

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
