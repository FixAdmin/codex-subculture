from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "subculture"
SKILL_FILE = SKILL_DIR / "SKILL.md"
BRIEF_FILE = SKILL_DIR / "references" / "implementation-brief.md"
OPENAI_FILE = SKILL_DIR / "agents" / "openai.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


skill = read(SKILL_FILE)
brief = read(BRIEF_FILE)
openai = read(OPENAI_FILE)

lines = skill.splitlines()
if not lines or lines[0] != "---":
    fail("SKILL.md must start with YAML frontmatter")

try:
    closing = lines.index("---", 1)
except ValueError:
    fail("SKILL.md frontmatter is not closed")

metadata: dict[str, str] = {}
for line in lines[1:closing]:
    match = re.fullmatch(r"([a-zA-Z0-9_-]+):\s*(.+)", line)
    if not match:
        fail(f"invalid frontmatter line: {line!r}")
    metadata[match.group(1)] = match.group(2).strip()

if set(metadata) != {"name", "description"}:
    fail("SKILL.md frontmatter must contain only name and description")
if metadata["name"] != "subculture":
    fail("skill name must be subculture")
if not metadata["description"]:
    fail("skill description must not be empty")
if len(lines) > 500:
    fail("SKILL.md must remain under 500 lines")

required_main_markers = (
    "SUBCULTURE",
    "create_thread",
    "spawn_agent",
    "references/implementation-brief.md",
    "protocol violation",
    "final adversarial risk check",
)
skill_folded = skill.casefold()
for marker in required_main_markers:
    if marker.casefold() not in skill_folded:
        fail(f"SKILL.md is missing required protocol marker: {marker}")

required_brief_sections = (
    "## Authoring rules",
    "## Required contract",
    "### Communication protocol",
    "### Terminal report format",
    "### Curator verification",
)
for section in required_brief_sections:
    if section not in brief:
        fail(f"implementation brief is missing section: {section}")
if brief.startswith("---"):
    fail("implementation brief must be a bundled reference, not a standalone skill")

combined = "\n".join((skill, brief, openai))
if re.search(r"[\u0400-\u04ff]", combined):
    fail("skill package must not contain Cyrillic text")
if "$write-implementation-brief" in combined:
    fail("retired standalone brief dependency is still referenced")
if "$subculture" not in openai:
    fail("agents/openai.yaml must mention $subculture in default_prompt")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() not in {".md", ".py", ".yaml", ".yml", ".txt"}:
        continue
    content = path.read_text(encoding="utf-8")
    if re.search(r"[\u0400-\u04ff]", content):
        fail(f"Cyrillic text is not allowed: {path.relative_to(ROOT)}")
    retired_name = "aiw" + "-codex-subculture"
    if retired_name in content.casefold():
        fail(f"retired repository name found: {path.relative_to(ROOT)}")

for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill):
    if target.startswith(("http://", "https://", "#")):
        continue
    local_target = target.split("#", 1)[0]
    if not (SKILL_DIR / local_target).is_file():
        fail(f"broken local link in SKILL.md: {target}")

print("OK: subculture skill package is valid")
