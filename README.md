# ML-Driven-Equity-Return-Prediction-Engine
A production-quality, end-to-end pipeline for predicting equity returns using machine-learning, engineered with reproducibility and rigor. Designed to demonstrate advanced quantitative methods, robust software engineering practices, and clear performance analytics in line with the D. E. Shaw Group’s standards for data-driven research.

# Contact
For questions or feedback, reach out to Kenneth LeGare at kennethlegare5@gmail.com or open an issue on GitHub

# Project Overview
This repository implements a systematic workflow to:

-   Ingest and validate historical OHLCV price data and company fundamentals

-   Engineer predictive features (momentum, volatility, valuation spreads)

-   Train and evaluate Random Forest and XGBoost models under time-series cross-validation

-   Backtest a long/short decile equity strategy with full performance and risk metrics

-   Visualize signals, feature importances, and P&L through an interactive dashboard

All code is modular, extensively tested, and documented to ensure transparency and reproducibility.

# Key Features
-   Data ingestion from Yahoo Finance and EDGAR API

-   Automated feature engineering with leakage avoidance

-   Hyperparameter tuning via GridSearchCV or RandomizedSearchCV

-   Backtester supporting transaction costs, slippage, and risk analysis

-   Unit tests with pytest and coverage reports

-   Interactive Plotly dashboard for real-time results exploration

# Pipeline Workflow
1. Data Ingestion (scripts/run_ingestion.py) Fetch raw price and fundamental data, perform sanity checks, and version outputs in data/raw/.

2. Feature Engineering (scripts/run_features.py) Compute momentum, volatility, valuation metrics, and save cleaned features to data/processed/.

3. Model Training (scripts/run_training.py) Train and validate Random Forest and XGBoost models using time-series cross-validation; save best models under models/.

4. Backtesting (scripts/run_backtest.py) Simulate long/short decile strategy, calculate performance and risk metrics, and export results to results/.

5. Dashboard (dashboards/app.py) Launch a Plotly Dash application for interactive exploration of signals, P&L, and risk analytics

# Contributing
-   Fork the repository and create feature branches (git checkout -b feature/xyz)

-   Write clear, descriptive commit messages

-   Submit pull requests with detailed descriptions and pass all CI checks