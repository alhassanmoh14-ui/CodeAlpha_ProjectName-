

\# CODEALPHA CYBERSECURITY INTERNSHIP

\# TASK 3: SECURE CODING REVIEW



\*\*Project Title:\*\* Python Web Application Security Audit  

\*\*Auditor:\*\* Jedidiah Kweku Dadzie  

\*\*Programming Language:\*\* Python  

\*\*Framework:\*\* Flask  

\*\*Database:\*\* SQLite  

\*\*Static Analysis Tool:\*\* Bandit  

\*\*Testing Tool:\*\* Pytest  

\*\*Date:\*\* 19 November 2026



\---



\## 1. Executive Summary



This project involved reviewing a Python Flask web application to identify security vulnerabilities and recommend secure coding practices.



The review included manual source-code inspection, static security analysis using Bandit, remediation of identified weaknesses, and automated testing using Pytest.



Two application versions were examined:

\- A deliberately vulnerable application.

\- A corrected application implementing safer coding practices.



The initial Bandit scan identified four findings. After remediation, the second scan reported no issues. All seven automated tests passed.



\## 2. Project Objectives



\- Identify common security vulnerabilities in Python applications.

\- Understand the risks associated with insecure coding practices.

\- Use Bandit for static security analysis.

\- Apply secure coding techniques.

\- Test the corrected application.

\- Document findings and remediation recommendations.



\## 3. Scope and Methodology



The audit covered the following areas:



1\. Source-code inspection.

2\. SQL query construction.

3\. Password storage.

4\. Secret management.

5\. HTML output handling.

6\. Application debugging configuration.

7\. Input validation.



Tools used:



| Tool | Purpose |

|---|---|

| Python | Programming language |

| Flask | Web application framework |

| SQLite | Database |

| Bandit | Static security analysis |

| Pytest | Automated testing |



The assessment was conducted locally using fictional data.



\## 4. Security Vulnerabilities Identified



\### Finding 1: Hardcoded Secret



\*\*Location:\*\* vulnerable\_app/app.py, line 8



\*\*Severity:\*\* Low in Bandit's report; potentially more serious depending on deployment.



\*\*Description:\*\*

The application contained a hardcoded secret:



`app.secret\_key = "mysecret123"`



\*\*Risk:\*\*

An attacker who obtains the source code could discover the secret and potentially compromise security mechanisms that depend on it.



\*\*Remediation:\*\*

Use a securely generated secret supplied through an environment variable or secrets manager.



\### Finding 2: SQL Injection in Registration



\*\*Location:\*\* vulnerable\_app/app.py, line 27



\*\*Severity:\*\* Medium in Bandit's report.



\*\*Description:\*\*

User-controlled data was inserted directly into an SQL statement using an f-string.



\*\*Risk:\*\*

Malicious input could change the meaning of a database query, potentially resulting in unauthorized database operations.



\*\*Remediation:\*\*

Use parameterized SQL queries.



Example:



`cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))`



\### Finding 3: SQL Injection in Search



\*\*Location:\*\* vulnerable\_app/app.py, line 44



\*\*Severity:\*\* Medium in Bandit's report.



\*\*Description:\*\*

The search function constructed SQL commands using untrusted user input.



\*\*Risk:\*\*

An attacker could manipulate database search operations.



\*\*Remediation:\*\*

Use parameterized queries and validate input.



\### Finding 4: Flask Debug Mode Enabled



\*\*Location:\*\* vulnerable\_app/app.py, line 66



\*\*Severity:\*\* High in Bandit's report.



\*\*Description:\*\*

The application was configured with:



`app.run(debug=True)`



\*\*Risk:\*\*

An exposed interactive debugger can allow serious compromise, including arbitrary code execution.



\*\*Remediation:\*\*

Disable debug mode in production and use a properly configured production server.



\### Finding 5: Plain-Text Password Storage



\*\*Location:\*\* vulnerable\_app/app.py, registration function.



\*\*Severity:\*\* High (manual review assessment).



\*\*Description:\*\*

Passwords were stored directly in the database without hashing.



\*\*Risk:\*\*

If the database is exposed, attackers could obtain users' original passwords.



\*\*Remediation:\*\*

Use a password hashing function such as Werkzeug's `generate\_password\_hash()`.



\### Finding 6: Cross-Site Scripting (XSS)



\*\*Location:\*\* vulnerable\_app/app.py, search function.



\*\*Severity:\*\* High (manual review assessment).



\*\*Description:\*\*

User input was inserted directly into an HTML response.



\*\*Risk:\*\*

Malicious HTML or JavaScript could execute in a visitor's browser.



\*\*Remediation:\*\*

Use template rendering with automatic HTML escaping and avoid inserting untrusted data directly into HTML.



\## 5. Remediation Implemented



The secure application includes:



\- Parameterized SQL queries.

\- Password hashing.

\- Environment-based secret configuration.

\- HTML escaping through Flask/Jinja templates.

\- Username and password validation.

\- Duplicate username handling.

\- Debug mode disabled.

\- Database operations using managed connections.



\## 6. Static Analysis Results



Bandit was used to scan both application versions.



\### Initial scan: Vulnerable application



| Severity | Findings |

|---|---:|

| High | 1 |

| Medium | 2 |

| Low | 1 |

| Total | 4 |



\### Second scan: Secure application



| Severity | Findings |

|---|---:|

| High | 0 |

| Medium | 0 |

| Low | 0 |

| Total | 0 |



\*\*Interpretation:\*\* Bandit found no issues covered by its checks in the corrected application. This does not guarantee the absence of all vulnerabilities.



\## 7. Automated Testing Results



Seven tests were executed using Pytest.



| Test | Result |

|---|---|

| Home page response | PASSED |

| Secure user registration | PASSED |

| Short password rejection | PASSED |

| Duplicate username rejection | PASSED |

| Password hashing verification | PASSED |

| SQL injection input handling | PASSED |

| XSS output escaping | PASSED |



\*\*Total:\*\* 7 passed, 0 failed.



\## 8. Secure Coding Recommendations



1\. Never store passwords in plain text.

2\. Use parameterized queries for all database operations.

3\. Store secrets outside source code.

4\. Disable debugging in production.

5\. Validate and sanitize untrusted input according to its intended use.

6\. Use secure template rendering and HTML escaping.

7\. Implement authentication, authorization and CSRF protection where applicable.

8\. Apply rate limiting to sensitive endpoints.

9\. Keep software dependencies updated.

10\. Perform regular security reviews and automated testing.



\## 9. Limitations



This was a limited educational code review of a small demonstration application.



The assessment did not include a full penetration test, production deployment review, authentication system assessment, or comprehensive dependency and infrastructure audit.



Bandit findings are limited to the checks it supports. Manual review and additional testing remain necessary.



\## 10. Conclusion



The Secure Coding Review project demonstrated how insecure coding practices can introduce vulnerabilities into Python web applications.



Through manual inspection, Bandit static analysis, remediation and automated testing, the application was improved.



The vulnerable version produced four Bandit findings, while the corrected version produced zero findings. All seven automated tests passed.



This project strengthened my understanding of secure software development, vulnerability identification, remediation and security testing.



\*\*Prepared by:\*\*  

Jedidiah Kweku Dadzie



\*\*CodeAlpha Cybersecurity Internship – Task 3\*\*



