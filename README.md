# 🎬 MoviWebApp

**MoviWebApp** is a fun and colorful web application built with Flask that allows users to manage their favorite movies.  
It features user accounts, movie search via an external API, and full CRUD functionality – all wrapped in a comic-style UI.
---
## 🧩 Project Overview

**MoviWebApp** is a Flask-based web application that allows users to manage and rate their favorite movies  
in a colorful, comic-style interface. It integrates an external movie API (OMDb) for fetching real movie data  
and provides full CRUD functionality for users and movies.

The project follows the **MVC (Model-View-Controller)** design pattern:
- **Model** – (`models.py`) defines the database structure using SQLAlchemy (User–Movie relationship).  
- **View** – (`templates/` + `static/style.css`) handles the user interface and design.  
- **Controller** – (`app.py`) manages routes, API calls, and database logic through `data_manager.py`.

This modular setup keeps the codebase clean, scalable, and easy to maintain —  
ideal for learning structured web development with Flask.
---

## 🚀 Features

- 🔹 Create users with duplicate-name validation
- 🔹 Add, display, update, and delete movies per user
- 🔹 Search movie details via external API (e.g. OMDb)
- 🔹 Stylish and creative interface with comic-style design
- 🔹 Error pages for 404, 405, 500, KeyError, and generic exceptions
- 🔹 Modular code structure (`data/` folder, Jinja templates, static CSS)

---
## 💡 To-Do / Ideas
	•	Login system with session handling
	•	Mark favorite movies
	•	Filter/search within added movies

## 🛠 Technologies

- **Python 3.11+**
- **Flask**
- **Flask-SQLAlchemy**
- **Jinja2**
- **Requests**
- **python-dotenv**

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:Mister-Calvin/MoviWebApp.git
   cd MoviWebApp
    ```
   
```bash ```
2.	Create and activate a virtual environment:  
```bash 
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows 
```
3.	Install dependencies:
``` bash
pip install -r requirements.txt
```
4. **Set up your `.env` file:**

   Create a `.env` file in the root directory with the following content:

   ```env
   API_KEY=your_api_key_here
   
You can get a free movie API key at:
👉 https://www.omdbapi.com/apikey.aspx
---
## 📁 Project Structure

```bash
MoviWebApp/
├── app.py
├── requirements.txt
├── .gitignore
├── .env              # <– not in git, only locally
├── README.md         
├── data/
│   ├── api_movies.py
│   ├── data_manager.py
│   └── models.py
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── show_movies.html
│   ├── error_404.html
│   ├── error_405.html
│   ├── error_500.html
│   ├── error_key.html
│   └── error_exception.html
 ```
---
### models.py

This module defines the SQLAlchemy ORM models used in the application.  
It includes the **User** and **Movie** classes, which represent the database tables  
and define the relationships between them.

- **User**: Represents a registered user in the system. Each user can have multiple movies.  
  Contains attributes such as `id`, `name`, and a relationship to the `Movie` table.

- **Movie**: Represents a movie entry associated with a specific user.  
  Stores details like `id`, `name`, `director`, `year`, `poster_url`, `rating`, and `user_id`.

- **Relationships**:  
  A one-to-many relationship is defined using `db.relationship('Movie', backref='user')`,  
  meaning each user can own multiple movies, but each movie belongs to one specific user.

- **Technical note:**  
  The models are implemented using SQLAlchemy ORM and are automatically created via  
  `db.create_all()` during application setup.
---
## 📊 data_manager.py

This module contains the **DataManager** class, which handles all database interactions  
between the Flask routes and the SQLAlchemy models. It acts as an abstraction layer,  
keeping the application logic clean and separating database operations from the views.

### Key Responsibilities

- **CRUD Operations:**  
  Provides create, read, update, and delete methods for both users and movies  
  (e.g., `add_movie()`, `get_movies()`, `update_movie_rating()`, `delete_user()`).

- **Error Handling:**  
  Each database operation is wrapped in `try/except` blocks to ensure that  
  exceptions are caught safely. Failed transactions are rolled back with  
  `db.session.rollback()` to maintain database integrity.

- **Session Management:**  
  Uses `finally: db.session.close()` after each operation to release connections  
  and avoid lingering sessions.

- **Code Readability:**  
  Every method includes clear docstrings describing its purpose, parameters,  
  and return values — following consistent and professional documentation standards.

### Technical Notes

- The `DataManager` works as a bridge between the Flask routes (`app.py`)  
  and the SQLAlchemy models (`models.py`).  
- It ensures a **clean MVC-like structure**, where the web layer never directly touches  
  the database, improving maintainability and scalability.
