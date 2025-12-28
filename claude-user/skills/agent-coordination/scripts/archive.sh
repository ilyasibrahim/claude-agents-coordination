#!/bin/bash
# Registry Archive Script
# Usage: ./archive.sh [days_threshold]
# Default: 7 days

set -e

DAYS=${1:-7}
REPORTS_DIR=".claude/reports"
ARCHIVE_DIR="$REPORTS_DIR/archive"
REGISTRY="$REPORTS_DIR/_registry.md"
ARCHIVE_REGISTRY="$ARCHIVE_DIR/_registry-archive.md"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Calculate threshold date
if [[ "$OSTYPE" == "darwin"* ]]; then
    THRESHOLD=$(date -v-${DAYS}d +%Y-%m-%d)
else
    THRESHOLD=$(date -d "${DAYS} days ago" +%Y-%m-%d)
fi

echo "Archiving entries older than $THRESHOLD ($DAYS days)"
echo "---"

# Create archive directories if needed
mkdir -p "$ARCHIVE_DIR"/{analysis,arch,bugs,design,impl,review,tests,handoff}

# Initialize archive registry if needed
if [ ! -f "$ARCHIVE_REGISTRY" ]; then
    cat > "$ARCHIVE_REGISTRY" << 'EOF'
# Registry Archive

Archived registry entries. For historical reference only.

---

EOF
fi

ARCHIVED=0

# Count actual entries (format: "- name | Status | summary")
TOTAL_ENTRIES=$(grep -c "^- .*|.*|" "$REGISTRY" 2>/dev/null || echo 0)
echo "Registry has $TOTAL_ENTRIES report entries"

# Find report files older than threshold
find "$REPORTS_DIR" -maxdepth 2 -name "*.md" -type f ! -path "*/archive/*" ! -name "_registry*" | while read -r file; do
    # Extract date from filename (assumes format *-YYYYMMDD.md)
    filename=$(basename "$file")

    # Try to extract date from filename
    if [[ $filename =~ ([0-9]{4})([0-9]{2})([0-9]{2})\.md$ ]]; then
        file_date="${BASH_REMATCH[1]}-${BASH_REMATCH[2]}-${BASH_REMATCH[3]}"

        if [[ "$file_date" < "$THRESHOLD" ]]; then
            # Determine category from path
            category=$(dirname "$file" | xargs basename)

            # Move to archive
            mv "$file" "$ARCHIVE_DIR/$category/"
            echo -e "${GREEN}[ARCHIVED]${NC} $filename → archive/$category/"

            ((ARCHIVED++)) || true
        fi
    fi
done

echo "---"
echo -e "${YELLOW}Archived $ARCHIVED report(s)${NC}"
echo ""
echo "Next steps:"
echo "1. Review $ARCHIVE_REGISTRY"
echo "2. Update active registry to remove archived entries"
echo "3. Run: grep -v 'YYYYMMDD' $REGISTRY (to find stale entries)"
