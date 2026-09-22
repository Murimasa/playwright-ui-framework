# Playwright UI Automation Framework

[![UI Automation Tests (Playwright)](https://github.com/Murimasa/playwright-ui-framework/actions/workflows/ui_tests.yml/badge.svg)](https://github.com/Murimasa/playwright-ui-framework/actions/workflows/ui_tests.yml)
[![Allure Report](https://img.shields.io/badge/Allure_Report-Live_Dashboard-success?logo=allure)](https://Murimasa.github.io/playwright-ui-framework/)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-Chromium-green)
![Pytest](https://img.shields.io/badge/Pytest-Automation-orange)

Automated end-to-end UI testing framework built with **Python**, **Playwright**, and **Pytest**, implementing the **Page Object Model (POM)** pattern.

The test suite covers the complete purchase flow and edge cases for the [SauceDemo](https://www.saucedemo.com/) e-commerce web application.

📊 **Live Test Report:** [View Allure Dashboard](https://Murimasa.github.io/playwright-ui-framework/)

---

## 🏗️ Project Architecture

The framework follows a modular Page Object Model structure:

```text
playwright-ui-framework/
├── .github/workflows/
│   └── ui_tests.yml               # CI pipeline with Allure deployment
├── fixtures/
│   └── page_fixtures.py           # Modular page fixture injections
├── pages/
│   ├── base_page.py               # Core base page with shared navigation methods
│   ├── login_page.py              # Authentication page locators and actions
│   ├── inventory_page.py          # Product catalog interactions and cart badges
│   ├── cart_page.py               # Shopping cart assertions and item removal
│   ├── checkout_step_one_page.py  # Buyer information form
│   └── checkout_step_two_page.py  # Order review and confirmation
├── tests/
│   ├── test_login.py              # Positive and parameterized negative login tests
│   ├── test_inventory.py          # Catalog rendering and cart badge validation
│   ├── test_cart.py               # Cart contents and item removal tests
│   └── test_checkout.py           # E2E checkout journey and validation checks
├── conftest.py                    # Plugin registrations and failure screenshot hook
├── pytest.ini                     # Pytest configuration and Allure directory path
└── requirements.txt               # Project dependencies