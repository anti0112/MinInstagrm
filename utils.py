import json

POST_PATH = "data/data.json"
COMMENT_PATH = "data/comments.json"
BOOK_PATH = 'data/bookmarks.json'


def get_post_all():
    """Получение данных из json файла и добавление нового ключа "tag" """
    with open(POST_PATH, "r+", encoding="utf-8") as file:
        data = json.load(file)
        for post in data:
            list_search_tag = post['content'].split(' ')
            for one_by_tag in list_search_tag:
                if one_by_tag[0] == "#":
                    post["tag"] = one_by_tag
        return data


posts = get_post_all()


def get_posts_by_user(user_name):
    """Получение списка постов по имени"""
    user_posts = []
    for post_name in posts:
        if user_name == post_name['poster_name']:
            user_posts.append(post_name)
    return user_posts


def get_comments_by_post_id(post_id):
    """Получение комментариев к определенному посту через сравнение "id" """
    with open(COMMENT_PATH, encoding="utf-8") as file:
        posts = json.load(file)
        list_comm = []
        for post_comment in posts:
            if post_id == post_comment['post_id']:
                list_comm.append(post_comment)
        return list_comm


def search_for_posts(query):
    """Поиск постов по вхождению слова"""
    list_of_posts = []
    for post in posts:
        if query.lower() in post['content'].lower():
            list_of_posts.append(post)
    return list_of_posts


def get_post_by_pk(pk):
    """Вывод определенного поста по "pk" """
    for post in posts:
        if pk == post["pk"]:
            return post


def get_name_tag(tag):
    """Функция для вывода тэга к посту """
    list_of_tags = []
    for post_tag in posts:
        if tag in post_tag['tag']:
            list_of_tags.append(post_tag)
    return list_of_tags


def load_bookmarks():
    """Загрузка страницы с закладками"""
    with open(BOOK_PATH, "r") as file:
        data = json.load(file)
        return data


def add_bookmarks(BOOK_PATH, data, new_data ):
    """Функция для добавления новой закладки, и удаления определенной закладки"""
    if new_data not in data:
        data.append(new_data)
    else:
        for post in data:
            if post == new_data:
                data.remove(post)
    with open(BOOK_PATH, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


