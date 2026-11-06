tasks = [
    {"name": "Complete Python assignment", "status": "Pending"},
    {"name": "Read course notes", "status": "Done"},
    {"name": "Practise Python loops", "status": "Pending"},
    {"name": "Install Python", "status": "Done"},
    {"name": "Review dictionaries", "status": "Pending"},
]

pending_tasks = []
done_tasks = []

for task in tasks:
    if task["status"] == "Pending":
        pending_tasks.append(task)
    elif task["status"] == "Done":
        done_tasks.append(task)
    else:
        raise ValueError(f"Invalid status for task: {task['name']}")

lines = [
    "TASK TRACKER SUMMARY",
    "====================",
    f"Total tasks: {len(tasks)}",
    f"Pending: {len(pending_tasks)}",
    f"Done: {len(done_tasks)}",
    "",
    "Pending tasks:",
]

for task in pending_tasks:
    lines.append(f"- {task['name']}")

lines.append("")
lines.append("Done tasks:")

for task in done_tasks:
    lines.append(f"- {task['name']}")

summary = "\n".join(lines) + "\n"

print(summary, end="")

with open("task_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

# Confirm the counts and saved output are correct.
assert len(tasks) == 5
assert len(pending_tasks) == 3
assert len(done_tasks) == 2

with open("task_summary.txt", "r", encoding="utf-8") as file:
    assert file.read() == summary
