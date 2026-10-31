"""Export the "## Miro cards" table of each sota/miro/0*.md file to csv/<file>.csv.

Run from anywhere:  python sota/miro/build_csv.py
CSV files are UTF-8 with BOM (opens correctly in Excel) and comma-separated.
Edit the markdown, not the CSV: the markdown is the source of truth.
"""
import csv
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "csv"
LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def clean(cell: str) -> str:
    cell = LINK.sub(r"\1", cell.strip())
    return cell.replace("*", "").replace("`", "")


def miro_table(md: str) -> list[list[str]]:
    lines = md.splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == "## Miro cards")
    rows = []
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = [clean(c) for c in line.strip().strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):
            continue  # separator row
        rows.append(cells)
    return rows


def reference_rows(md: str) -> list[list[str]]:
    rows = [["Section", "Reference", "Cited in", "New in this deep dive"]]
    section = ""
    for line in md.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        elif line.startswith("- "):
            tag = re.search(r"`\[([^\]]+)\]`\s*$", line)
            text = re.sub(r"\s*`\[[^\]]+\]`\s*$", "", line[2:])
            new = "yes" if "**New**" in text else ""
            rows.append([section, clean(text.replace("**New**", "")),
                         tag.group(1) if tag else "", new])
    return rows


def write(target: Path, rows: list[list[str]]) -> None:
    with target.open("w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"{target.relative_to(HERE)}: {len(rows) - 1} rows")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for md_file in sorted(HERE.glob("0*.md")):
        write(OUT / f"{md_file.stem}.csv", miro_table(md_file.read_text(encoding="utf-8")))
    refs = (HERE / "references.md").read_text(encoding="utf-8")
    write(OUT / "07_references.csv", reference_rows(refs))


if __name__ == "__main__":
    main()
