# OrangeHRM Test Automation (Python + Playwright)

Automated UI test suite for the [OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/),
built with **Playwright** + **pytest**, using the **Page Object Model (POM)**.

## Project Structure

```
orangehrm-playwright-tests/
├── pages/                  # Page Object classes (one per screen/module)
│   ├── base_page.py        # Shared helpers (click, fill, waits, etc.)
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── pim_page.py
├── tests/                  # Test cases (pytest)
│   ├── test_login.py
│   ├── test_dashboard.py
│   └── test_pim.py
├── utils/
│   └── config.py           # Reads env vars (base URL, credentials)
├── conftest.py             # Pytest fixtures (browser, page, logged_in_page)
├── pytest.ini               # Pytest config (markers, HTML report)
├── requirements.txt
├── .env                     # Base URL + demo credentials
└── README.md
```

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install chromium
# or: playwright install    (installs chromium, firefox, webkit)
```

## Running Tests

```bash
# Run everything
pytest

# Run only smoke tests
pytest -m smoke

# Run only regression tests
pytest -m regression

# Run a single file
pytest tests/test_login.py

# Run with browser visible (edit conftest.py: headless=False)
pytest -s

# Run in parallel (optional, install pytest-xdist first)
pip install pytest-xdist
pytest -n auto
```

An HTML report is generated automatically at `reports/report.html` after every run
(configured via `pytest.ini`).

## What's covered

- **Login**: valid login, invalid credentials, empty-field validation, logout
- **Dashboard**: post-login load check, sidebar navigation across modules
- **PIM**: adding a new employee, searching for an employee

## Design notes

- **Page Object Model**: every screen is a class in `pages/`, holding its locators
  and actions. Tests never touch raw Playwright locators directly — this keeps
  tests readable and means a UI change only requires updating one page class.
- **`logged_in_page` fixture** (in `conftest.py`): most OrangeHRM modules require
  auth, so this fixture logs in once per test and hands back an authenticated page,
  avoiding copy-pasted login code in every test.
- **`.env` config**: base URL and credentials are not hardcoded in tests, so you can
  point the suite at a different environment by editing `.env`.
- **Markers** (`smoke` / `regression`): lets you run a fast subset in CI on every
  commit, and the fuller set on a schedule.

## Next steps you could add

- More modules: Leave requests, Recruitment (candidate add), Admin (user management)
- API-layer tests using Playwright's `request` fixture for faster setup/teardown
  (e.g. creating test employees via API instead of the UI)
- CI integration (GitHub Actions) to run the suite on every push
- Visual regression or accessibility checks
