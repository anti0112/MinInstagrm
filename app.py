from flask import Flask, render_template, request
from utils import *

posts = get_post_all()
app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:pk>")
def post_id(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search")
def get_posts():
    s = request.args["s"]
    list_of_posts = search_for_posts(s)
    return render_template("search.html", s=s, posts=list_of_posts)


@app.route("/user/<username>")
def get_user(username):
    users = get_posts_by_user(username)
    return render_template("user-feed.html", users=users)


@app.route("/tag/<tag>")
def get_post_by_tag(tag):
    tag_name = get_name_tag(tag)
    return render_template("tag.html", posts=posts, tag_name=tag_name)


@app.route("/api/posts")
def all_posts_json():
    return render_template("api_posts.html", posts=posts)


@app.route("/api/post/<int:pk>")
def get_post_json(pk):
    post = get_post_by_pk(pk)
    return render_template("api_post_pk.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)

