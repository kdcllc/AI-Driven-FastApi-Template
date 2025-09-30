# Quick Start Guide

This guide will get you up and running with the AI-Driven FastAPI Template in 5 minutes.

## Prerequisites

- Python 3.11 or higher
- UV package manager (we'll install this in step 1)

## 5-Minute Setup

### Step 1: Install UV

**On Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Or using pip:**
```bash
pip install uv
```

### Step 2: Clone and Setup

```bash
# Clone the repository
git clone https://github.com/kdcllc/AI-Driven-FastApi-Template.git
cd AI-Driven-FastApi-Template

# Install dependencies
uv sync

# Copy environment variables
cp .env.example .env
```

### Step 3: Run the Application

```bash
# Option 1: Using Make
make run

# Option 2: Using UV directly
cd src
uv run python -m uvicorn app.main:app --reload

# Option 3: Using the run script
cd src
uv run python run.py
```

### Step 4: Test the API

Open your browser and visit:
- **API Documentation**: http://localhost:8000/api/docs
- **Root Endpoint**: http://localhost:8000

Or use curl:
```bash
# Test root endpoint
curl http://localhost:8000

# Test health endpoint
curl http://localhost:8000/api/health

# Create an item
curl -X POST http://localhost:8000/api/example/ \
  -H "Content-Type: application/json" \
  -d '{"name":"My Item","price":29.99,"quantity":1}'

# Get all items
curl http://localhost:8000/api/example/
```

### Step 5: Run Tests

```bash
# Run all tests
make test

# Or using uv directly
uv run pytest -v
```

## Next Steps

### Development Workflow

1. **Install dev dependencies**:
   ```bash
   make dev
   ```

2. **Format and lint code**:
   ```bash
   make format
   make lint
   ```

3. **Use AI Chat Modes**:
   - Check `.github/chatmodes/` for AI-assisted development
   - Reference `.github/prompts/` for common patterns

### VS Code Setup

1. Open the project in VS Code
2. Install recommended extensions (see `.vscode/extensions.json`)
3. Press F5 to start debugging

### Adding New Features

Follow the prompts in `.github/prompts/`:
- `api-endpoint.md` - Creating new API endpoints
- `test-writing.md` - Writing tests
- `refactoring.md` - Refactoring code

## Common Commands

```bash
# Development
make install    # Install dependencies
make dev        # Install dev dependencies
make run        # Run the server
make test       # Run tests
make lint       # Check code quality
make format     # Format code
make clean      # Clean cache files

# Testing
uv run pytest              # Run all tests
uv run pytest -v           # Verbose output
uv run pytest -k test_name # Run specific test

# Linting
uv run ruff check .        # Check for issues
uv run ruff check --fix .  # Auto-fix issues
uv run ruff format .       # Format code
```

## Project Structure

```
src/app/
├── api/routes/    # Add your API endpoints here
├── core/          # Configuration and core utilities
├── models/        # Database models (when needed)
├── schemas/       # Pydantic schemas for validation
└── main.py        # FastAPI app initialization
```

## Troubleshooting

### UV not found
```bash
# Make sure UV is in your PATH
export PATH="$HOME/.cargo/bin:$PATH"

# Or reinstall
pip install uv
```

### Import errors
```bash
# Make sure you're in the right directory
cd src

# Set PYTHONPATH
export PYTHONPATH=/path/to/project/src
```

### Tests failing
```bash
# Reinstall dependencies
uv sync --all-extras

# Clear cache
make clean
```

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [UV Documentation](https://github.com/astral-sh/uv)
- [Full README](README.md)
- [Contributing Guide](CONTRIBUTING.md)

## Getting Help

- Check the [README](README.md) for detailed information
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
- Use AI chat modes in `.github/chatmodes/` for guidance
- Open an issue on GitHub for bugs or questions

---

**You're all set! Happy coding! 🚀**
