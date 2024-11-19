from flask import Blueprint
from post_app.controllers.post_controller import PostController


post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/api/posts', methods=['GET'])
def get_all_posts():
    return PostController.get_all_posts()

@post_bp.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    return PostController.get_post(post_id)

@post_bp.route('/api/posts', methods=['POST'])
def create_post():
    return PostController.create_post()

@post_bp.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    return PostController.update_post(post_id)

@post_bp.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    return PostController.delete_post(post_id)