# AI Adaptive CRM - Phase 1 Backend

Production-ready backend for mobile-first AI-powered Mini CRM.

## Features

- ✅ JWT Authentication (signup/login)
- ✅ Business profile management
- ✅ Service management
- ✅ Customer management with stats tracking
- ✅ Visit logging with auto-stats update
- ✅ Booking system with auto end-time calculation

## Tech Stack

- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Database
- **SQLAlchemy** - ORM
- **Alembic** - Database migrations
- **JWT** - Authentication

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Edit `.env` file with your PostgreSQL credentials:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/ai_crm
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 4. Create PostgreSQL Database

```sql
CREATE DATABASE ai_crm;
```

### 5. Run Migrations

```bash
alembic upgrade head
```

### 6. Start Server

```bash
uvicorn app.main:app --reload
```

Server runs at: http://localhost:8000

## API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /auth/signup` - Register new user
- `POST /auth/login` - Login and get JWT token

### Business
- `POST /business` - Create business profile
- `GET /business/me` - Get current user's business

### Services
- `POST /services` - Add service
- `GET /services` - List services

### Customers
- `POST /customers` - Create customer
- `GET /customers` - List customers

### Visits
- `POST /visits` - Log a visit (updates customer stats)

### Bookings
- `POST /bookings` - Create booking (auto-calculates end time)
- `GET /bookings/today` - Get today's bookings

## Project Structure

```
app/
├── main.py              # FastAPI app entry
├── database.py          # SQLAlchemy setup
├── dependencies.py      # DI dependencies
├── core/
│   ├── config.py        # Settings
│   └── security.py      # JWT & hashing
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── routers/             # API routes
└── services/            # Business logic
```
