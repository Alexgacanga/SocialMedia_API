# Social Media API 🚀

A robust RESTful API built with Django and Django Rest Framework (DRF) that simulates a social media backend. Users can post content, follow other users, and view a personalized activity feed.

**Live Demo:** [https://alexgacanga.pythonanywhere.com/api/](https://alexgacanga.pythonanywhere.com/api/)

## 🛠 Features
* **User Authentication:** Secure registration and login using JWT (JSON Web Tokens).
* **Profile Management:** Custom user models with bios and profile pictures.
* **Social Graph:** Follow/Unfollow system to track user relationships.
* **The Feed:** An intelligent feed endpoint that aggregates posts *only* from followed users.
* **Content Management:** Full CRUD capabilities for posts with image upload support.
* **Security:** * Passwords are hashed.
    * `IsAuthorOrReadOnly` permissions ensure users can only edit their own content.

## 📚 Tech Stack
* **Framework:** Django 5, Django Rest Framework
* **Database:** SQLite (Dev), PostGreSQL (Prod ready)
* **Authentication:** SimpleJWT
* **Deployment:** PythonAnywhere / Gunicorn
* **Media Storage:** Local Filesystem (configured for scale)

## 🔗 API Endpoints

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| **AUTH** | | | |
| `POST` | `/api/users/` | Register a new user | No |
| `POST` | `/api/token/` | Get Access & Refresh Tokens | No |
| **SOCIAL** | | | |
| `POST` | `/api/users/<id>/follow/` | Follow a user | Yes 🔐 |
| `POST` | `/api/users/<id>/unfollow/` | Unfollow a user | Yes 🔐 |
| `GET` | `/api/feed/` | View posts from followed users | Yes 🔐 |
| **POSTS** | | | |
| `GET` | `/api/posts/` | List all posts | No |
| `POST` | `/api/posts/` | Create a post | Yes 🔐 |
| `PUT` | `/api/posts/<id>/` | Update a post | Yes (Author only) |
| `DELETE` | `/api/posts/<id>/` | Delete a post | Yes (Author only) |
