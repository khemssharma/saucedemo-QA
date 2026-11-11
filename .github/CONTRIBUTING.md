# Contributing to saucedemo-QA

Thanks for your interest in improving **saucedemo-QA**, an end-to-end QA automation suite for saucedemo.com using Python, Selenium and Pytest with the Page Object Model. Bug reports, fixes, docs and new features are all welcome.

**Stack:** Python · Selenium · Pytest · Page Object Model

## Ways to contribute

- 🐛 **Report a bug:** [open a bug report](https://github.com/khemssharma/saucedemo-QA/issues/new?template=bug_report.yml)
- 💡 **Suggest a feature:** [open a feature request](https://github.com/khemssharma/saucedemo-QA/issues/new?template=feature_request.yml)
- 📝 **Improve the docs:** typos, unclear steps and missing examples all count
- 🔧 **Fix an issue:** look for issues labelled `good first issue` or `help wanted`

For anything bigger than a small fix, please **open an issue first**, so we can agree on the approach before you spend time on it.

## Local setup

```bash
git clone https://github.com/<your-username>/saucedemo-QA.git
cd saucedemo-QA
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

You need Google Chrome installed. Selenium Manager downloads the matching driver automatically.

## Project layout

| Path | What lives there |
| --- | --- |
| `pages/` | Page Objects: one class per page, holding locators and actions |
| `conftest.py` | Shared Pytest fixtures (browser setup and teardown) |
| `test_*.py` | Test cases |

## Making a change

1. **Fork** the repo and create a branch from `main`:
   ```bash
   git checkout -b feat/short-description   # or fix/…, docs/…, refactor/…
   ```
2. Make your change. Keep each PR focused on **one** thing.
3. Run the checks below.
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/):
   ```
   feat: add rematch button
   fix: handle disconnect during game
   docs: clarify .env setup
   ```
5. Push to your fork and open a pull request against `main`. Fill in the PR template.

## Checks before you open a PR

```bash
pytest -v                   # run the whole suite
pytest -v -k checkout       # run tests matching a keyword
```

All tests must pass locally before you open a PR.

## Project-specific guidelines

- **Follow the Page Object Model.** Locators and page actions go in a class in `pages/`. Tests should read like user steps and never call `find_element` directly.
- **No hard sleeps.** Use explicit waits (`WebDriverWait`) instead of `time.sleep`.
- **One behaviour per test.** Name tests `test_<what>_<expected_result>`, for example `test_login_with_locked_user_shows_error`.
- **Keep tests independent.** Each test sets up its own state through fixtures, so tests can run in any order.
- **Use saucedemo's public test users only.** Don't add real credentials.

## Code style

- Match the style of the code around your change.
- Use clear, descriptive names; avoid unexplained abbreviations.
- Remove debug logs and commented-out code before committing.
- Update the README if your change affects setup or usage.

## Reporting security issues

Please **don't open a public issue** for security vulnerabilities. Contact the maintainer privately through the [GitHub profile](https://github.com/khemssharma) with the details and steps to reproduce.

## Code of conduct

Be respectful and constructive. Harassment, personal attacks and spam aren't tolerated.

## License

This repository doesn't have an open-source license yet. Until one is added, by submitting a contribution you agree that it may be used, modified and distributed as part of this project.
