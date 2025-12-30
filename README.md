# Selenium Automation Framework for AQX Trader

This project is a Selenium automation framework designed to test the [AQX Trader](https://aqxtrader.aquariux.com/web/login) platform. It uses Python and Pytest to ensure robust automated testing of trading functionalities.

## Features / Test Scenarios

The framework currently covers the following trading scenarios as implemented in `tests/test_trading.py`:

### 1. Market Orders
- **Buy Market Order**: Place a standard Buy Market order and verify position opening.
- **Sell Market Order**: Place a standard Sell Market order and verify position opening.
- **Buy Market with SL/TP**: Place a Buy Market order with Stop Loss and Take Profit levels associated.
- **Sell Market with SL/TP**: Place a Sell Market order with Stop Loss and Take Profit levels associated.

### 2. Position Management
- **Edit Position**: Edit an existing open position to update Stop Loss and Take Profit levels.
- **Close Position**: Fully close an existing open position and verify removal from the list.
- **Partial Close**: Partially close a position (e.g., closing 1 lot of a 2 lot position) and verify the remaining volume.

### 3. Pending Orders (Limit & Stop) with Expiry
- **Buy Limit Order (GTC)**: Place a Buy Limit order with "Good Till Canceled" expiry.
- **Buy Stop Order (GTC)**: Place a Buy Stop order with "Good Till Canceled" expiry.
- **Buy Limit Order (GTD)**: Place a Buy Limit order with "Good Till Day" expiry.
- **Buy Stop Order (GTD)**: Place a Buy Stop order with "Good Till Day" expiry.
- **Buy Limit Order (Specified Date)**: Place a Buy Limit order expiring on a specified date.
- **Buy Stop Order (Specified Date)**: Place a Buy Stop order expiring on a specified date.
- **Buy Limit Order (Specified Date & Time)**: Place a Buy Limit order expiring on a specific date and time.
- **Buy Stop Order (Specified Date & Time)**: Place a Buy Stop order expiring on a specific date and time.
- **Edit Pending Order**: Edit an existing pending order (Limit/Stop) to update Stop Loss and Take Profit levels.

### 4. Bulk Operations
- **Bulk Close All Positions**: Close all open positions simultaneously and verify that no open positions remain.

## Prerequisites

- Python 3.x
- Google Chrome Browser

## Installation

1.  Clone the repository.
2.  Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

To run the trading tests, use the following command from the root directory:

```bash
pytest tests/test_trading.py --html=report_trading.html --alluredir=allure-results
```

### Generating Allure Report

**Prerequisite:**
To view the report, you must have the **[Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline)** tool installed on your system (e.g., via `scoop install allure` on Windows or `brew install allure` on macOS). This is separate from the python library installed via `requirements.txt`.

**Steps:**
1.  **Generate Data**: Run the tests with the `--alluredir` flag (included in the command above).
2.  **View Report**: Run the following command to serve the report in your browser:

```bash
allure serve allure-results
```

## Project Structure

- `pages/`: Page Object Model (POM) classes representing web pages (`trading_page.py`, `login_page.py`).
- `tests/`: Test scripts using Pytest.
- `report_trading.html`: Generated test report for trading tests.
