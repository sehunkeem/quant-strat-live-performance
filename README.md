# Quantitative Strategy – Live Performance Tracking


This repository documents a deep learning–based, market-neutral statistical arbitrage strategy deployed live in the cryptocurrency futures market since **January 31, 2025**. The strategy is rebalanced once per day, with all performance metrics and visualizations automatically refreshed on a daily basis.

The core architecture combines **PCA-based residual construction** with deep neural networks to capture temporal patterns for portfolio construction.

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

- **2025-05-31 – Tail Event**  
  Incurred a **-6.07% daily loss** due to a short position in **LPTUSDT**, which experienced a sudden 100+% daily surge. An extreme move rarely seen even in historical stress periods, and not the level of daily loss observed during backtest.

- **2025-06-17 – Over-concentration**  
  The strategy assigned an unusually high **26.6% weight** to **MAGICUSDT**.
  - **Fix**: Introduced max weight constraint in v3 to control excessive exposures.  

- **2025-07-01 – Tail Event**  
  Incurred a **-4.66% daily loss** due to a short position in **HFTUSDT**, which rose over 100% in a single day.

---

## Strategy Thoughts


### 2025-05

- **Intraday vs. Daily Divergence**: Noted that two tokens with nearly identical current-day daily return signals often showed very different intraday PnL paths.
  - Hypothesis: Incorporating intraday signals may improve robustness.
- **Sudden Dumps**: Some small cap altcoins exhibited sharp dumps with no preceding pumps. Could be due to growing fear in the market.

---

### 2025-06

- **Possible Regime Shift**: The market may have entered a new regime not seen during the backtest period.
  - Following tariff announcements and geopolitical tensions, behavior seems to have become non-stationary. The frequent and sudden direction/sentiment reversals regime may not be ideal for the model.

---

## Key Assumptions

- **Sharpe Ratio**  
  Computed assuming a zero risk-free rate and annualized by $\sqrt{365}$.

- **Net Performance**  
  All returns are reported net of transaction costs and slippage.

- **Leverage Normalization**  
  Leverage may be adjusted; however, all reported performance metrics are normalized to a **zero-leverage** baseline for consistency and comparability.
