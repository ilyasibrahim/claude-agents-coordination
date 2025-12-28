#!/usr/bin/env python3
"""Archive old registry entries and reports.

Moves registry entries and their associated report files older than N days
to the archive directory while preserving structure and maintaining history.
"""

import re
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Tuple


def parse_date(date_str: str) -> datetime:
    """Parse date from registry entry (YYYY-MM-DD format)."""
    return datetime.strptime(date_str, "%Y-%m-%d")


def is_older_than(date_str: str, days_threshold: int) -> bool:
    """Check if date is older than threshold days."""
    entry_date = parse_date(date_str)
    threshold_date = datetime.now() - timedelta(days=days_threshold)
    return entry_date < threshold_date


def extract_report_info(line: str) -> Tuple[str, str, str, str]:
    """Extract report filename, date, status, and category from registry line.

    Returns:
        (filename, date, status, category) or (None, None, None, None) if not a report line
    """
    # Match pattern: | [filename](category/filename) | YYYY-MM-DD | Status | Summary |
    pattern = r'\| \[(.*?)\]\((.*?)\) \| (\d{4}-\d{2}-\d{2}) \| (.*?) \|'
    match = re.match(pattern, line)

    if not match:
        return None, None, None, None

    filename = match.group(1)
    full_path = match.group(2)
    date = match.group(3)
    status = match.group(4)

    # Extract category from path (e.g., "analysis/file.md" -> "analysis")
    category = full_path.split('/')[0] if '/' in full_path else None

    return filename, date, status, category


def archive_reports(days_threshold: int = 7, dry_run: bool = False) -> None:
    """Archive reports older than days_threshold.

    Args:
        days_threshold: Archive entries older than this many days
        dry_run: If True, only print what would be archived without moving files
    """
    reports_dir = Path(".claude/reports")
    registry_file = reports_dir / "_registry.md"
    archive_dir = reports_dir / "archive"

    # Create dated archive registry (e.g., _registry-archive-20251228.md)
    archive_date = datetime.now().strftime("%Y%m%d")
    archive_registry = archive_dir / f"_registry-archive-{archive_date}.md"

    if not registry_file.exists():
        print(f"❌ Registry not found: {registry_file}")
        return

    # Create archive directory structure
    if not dry_run:
        archive_dir.mkdir(exist_ok=True)

    # Read current registry
    with open(registry_file, 'r') as f:
        lines = f.readlines()

    # Process registry
    archived_entries = []
    remaining_entries = []
    current_category = None
    in_category_table = False

    for line in lines:
        # Track current category section
        if line.startswith("### "):
            current_category = line.strip().replace("### ", "").lower()
            remaining_entries.append(line)
            in_category_table = False
            continue

        # Track if we're in a table
        if line.startswith("| Report |"):
            in_category_table = True
            remaining_entries.append(line)
            continue

        if line.startswith("|---"):
            remaining_entries.append(line)
            continue

        # Process report entries
        filename, date, status, category = extract_report_info(line)

        if filename and date and category:
            if is_older_than(date, days_threshold):
                # Mark for archiving
                archived_entries.append((line, filename, date, status, category))
                print(f"📦 Archiving: {category}/{filename} (Date: {date}, Status: {status})")

                # Move report file
                source_file = reports_dir / category / filename
                if source_file.exists():
                    if not dry_run:
                        archive_category_dir = archive_dir / category
                        archive_category_dir.mkdir(exist_ok=True)
                        dest_file = archive_category_dir / filename
                        shutil.move(str(source_file), str(dest_file))
                        print(f"  ✅ Moved: {source_file} → {dest_file}")
                    else:
                        print(f"  [DRY RUN] Would move: {source_file} → {archive_dir / category / filename}")
                else:
                    print(f"  ⚠️  File not found: {source_file}")
            else:
                # Keep in active registry
                remaining_entries.append(line)
        else:
            # Keep non-report lines (headers, separators, etc.)
            remaining_entries.append(line)

    # Write updated registry
    if not dry_run:
        with open(registry_file, 'w') as f:
            f.writelines(remaining_entries)
        print(f"\n✅ Updated active registry: {registry_file}")
    else:
        print(f"\n[DRY RUN] Would update: {registry_file}")

    # Create dated archive registry
    if archived_entries and not dry_run:
        # Create new dated archive registry (always creates new file)
        with open(archive_registry, 'w') as f:
            # Create header
            f.write("# Archived Reports\n\n")
            f.write(f"**Archive Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f"**Threshold:** Reports older than {days_threshold} days\n")
            f.write(f"**Total Archived:** {len(archived_entries)} reports\n\n")
            f.write("---\n\n")

            # Group by category
            by_category = {}
            for line, filename, date, status, category in archived_entries:
                if category not in by_category:
                    by_category[category] = []
                by_category[category].append(line)

            # Write by category
            for category, entries in sorted(by_category.items()):
                f.write(f"### {category.title()}\n\n")
                f.write("| Report | Date | Status | Summary |\n")
                f.write("|--------|------|--------|---------|\n")
                for entry in entries:
                    # Update status to "Archived"
                    entry_modified = re.sub(
                        r'\| (.*?) \| (.*?) \| (.*?) \|',
                        r'| \1 | \2 | Archived |',
                        entry,
                        count=1
                    )
                    f.write(entry_modified)
                f.write("\n---\n\n")

        print(f"✅ Created dated archive registry: {archive_registry}")
    elif archived_entries and dry_run:
        print(f"\n[DRY RUN] Would create: {archive_registry}")

    # Summary
    print(f"\n📊 Summary:")
    print(f"  - Archive Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"  - Threshold: {days_threshold} days")
    print(f"  - Archived: {len(archived_entries)} reports")
    print(f"  - Remaining: {len([l for l in remaining_entries if extract_report_info(l)[0]])} reports")
    if archived_entries:
        print(f"  - Registry: {archive_registry.name}")

    if dry_run:
        print("\n⚠️  DRY RUN - No files were actually moved")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Archive old registry entries")
    parser.add_argument(
        "days",
        type=int,
        nargs="?",
        default=7,
        help="Archive entries older than N days (default: 7)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be archived without moving files"
    )

    args = parser.parse_args()

    print(f"🗄️  Archive Reports")
    print(f"{'=' * 60}\n")

    archive_reports(days_threshold=args.days, dry_run=args.dry_run)
