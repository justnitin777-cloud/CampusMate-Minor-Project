from datetime import date
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, abort

app = Flask(__name__)
app.secret_key = "change-this-secret-key-for-your-own-project"
DATABASE = "campusmate.db"

def get_db_connection():
    """Open a database connection and return rows as dictionary-like objects."""
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    """Create the tasks table if it does not already exist."""
    connection = get_db_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT NOT NULL,
            due_date TEXT NOT NULL,
            priority TEXT NOT NULL DEFAULT 'Medium',
            status TEXT NOT NULL DEFAULT 'Pending',
            created_at TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

@app.route("/")
def index():
    connection = get_db_connection()
    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY "
        "CASE status WHEN 'Pending' THEN 0 ELSE 1 END, due_date ASC, id DESC"
    ).fetchall()
    total = connection.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    pending = connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Pending'"
    ).fetchone()[0]
    completed = connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Completed'"
    ).fetchone()[0]
    overdue = connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Pending' AND due_date < ?",
        (date.today().isoformat(),)
    ).fetchone()[0]
    connection.close()
    return render_template(
        "index.html", tasks=tasks, total=total, pending=pending,
        completed=completed, overdue=overdue, today=date.today().isoformat()
    )

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    subject = request.form.get("subject", "").strip()
    due_date = request.form.get("due_date", "").strip()
    priority = request.form.get("priority", "Medium")
    allowed_priorities = {"Low", "Medium", "High"}

    if not title or not subject or not due_date:
        flash("Please fill in all required fields.", "error")
        return redirect(url_for("index"))
    if len(title) > 100 or len(subject) > 60:
        flash("Title must be at most 100 characters and subject at most 60.", "error")
        return redirect(url_for("index"))
    try:
        date.fromisoformat(due_date)
    except ValueError:
        flash("Please enter a valid due date.", "error")
        return redirect(url_for("index"))
    if priority not in allowed_priorities:
        priority = "Medium"

    connection = get_db_connection()
    connection.execute(
        "INSERT INTO tasks (title, subject, due_date, priority, status, created_at) "
        "VALUES (?, ?, ?, ?, 'Pending', ?)",
        (title, subject, due_date, priority, date.today().isoformat())
    )
    connection.commit()
    connection.close()
    flash("Task added successfully!", "success")
    return redirect(url_for("index"))

@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    connection = get_db_connection()
    task = connection.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if task is None:
        connection.close()
        abort(404)
    new_status = "Completed" if task["status"] == "Pending" else "Pending"
    connection.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    connection.commit()
    connection.close()
    flash("Task status updated.", "success")
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    connection = get_db_connection()
    connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()
    flash("Task deleted.", "success")
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    connection = get_db_connection()
    task = connection.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if task is None:
        connection.close()
        abort(404)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        subject = request.form.get("subject", "").strip()
        due_date = request.form.get("due_date", "").strip()
        priority = request.form.get("priority", "Medium")
        if not title or not subject or not due_date:
            flash("Please fill in all required fields.", "error")
            connection.close()
            return redirect(url_for("edit_task", task_id=task_id))
        if len(title) > 100 or len(subject) > 60:
            flash("Title must be at most 100 characters and subject at most 60.", "error")
            connection.close()
            return redirect(url_for("edit_task", task_id=task_id))
        try:
            date.fromisoformat(due_date)
        except ValueError:
            flash("Please enter a valid due date.", "error")
            connection.close()
            return redirect(url_for("edit_task", task_id=task_id))
        if priority not in {"Low", "Medium", "High"}:
            priority = "Medium"
        connection.execute(
            "UPDATE tasks SET title=?, subject=?, due_date=?, priority=? WHERE id=?",
            (title, subject, due_date, priority, task_id)
        )
        connection.commit()
        connection.close()
        flash("Task updated successfully.", "success")
        return redirect(url_for("index"))

    connection.close()
    return render_template("edit.html", task=task)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
