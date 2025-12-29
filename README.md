# Selenium Automation Framework for AQX Trader

This project is a Selenium automation framework designed to test the [AQX Trader](https://aqxtrader.aquariux.com/web/login) platform. It uses Python and Pytest to ensure robust automated testing of trading functionalities.

## Features / Test Scenarios

The framework covers (or aims to cover) the following key trading functionalities:

1.  **Buy/Sell order without One-Click Trading function**
    - Verification of standard order placement flow involving confirmation steps.
2.  **See the list of trading transactions and order notifications**
    - validation of transaction history and real-time order notifications.
3.  **Bulk close / delete orders**
    - Testing functionality to close multiple positions or delete multiple pending orders simultaneously.
4.  **Place Market with Stop Loss and Take Profit**
    - Executing market orders with attached SL/TP parameters.
5.  **Edit, partial close and close Open position**
    - Modifying existing open positions, including partial closures and full closures.
6.  **Place Limit / Stop order with different types of Expiry**
    - Creating pending orders (Limit/Stop) with various expiry settings (GTC, GTD, etc.).
7.  **Edit Pending Orders for all values included**
    - Updating parameters (Price, SL, TP, Expiry) of existing pending orders.

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

To run the tests, use the following command from the root directory:

```bash
pytest tests/test_login.py --html=report.html
```

## Project Structure

- `pages/`: Page Object Model (POM) classes representing web pages.
- `tests/`: Test scripts using Pytest.
- `report.html`: Generated test report (after running tests).
