# Quantitative Strategy – Live Performance Tracking

This repository hosts a deep-learning driven market-neutral quantitative portfolio management strategy that has been running live in the cryptocurrency market since **January 31, 2025**. The portfolio is rebalanced once per day, and all performance metrics and visualizations are updated automatically on a daily cadence.


All live and backtest-related metrics and plots are located in the `metrics` directory.

---

## Model Versions

| Version | Dates                      | Notes                                                                 |
| ------- | -------------------------- | --------------------------------------------------------------------- |
| **v1**  | 2025-01-31 → 2025-05-15     | Initial deployment using residual-based signals and DL prediction head |
| **v2**  | 2025-05-15 → 2025-06-18     | Integrated model ensembling to improve stability |
| **v3**  | 2025-06-21 → Present        | Introduced dynamic position capping to mitigate outlier exposure risks |

---



## Notable Observations

This section highlights significant stress events, model failures, and noteworthy patterns encountered during live trading.

- **2025-05-31 – Tail Event**  
  Incurred a **-6.07% daily loss** due to a short position in **LPTUSDT**, which experienced a sudden **100+% daily surge**.

- **2025-06-17 – Over-concentration**  
  The strategy assigned an unusually high **26.6% weight** to **MAGICUSDT**.
  - **Fix**: Introduced **max weight constraint** in v3 to control excessive exposures.  

- **2025-07-01 – Tail Event**  
  Incurred a **-4.66% daily loss** due to a short position in **HFTUSDT**, which rose over **100% in a single day** — an extreme move rarely seen even in historical stress periods.

---

## Strategy Thoughts

This section documents evolving thoughts about market behavior and model limitations observed during live deployment. Entries are grouped by month.

---

### 2025-05

- **Intraday vs. Daily Divergence**: Noted that two tokens with nearly identical current-day **daily return signals** often showed **very different intraday PnL paths**.
  - Hypothesis: Incorporating **intraday signals** may improve robustness.
- **Sudden Dumps**: Some small cap altcoins exhibited sharp dumps with no preceding pumps.

---

### 2025-06

- **Possible Regime Shift**: The market may have entered a new regime not seen during the backtest period.
  - Following tariff announcements and geopolitical tensions, behavior seems to have become **non-stationary**. The frequent and sudden direction and sentiment reversals regime may not be ideal for the model.
  
<!------->
<!---->
<!--### 2025-07-->
<!---->
<!--- Observation: tokens that outperform on one day **often continue to outperform** for 1–3 days.-->
<!--- Could signal a **temporary momentum regime** emerging.-->
<!--- Ongoing investigation: Can a regime classifier detect this and adapt allocation?-->
<!---->
---


## Daily Metrics

- **`evaluation_summary.csv`**  
  Contains end-of-day performance and risk statistics (e.g., Sharpe, volatility, max drawdown).

---

## Performance Visualizations

- **`cumulative_return.png`** – Cumulative net return  
- **`drawdown.png`** – Peak-to-trough drawdown curve  
- **`monthly_returns_heatmap.png`** – Calendar heatmap of monthly returns


---

## Key Assumptions

- **Sharpe Ratio**  
  Computed assuming a zero risk-free rate and annualized by $\sqrt{365}$.

- **Net Performance**  
  All returns are reported net of transaction costs and slippage.

- **Leverage Normalization**  
  Leverage may be adjusted; however, all reported performance metrics are normalized to a **zero-leverage** baseline for consistency and comparability.
