from typing import List

from _recipe_utils import CoverOptions, Recipe

categories_sort: List[str] = ["News"]

recipes: List[Recipe] = [
    Recipe(
        recipe="ft",
        slug="ft-online",
        src_ext="mobi",
        target_ext=["epub"],
        category="News",
        tags=["business"],
        cover_options=CoverOptions(
            logo_path_or_url="https://www.ft.com/partnercontent/content-hub/static/media/ft-horiz-new-black.215c1169.png"
        ),
    ),
]
