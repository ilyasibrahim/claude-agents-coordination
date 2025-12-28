#!/bin/bash
# Agent Deliverable Verification Script
# Usage: ./verify.sh <category> <name> <date> [git-path]
# Returns: 0 if all checks pass, 1 if any fail

set -e

# Arguments
CATEGORY="$1"
NAME="$2"
DATE="$3"
GIT_PATH="$4"

# Derived paths
REPORT=".claude/reports/$CATEGORY/$NAME-$DATE.md"
REGISTRY=".claude/reports/_registry.md"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

PASS=0
FAIL=0

check() {
    local desc="$1"
    local result="$2"
    if [ "$result" -eq 0 ]; then
        echo -e "${GREEN}[PASS]${NC} $desc"
        ((PASS++))
    else
        echo -e "${RED}[FAIL]${NC} $desc"
        ((FAIL++))
    fi
}

echo "Verifying: $REPORT"
echo "---"

# Check 1: Report exists
if [ -f "$REPORT" ]; then
    check "Report file exists" 0
else
    check "Report file exists" 1
fi

# Check 2: Report has content (>10 lines)
if [ -f "$REPORT" ]; then
    LINES=$(wc -l < "$REPORT" | tr -d ' ')
    if [ "$LINES" -gt 10 ]; then
        check "Report has content ($LINES lines)" 0
    else
        check "Report has content ($LINES lines < 10)" 1
    fi
else
    check "Report has content" 1
fi

# Check 3: Registry updated
if grep -q "$NAME-$DATE" "$REGISTRY" 2>/dev/null; then
    check "Registry entry exists" 0
else
    check "Registry entry exists" 1
fi

# Check 4: Git changes (optional)
if [ -n "$GIT_PATH" ]; then
    if git status --short 2>/dev/null | grep -q "$GIT_PATH"; then
        check "Git changes detected in $GIT_PATH" 0
    else
        check "Git changes detected in $GIT_PATH" 1
    fi
fi

echo "---"
echo "Results: $PASS passed, $FAIL failed"

# Exit code
if [ "$FAIL" -gt 0 ]; then
    exit 1
else
    exit 0
fi
