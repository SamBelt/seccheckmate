# Contributing to SecCheckmate

We love your input! We want to make contributing to SecCheckmate as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Adding new checklists

## We Use Github Flow, So All Code Changes Happen Through Pull Requests

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `master`
2. If you've added code, add tests
3. Ensure the test suite passes
4. Make sure your code follows the existing style
5. Issue a pull request with a clear description

## Any contributions you make will be under the MIT License

When you submit code changes, your submissions are understood to be under the same MIT License that covers the project.

## Report bugs using Github's Issues

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/yourusername/seccheckmate/issues); it's that easy!

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Use a Consistent Coding Style

* Follow PEP 8 guidelines for Python code
* Use 4 spaces for indentation
* Use meaningful variable names
* Add comments for complex logic

## Adding New Checklists

To add a new security checklist:

1. Create a new YAML file in the `checklists/` directory
2. Follow the existing format with proper categories and severity levels
3. Ensure each test has: `id`, `title`, `description`, `severity`, and `category`
4. Test the checklist with the application
5. Submit a pull request with documentation

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing opinions, viewpoints, and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated.

## References

This document was adapted from the [Atom Contributing Guidelines](https://github.com/atom/atom/blob/master/CONTRIBUTING.md).

---

Thank you for contributing to SecCheckmate! 🛡️
