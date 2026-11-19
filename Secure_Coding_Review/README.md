

\# CodeAlpha Task 3: Secure Coding Review



\*\*Author:\*\* Jedidiah Kweku Dadzie



\## Overview



This project demonstrates a security audit of a Python Flask web application.



It identifies common vulnerabilities, implements secure coding improvements, and validates the corrected application using Bandit and Pytest.



\## Project Structure



```text

Secure\_Coding\_Review/

│

├── vulnerable\_app/

│   └── app.py

│

├── secure\_app/

│   └── app.py

│

├── reports/

│   ├── SECURITY\_AUDIT\_REPORT.md

│   ├── bandit\_vulnerable\_report.txt

│   └── bandit\_secure\_report.txt

│

├── screenshots/

│

├── tests/

│   └── test\_security.py

│

├── requirements.txt

└── README.md

```



\## Vulnerabilities Reviewed



\- SQL Injection

\- Hardcoded Secrets

\- Plain-text Password Storage

\- Cross-Site Scripting (XSS)

\- Flask Debug Mode

\- Weak Input Validation



\## Tools Used



\- Python

\- Flask

\- SQLite

\- Bandit

\- Pytest



\## Results



| Assessment | Result |

|---|---|

| Vulnerable application Bandit scan | 4 findings |

| Secure application Bandit scan | 0 findings |

| Automated tests | 7 passed |



\## Installation



Create and activate a virtual environment.



```bash

python -m venv .venv

```



Windows CMD:



```bat

.venv\\Scripts\\activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\## Run Security Tests



```bash

pytest tests -v

```



\## Run Bandit



```bash

bandit -r vulnerable\_app

bandit -r secure\_app

```



\## Run Secure Application



```bash

python secure\_app/app.py

```



Open:



http://127.0.0.1:5000



The vulnerable application is for controlled educational review only. Never deploy it or use real credentials.



\## Conclusion



This project demonstrates practical vulnerability identification, secure coding remediation, static analysis and automated security testing.



\*\*CodeAlpha Cybersecurity Internship – Task 3\*\*



