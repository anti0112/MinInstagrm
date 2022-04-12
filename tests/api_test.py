from app import app


def test_post():
    """Проверка на вхождение ключей в словаре"""
    allowed_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk", "tag"}
    response = app.test_client().get('/api/post/3')
    fact_keys = set(response.json.keys())
    assert fact_keys == allowed_keys, 'Wrong keys'
    assert response.json.get('pk') == 3, 'Wrong post ID'


def test_posts():
    response = app.test_client().get('/api/posts')
    allowed_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk", "tag"}
    assert response.status_code == 200, 'Wrong status-code'
    assert len(response.json) > 0, 'Data list is empty'

    for elem in response.json:
        fact_keys = set(elem.keys())
        assert fact_keys == allowed_keys, 'Wrong keys'
