# Feature Tiers

This document defines the boundary between MIT-licensed open-source code and proprietary premium features.

## Tier Overview

| Tier | License | Description |
|------|---------|-------------|
| **Core** | MIT | Basic portfolio tracking, transactions, tax lots |
| **Premium** | Proprietary | Advanced analytics, AI features, priority support |

## Directory Structure

```
backend/
├── app/
│   ├── core/           # Core utilities (MIT)
│   ├── models/         # Data models (MIT)
│   ├── schemas/        # API schemas (MIT)
│   ├── services/       # Business logic (MIT)
│   ├── api/            # API routes (MIT)
│   └── features/
│       └── premium/    # Proprietary features (PROPRIETARY)
├── scripts/            # MIT
└── LICENSE.md          # MIT

frontend-web/
├── src/
│   ├── components/     # Shared UI (MIT)
│   ├── pages/          # Core pages (MIT)
│   ├── hooks/          # Shared hooks (MIT)
│   └── features/
│       └── premium/    # Proprietary UI (PROPRIETARY)
└── LICENSE.md          # MIT
```

## MIT-Licensed (Core)

Everything under `backend/app/` except `features/premium/` is MIT-licensed:
- Authentication — JWT, Clerk integration, session management
- Portfolio tracking — holdings, positions, performance
- Transaction management — buys, sells, dividends, splits
- Tax lot tracking — FIFO, weighted average cost basis
- Market data — price updates, exchange rates
- Document upload — basic classification, storage
- Core API — all public API endpoints

All frontend code under `src/` except `features/premium/` is MIT-licensed.

## Proprietary (Premium)

### Backend: `backend/app/features/premium/`
- Advanced retirement planning (Monte Carlo simulations)
- AI-powered document extraction and reconciliation
- Priority support ticketing integration
- Advanced analytics and forecasting

### Frontend: `frontend-web/src/features/premium/`
- Premium dashboard widgets
- AI assistant UI components
- Advanced chart components
- Priority support chat

## Verification

A CI check runs on every PR to ensure:
1. MIT LICENSE.md exists in `backend/` and `frontend-web/`
2. PROPRIETARY_LICENSE.md exists in all `premium/` directories
3. No proprietary code leaks into MIT-licensed paths

Run locally: `.github/scripts/verify-licenses.sh`