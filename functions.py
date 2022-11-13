import json


def load_posts():
    """
    Функция, которая возвращает данные из Json-файла
    Args -
    Returns: декодированные данные
    """
    with open("posts.json", "rt", encoding="utf-8") as file:
        return json.load(file)


def search_posts_by_word(word):
    """
    Функция, которая осуществляет поиск поста по слову.
    Args: word - слово или строка, по которому происходит поиск постов.
    Returns: result - список найденных постов
    """
    result = []
    for post in load_posts():
        if word.lower() in post["content"].lower():
            result.append(post)
    return result


def save_picture(picture):
    """
    Функция, которая возвращает путь, куда сохраняется картинка.
    Args: picture - картинка
    Returns: path - путь, куда сохраняется картинка
    """
    filename = picture.filename
    path = f"./uploads/images/{filename}"
    picture.save(path)
    return path


def add_post(post):
    """
    Функция, которая добавляет пост.
    Args: post - пост, который добавляется в список постов.
    Returns: post - текущий пост, который был добавлен.
    """
    posts = load_posts()
    posts.append(post)
    with open("posts.json", "wt", encoding="utf-8") as file:
        json.dump(posts, file)
    return post
