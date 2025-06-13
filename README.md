# Blog Post Application

This is a simple web application for managing blog posts. It consists of a Python Flask backend providing a REST API and a frontend built with HTML, CSS, and JavaScript.

## Backend API Endpoints

The backend provides a REST API for managing blog posts.

### Get All Posts

- **Endpoint:** `/api/posts`
- **Method:** `GET`
- **Parameters:**
    - `sort` (optional): Field to sort by (`title` or `content`).
    - `direction` (optional): Sort direction (`asc` or `desc`).
- **Response:**
    - `200 OK`: A list of posts.

### Add a New Post

- **Endpoint:** `/api/posts`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "title": "string",
        "content": "string"
    }
    ```
- **Response:**
    - `201 Created`: The created post.
    - `400 Bad Request`: Missing title or content.

### Delete a Post

- **Endpoint:** `/api/delete/<id>`
- **Method:** `DELETE`
- **Parameters:**
    - `id` (path): The ID of the post to delete.
- **Response:**
    - `200 OK`: Post deleted successfully.
    - `404 Not Found`: Post not found.

### Update a Post

- **Endpoint:** `/api/update/<id>`
- **Method:** `PUT`
- **Parameters:**
    - `id` (path): The ID of the post to update.
- **Request Body:**
    ```json
    {
        "title": "string" (optional),
        "content": "string" (optional)
    }
    ```
- **Response:**
    - `200 OK`: The updated post.
    - `404 Not Found`: Post not found.

### Search Posts

- **Endpoint:** `/api/posts/search`
- **Method:** `GET`
- **Parameters:**
    - `title` (optional): Search term for post titles.
    - `content` (optional): Search term for post content.
- **Response:**
    - `200 OK`: A list of matching posts.

### API Documentation

The API is documented using Swagger. You can access the Swagger UI at `/apidocs` (e.g., `http://127.0.0.1:5003/apidocs`) when the backend server is running.

## Setup and Running the Application

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r ../requirements.txt
    ```
    *Note: The requirements.txt is in the root directory.*
4.  **Run the backend server:**
    ```bash
    flask run --host=0.0.0.0 --port=5003
    ```
    The backend API will be available at `http://127.0.0.1:5003`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```
2.  **Create a virtual environment (recommended, if not already in one from backend setup):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies (Flask for serving the HTML):**
    ```bash
    pip install -r ../requirements.txt
    ```
    *Note: The requirements.txt is in the root directory and shared with the backend.*
4.  **Run the frontend server:**
    ```bash
    flask run --host=0.0.0.0 --port=5001
    ```
    The frontend application will be accessible at `http://127.0.0.1:5001`.

**Important:** Make sure the backend server is running and accessible by the frontend. By default, the frontend `index.html` attempts to connect to the API at `http://127.0.0.1:5002/api`. You might need to adjust the `API Base URL` in the frontend UI or the `backend_app.py` port if you change the default port for the backend (5003). The `index.html` has an input field to change the API base URL. For the default setup, you would change it to `http://127.0.0.1:5003/api`.

## Frontend Functionality

The frontend provides a user interface to interact with the blog posts:

-   **Load Posts:** Enter the API Base URL (e.g., `http://127.0.0.1:5003/api`) and click "Load Posts" to fetch and display existing blog posts.
-   **Add Post:** Enter a title and content for a new post and click "Add Post". The new post will appear in the list.
-   **View Posts:** Posts are displayed in a list format.
-   **(Implicitly) Delete/Update/Search:** While the current basic UI in `index.html` primarily focuses on loading and adding posts, the backend API supports deleting, updating, and searching posts. These functionalities can be tested using tools like Postman or by extending the frontend.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3.  **Make your changes** and commit them with clear messages.
4.  **Push your changes** to your forked repository.
5.  **Create a pull request** to the main repository.

Please ensure your code follows the existing style and includes tests if applicable.
