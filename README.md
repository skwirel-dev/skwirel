# Skwirel

**Track investments. Plan for retirement. Share your financial story.**

Skwirel is a personal finance platform that helps you track investments, plan for retirement, and share your financial story — on your own terms.

## Features

- **Portfolio Tracking** — Track holdings, positions, and performance across multiple accounts
- **Transaction Management** — Record buys, sells, dividends, and splits
- **Tax Lot Tracking** — FIFO and weighted average cost basis methods
- **Market Data** — Real-time price updates and exchange rates
- **Document Upload** — Basic classification and storage for financial documents
- **Open API** — RESTful API for building custom integrations

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.11+ / FastAPI |
| Frontend | TypeScript / Vite / React |
| Database | PostgreSQL |
| Auth | JWT / Clerk |

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 20+
- PostgreSQL 15+

### Backend Setup

```bash
cd backend
cp .env.example .env
pip install -r requirements.txt
python -m app.main
```

### Frontend Setup

```bash
cd frontend-web
npm install
npm run dev
```

## Project Structure

```
skwirel/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Core utilities
│   │   ├── models/       # Data models
│   │   ├── schemas/      # API schemas
│   │   ├── services/     # Business logic
│   │   └── features/     # Feature modules
│   ├── scripts/          # Utility scripts
│   └── LICENSE.md        # MIT License
├── frontend-web/
│   ├── src/
│   │   ├── components/   # Shared UI components
│   │   ├── pages/        # Page components
│   │   ├── hooks/        # Shared React hooks
│   │   └── features/     # Feature modules
│   └── LICENSE.md        # MIT License
├── docs/                 # Documentation
└── .github/              # GitHub configuration
```

## License

This project is dual-licensed:

- **MIT License** — Core platform features (see `backend/LICENSE.md` and `frontend-web/LICENSE.md`)
- **Proprietary License** — Premium features (see `backend/app/features/premium/PROPRIETARY_LICENSE.md`)

For licensing questions: [licensing@skwirel.com](mailto:licensing@skwirel.com)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Support

- **Issues** — Report bugs and request features via [GitHub Issues](https://github.com/skwirel-dev/skwirel/issues)
- **Documentation** — [docs/](docs/) folder
- **Security** — See [SECURITY.md](SECURITY.md) for vulnerability reporting

---

Copyright (c) 2026 Skwirel, Inc.