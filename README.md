# Quantitative Strategy – Live Performance Tracking

This repository hosts a market-neutral quantitative portfolio management strategy that has been running live in the cryptocurrency market since **January 31, 2025**. The portfolio is rebalanced once per day, and all performance metrics and visualizations are updated automatically on a daily cadence.


All live and backtest-related metrics and plots are located in the `metrics` directory.

---

## Key Assumptions

- **Sharpe Ratio**  
  Computed assuming a zero risk-free rate and annualized by $\sqrt{365}$.

- **Net Performance**  
  All returns are reported net of transaction costs and slippage.

- **Leverage Normalization**  
  Leverage may be adjusted; however, all reported performance metrics are normalized to a **zero-leverage** baseline for consistency and comparability.

---

## Model Versions

| Version | Dates                      | Notes                                                                 |
| ------- | -------------------------- | --------------------------------------------------------------------- |
| **v1**  | 2025-01-31 → 2025-05-15     | Initial deployment using residual-based signals and DL prediction head |
| **v2**  | 2025-05-15 → 2025-06-18     | Integrated model ensembling to improve stability |
| **v3**  | 2025-06-21 → Present        | Introduced dynamic position capping to mitigate outlier exposure risks |

---

## Daily Metrics

- **`evaluation_summary.csv`**  
  Contains end-of-day performance and risk statistics (e.g., Sharpe, volatility, max drawdown).

---

## Performance Visualizations

- **`cumulative_return.png`** – Cumulative net return  
- **`drawdown.png`** – Peak-to-trough drawdown curve  
- **`monthly_returns_heatmap.png`** – Calendar heatmap of monthly returns
