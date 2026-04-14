# 💬 Django Chat Project

This project is a real-time chat application built using **Django** and **Channels**. It supports user authentication and secure WebSocket communication.

## 📅 Progress Report

### Week 1: Foundation & Project Architecture
* **Environment Setup**: Initialized a Python virtual environment (`venv`) to isolate dependencies and managed project files using VS Code.
* **Django Core Configuration**: 
    * Created the main project directory and initialized the `chat` application.
    * Configured the `BASE_DIR` and project settings for local development.
* **Version Control**: Integrated GitHub for version control, managing code snapshots and troubleshooting pull request workflows.
* **Database & Routing**: 
    * Initialized the default SQLite database.
    * Set up the initial URL routing patterns to connect the core project to the chat app.
* **Milestone**: Successfully achieved a working local host connection on port `8000` for the "chat_project" application.

### Week 2: Authentication & Real-Time Communication
* **User Authentication**:
    * Created specialized Login and Registration views.
    * Implemented secure logout functionality to manage user sessions.
* **ASGI & Channels**:
    * Configured `asgi.py` to allow the server to handle both standard HTTP and real-time WebSocket protocols.
    * Set up `CHANNEL_LAYERS` in `settings.py` using `InMemoryChannelLayer` for message passing.
* **WebSocket Integration**:
    * Developed `ChatConsumer` to handle the logic of socket connections.
    * Created `routing.py` for WebSocket URL mapping, similar to standard Django `urls.py`.
    * Added frontend JavaScript to the `index.html` template to establish a secure handshake with the socket (`ws://`).

---

## 🚀 How to Run
1. Activate the virtual environment: `.\venv\Scripts\activate`
2. Run the server: `python manage.py runserver`
3. Access the app: `http://127.0.0.1:8000/`