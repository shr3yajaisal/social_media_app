from flask import request
from post_app.services.post_service import PostService
from post_app.views.post_view import PostView

class PostController:
    @staticmethod
    def get_all_posts():
        posts = PostService.get_all_posts()
        return PostView.render_posts(posts), 200

    @staticmethod
    def get_post(post_id):
        post = PostService.get_post_by_id(post_id)
        if not post:
            return PostView.render_error('Post not found'), 404
        return PostView.render_post(post), 200

    @staticmethod
    def create_post():
        data = request.get_json()
        user_id = data.get('user_id')
        content = data.get('content')

        post = PostService.create_post(user_id, content)
        return PostView.render_success('Post created successfully', post.post_id), 201

    @staticmethod
    def update_post(post_id):
        data = request.get_json()
        new_content = data.get('content')

        post = PostService.update_post(post_id, new_content)
        if post:
            return PostView.render_success('Post updated successfully', post.post_id), 200
        return PostView.render_error('Post not found'), 404

    @staticmethod
    def delete_post(post_id):
        post = PostService.delete_post(post_id)
        if post:
            return PostView.render_success('Post deleted successfully', post.post_id), 200
        return PostView.render_error('Post not found'), 404
