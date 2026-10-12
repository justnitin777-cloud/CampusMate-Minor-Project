# CampusMate Viva Questions and Answers

1. **What is CampusMate?**  
   CampusMate is a web-based student task planner that helps users add and track academic assignments.

2. **Why did you choose this project?**  
   Students often need a simple way to organize assignment deadlines. This project solves that practical problem and is suitable for demonstrating Python web development.

3. **Which programming language is used?**  
   Python is used for the main application logic.

4. **What is Flask?**  
   Flask is a lightweight Python web framework used to build web applications and handle browser requests.

5. **What is SQLite?**  
   SQLite is a small relational database that stores data in a local file and does not require a separate database server.

6. **What is HTML used for?**  
   HTML defines the structure of the web pages, such as headings, forms, inputs, and buttons.

7. **What is CSS used for?**  
   CSS controls the appearance of the website, including colors, spacing, layout, and responsiveness.

8. **What is a route in Flask?**  
   A route connects a URL and HTTP method to a Python function. For example, `/` displays the dashboard.

9. **What is CRUD?**  
   CRUD means Create, Read, Update, and Delete. CampusMate supports these operations for tasks.

10. **How is data saved?**  
    Task data is stored in the `tasks` table in the `campusmate.db` SQLite database.

11. **What is a primary key?**  
    A primary key uniquely identifies each row. In this project, `id` is the primary key.

12. **Why use parameterized SQL queries?**  
    They safely pass values separately from SQL instructions and help reduce SQL injection risk.

13. **What is Jinja?**  
    Jinja is a template engine used by Flask to insert dynamic Python data into HTML templates.

14. **What does `request.form` do?**  
    It reads values submitted by an HTML form.

15. **What does `redirect()` do?**  
    It sends the browser to another route, such as returning to the dashboard after saving a task.

16. **What is the difference between GET and POST?**  
    GET usually requests or displays information. POST is commonly used to submit data or perform an action.

17. **How do you calculate pending tasks?**  
    The application runs an SQL COUNT query for rows whose status is `Pending`.

18. **How is an overdue task identified?**  
    A task is considered overdue when its status is Pending and its due date is earlier than today's date.

19. **Does the project require internet to run?**  
    No, not after Python and Flask are installed. The Google Fonts styling may need internet, but the core app works without it.

20. **What are the limitations?**  
    The current version has no login, multi-user support, or actual reminder notifications.

21. **What can be added in the future?**  
    Login, attendance tracking, a calendar, search, reports, and reminders can be added.

22. **What did you learn from this project?**  
    I learned how Flask routes, HTML forms, Python functions, SQL queries, and a database work together in a web application.

**Viva tip:** Understand each answer and practice demonstrating add, edit, complete, and delete features. Be ready to explain the code you submit.
