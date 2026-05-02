# Contributing to Skwirel

Thank you for your interest in contributing to Skwirel!

## Getting Started

### Fork and Clone

```bash
git clone https://github.com/skwirel-dev/skwirel.git
cd skwirel
```

### Development Setup

```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend-web
npm install
```

## Making Changes

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and commit
3. Push and create a pull request

## Pull Request Guidelines

- Include tests for new functionality
- Run linting: `ruff check .`
- Ensure CI passes
- Follow conventional commit format

## License Boundaries

**Important**: This project has a dual-license structure:

- `backend/app/` and `frontend-web/src/` — MIT License
- `backend/app/features/premium/` and `frontend-web/src/features/premium/` — Proprietary

Do not add proprietary code to MIT-licensed paths. CI verifies license boundaries.

## Questions?

Open an issue on GitHub.

---

By contributing, you agree that your contributions will be licensed under the MIT License.