from .cats_info import get_cats_info, DEFAULT_CATS_FILE


if __name__ == "__main__":
    cats = get_cats_info(DEFAULT_CATS_FILE)
    for cat in cats:
        print(cat)