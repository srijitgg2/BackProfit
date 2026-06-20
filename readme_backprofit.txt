======================================================
                 BACKPROFIT GUIDE
======================================================

Welcome to BackProfit (locally known as StockRocket)! 
This is your AI-enabled trading, investing, and backtesting platform.

1. OVERVIEW
-----------
BackProfit allows you to combine technical indicators, company fundamentals, and AI-generated synthesis into one market analysis cockpit. A key feature is the "Backtest Workspace", where you can run trading strategies against historical market data to see how they would have performed.

2. RUNNING A BACKTEST
---------------------
1. Navigate to the "Backtest" tab in the application.
2. Market Data:
   - Ticker Symbol: Enter the stock symbol you want to test (e.g., AAPL). For Indian stocks, suffix it with .NS (e.g., RELIANCE.NS).
   - Date Range: Choose the historical window for your test.
   - Interval: Choose 1 day, 1 week, or 1 month candles.
3. Conditions:
   - Define your Buy Conditions (e.g., RSI <= 40).
   - Define your Sell Conditions (e.g., RSI >= 60).
   - Both buy and sell logic support RSI, MACD bounds, and SMA filters.
4. Run:
   - Click "Run Backtest". The system will scan historical data and generate a performance report.

3. INTERPRETING RESULTS
-----------------------
- Win Rate: The percentage of trades that were profitable.
- Max Drawdown: The maximum observed loss from a peak to a trough.
- Profit Factor: The ratio of gross profits to gross losses.
- CAGR / Total Return: Your annualized and overall returns over the tested period.
- You can review every single trade triggered in the "Trade Log" table.

4. DOWNLOADING & EMAILING REPORTS
---------------------------------
Because BackProfit is designed to be fully stateless and cloud-deployable (e.g., on Vercel), your backtest reports are generated and embedded directly into your browser memory!
- Download: Click "Download Excel Report" to instantly save a multi-tab .xlsx file with Risk Metrics, Trade Logs, and Raw Signals.
- Email: Type your email address and click "Email Report" to have the same Excel file sent directly to your inbox.

5. DEPLOYMENT (VERCEL)
----------------------
If you are deploying BackProfit to Vercel, the application is pre-configured to work smoothly.
- Vercel uses the `@vercel/python` builder defined in `vercel.json`.
- Keep an eye on the "Logs" tab in your Vercel Dashboard if you see a `500: INTERNAL_SERVER_ERROR`. On the free Hobby tier, heavy analyses (like massive historical datasets) might exceed the 10-second serverless execution limit.
- If timeouts occur frequently, consider testing over shorter date ranges or upgrading your hosting tier.

======================================================
Happy testing and may your backtests be profitable!
