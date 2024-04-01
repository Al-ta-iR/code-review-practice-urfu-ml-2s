import requests


def check_for_updates():
    url = "https://huggingface.co/utrobinmv/t5_translate_en_ru_zh_large_1024/tree/main"
    response = requests.get(url)
    if 'commit/76a99a3' in response.text:
        return "Обновлений не найдено"
    else:
        return "Есть обновления"

print(check_for_updates())
