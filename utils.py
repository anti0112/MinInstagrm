import json

POST_PATH = "data/data.json"
COMMENT_PATH = "data/comments.json"


def get_post_all():
    with open(POST_PATH, "r+", encoding="utf-8") as file:
        data = json.load(file)
        post_tag = []
        for post in data:
            list_search_tag = post['content'].split(' ')
            for one_by_tag in list_search_tag:
                if one_by_tag[0] == "#":
                    post["tag"] = one_by_tag
            #         post.append(one_by_tag)
            # post["tag"] = post_tag
            # post_tag.clear()
        return data


posts = get_post_all()


def get_posts_by_user(user_name):
    user_posts = []
    for post_name in posts:
        if user_name == post_name['poster_name']:
            user_posts.append(post_name)
    return user_posts


def get_comments_by_post_id(post_id):
    with open(COMMENT_PATH, encoding="utf-8") as file:
        posts = json.load(file)
        list_comm = []
        for post_comment in posts:
            if post_id == post_comment['post_id']:
                list_comm.append(post_comment)
        return list_comm


def search_for_posts(query):
    list_of_posts = []
    for post in posts:
        if query.lower() in post['content'].lower():
            list_of_posts.append(post)
    return list_of_posts


def get_post_by_pk(pk):
    for post in posts:
        if pk == post["pk"]:
            return post


def get_name_tag(tag):
    for post_tag in posts:
        if tag == post_tag['tag']:
            return tag




# def upload(post):
#     with open(POST_PATH, "w", encoding="utf-8") as file:
#         json.dump(post, file, ensure_ascii=False, indent=4)
