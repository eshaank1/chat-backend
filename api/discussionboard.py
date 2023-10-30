# ... (previous code)

# Sample data for discussion posts and comments
discussion_posts = []

# API route to create a new post in a discussion
@app.route('/discussions/<int:discussion_id>/posts', methods=['POST'])
@jwt_required
def create_post(discussion_id):
    data = request.get_json()
    if 'content' in data:
        new_post = {
            'discussion_id': discussion_id,
            'content': data['content'],
            'created_by': get_jwt_identity(),
            'comments': []  # Initialize comments as an empty list
        }
        discussion_posts.append(new_post)
        return jsonify({'message': 'Post created successfully'}), 201
    return jsonify({'message': 'Invalid data'}), 400

# API route to get all posts in a discussion
@app.route('/discussions/<int:discussion_id>/posts', methods=['GET'])
def get_posts_in_discussion(discussion_id):
    discussion_posts_list = [post for post in discussion_posts if post['discussion_id'] == discussion_id]
    return jsonify(discussion_posts_list)

# API route to add a comment to a post
@app.route('/discussions/<int:discussion_id>/posts/<int:post_id>/comments', methods=['POST'])
@jwt_required
def add_comment(discussion_id, post_id):
    data = request.get_json()
    if 'content' in data:
        post = next((post for post in discussion_posts if post['discussion_id'] == discussion_id and post['post_id'] == post_id), None)
        if post:
            new_comment = {
                'content': data['content'],
                'created_by': get_jwt_identity()
            }
            post['comments'].append(new_comment)
            return jsonify({'message': 'Comment added successfully'}), 201
    return jsonify({'message': 'Invalid data'}), 400

# ... (remaining code)