# Quantitative Strategy – Live Performance Tracking

This repository tracks a deep learning–based, market-neutral statistical arbitrage strategy deployed live in cryptocurrency futures since **January 31, 2025**. The system combines PCA residual factor construction with neural network models for daily portfolio construction. All metrics (live and backtest) and visualizations refresh automatically.

All plots and metrics are located in the `metrics/` directory.

---

## Model Versions

| Version | Dates                      | Key Changes / Notes |
| ------- | -------------------------- | ------------------- |
| **v1**  | 2025-01-31 → 2025-05-15     | Initial live deployment (residual signals + DL head) |
| **v2**  | 2025-05-15 → 2025-06-18     | Improved output stability to reduce stochasticity |
| **v3**  | 2025-06-21 → 2025-07-28     | Introduced dynamic position capping to limit outlier exposure |
| **v4**  | 2025-07-28 → Present        | Fixed a live/backtest implementation divergence; this is the first version expected to faithfully reflect backtest behavior (remaining differences from funding and slippage) |

---

## Performance Reporting

- **Sharpe Ratio**: Annualized by √365, assuming zero risk-free rate.  
- **Net Returns**: All returns are net of estimated transaction costs and slippage.  
- **Leverage Normalization**: Metrics are normalized to a zero-leverage baseline to ensure comparability across versions.

### Versioned Metrics

- Historical (v1–v3) performance is presented for transparency; these versions included implementation discrepancies and were exposed to turbulent regime conditions that contributed to divergence from backtest expectations.  
- **v4-only metrics** are highlighted as the current reliable baseline, post-fix, and are the primary reference for ongoing evaluation.

---

## Recent Improvements

- Diagnosed and corrected a subtle implementation mismatch between the live execution and backtest pipeline in v4, reducing pipeline drift and improving live/backtest alignment.  
- Enhanced risk controls (e.g., dynamic capping) and ensemble stability mechanisms over successive versions.  
- Ongoing monitoring indicates that v4 live performance now closely tracks the corresponding backtest, with residual deviations attributable to real-market frictions (funding, slippage).


<!---->
<!---->
<!---->
<!--# Quantitative Strategy – Live Performance Tracking-->
<!---->
<!---->
<!--This repository documents a deep learning–based, market-neutral statistical arbitrage strategy deployed live in the cryptocurrency futures market since **January 31, 2025**. The strategy is rebalanced once per day, with all performance metrics and visualizations automatically refreshed on a daily basis.-->
<!---->
<!--The core architecture combines **statistical factors-based residual construction** with deep neural networks to capture temporal patterns for portfolio construction.-->
<!---->
<!--All live and backtest-related metrics and plots are located in the `metrics` directory.-->
<!---->
<!------->
<!---->
<!--## Model Versions-->
<!---->
<!--| Version | Dates                      | Notes                                                                 |-->
<!--| ------- | -------------------------- | --------------------------------------------------------------------- |-->
<!--| **v1**  | 2025-01-31 → 2025-05-15     | Initial deployment using residual-based signals and DL prediction head |-->
<!--| **v2**  | 2025-05-15 → 2025-06-18     | Integrated model ensembling to improve stability |-->
<!--| **v3**  | 2025-06-21 → 2025-07-28     | Introduced dynamic position capping to mitigate outlier exposure risks |-->
<!--| **v4**  | 2025-07-28 → Present        | Fixed a crucial implementation bug. Consequently, models v2 and v3 may have performed significantly worse than what backtest presented |-->
<!---->
<!------->
<!---->
<!--## Key Assumptions-->
<!---->
<!--- **Sharpe Ratio**  -->
<!--  Computed assuming a zero risk-free rate and annualized by $\sqrt{365}$.-->
<!---->
<!--- **Net Performance**  -->
<!--  All returns are reported net of transaction costs and slippage.-->
<!---->
<!--- **Leverage Normalization**  -->
<!--  Leverage may be adjusted; however, all reported performance metrics are normalized to a **zero-leverage** baseline for consistency and comparability.-->





<!------->
<!---->
<!---->
<!---->
<!--## Notable Observations-->
<!---->
<!--- **2025-05-31 – Tail Event**  -->
<!--  Incurred a **-6.07% daily loss** due to a short position in **LPTUSDT**, which experienced a sudden 100+% daily surge. An extreme move rarely seen even in historical stress periods, and not the level of daily loss observed during backtest.-->
<!---->
<!--- **2025-06-17 – Over-concentration**  -->
<!--  The strategy assigned an unusually high **26.6% weight** to **MAGICUSDT**.-->
<!--  - **Fix**: Introduced max weight constraint in v3 to control excessive exposures.  -->
<!---->
<!--- **2025-07-01 – Tail Event**  -->
<!--  Incurred a **-4.66% daily loss** due to a short position in **HFTUSDT**, which rose over 100% in a single day.-->
<!---->
<!------->
<!---->
<!--## Strategy Thoughts-->
<!---->
<!---->
<!--### 2025-05-->
<!---->
<!--- **Intraday vs. Daily Divergence**: Noted that two tokens with nearly identical current-day daily return signals often showed very different intraday PnL paths.-->
<!--  - Hypothesis: Incorporating intraday signals may improve robustness.-->
<!--- **Sudden Dumps**: Some small cap altcoins exhibited sharp dumps with no preceding pumps. Could be due to growing fear in the market.-->
<!---->
<!------->
<!---->
<!--### 2025-06-->
<!---->
<!--- **Possible Regime Shift**: Since April 2025, the market may have entered a new regime not seen during the backtest period.-->
<!--  - Following tariff announcements and geopolitical tensions, behavior seems to have become non-stationary. The frequent and sudden direction/sentiment reversals regime may not be ideal for the model.-->
<!---->
<!------->
