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

    # Week 4: Authentication & User Management Enhancements

## 📝 Project Overview
This week focused on hardening the security and accessibility of the real-time chat application. By implementing a mandatory email registration system and a full password recovery workflow, the application now provides a professional-grade user management experience without administrative hierarchy.

## 🚀 Key Accomplishments
* **Custom Registration Flow**: Updated the `register` view to use a custom form (`UserRegisterForm`) that forces users to provide an email address, ensuring account recoverability.
* **Password Reset Integration**: Leveraged Django's built-in authentication system to handle the four-stage password reset process (Request, Email Sent, Link Confirmation, and Success).
* **Console Email Backend**: Configured a local development email backend that outputs password reset links directly to the VS Code terminal for testing.
* **Generalized User Permissions**: Maintained a flat access model where any registered user can create chat rooms and join conversations, removing superuser dependencies for core features.
* **UI/UX Improvements**: Developed a dedicated `registration/` template directory including login, registration, and all password reset state pages.

## 🛠 Technical Stack Updated
* **Backend**: Django 6.0.3
* **Real-time**: Django Channels & Daphne
* **Auth**: Django contrib auth with custom Email Backend