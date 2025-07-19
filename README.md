![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/github/license/Pinakbakshi/Daily_digest_automation)
![Last Commit](https://img.shields.io/github/last-commit/Pinakbakshi/Daily_digest_automation)
![Repo Size](https://img.shields.io/github/repo-size/Pinakbakshi/Daily_digest_automation)
![Top Language](https://img.shields.io/github/languages/top/Pinakbakshi/Daily_digest_automation)

---

## 📚 Table of Contents

- [📖 Overview](#-overview)
- [🚀 Getting Started](#-getting-started)
- [🛠️ Prerequisites](#️-prerequisites)
- [📦 Installation](#-installation)
- [⚙️ Usage](#️-usage)
- [🧪 Testing](#-testing)

---

## 📖 Overview

**Daily_digest_automation** is a comprehensive tool that automates the creation and delivery of personalized, curated tech digests—empowering individuals and teams with insightful, up-to-date summaries.

It ensures your setup is robust and delivers content reliably through validated environment variables, testable workflows, and scheduled automation.

---

### ✨ Why Daily_digest_automation?

- 🛠️ **Environment & SMTP Validation**  
  Ensures required environment variables are present and validates Gmail SMTP credentials to avoid failures.

- 🚀 **Automated Digest Generation**  
  Aggregates the latest news, trending repositories, media, and challenges into a unified digest.

- ⏱️ **Workflow Automation**  
  Executes digests daily via cron or job schedulers using shell scripts and Python automation.

- 📊 **Content & Feedback Logging**  
  User feedback is stored securely in **Google Sheets** for future personalization and improvement.

- 🔧 **Reliable Email Delivery**  
  Integrated testing utilities confirm that email services function correctly before going live.

---

## 🚀 Getting Started

### 🛠️ Prerequisites

Make sure you have the following:

- ✅ **Python 3.8+**
- ✅ **[Conda](https://docs.conda.io/en/latest/) (for environment management)**
- ✅ Gmail account for SMTP (or update `.env` for your email service)
- ✅ Google Cloud project with a service account for Sheets API access

name: daily_digest_env
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.10
  - pip
  - pip:
      - google-auth
      - google-auth-oauthlib
      - google-api-python-client
      - openai
      - beautifulsoup4
      - requests
      - schedule
      - python-dotenv
      - smtplib
      - email-validator
      - pytz
      - feedparser


---

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/Pinakbakshi/Daily_digest_automation
cd Daily_digest_automation
````

### Install Dependencies

Using Conda:

```bash
conda env create -f conda.yml
conda activate daily_digest_env
```

Fill in your `.env`:

```bash
cp .env.template .env
```

> ⚠️ Make sure to add your `GOOGLE_CREDS_JSON`, `SPREADSHEET_ID`, SMTP credentials, etc.

---

## ⚙️ Usage

Run the digest generator manually:

```bash
conda activate daily_digest_env
python daily_digest.py
```

Schedule with Cron (runs every day at 8 AM):

```bash
0 8 * * * /path/to/run_digest.sh
```

---

## 🧪 Testing

The project uses **`pytest`** as the testing framework.

Run tests with:

```bash
conda activate daily_digest_env
pytest
```

Test email setup:

```bash
python validate_env_email.py
```

Test environment variables:

```bash
python test_env.py
```

---

## 📌 Notes

* `.env` and Google credential JSON are **not** committed to GitHub.
* Use `.env.template` to share safe configuration templates.
* Keep your Gmail and Google API credentials private and secure.

---

## 🙋‍♂️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

[MIT](LICENSE)

---

## 👤 Author

**Pinak Bakshi**
🔗 [GitHub](https://github.com/Pinakbakshi) | 💼 Cognizant Healthcare Solutions | 🧠 AI & Automation Enthusiast

---

> “Automate the routine. Empower the decision.”

```

---

Would you like me to:

- Add a **demo screenshot or GIF** section?
- Generate badges for Python version, license, etc.?
- Help you auto-generate the `conda.yml` or `requirements.txt` file?

Let me know if you’d like this pushed to your GitHub `README.md` via a pull request-style commit.
```
