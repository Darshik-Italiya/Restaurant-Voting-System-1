# Restaurant Voting System Backend

A FastAPI-based backend for a restaurant voting system where users can vote for restaurants with a daily limit and point decay system.

## Features

- User authentication (register/login)
- Restaurant management (create, list, delete)
- Daily voting system with point decay
- Leaderboards (daily, weekly, monthly)
- JWT token-based authentication

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp env.example .env
# Edit .env with your database credentials
```

3. Set up PostgreSQL database:
```bash
createdb restaurant_db
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Start the server:
```bash
python run.py
```

The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user

### Users
- `GET /users/me` - Get current user info
- `GET /users/{user_id}` - Get user by ID
- `GET /users/` - List all users

### Restaurants
- `POST /restaurants/` - Create restaurant
- `GET /restaurants/` - List restaurants
- `DELETE /restaurants/{restaurant_id}` - Delete restaurant

### Votes
- `POST /votes/` - Cast a vote
- `GET /votes/my-votes` - Get user's votes

### Leaderboard
- `GET /leaderboard/daily` - Daily leaderboard
- `GET /leaderboard/weekly` - Weekly leaderboard
- `GET /leaderboard/monthly` - Monthly leaderboard