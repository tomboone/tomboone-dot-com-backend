# Tom Boone Portfolio Backend

FastAPI backend for [tomboone.com](https://tomboone.com/) portfolio website.

## Setup

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Environment setup:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Database setup:**
   ```bash
   alembic upgrade head
   ```

4. **Run development server:**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Public (No Auth Required)
- `GET /api/v1/profile/` - Get first profile
- `GET /api/v1/profile/{id}` - Get specific profile

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.