from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
Swagger(app)

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """
    Get all posts
    ---
    tags:
      - posts
    parameters:
      - name: sort
        in: query
        type: string
        required: false
        description: Specifies the field by which posts should be sorted. Accepts 'title' or 'content'.
      - name: direction
        in: query
        type: string
        required: false
        description: Specifies the sort order. Accepts 'asc' for ascending order and 'desc' for descending order.
    responses:
      200:
        description: A list of posts
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: The post ID
              title:
                type: string
                description: The post title
              content:
                type: string
                description: The post content
    """
    sort = request.args.get('sort')
    direction = request.args.get('direction')
    if sort in ['title', 'content'] and direction in ['desc', 'asc']:
        reverse = direction == 'desc'
        POSTS.sort(key=lambda post: post[sort], reverse=reverse)
    return jsonify(POSTS)

@app.route('/api/posts', methods=['POST'])
def add_post():
    """
    Add a new post
    ---
    tags:
      - posts
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - title
            - content
          properties:
            title:
              type: string
              description: The post title
            content:
              type: string
              description: The post content
    responses:
      201:
        description: The created post
        schema:
          type: object
          properties:
            id:
              type: integer
              description: The post ID
            title:
              type: string
              description: The post title
            content:
              type: string
              description: The post content
      400:
        description: Missing title and/or content
    """
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({'error': 'Missing title and/or content'}), 400

    new_id = max(post['id'] for post in POSTS) + 1
    new_post = {
        "id": new_id,
        "title": title,
        "content": content
    }
    POSTS.append(new_post)
    return jsonify(new_post), 201

@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_post(id):
    """
    Delete a post
    ---
    tags:
      - posts
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The post ID
    responses:
      200:
        description: Post deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              description: Success message
      404:
        description: Post not found
        schema:
          type: object
          properties:
            error:
              type: string
              description: Error message
    """
    global POSTS
    initial_length = len(POSTS)
    new_posts = [post for post in POSTS if post['id'] != id]

    if len(new_posts) == initial_length:
        return jsonify({"error": f"Post with ID {id} not found."}), 404

    POSTS = new_posts
    return jsonify({"message": f"Post with ID {id} has been deleted."}), 200

@app.route('/api/update/<int:id>', methods=['PUT'])
def update_post(id):
    """
    Update an existing post
    ---
    tags:
      - posts
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The post ID
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              description: The post title
            content:
              type: string
              description: The post content
    responses:
      200:
        description: The updated post
        schema:
          type: object
          properties:
            id:
              type: integer
              description: The post ID
            title:
              type: string
              description: The post title
            content:
              type: string
              description: The post content
      404:
        description: Post not found
        schema:
          type: object
          properties:
            error:
              type: string
              description: Error message
    """
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    for post in POSTS:
        if post['id'] == id:
            if title is not None:
                post['title'] = title
            if content is not None:
                post['content'] = content
            return jsonify(post), 200

    return jsonify({"error": f"Post with ID {id} not found."}), 404

@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    """
    Search posts by title or content
    ---
    tags:
      - posts
    parameters:
      - name: title
        in: query
        type: string
        required: false
        description: The title search term
      - name: content
        in: query
        type: string
        required: false
        description: The content search term
    responses:
      200:
        description: A list of matching posts
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: The post ID
              title:
                type: string
                description: The post title
              content:
                type: string
                description: The post content
    """
    title_term = request.args.get('title')
    content_term = request.args.get('content')

    filtered_posts = POSTS

    if title_term:
        filtered_posts = [post for post in filtered_posts if title_term.lower() in post['title'].lower()]
    if content_term:
        filtered_posts = [post for post in filtered_posts if content_term.lower() in post['content'].lower()]

    return jsonify(filtered_posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)
