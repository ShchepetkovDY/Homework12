import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import save_picture, add_post

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post")
def page_post():
    """
    Блупринт представления страницы для добавления поста
    """
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def add_post_page():
    """
    Блупринт представления добавления поста.
    """
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        return 'Нет картинки или контента'

    if picture.filename.split(".")[-1] not in ["jpeg", "png"]:
        logging.info("Загруженный файл не картинка")
        return "Неверное расширение файла"
    try:
        picture_path = "/" + save_picture(picture)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Неверный файл"
    post = add_post({"pic": picture_path, "content": content})

    return render_template("post_uploaded.html", post=post)
