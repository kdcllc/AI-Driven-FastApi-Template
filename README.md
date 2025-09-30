# AI-Driven FastAPI Template

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://raw.githubusercontent.com/kdcllc/AI-Driven-FastApi-Template/master/LICENSE)

A modern, production-ready FastAPI template optimized for AI-driven development workflows with UV dependency management.

![Stand With Israel](./img/IStandWithIsrael.png)

## Hire me

Please send [email](mailto:info@kingdavidconsulting.com) if you consider to **hire me**.

[![buymeacoffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/vyve0og)

## Give a Star! :star:

If you like or are using this project to learn or start your solution, please give it a star. Thanks!


## ✨ Features

- **🐍 Python 3.11+**: Modern Python with type hints
- **⚡ FastAPI**: High-performance async web framework
- **📦 UV**: Fast Python package installer and dependency manager
- **🤖 AI-Optimized**: GitHub Copilot chat modes and prompts for agentic development
- **🔧 VS Code**: Pre-configured settings and debugging configurations
- **✅ Testing**: Pytest setup with async support
- **🎨 Code Quality**: Ruff for linting and formatting
- **📝 Type Safety**: MyPy configuration for static type checking

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- [UV](https://github.com/astral-sh/uv) package manager

### Installation

1. **Clone the repository** (or use as template):

   ```bash
   git clone https://github.com/kdcllc/AI-Driven-FastApi-Template.git
   cd AI-Driven-FastApi-Template
   ```

2. **Install UV** (if not already installed):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies**:

   ```bash
   make install
   # or
   uv sync
   ```

4. **Install development dependencies**:

   ```bash
   make dev
   # or
   uv sync --all-extras
   ```

5. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

### Running the Application

**Using Make**:

```bash
make run
```

**Using UV directly**:

```bash
cd src
uv run python -m uvicorn app.main:app --reload
```

**Using the run script**:

```bash
cd src
uv run python run.py
```

The API will be available at:

- **API**: http://localhost:1212
- **Docs**: http://localhost:1212/api/docs
- **ReDoc**: http://localhost:1212/api/redoc

## 📁 Project Structure

```
.
├── .github/
│   ├── chatmodes/          # GitHub Copilot chat modes
│   │   ├── code-review.md
│   │   ├── debugging.md
│   │   └── feature-development.md
│   └── prompts/            # Reusable AI prompts
│       ├── api-endpoint.md
│       ├── refactoring.md
│       └── test-writing.md
├── .vscode/
│   ├── extensions.json     # Recommended extensions
│   ├── launch.json         # Debug configurations
│   └── settings.json       # VS Code settings
├── src/
│   └── app/
│       ├── api/
│       │   └── routes/     # API endpoints
│       │       ├── health.py
│       │       └── example.py
│       ├── core/
│       │   └── config.py   # Configuration
│       ├── models/         # Database models (add as needed)
│       ├── schemas/        # Pydantic schemas (add as needed)
│       └── main.py         # FastAPI app initialization
├── tests/
│   ├── conftest.py         # Test fixtures
│   ├── test_health.py
│   └── test_example.py
├── .env.example            # Environment variables template
├── .gitignore
├── Makefile                # Common development tasks
├── pyproject.toml          # Project configuration
└── README.md
```

## 🧪 Testing

Run tests:

```bash
make test
# or
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=app --cov-report=html
```

## 🎨 Code Quality

**Linting**:

```bash
make lint
# or
uv run ruff check .
uv run mypy src/app
```

**Formatting**:

```bash
make format
# or
uv run ruff format .
uv run ruff check --fix .
```

## 🤖 AI-Driven Development

This template includes specialized GitHub Copilot chat modes and prompts to enhance your development workflow:

### Chat Modes (`.github/chatmodes/`)

1. **Code Review Mode** (`code-review.md`)

   - Security-first code review
   - Best practices validation
   - Performance optimization suggestions

2. **Feature Development Mode** (`feature-development.md`)

   - Guided feature implementation
   - TDD workflow support
   - Project structure patterns

3. **Debugging Mode** (`debugging.md`)
   - Systematic bug investigation
   - Common issue solutions
   - Debug tool recommendations

### Prompts (`.github/prompts/`)

1. **API Endpoint Prompt** (`api-endpoint.md`)

   - Template for new API endpoints
   - Validation and error handling patterns

2. **Test Writing Prompt** (`test-writing.md`)

   - Comprehensive test patterns
   - Coverage guidelines

3. **Refactoring Prompt** (`refactoring.md`)
   - Safe refactoring practices
   - Common refactoring patterns

### Using Chat Modes

In GitHub Copilot Chat:

1. Reference a chat mode: `@workspace /chatmode code-review`
2. Or paste the content from `.github/chatmodes/` into your chat

## 🛠️ VS Code Setup

This template includes pre-configured VS Code settings:

- **Python interpreter**: Automatically uses `.venv`
- **Linting**: Ruff integration
- **Formatting**: Auto-format on save
- **Testing**: Pytest integration
- **Debugging**: FastAPI debug configuration

### Recommended Extensions

Install all recommended extensions:

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for `@recommended`
4. Install all workspace recommendations

## 📝 API Endpoints

### Health Checks

- `GET /api/health` - Health check
- `GET /api/health/ready` - Readiness probe
- `GET /api/health/live` - Liveness probe

### Example CRUD

- `GET /api/example/` - List items
- `GET /api/example/{id}` - Get item
- `POST /api/example/` - Create item
- `PUT /api/example/{id}` - Update item
- `DELETE /api/example/{id}` - Delete item

### Documentation

- `GET /api/docs` - Swagger UI
- `GET /api/redoc` - ReDoc UI
- `GET /api/openapi.json` - OpenAPI schema

## 🔧 Configuration

Configuration is managed through:

1. Environment variables (`.env` file)
2. `src/app/core/config.py` using pydantic-settings

Key configuration options:

- `ENVIRONMENT`: development, staging, production
- `DEBUG`: Enable debug mode
- `HOST`: Server host
- `PORT`: Server port
- `ALLOWED_ORIGINS`: CORS allowed origins

## 📚 Development Workflow

1. **Create a feature branch**:

   ```bash
   git checkout -b feature/my-feature
   ```

2. **Develop with AI assistance**:

   - Use GitHub Copilot chat modes
   - Reference prompts for common patterns
   - Follow TDD practices

3. **Test your changes**:

   ```bash
   make test
   make lint
   ```

4. **Commit and push**:
   ```bash
   git add .
   git commit -m "feat: add my feature"
   git push origin feature/my-feature
   ```

## 🚢 Deployment

### Using Docker (add Dockerfile as needed)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install UV
RUN pip install uv

# Copy project files
COPY . .

# Install dependencies
RUN uv sync --no-dev

# Run the application
CMD ["uv", "run", "python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "1212"]
```

### Environment Variables for Production

Update `.env` for production:

- Set `ENVIRONMENT=production`
- Set `DEBUG=false`
- Set `RELOAD=false`
- Configure `ALLOWED_ORIGINS` appropriately

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [UV](https://github.com/astral-sh/uv)
- [Ruff](https://github.com/astral-sh/ruff)
- [Pydantic](https://docs.pydantic.dev/)

## 📧 Support

For issues and questions:

- Open an issue on GitHub
- Check existing documentation
- Use AI chat modes for development guidance

---

**Happy coding with AI! 🤖✨**
