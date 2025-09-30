# Contributing to AI-Driven FastAPI Template

Thank you for your interest in contributing to this project! This guide will help you get started.

## Development Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/your-username/AI-Driven-FastApi-Template.git
   cd AI-Driven-FastApi-Template
   ```

2. **Install UV** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # or
   pip install uv
   ```

3. **Install dependencies**:
   ```bash
   make dev
   # or
   uv sync --all-extras
   ```

4. **Set up environment**:
   ```bash
   cp .env.example .env
   ```

## Development Workflow

### Using AI-Assisted Development

This template is optimized for AI-driven development. Use the chat modes in `.github/chatmodes/`:

- **Feature Development**: When adding new features
- **Code Review**: Before submitting PRs
- **Debugging**: When troubleshooting issues

Reference prompts from `.github/prompts/` for common patterns.

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow the existing code structure
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests**:
   ```bash
   make test
   ```

4. **Run linting**:
   ```bash
   make lint
   ```

5. **Format code**:
   ```bash
   make format
   ```

### Testing

- Write tests for all new features
- Ensure all tests pass before submitting
- Follow the test patterns in `tests/`
- Use the test writing prompt from `.github/prompts/test-writing.md`

### Code Style

- Follow PEP 8 style guidelines
- Use type hints for all functions
- Write descriptive docstrings
- Keep functions small and focused
- Ruff handles formatting automatically

### Commit Messages

Use conventional commit format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Test additions or changes
- `refactor:` Code refactoring
- `chore:` Maintenance tasks
- `style:` Code style changes

Example:
```
feat: add user authentication endpoint

- Add login and signup endpoints
- Implement JWT token generation
- Add authentication middleware
```

## Pull Request Process

1. **Update documentation** if you've made changes to:
   - API endpoints
   - Configuration options
   - Project structure

2. **Ensure CI passes**:
   - All tests pass
   - Code is properly formatted
   - No linting errors

3. **Write a clear PR description**:
   - Explain what changes you made
   - Why you made them
   - How to test them

4. **Request review**:
   - Tag relevant maintainers
   - Address review comments promptly

## Issue Templates and Automation

This project uses GitHub issue templates and automated workflows to streamline contributions.

### Creating Issues

When creating a new issue, select the appropriate template:

- **Bug Report** (`.github/ISSUE_TEMPLATE/bug_report.md`): For reporting bugs and errors
- **Feature Request** (`.github/ISSUE_TEMPLATE/feature_request.md`): For suggesting new features
- **Update/Enhancement** (`.github/ISSUE_TEMPLATE/update_enhancement.md`): For proposing updates to existing functionality

### Automated PR Features

The repository includes automated workflows that help maintain quality:

1. **Auto-labeling** (`.github/workflows/pr-automation.yml`):
   - Labels PRs based on branch name (e.g., `feat/`, `fix/`, `docs/`)
   - Labels PRs based on title prefix (e.g., `feat:`, `fix:`, `docs:`)
   - Checks for empty PR descriptions
   - Reminds to link related issues

2. **Issue-PR Linking** (`.github/workflows/issue-pr-linker.yml`):
   - Automatically links issues and PRs when referenced
   - Validates conventional commit format in PR titles
   - Provides helpful comments for format guidance

**Tip:** Use conventional commit prefixes in your branch names and PR titles to get automatic labels:
- `feat/` or `feat:` for new features
- `fix/` or `fix:` for bug fixes
- `docs/` or `docs:` for documentation
- `test/` or `test:` for tests
- `refactor/` or `refactor:` for refactoring
- `chore/` or `chore:` for maintenance tasks

## Project Structure

```
.
├── src/app/           # Application code
│   ├── api/          # API endpoints
│   ├── core/         # Core functionality
│   ├── models/       # Database models
│   ├── schemas/      # Pydantic schemas
│   └── main.py       # App initialization
├── tests/            # Test files
├── .github/
│   ├── chatmodes/    # AI chat modes
│   └── prompts/      # Reusable prompts
└── .vscode/          # VS Code configuration
```

## Adding New Features

### New API Endpoint

1. Use the API endpoint prompt: `.github/prompts/api-endpoint.md`
2. Create route file in `src/app/api/routes/`
3. Add Pydantic schemas if needed
4. Register router in `src/app/main.py`
5. Add tests in `tests/`

### New Dependencies

Add to `pyproject.toml`:
```toml
[project]
dependencies = [
    "new-package>=1.0.0",
]
```

Then run:
```bash
uv sync
```

## Questions?

- Open an issue for bugs or feature requests
- Start a discussion for general questions
- Use AI chat modes for development guidance

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

Thank you for contributing! 🎉
