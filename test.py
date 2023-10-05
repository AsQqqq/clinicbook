import json


def load_translation(language):
    with open(f'language/{language}.json', 'r', encoding='utf-8') as file:
        translation = json.load(file)
    print(type(translation))
    print(translation['SignUp'])
    print(translation['Register'])

if __name__ == "__main__":
    load_translation('ru_RU')