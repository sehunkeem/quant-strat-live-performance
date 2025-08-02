# Quantitative Strategy – Live Performance Tracking


This repository tracks a deep-learning, market-neutral statistical-arbitrage strategy deployed live in cryptocurrency futures since **31 Jan 2025**.  
The system combines PCA-based residual factors with neural networks for daily portfolio construction.  
All live and back-test metrics refresh automatically and are published under **`metrics/`**.

---

## Recent Improvements

| Date        | Change |
|-------------|--------|
| **2025-07-28 (v4)** | **Pipeline fix** – removed a subtle live/back-test logic mismatch that had lowered live Sharpe; live results now track back-tests except for normal frictions (funding, slippage). |
| 2025-06-21 (v3) | Added dynamic position caps to curb tail exposure. |
| 2025-05-15 (v2) | Stabilized model outputs to reduce stochastic noise. |

*(Earlier versions kept for full transparency; v4 is the baseline.)*

---

## Model Versions

| Version | Dates | Key Notes |
|---------|-------|-----------|
| **v1** | 2025-01-31 → 2025-05-15 | Initial deployment |
| **v2** | 2025-05-15 → 2025-06-18 | Output-stability enhancements |
| **v3** | 2025-06-21 → 2025-07-28 | Dynamic position capping |
| **v4** | 2025-07-28 → **Present** | Pipeline fix — first version expected to align closely with back-tests |

---

## Performance Reporting

* **Sharpe Ratio** – annualized by √365, zero risk-free rate  
* **Net Returns** – after estimated fees & slippage  
* **Leverage Normalization** – all metrics shown on a 1x baseline

### Versioned Metrics

- **v1–v3 (historical):** Shown for transparency. v2–v3 contained a live/back-test logic mismatch and ran through highly volatile market regimes, may have produced live Sharpe well below the backtest Sharpe.  

- **v4-only (current baseline):** Post-fix metrics; first version that reliably mirrors the back-test. These are the primary numbers to reference going forward.

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
