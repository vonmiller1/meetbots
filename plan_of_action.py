import argparse
import re
from pathlib import Path


_ITEM_BOUNDARY = re.compile(r"(?<=[.!?])\s+")
_LIST_MARKER = re.compile(r"^(?:[-*+]\s+|\d+[.)]\s+)")


def generate_plan_of_action(summary):
    """Format summary sentences or existing list entries as bullet points."""
    action_items = []
    for line in summary.splitlines():
        line = line.strip()
        if not line:
            continue
        items = [line] if _LIST_MARKER.match(line) else _ITEM_BOUNDARY.split(line)
        for item in items:
            item = _LIST_MARKER.sub("", item.strip()).rstrip(".!?").strip()
            if item:
                action_items.append(f"- {item}")
    return "\n".join(action_items)


def main():
    parser = argparse.ArgumentParser(description="Create an action-item list from a summary.")
    parser.add_argument("summary", type=Path, help="Path to a UTF-8 meeting summary")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("plan_of_action.txt"),
        help="Output path (default: plan_of_action.txt)",
    )
    args = parser.parse_args()

    plan = generate_plan_of_action(args.summary.read_text(encoding="utf-8"))
    args.output.write_text(plan, encoding="utf-8")
    print(f"Plan of action saved to: {args.output}")


if __name__ == "__main__":
    main()
