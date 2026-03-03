"""To-Do list manages with Categories and tasks, set deadlines, asign priority, and filter by projects or tag."""
from datetime import datetime

class Task:
    def __init__(self, title, project, tags, deadline_str, priority):
        self.title = title
        self.project = project
        self.tags = tags if isinstance(tags, list) else [tags]
        self.priority = str(priority).upper()
        self.is_completed = False
        
        # Parse the deadline string into a date object (Format: YYYY-MM-DD)
        try:
            self.deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        except ValueError:
            print(f"Warning: Invalid date format for '{title}'. Using today's date.")
            self.deadline = datetime.today().date()

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "✓" if self.is_completed else "✗"
        tags_str = ", ".join(self.tags)
        return (f"[{status}] {self.title} | Project: {self.project} | "
                f"Tags: [{tags_str}] | Priority: {self.priority} | Due: {self.deadline}")


class ToDoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, project, tags, deadline_str, priority):
        new_task = Task(title, project, tags, deadline_str, priority)
        self.tasks.append(new_task)
        print(f"Added: '{title}'")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_completed()
                print(f"Completed: '{task.title}'")
                return
        print(f"Task '{title}' not found.")

    def display_tasks(self, task_list=None):
        tasks_to_display = task_list if task_list is not None else self.tasks
        if not tasks_to_display:
            print("No tasks found.")
            return
            
        print("-" * 60)
        for task in tasks_to_display:
            print(task)
        print("-" * 60)

    def filter_by_project(self, project_name):
        filtered = [task for task in self.tasks if task.project.lower() == project_name.lower()]
        print(f"\n--- Tasks for Project: {project_name} ---")
        self.display_tasks(filtered)

    def filter_by_tag(self, tag_name):
        filtered = [task for task in self.tasks if tag_name.lower() in [t.lower() for t in task.tags]]
        print(f"\n--- Tasks with Tag: {tag_name} ---")
        self.display_tasks(filtered)

    def sort_by_deadline(self):
        # Sorts tasks by date. Incomplete tasks appear first.
        sorted_tasks = sorted(self.tasks, key=lambda x: (x.is_completed, x.deadline))
        print("\n--- Tasks Sorted by Deadline ---")
        self.display_tasks(sorted_tasks)


# ==========================================
# Demonstration of the To-Do Manager
# ==========================================
if __name__ == "__main__":
    # Initialize the manager
    manager = ToDoManager()

    # 1. Add some tasks
    print("Initializing tasks...\n")
    manager.add_task("Write Python Script", "Development", ["coding", "python"], "2026-03-05", "High")
    manager.add_task("Buy Groceries", "Personal", ["errands", "food"], "2026-03-03", "Medium")
    manager.add_task("Prepare Presentation", "Work", ["slides", "meeting"], "2026-03-10", "High")
    manager.add_task("Update Server Packages", "Development", ["maintenance", "linux"], "2026-03-08", "Low")

    # 2. View all tasks
    print("\nAll Tasks:")
    manager.display_tasks()

    # 3. Mark a task as completed
    print("\nCompleting a task...")
    manager.complete_task("Buy Groceries")

    # 4. Filter by Project
    manager.filter_by_project("Development")

    # 5. Filter by Tag
    manager.filter_by_tag("meeting")

    # 6. View tasks sorted by deadline
    manager.sort_by_deadline()