# 🎬 MoviWebApp

**MoviWebApp** is a fun and colorful web application built with Flask that allows users to manage their favorite movies.  
It features user accounts, movie search via an external API, and full CRUD functionality – all wrapped in a comic-style UI.

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
## 👨‍💻 Author

**Calvin Kuven** — [Mister-Calvin](https://github.com/Mister-Calvin)

---

## 📜 License

This project is intended for **educational purposes only**.  
You are free to explore, learn from, and modify the code.  
Commercial use is not permitted without explicit permission from the author.