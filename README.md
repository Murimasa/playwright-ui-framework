# 🎭 Playwright UI Automation Framework

[![UI Automation Tests (Playwright)](https://github.com/Murimasa/playwright-ui-framework/actions/workflows/ui_tests.yml/badge.svg)](https://github.com/Murimasa/playwright-ui-framework/actions/workflows/ui_tests.yml)
[![Allure Report](https://img.shields.io/badge/Allure_Report-Live_Dashboard-success?logo=allure)](https://Murimasa.github.io/playwright-ui-framework/)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-Chromium-green)
![Pytest](https://img.shields.io/badge/Pytest-Automation-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

An enterprise-ready end-to-end (E2E) UI testing framework built with **Python**, **Playwright**, and **Pytest**, strictly following the **Page Object Model (POM)** design pattern.

The test suite validates critical user journeys, boundary conditions, and state management for the [SauceDemo](https://www.saucedemo.com/) e-commerce web platform.

📊 **Live Test Report:** [View Live Allure Dashboard](https://Murimasa.github.io/playwright-ui-framework/)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Architectural Features](#-key-architectural-features)
- [Test Suite Coverage (19 Tests)](#-test-suite-coverage-19-tests)
- [Project Architecture](#-project-architecture)
- [Prerequisites](#-prerequisites)
- [Local Setup & Execution](#-local-setup--execution)
- [Allure Reporting](#-allure-reporting)
- [CI/CD Pipeline](#-cicd-pipeline)

---

## 🔎 Overview

This repository demonstrates modern automated UI testing standards for single-page applications (SPA). It eliminates flakiness through Playwright's built-in auto-waiting mechanisms and web-first assertions, isolates page interactions into reusable components via POM, and offers full visibility into test runs with step-by-step Allure reporting and automatic failure screenshot capture.

---

## ✨ Key Architectural Features

- **Page Object Model (POM)**: Complete separation between test logic and UI selectors/interactions across base and child page objects.
- **Web-First Assertions**: Relies on Playwright's async assertions (`expect(locator).to_be_visible()`, `to_have_text()`) to minimize race conditions without explicit sleeps.
- **Data-Driven Testing (DDT)**: Exhaustive test matrix coverage via `@pytest.mark.parametrize` for negative login variants, checkout form errors, and catalog sorting.
- **Automatic Failure Artifacts**: Pytest hooks configured to capture screenshot artifacts and page state automatically upon test failure.
- **Modular Fixture Architecture**: Decoupled browser context and page fixture provisioning via `conftest.py` and dedicated fixture modules.
- **CI/CD Orchestration**: Automated test execution via GitHub Actions with immediate deployment to GitHub Pages for live reporting.

---

## 🧪 Test Suite Coverage (19 Tests)

| Module | Test Suite / Focus | Scenarios Covered |
| :--- | :--- | :--- |
| **`test_login.py`** | Authentication & Access Control | Standard login, locked-out user verification, parameterized empty and invalid credential combinations. |
| **`test_inventory.py`** | Catalog & App State Management | Parameterized sorting (A-Z, Z-A, Price Low-High, Price High-Low), App State Reset (cart badge clearance), and Logout flow. |
| **`test_cart.py`** | Cart Lifecycle & Navigation | Adding items, cart badge count updates, single-item deletion, and Step 1 / Step 2 checkout cancel returns. |
| **`test_checkout.py`** | End-to-End Purchase Flow | Complete checkout journey (Information -> Overview -> Order Confirmation) and parameterized form validation checks. |

---

## 🗂 Project Architecture

```text
playwright-ui-framework/
├── .github/
│   └── workflows/
│       └── ui_tests.yml               # GitHub Actions CI pipeline and Allure publishing
├── fixtures/
│   └── page_fixtures.py           # Dependency injection fixtures for page objects
├── pages/
│   ├── base_page.py               # Abstract base page providing shared actions and navigation
│   ├── login_page.py              # Login page locators and authentication methods
│   ├── inventory_page.py          # Catalog sorting, cart badges, and sidebar controls
│   ├── cart_page.py               # Cart items, item removal, and checkout trigger
│   ├── checkout_step_one_page.py  # Customer information form inputs and validation errors
│   └── checkout_step_two_page.py  # Overview calculations, finish action, and completion headers
├── tests/
│   ├── test_login.py              # Authentication test specifications
│   ├── test_inventory.py          # Catalog behavior, sorting, and menu actions
│   ├── test_cart.py               # Cart modifications and cancel navigation checks
│   └── test_checkout.py           # End-to-end checkout completion and input validation
├── conftest.py                    # Root pytest fixtures and failure screenshot hooks
├── pytest.ini                     # Global Pytest configuration and Allure directory path
└── requirements.txt               # Locked project dependencies
```

---

## 🛠 Prerequisites

Ensure you have the following installed locally:
- **Python 3.11+**
- **pip** package manager
- **Java (JRE/JDK 11+)** *(Required only for rendering Allure CLI reports locally)*

---

## 💻 Local Setup & Execution

### 1. Clone the repository and initialize virtual environment
```bash
git clone https://github.com/Murimasa/playwright-ui-framework.git
cd playwright-ui-framework

python -m venv .venv
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate
```

### 2. Install dependencies and browser binaries
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Run the automated test suite
```bash
# Run all tests in headless mode with Allure telemetry
pytest --alluredir=allure-results --clean-alluredir

# Run in headed mode (visible browser window)
pytest --headed

# Run a specific test module
pytest tests/test_checkout.py
```

---

## 📊 Allure Reporting

Generate and open the interactive dashboard directly in your default browser:

```bash
allure serve allure-results
```

The report provides:
- Categorized suites matching `@allure.feature` and `@allure.story` annotations.
- Step-by-step breakdown with execution timestamps.
- Attached screenshots on any test failure.

---

## 🚀 CI/CD Pipeline

The framework is configured with a GitHub Actions workflow (`ui_tests.yml`):
- Runs automatically on every `push` and `pull_request` targeting `main`.
- Sets up Python, installs dependencies, and acquires Chromium binaries.
- Executes the entire test suite in headless mode.
- Builds and publishes the interactive Allure Dashboard to **GitHub Pages** on every successful run.