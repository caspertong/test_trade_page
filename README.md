# Selenium Automation Framework for eCommerce

This project is a Selenium automation framework designed to test the eCommerce platform. It uses Python and Pytest to ensure robust automated testing of key functionalities.

## Prerequisites

- Python 3.x
- Google Chrome Browser
- **[Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline)** tool (for viewing reports)
  - Windows: `scoop install allure`
  - macOS: `brew install allure`

## Installation

1.  Clone the repository.
2.  Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Running Tests

To run the eCommerce tests and generate the Allure results, execute the following command from the root directory:

```bash
python -m pytest tests/test_ecommerce.py --alluredir=allure-results
```

## Viewing Test Reports

After running the tests, you can view the detailed Allure report by running:

```bash
allure serve allure-results
```

This command will start a local server and open the report in your default web browser.

## Project Structure

- `pages/`: Page Object Model (POM) classes representing web pages.
- `tests/`: Test scripts using Pytest (e.g., `test_ecommerce.py`).
- `requirements.txt`: Python dependencies required for the project.
