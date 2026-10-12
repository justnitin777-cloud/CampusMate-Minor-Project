# CAMPUSMATE – STUDENT TASK & STUDY PLANNER
## Minor Project Report (BCA 5th Semester)

**Submitted by:** [Your Name]  
**Roll Number:** [Your Roll Number]  
**Course:** Bachelor of Computer Applications (BCA), 5th Semester  
**College:** [College Name]  
**Submitted to:** [Teacher/Guide Name]  
**Academic Session:** [Year]

---

## 1. Abstract
CampusMate is a web-based student task and study planner developed using Python and Flask. It helps students organize assignments and academic tasks by storing a task title, subject, due date, and priority. The dashboard displays the total number of tasks, pending tasks, completed tasks, and overdue tasks. Users can add, edit, complete, and delete tasks. SQLite is used to store data locally, so task records remain available after the application is restarted. The project demonstrates the practical use of web development, database operations, and basic software design.

## 2. Introduction
Students often manage assignment deadlines and study tasks using paper notes or scattered reminders. This can make it difficult to see all pending work in one place. CampusMate provides a simple dashboard where academic tasks can be recorded and tracked. The application is designed as a small, understandable project for learning Python-based web development.

## 3. Problem Statement
Students may forget deadlines or find it difficult to track completed and pending assignments. A simple system is needed to store academic tasks and present their current status in one place.

## 4. Objectives
- Create a simple student-friendly web interface.
- Allow users to add tasks with subjects, due dates, and priorities.
- Allow tasks to be edited, completed, or deleted.
- Store task information in an SQLite database.
- Show a summary of total, pending, completed, and overdue tasks.
- Practice Python, Flask, HTML, CSS, and SQL concepts.

## 5. Scope
The project is intended for a local single-user demonstration. It can be extended in the future with login accounts, attendance tracking, notifications, calendar views, and cloud hosting. The current version does not send real notifications and does not have separate accounts for multiple students.

## 6. Tools and Technologies
- **Python:** Main programming language and application logic.
- **Flask:** Python web framework that handles URLs and requests.
- **HTML:** Defines page structure and forms.
- **CSS:** Controls layout, colors, spacing, and responsive styling.
- **SQLite:** Local relational database for task records.
- **Jinja templates:** Display dynamic task data in HTML pages.
- **Visual Studio Code or any text editor:** Optional code editor.

## 7. System Requirements
### Hardware
- Computer or laptop
- At least 2 GB RAM recommended
- Keyboard, mouse/touchpad, and display

### Software
- Windows, macOS, or Linux
- Python 3.10 or newer recommended
- Flask package
- Modern web browser

## 8. Main Modules
1. **Dashboard Module:** Displays all tasks and summary counts.
2. **Add Task Module:** Accepts title, subject, due date, and priority.
3. **Edit Task Module:** Updates existing task details.
4. **Status Module:** Switches a task between Pending and Completed.
5. **Delete Module:** Removes a task after confirmation.
6. **Database Module:** Stores and retrieves task records from SQLite.

## 9. Database Design
Table name: `tasks`

| Field | Type | Description |
|---|---|---|
| id | INTEGER, Primary Key | Unique task identifier |
| title | TEXT | Task or assignment name |
| subject | TEXT | Related subject |
| due_date | TEXT | Due date in YYYY-MM-DD format |
| priority | TEXT | Low, Medium, or High |
| status | TEXT | Pending or Completed |
| created_at | TEXT | Date the task was created |

## 10. Working of the System
1. The user opens the local website in a browser.
2. Flask handles the request for the dashboard.
3. The application reads task records and summary counts from SQLite.
4. The user submits a form to add a task.
5. Flask validates the submitted fields and saves the task using a parameterized SQL query.
6. The dashboard reloads and shows the updated information.
7. The user can edit a task, change its status, or delete it.

## 11. Algorithm
1. Start the application.
2. Create the database table if it does not exist.
3. Display the dashboard and read saved tasks.
4. If the user adds a task, validate the inputs and save it.
5. If the user edits a task, validate and update its record.
6. If the user changes status, switch Pending to Completed or vice versa.
7. If the user deletes a task, remove the record.
8. Refresh the dashboard and display updated counts.
9. Stop the application when the server is interrupted.

## 12. Testing
| Test | Input/Action | Expected Result |
|---|---|---|
| Add task | Valid title, subject, date, priority | Task appears in list |
| Empty form | Missing required field | Error message appears |
| Complete task | Click circle/check control | Status changes to Completed |
| Edit task | Change subject or date | Updated values appear |
| Delete task | Confirm deletion | Task is removed |
| Dashboard count | Add or complete task | Counts update correctly |
| Restart app | Stop and run app again | Saved tasks remain |

## 13. Advantages
- Simple and easy to use.
- Saves task records locally.
- Makes pending work visible.
- Uses free and commonly taught technologies.
- Easy to modify and extend.

## 14. Limitations
- The current version is designed for a local single-user demo.
- No account/login system is included.
- It does not send email, SMS, or phone notifications.
- Records are stored on the computer where the app runs.
- The Flask development server is not intended for production hosting.

## 15. Future Enhancements
- Student registration and login.
- Attendance percentage calculator.
- Weekly calendar and search/filter.
- Downloadable task report.
- Email or in-app reminders.
- Multiple users and online hosting.

## 16. Conclusion
CampusMate demonstrates how a simple web application can solve a practical student organization problem. It combines Python logic, Flask routing, HTML forms, CSS styling, and SQLite data storage. The project is suitable for learning and demonstrating basic full-stack web development concepts.

## 17. References
- Python documentation: https://docs.python.org/3/
- Flask documentation: https://flask.palletsprojects.com/
- SQLite documentation: https://www.sqlite.org/docs.html
- MDN HTML documentation: https://developer.mozilla.org/en-US/docs/Web/HTML

---
**Before submission:** Replace all bracketed placeholders with your actual details. Add screenshots of your own running project (dashboard, adding a task, completed task, and edit screen), and follow your college's report format.
