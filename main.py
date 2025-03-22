# All necessarry imports

from tkinter import *
import os
import datetime
import git
from tkinter import ttk, messagebox

# Function to save data to README.md
def save_to_readme():
    date = datetime.date.today().strftime("%Y-%m-%d")
    # priorities = entry_priorities.get("1.0", tk.END).strip()
    # routine = entry_routine.get("1.0", tk.END).strip()
    # secondary_tasks = entry_secondary.get("1.0", tk.END).strip()
    # notes = entry_notes.get("1.0", tk.END).strip()
    # reflection = entry_reflection.get("1.0", tk.END).strip()
    priorities1 = entryPriorities1.get().strip()
    priorities2 = entryPriorities2.get().strip()
    priorities3 = entryPriorities3.get().strip()

    secondaryTask1 = entrySecondaryTasks1.get().strip()
    secondaryTask2 = entrySecondaryTasks2.get().strip()

    notes = entryNotes.get().strip()

    if priorities1 and priorities2 and priorities3 and secondaryTask1 and secondaryTask2 and notes != "":
        # Convert data into a well-formatted Markdown
        markdown_content = f"""
# 📅 Date - {date}

## 🌟 Top 3 Priorities
### 1. {priorities1}
### 2. {priorities2}
### 3. {priorities3}

## 📌 Secondary Tasks
### 1. {secondaryTask1}
### 2. {secondaryTask2}

## 📝 Notes / Reminders for Tomorrow
### {notes}

---

    """
        try:
            # Write to README.md
            with open("Dashboard_data.md", "w", encoding="utf-8") as file:
                file.write(markdown_content)

            messagebox.showinfo("Success", "Saved to README.md successfully!")

            # Automate commit & push
            commit_and_push()
        except Exception as e:
            messagebox.showerror("Error", {e})
    elif (secondaryTask1 and secondaryTask2 == ""):
        secondaryTask1 = "No secondary task"
        secondaryTask2 = "No secondary task"
    else:
        messagebox.showerror("Error", "Please fill the data")

# Function to commit & push using GitPython
def commit_and_push():
    try:
        repo = git.Repo(os.getcwd())  # Get the current Git repo
        repo.git.add(".")  # Stage changes
        repo.index.commit(f"Updated Daily Planner - {datetime.date.today()}")  # Commit changes
        origin = repo.remote(name='origin')
        origin.push()  # Push to GitHub
        messagebox.showinfo("Success", "Changes pushed to GitHub successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Git push failed: {e}")

# Creating UI

# initiallizing window
root = Tk()
# setting window title
root.title("Personal Productivity Dashboard")
# setting window size
root.geometry("800x600")
# setting window background color to dark theme
root.configure(bg="#393838")

# # creating a frame to hold the dashboard with dark theme
# frame = Frame(root, bg="#2e2e2e")
# frame.pack(fill="both", expand=True)

# Creating a frame for the priorities section
priorities_frame = Frame(root, bg="#2e2e2e")
priorities_frame.pack(pady=20, padx=20, fill="x")

# Adding a label for the priorities section
Label(priorities_frame, text="🌟 Top 3 Priorities", font=("Arial", 14, "bold"), bg="#2e2e2e", fg="white").pack()

# Adding entry fields for the top 3 priorities with some padding and modern styling
style = ttk.Style()
style.configure("TEntry", padding=5, relief="flat", font=("Arial", 12))

entryPriorities1 = ttk.Entry(priorities_frame, width=100, style="TEntry")
entryPriorities1.pack(pady=5, fill="x")

entryPriorities2 = ttk.Entry(priorities_frame, width=100, style="TEntry")
entryPriorities2.pack(pady=5, fill="x")

entryPriorities3 = ttk.Entry(priorities_frame, width=100, style="TEntry")
entryPriorities3.pack(pady=5, fill="x")

# Creating a frame for handling Daily Routine (Flexible Time Blocks)
secondary_tasks_frame = Frame(root, bg="#2e2e2e")
secondary_tasks_frame.pack(pady=20, padx=20, fill="x")

# Adding a label for the daily routine section
Label(secondary_tasks_frame, text=" 📌 Secondary Tasks (If time allows)", font=("Arial", 14, "bold"), bg="#2e2e2e", fg="white").pack()
# Adding entry fields for the daily routine with some padding and modern styling
# style = ttk.Style()
# style.configure("TEntry", padding=5, relief="flat", font=("Arial", 12))

entrySecondaryTasks1 = ttk.Entry(secondary_tasks_frame, width=100, style="TEntry")
entrySecondaryTasks1.pack(pady=5, fill="x")

entrySecondaryTasks2 = ttk.Entry(secondary_tasks_frame, width=100, style="TEntry")
entrySecondaryTasks2.pack(pady=5, fill="x")
                                                 
# creating a frame for handling daily Nonets or Reminder for Tomorrow
daily_reminder_frame = Frame(root, bg="#2e2e2e")
daily_reminder_frame.pack(pady=20, padx=20, fill="x")

# Adding a label for the daily notes
Label(daily_reminder_frame, text=" 📝 Daily Notes or Reminder for Tomorrow", font=("Arial", 14, "bold"), bg="#2e2e2e",fg="white").pack()
# Adding entry fields for the daily notes with some padding and modern styling
entryNotes = ttk.Entry(daily_reminder_frame,  width=100, style="TEntry")
entryNotes.pack(pady=5, fill="x")

# # Creating a frame for handling day reflections
# day_reflection_frame = Frame(root, bg="#2e2e2e")
# day_reflection_frame.pack(pady=20, padx=20, fill="x")
# # Adding a label for the day reflections section
# Label(day_reflection_frame, text=" 🔍 End-of-Day Reflection", font=("Arial", 14, "bold"), bg="#2e2e2e", fg="white").pack()


# Adding save button

save_button = Button(root, text="Save & Push to GitHub", command=save_to_readme, bg="green", fg="white", font=("Arial", 12, "bold"))
save_button.pack(pady=10)

# Ending loop of window
root.mainloop()