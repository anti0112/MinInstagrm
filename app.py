from flask import Flask, render_template, request, redirect, jsonify
from utils import *

posts = get_post_all()
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def get_all_posts():
    """Главная страница"""
    bookmarks = load_bookmarks()
    return render_template("index.html", posts=posts, bookmarks=bookmarks)


@app.route("/post/<int:pk>")
def post_id(pk):
    """Страница поста"""
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search")
def get_posts():
    """Вывод постов по вхождению слова"""
    s = request.args["s"]
    list_of_posts = search_for_posts(s)
    return render_template("search.html", s=s, posts=list_of_posts)


@app.route("/user/<username>")
def get_user(username):
    """Страница пользователя"""
    users = get_posts_by_user(username)
    return render_template("user-feed.html", users=users)


@app.route("/tags/<tag>")
def get_post_by_tag(tag):
    """Вывод постов по тэгу"""
    tag_name = get_name_tag(tag)
    return render_template("tag.html", tag_name=tag_name, tag=tag)


@app.route('/bookmarks/add/<int:postid>')
def add_to_bookmarks(postid):
    """Удаление закладок"""
    bookmark = request.args.get('bookmark')
    posts = load_bookmarks()
    post = get_post_by_pk(postid)
    add_bookmarks(BOOK_PATH, posts, post)
    return redirect('/', code=302)


@app.route('/bookmarks')
def show_bookmarks():
    """Страница с закладками"""
    bookmarks = load_bookmarks()
    return render_template('bookmarks.html', posts=bookmarks)


@app.route("/api/posts")
def all_posts_json():
    """Информация по всему json файлу"""
    return jsonify(posts)


@app.route("/api/post/<int:pk>")
def get_post_json(pk):
    """Информация об отдельном словаре в файле"""
    post = get_post_by_pk(pk)
    return jsonify(post)


if __name__ == "__main__":
    app.run()