---
## 🌐 api_movies.py

This module handles all communication with the external movie API (e.g., OMDb).  
It provides helper functions to search for and retrieve detailed movie information  
based on user input in the Flask web application.

### Key Responsibilities

- **External API Requests:**  
  Uses the `requests` library to call the OMDb API and retrieve movie details  
  such as title, director, release year, and poster URL.

- **Data Parsing:**  
  Extracts and formats JSON responses from the API into Python dictionaries  
  that can be easily used by the `DataManager` or Flask routes.

- **Error Handling:**  
  Catches potential connection issues, invalid API keys, or missing data fields,  
  and returns meaningful error messages or fallback values instead of crashing the app.

- **API Key Management:**  
  Loads the API key securely from the `.env` file using `python-dotenv` to keep  
  sensitive information out of the source code and Git repository.

### Technical Notes

- This module allows the app to dynamically fetch movie data by title or ID.  
- It helps ensure that user-added movies have accurate metadata and images.  
- The functions inside `api_movies.py` are stateless and reusable across routes,  
  maintaining clean code separation from the Flask logic.
---
## 🎬 app.py

This is the **main Flask application file** and serves as the central controller of the project.  
It defines all routes, initializes the database, manages the app configuration,  
and connects the frontend templates with the backend logic.

### Key Responsibilities

- **Routing:**  
  Defines all endpoints (`@app.route`) for user management and movie handling.  
  Each route handles requests, interacts with the `DataManager`, and renders templates.

- **Integration:**  
  Uses the `DataManager` class for all database operations and the `api_movies` module  
  to retrieve external movie data from the OMDb API.

- **Error Handling:**  
  Implements global error handlers for 404, 405, 500, and general exceptions.  
  Ensures the application displays user-friendly error pages instead of crashing.

- **Session and Flash Messages:**  
  Uses Flask’s session management to store state and `flash()` to show messages  
  for success, errors, or validation results.

- **App Initialization:**  
  Connects the Flask app with the SQLAlchemy database through `db.init_app(app)`  
  and creates tables automatically with `db.create_all()`.

---

## 🔗 How the Modules Work Together

The project follows a clean, modular architecture inspired by the **MVC (Model-View-Controller)** pattern:

1. **app.py (Controller):**  
   - Handles all HTTP requests from the user (e.g., adding, updating, or deleting movies).  
   - Calls the appropriate methods from the `DataManager` to interact with the database.  
   - Renders templates with the data returned from the backend.

2. **data_manager.py (Data Layer):**  
   - Acts as the interface between `app.py` and the SQLAlchemy models.  
   - Contains reusable methods for all CRUD operations (Create, Read, Update, Delete).  
   - Includes robust error handling and session management to ensure database stability.

3. **models.py (Model Layer):**  
   - Defines the database structure using SQLAlchemy ORM.  
   - Includes `User` and `Movie` classes with a one-to-many relationship  
     (`User` → `Movie`).

4. **api_movies.py (External Integration Layer):**  
   - Connects the application to the OMDb API to fetch real movie data.  
   - Returns structured data (title, director, year, rating, poster URL)  
     that is used when creating new movie entries.

5. **templates/ & static/: (View Layer)**  
   - `templates/` contains the HTML files rendered by Flask (user list, movie list, forms).  
   - `static/` holds the CSS (`style.css`) and images, creating a vibrant, movie-inspired design.  

---

### 🧠 Summary

When a user interacts with the web interface:

1. Flask (`app.py`) receives the request.  
2. It asks `data_manager.py` to perform the required database operation.  
3. If the request involves fetching movie info, `api_movies.py` provides the data from the OMDb API.  
4. `models.py` defines how this data is stored and related.  
5. Flask then renders the response using the templates, styled with `static/style.css`.

This structure keeps the project clean, maintainable, and easy to expand —  
for example, by adding login systems, favorites, or review sections in the future.
## 👨‍💻 Author

**Calvin Kuven** — [Mister-Calvin](https://github.com/Mister-Calvin)

If you have suggestions, bug reports, or ideas for improvement,
feel free to reach out — feedback is always appreciated!

**📧 kuven.calvin@yahoo.com**

---

## 🎓 Learning Goals

This project was developed as a hands-on learning exercise  
to practice Python web development with Flask, SQLAlchemy, and REST API integration.  
It focuses on:
- Writing clean, modular backend code
- Implementing error handling and validation
- Creating visually engaging frontend layouts with CSS

---


## 📜 License

This project is intended for **educational purposes only**.  
You are free to explore, learn from, and modify the code.  
Commercial use is not permitted without explicit permission from the author.