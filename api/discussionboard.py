from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a strong secret key
jwt = JWTManager(app)

# Sample data for discussions, posts, and comments
discussions = []
posts = []
comments = []

# Sample user data (you would typically use a database)
users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"}
]

# API route to create a new discussion
@app.route('/discussions', methods=['POST'])
@jwt_required
def create_discussion():
    data = request.get_json()
    if 'title' in data:
        new_discussion = {
            'title': data['title'],
            'created_by': get_jwt_identity()  # Get the current user from the JWT token
        }
        discussions.append(new_discussion)
        return jsonify({'message': 'Discussion created successfully'}), 201
    return jsonify({'message': 'Invalid data'}), 400

# API route to get all discussions
@app.route('/discussions', methods=['GET'])
def get_discussions():
    return jsonify(discussions)

# API route to create a new post in a discussion
@app.route('/discussions/<discussion_title>/posts', methods=['POST'])
@jwt_required
def create_post(discussion_title):
    data = request.get_json()
    if 'content' in data:
        new_post = {
            'discussion_title': discussion_title,
            'content': data['content'],
            'created_by': get_jwt_identity()
        }
        posts.append(new_post)
        return jsonify({'message': 'Post created successfully'}), 201
    return jsonify({'message': 'Invalid data'}), 400

# API route to get all posts in a discussion
@app.route('/discussions/<discussion_title>/posts', methods=['GET'])
def get_posts_in_discussion(discussion_title):
    discussion_posts = [post for post in posts if post['discussion_title'] == discussion_title]
    return jsonify(discussion_posts)

# API route to add a comment to a post
@app.route('/discussions/<discussion_title>/posts/<int:post_id>/comments', methods=['POST'])
@jwt_required
def add_comment(discussion_title, post_id):
    data = request.get_json()
    if 'content' in data:
        post = next((post for post in posts if post['discussion_title'] == discussion_title and post['post_id'] == post_id), None)
        if post:
            new_comment = {
                'content': data['content'],
                'created_by': get_jwt_identity()
            }
            comments.append(new_comment)
            return jsonify({'message': 'Comment added successfully'}), 201
    return jsonify({'message': 'Invalid data'}), 400
if __name__ == '__main__':
    app.run(debug=True)