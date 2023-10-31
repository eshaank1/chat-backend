from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

discussion_api = Blueprint('discussion_api', __name__, url_prefix='/api/discussions')
api = Api(discussion_api)
CORS(discussion_api, resources={r"/api/*": {"origins": "*"}})

# Sample data
discussions = []
posts = []
comments = []

class DiscussionAPI:
    class CreateDiscussion(Resource):
        def post(self):
            data = request.json
            discussion = {
                'title': data.get('title'),
                'posts': []  # Store posts related to this discussion
            }
            discussions.append(discussion)
            return jsonify({"message": "Discussion created successfully"})

    class ListDiscussions(Resource):
        def get(self):
            return jsonify(discussions)

    class CreatePost(Resource):
        def post(self, discussion_id):
            data = request.json
            post = {
                'content': data.get('content'),
                'comments': []  # Store comments related to this post
            }
            discussion = next((d for d in discussions if d['title'] == discussion_id), None)
            if discussion:
                discussion['posts'].append(post)
                posts.append(post)
                return jsonify({"message": "Post created successfully"})
            return jsonify({"message": "Discussion not found"}, 404)

    class CreateComment(Resource):
        def post(self, discussion_id, post_id):
            data = request.json
            comment = {
                'content': data.get('content')
            }
            discussion = next((d for d in discussions if d['title'] == discussion_id), None)
            if discussion:
                post = next((p for p in discussion['posts'] if p == post_id), None)
                if post:
                    post['comments'].append(comment)
                    comments.append(comment)
                    return jsonify({"message": "Comment created successfully"})
            return jsonify({"message": "Discussion or post not found"}, 404)

api.add_resource(DiscussionAPI.CreateDiscussion, '/create')
api.add_resource(DiscussionAPI.ListDiscussions, '/list')
api.add_resource(DiscussionAPI.CreatePost, '/<string:discussion_id>/create')
api.add_resource(DiscussionAPI.CreateComment, '/<string:discussion_id>/<string:post_id>/comment')

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)