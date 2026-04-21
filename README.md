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

# Week 5: Frontend UI & Real-Time Messaging

## 🚀 Project Overview
Week 5 focused on transforming the static chat interface into a fully dynamic, real-time experience. By implementing the WebSocket API and JavaScript DOM manipulation, the application now supports instant message broadcasting and user presence tracking without requiring page reloads.

## 🛠️ Key Features
* **WebSocket API Integration**: Established a persistent bi-directional connection between the client and the Django Channels server to handle real-time data flow.
* **Dynamic UI Updates**: Leveraged JavaScript DOM manipulation (`document.createElement`, `appendChild`) to inject new messages into the chat log instantly.
* **Real-Time Roll Call**: Implemented an automated "Online Users" sidebar that updates dynamically as users join or leave the room.
* **Asynchronous Communication**: Utilized `JSON.parse()` and `JSON.stringify()` to manage data packets, ensuring seamless communication between the frontend and the backend consumer.
* **UX Enhancements**: Integrated automatic scrolling to the latest message and instant input clearing to maintain a modern chat experience.

## 📚 Technical Reference
* **Frontend**: Vanilla JavaScript, WebSocket API, HTML5/CSS3.
* **Backend**: Django Channels, Daphne ASGI server.
* **Data Format**: JSON.

# Week 6: Storing Chat History

## 🌟 Milestone Task
* **Task:** Integrate database logic to save chat messages for persistence, allowing users to see past conversations.

## 🛠️ Key Technical Implementations

* **Framework ORM Persistence:** Utilized the Django ORM to securely store every transmitted message into the database. This ensures that conversations are no longer ephemeral and can be retrieved at any time.
* **Asynchronous Database Access:** Implemented `database_sync_to_async` within the WebSocket consumers. This allows the application to perform database "write" operations without blocking the asynchronous chat server, maintaining a lag-free user experience.
* **Historical Data Retrieval:** Configured the room view to query the database using the ORM when a user first enters. This loads past messages into the chat window dynamically before the live connection takes over.
* **Real-Time System Notifications:** Added logic to broadcast an automated greeting whenever a new user joins a room, improving the interactive feel of the interface.

## 💻 Reference Materials Applied
* **Django ORM:** For model querying and data persistence.
* **Channels Database Sync:** For safe asynchronous database handling.
* **Meta Ordering:** For ensuring historical messages appear in the correct chronological sequence.

# 🚀 Django Real-Time Chat App - Week 7

## 🌟 Overview
Week 7 was the most significant milestone in this project's development. I transitioned the application from a basic message-storing site into a **fully dynamic, real-time communication platform**. By leveraging **WebSockets** and **Django Channels**, the app now mimics modern industry standards like WhatsApp or Slack.

---

## ✨ Key Accomplishments in Week 7

### 🛠️ 1. Full Message Lifecycle (CRUD via WebSockets)
* **Real-Time Deletion:** Users can now delete their own messages. Using the `delete_handler` in the backend, the message is removed from the database and instantly vanishes from every connected user's screen without a page refresh.
* **In-Place Editing:** Implemented a secure editing feature. Users can update their message content, which broadcasts an `edit_handler` signal to sync the change across all active browsers.
* **Security:** Added server-side checks to ensure only the original sender of a message has the permission to trigger edit or delete actions.

### 👥 2. Dynamic User Presence (Online List)
* **State Tracking:** Implemented a "Roll Call" protocol. When a user joins, a signal is sent to everyone else to "identify themselves," allowing the new joiner to see an accurate list of who is already online.
* **Join/Leave Notifications:** Real-time updates to the sidebar when users connect or disconnect from the room.

### ⌨️ 3. Typing Indicators
* **Live Feedback:** Added a "User is typing..." feature. 
* **Smart Throttling:** Used JavaScript timers to ensure the indicator automatically clears after 1 second of inactivity, providing a smooth and responsive UX.

### 🏗️ 4. Technical Architecture: The "Handler Pattern"
* Restructured `consumers.py` to use an explicit **Handler Pattern**. This separates the logic of receiving data from the logic of pushing it back to the client, making the code much more scalable and preventing data-loss errors.

---

## 🛠️ Technical Stack Used
* **Backend:** Python 3.x, Django 5.x
* **Real-Time:** Django Channels, Daphne (ASGI), WebSockets
* **Database:** SQLite (Local) / PostgreSQL (Ready)
* **Frontend:** JavaScript (ES6+), HTML5, CSS3

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>