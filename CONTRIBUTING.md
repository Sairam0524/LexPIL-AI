# Contributing to LexPIL AI

Thank you for your interest in contributing to LexPIL AI!

## Code of Conduct

Be respectful, inclusive, and professional. We're building a platform for the legal community.

## How to Contribute

### Reporting Bugs

1. Check if the bug is already reported
2. Include Python/Node version
3. Provide minimal reproduction steps
4. Include error messages and logs

### Suggesting Features

1. Check existing issues and discussions
2. Clearly describe the use case
3. Explain why this feature benefits PIL research
4. Provide examples if applicable

### Code Contributions

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Follow code style guidelines
4. Add tests for new features
5. Write clear commit messages
6. Submit a pull request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/LexPIL-AI.git
cd LexPIL-AI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
cd backend
pip install -r requirements-dev.txt

cd ../frontend
npm install
```

## Code Style

**Python:**
- Follow PEP 8
- Use type hints
- Black formatter: `black .`
- Flake8 linting: `flake8 .`

**TypeScript/React:**
- Use ESLint and Prettier
- Follow React hooks best practices
- TypeScript strict mode enabled

## Testing

```bash
# Backend
cd backend
pytest --cov=.

# Frontend
cd ../frontend
npm test -- --coverage

# Integration
pytest integration/ -v
```

## Documentation

- Update README if adding features
- Document API changes in api_reference.md
- Add docstrings to all functions
- Update CHANGELOG for significant changes

## Legal Sources

When adding new legal sources:

1. Verify source is publicly accessible
2. Check terms of service
3. Add to authorized sources list
4. Create ingestion parser
5. Add to corpus configuration
6. Document in corpus_design.md

## Pull Request Process

1. Update documentation
2. Add/update tests
3. Ensure all tests pass
4. Keep commits atomic and well-messaged
5. Reference related issues
6. Request review from maintainers

## License

By contributing, you agree your code will be licensed under MIT License.
