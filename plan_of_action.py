import argparse
from pathlib import Path


def generate_plan_of_action(summary):
    """Turn summary sentences into a simple list of action items."""
    action_items = (item.strip() for item in summary.split("."))
    return "\n".join(f"- {item}" for item in action_items if item)


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
