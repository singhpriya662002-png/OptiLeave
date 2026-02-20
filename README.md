# Intelligent Leave Management System

A full-stack web application for automated leave request evaluation and approval based on team workload, project deadlines, and team availability.

## Features

- 🔐 Secure authentication with JWT
- 📝 Leave request submission and management
- ✅ Automated approval/escalation based on configurable rules
- 📊 Real-time workload analysis
- 📅 Team calendar with leave visualization
- 👥 Role-based access control (Employee, Manager, Admin)
- 🎨 Modern glassmorphism UI design
- 🔄 Real-time updates with WebSocket
- 📱 Responsive design

## Tech Stack

### Frontend
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Recharts (data visualization)
- FullCalendar (calendar view)
- Socket.io-client (real-time updates)
- Axios (API client)

### Backend
- Node.js + Express
- TypeScript
- Prisma ORM
- PostgreSQL
- Redis (caching)
- JWT authentication
- Socket.io (WebSocket)

## Quick Start

### Prerequisites

- Node.js 18+
- Docker Desktop (for PostgreSQL and Redis)
- Git

### 1. Clone the Repository

```bash
git clone <repository-url>
cd OptiLeave
```

### 2. Setup Backend

```bash
# Run the setup script (Windows PowerShell)
.\setup-backend.ps1

# Or manually:
docker-compose up -d postgres redis
cd backend
npm install
npm run prisma:generate
npm run prisma:migrate
npm run prisma:seed
npm run dev
```

The backend will be running at `http://localhost:4000`

### 3. Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will be running at `http://localhost:3000`

## Test Credentials

After running the seed script, you can login with:

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@example.com | password123 |
| Manager | manager.eng@example.com | password123 |
| Employee | john.doe@example.com | password123 |
| Employee | jane.smith@example.com | password123 |

## Project Structure

```
OptiLeave/
├── backend/                 # Backend API
│   ├── src/
│   │   ├── config/         # Configuration files
│   │   ├── middleware/     # Express middleware
│   │   ├── routes/         # API routes
│   │   ├── utils/          # Utility functions
│   │   └── index.ts        # Entry point
│   ├── prisma/
│   │   ├── schema.prisma   # Database schema
│   │   └── seed.ts         # Seed data
│   └── package.json
├── frontend/                # Frontend application
│   ├── src/
│   │   ├── app/            # Next.js pages
│   │   ├── components/     # React components
│   │   ├── contexts/       # React contexts
│   │   ├── hooks/          # Custom hooks
│   │   ├── lib/            # Utilities
│   │   ├── services/       # API services
│   │   └── types/          # TypeScript types
│   └── package.json
├── .kiro/                   # Spec files
│   └── specs/
│       └── intelligent-leave-management-system/
│           ├── requirements.md
│           ├── design.md
│           └── tasks.md
├── docker-compose.yml       # Docker services
├── .env                     # Environment variables
└── README.md
```

## API Endpoints

### Authentication
- `POST /api/auth/login` - Login
- `POST /api/auth/logout` - Logout

### Leave Management
- `GET /api/leave/balance` - Get leave balance
- `POST /api/leave/request` - Submit leave request
- `GET /api/leave/history` - Get leave history
- `GET /api/leave/pending` - Get pending requests (Manager)
- `PUT /api/leave/:id/approve` - Approve request (Manager)
- `PUT /api/leave/:id/reject` - Reject request (Manager)
- `DELETE /api/leave/:id` - Cancel request

## Development

### Backend Development

```bash
cd backend

# Start development server with hot reload
npm run dev

# Run tests
npm test

# Run linter
npm run lint

# Open Prisma Studio (database GUI)
npm run prisma:studio
```

### Frontend Development

```bash
cd frontend

# Start development server
npm run dev

# Run tests
npm test

# Run linter
npm run lint
```

### Database Management

```bash
cd backend

# Create new migration
npm run prisma:migrate

# Reset database (WARNING: deletes all data)
npm run prisma:migrate reset

# Seed database
npm run prisma:seed

# Generate Prisma Client
npm run prisma:generate
```

## Testing

### Backend Tests
```bash
cd backend
npm test
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Documentation

- [Backend Setup Guide](./BACKEND_SETUP.md)
- [Requirements Document](./.kiro/specs/intelligent-leave-management-system/requirements.md)
- [Design Document](./.kiro/specs/intelligent-leave-management-system/design.md)
- [Implementation Tasks](./.kiro/specs/intelligent-leave-management-system/tasks.md)

## Troubleshooting

### Backend won't start
- Ensure PostgreSQL and Redis are running: `docker-compose ps`
- Check environment variables in `.env`
- Verify database connection: `npm run prisma:studio`

### Frontend won't connect to backend
- Ensure backend is running on port 4000
- Check `frontend/.env.local` has correct API URL
- Verify CORS settings in backend

### Database migration issues
- Reset database: `npm run prisma:migrate reset`
- Regenerate client: `npm run prisma:generate`

## License

MIT

## Support

For issues and questions, please open an issue on GitHub.
