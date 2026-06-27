# Security Policy

## Supported Versions

The following versions of the Company Employees Management System currently receive security updates.

| Version        | Supported |
| -------------- | --------- |
| Latest Release | ✅ Yes     |
| Older Releases | ❌ No      |

Please ensure you are using the latest version before reporting security issues.

---

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly.

### Please Do Not

* Open a public GitHub issue for security vulnerabilities.
* Disclose the vulnerability publicly before it has been reviewed and fixed.
* Share exploit code publicly before a fix is available.

### Please Include

When reporting a vulnerability, provide as much information as possible:

* Description of the vulnerability
* Steps to reproduce
* Potential impact
* Affected endpoints or files
* Suggested mitigation (if available)
* Screenshots or proof-of-concept examples (if applicable)

---

## Response Process

After receiving a security report, the project maintainer will:

1. Acknowledge receipt of the report.
2. Investigate the issue.
3. Assess the severity and impact.
4. Develop and test a fix.
5. Release a security update if necessary.
6. Credit the reporter (if desired).

---

## Security Best Practices

When deploying this project, it is recommended to:

### Django Settings

* Set `DEBUG = False` in production.
* Use a strong `SECRET_KEY`.
* Configure `ALLOWED_HOSTS` properly.
* Enable HTTPS.
* Use secure session cookies.

Example:

```python
DEBUG = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
```

### Database Security

* Use strong database passwords.
* Restrict database access to trusted hosts.
* Avoid using the root database account.
* Regularly back up your database.

### API Security

* Validate all user input.
* Use serializer validation.
* Implement authentication and authorization when required.
* Avoid exposing sensitive information in API responses.
* Return appropriate HTTP status codes.

### Dependency Management

Regularly update dependencies:

```bash
pip install --upgrade django
pip install --upgrade djangorestframework
```

Check for known vulnerabilities:

```bash
pip list --outdated
```

---

## Known Security Considerations

This project:

* Uses Django ORM to reduce SQL Injection risks.
* Uses Django REST Framework serializers for input validation.
* Supports Django's built-in security protections such as CSRF protection, XSS mitigation, and secure password hashing.

Developers should still follow secure coding practices when extending the project.

---

## Disclosure Policy

Security issues will be handled privately until a fix is available.

Once resolved, security-related changes may be documented in release notes or commit history.

---

## Contact

Project Maintainer: Sohel Mallik

For security-related concerns, please contact the maintainer through GitHub or other official project communication channels.

---

## Acknowledgements

We appreciate security researchers and contributors who help improve the safety and reliability of this project through responsible disclosure.
