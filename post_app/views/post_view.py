class PostView:
    @staticmethod
    def render_post(post):
        return {
            "post_id": post.post_id,
            "user_id": post.user_id,
            "content": post.content,
            "created_at": post.created_at,
            "updated_at": post.updated_at
        }

    @staticmethod
    def render_posts(posts):
        return [PostView.render_post(post) for post in posts]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, post_id=None):
        response = {"message": message}
        if post_id:
            response["post_id"] = post_id
        return response
