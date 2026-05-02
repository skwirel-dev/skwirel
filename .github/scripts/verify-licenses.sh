#!/bin/bash
set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

echo "=== Skwirel License Verification ==="

echo "Checking MIT LICENSE.md files..."
for dir in "$REPO_ROOT/backend" "$REPO_ROOT/frontend-web"; do
    if [ ! -f "$dir/LICENSE.md" ]; then
        echo "FAIL: $dir/LICENSE.md not found"
        exit 1
    fi
    echo "  ✓ $dir/LICENSE.md exists"
done

echo "Checking PROPRIETARY_LICENSE.md in premium directories..."
PREMIUM_DIRS=(
    "$REPO_ROOT/backend/app/features/premium"
    "$REPO_ROOT/frontend-web/src/features/premium"
)

for dir in "${PREMIUM_DIRS[@]}"; do
    if [ ! -f "$dir/PROPRIETARY_LICENSE.md" ]; then
        echo "FAIL: $dir/PROPRIETARY_LICENSE.md not found"
        exit 1
    fi
    echo "  ✓ $dir/PROPRIETARY_LICENSE.md exists"
done

echo "Checking for proprietary code in MIT paths..."
PREMIUM_IMPORTS=$(find "$REPO_ROOT/backend/app" -name "*.py" \
    ! -path "$REPO_ROOT/backend/app/features/premium/*" \
    -exec grep -l "from.*features.premium\|import.*features.premium" {} \; 2>/dev/null || true)

if [ -n "$PREMIUM_IMPORTS" ]; then
    echo "FAIL: MIT-licensed files importing from premium:"
    echo "$PREMIUM_IMPORTS"
    exit 1
fi

PREMIUM_IMPORTS=$(find "$REPO_ROOT/frontend-web/src" -name "*.ts" -o -name "*.tsx" \
    ! -path "$REPO_ROOT/frontend-web/src/features/premium/*" \
    -exec grep -l "from.*features/premium\|import.*features/premium" {} \; 2>/dev/null || true)

if [ -n "$PREMIUM_IMPORTS" ]; then
    echo "FAIL: MIT-licensed files importing from premium:"
    echo "$PREMIUM_IMPORTS"
    exit 1
fi

echo "=== All checks passed ==="
exit 0