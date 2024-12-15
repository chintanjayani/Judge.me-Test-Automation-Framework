# Judge.me Test Automation Framework

A cross-platform test automation framework for Judge.me reviews platform using Python and Playwright.


## Prerequisites and Local Setup Guide
- Python 3.8+
- pip
- Git

1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```bash
   playwright install
   ```
   
4. Install Node if want to run performance tests locally 
    ```bash
    # installs nvm (Node Version Manager)
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
    # download and install Node.js (you may need to restart the terminal)
    nvm install 22
    npm -v
    #install artillery
    npm install -g artillery
    ```

## Running Tests
To run all tests:
```bash
pytest --html=reports/report.html
```
or
```bash
python run_tests.py
```

To run specific test categories:
```bash
pytest -m ui --html=reports/report.html  # UI tests only
pytest -m api --html=reports/report.html  # API tests only
```

### Note: All the UI test runs in headless mode, to enable run with a browser set HEADLESS=false in .env file

## Test Reports
- HTML reports are generated in the `reports` directory after each test run

## CI/CD Integration
This framework includes GitHub Actions configuration for automated test execution on push and pull requests.


## Test Coverage
High-priority areas covered:
1. Review page UI checks 
2. Review filtering and sorting
3. Product and Review Search
4. Currency Filters
5. API tests for review search endpoint
6. Performance tests for review search endpoint

## Bugs
1. Session doesn’t expire
2. Footer still contains year 2023 
3. After page change UI doesn’t move to top most review
4. Automatic window resolution doesnt work properly
5. Review search API give 504 for Invalid parameters
6. Once a review is deleted change doesn’t reflect on the UI for long time

## Framework Features Overview
1. Page Object Model design pattern
2. Separate UI and API test suites
3. Config management for different environments
4. HTML report generation
5. CI/CD integration with GitHub Actions
6. Screenshots on failures
7. Performance tests with Artillery in CI/CD and Locally
8. Environment variables support for variable configs


## Future Test Areas
- Filter functionality
- Pagination
- Review ratings distribution
- Mobile responsiveness
- Accessibility checks
- Performance metrics (SLO/SLIs)
- Cross-browser testing
- Advanced search scenarios
- Advanced API test coverage
- Currency changes checks
- Photo/Video reviews check
- E2E product review life cycle
- Broken images/links UI checks
- UI self serve toggle tests
- User/Business E2E tests
- Security testing for UI/API
- Localization tests

