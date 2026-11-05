# Functional Testing & CI/CD Pipeline Assignment

A robust Python Flask web application featuring strict test-driven development, 100% code coverage enforcement, automated multi-version GitHub Actions CI/CD workflows, secure deployment webhooks, and live health/commit tracking.

---

## Project Structure

```text
functional-testing-2507203/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD pipeline configuration
├── static/                    # Frontend styling / assets
├── templates/                 # HTML templates (including live commit SHA footer)
├── tests/
│   └── test_target.py         # Pytest test suite ensuring 100% coverage
├── app.py                     # Flask application with /health and commit tracking
├── target.py                  # Core logic module under test
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation