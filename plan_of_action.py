def generate_plan_of_action(summary):
    """Generate a simple plan of action based on the meeting summary."""
    # Example: Split the summary into action items
    action_items = summary.split(". ")
    plan_of_action = [f"- {item.strip()}" for item in action_items if item]

    return "\n".join(plan_of_action)

if __name__ == "__main__":
    with open("data/text/summary.txt", "r") as file:
        summary = file.read()

    plan_of_action = generate_plan_of_action(summary)
    print("Plan of Action: ", plan_of_action)

    # Save the plan of action to a text file
    with open("data/text/plan_of_action.txt", "w") as f:
        f.write(plan_of_action)
