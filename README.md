# Daily Digest Automation

A Python automation project for collecting useful daily content and presenting it in one digest. The planned sources include developer news, GitHub Trending, LeetCode, Hacker News, YouTube, podcasts, and Formula 1 highlights; availability depends on the current source integrations.

## Features and design goals

- Consolidate selected feeds and content sources into one daily summary.
- Support scheduled execution with a local scheduler such as cron.
- Optionally log feedback or selected items to Google Sheets.
- Keep source-specific fetching separate so an individual integration can fail without breaking the entire digest.

## Setup

1. Clone this repository and inspect the entry point and dependency files.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the dependencies declared by the project (for example, `pip install -r requirements.txt` if that file exists).
4. Configure required API credentials and Google service-account settings using environment variables or a local configuration file excluded from Git.
5. Run the documented entry point manually before scheduling it.

Exact commands and required variables should be confirmed against the current source files.

## Security

- Never commit API keys, OAuth tokens, service-account JSON files, or personal data.
- Restrict Google Sheets access to the minimum required.
- Treat scraped or externally supplied content as untrusted input.
- Respect source websites' terms, rate limits, and API policies.

## Reliability and testing

Add tests for feed parsing, empty responses, timeouts, duplicate items, malformed content, and API quota failures. Use bounded retries and logging without printing secrets. A scheduled run should fail visibly and avoid sending a misleading empty digest.

## Limitations

External feeds and scraping selectors can change. This README describes the project's intent; verify each integration and setup command against the checked-out code before relying on it.
