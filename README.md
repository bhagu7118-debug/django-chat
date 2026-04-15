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

### Week 3: Secure Authentication Loop & UI Architecture
* **Advanced User Registration**:
    * Implemented a comprehensive user creation form that automatically logs in new users upon successful registration and redirects them to the chat room.
* **Security & Session Management**:
    * Secured the Global Chat Room by applying the `@login_required` decorator, ensuring only authorized participants can access the real-time WebSocket environment.
    * Developed a custom logout view and prioritized its URL routing to bypass Django 5.0+ HTTP 405 errors, allowing for safe session termination via standard UI links.
    * Configured `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL` in project settings to create a seamless, infinite navigation loop for the user.
* **Template Organization**:
    * Refactored the frontend file structure by establishing a dedicated `registration` directory for `login.html` and `register.html`, aligning perfectly with Django's built-in auth framework requirements.
* **Version Control**:
    * Committed and pushed the finalized, fully functional Week 3 milestone (complete with bug fixes and secure routing) to the GitHub repository.