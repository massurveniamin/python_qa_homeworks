import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

response = requests.get(search_url, params=search_params)
data = response.json()
items = data['collection']['items']

for i in range(2):
    nasa_id = items[i]['data'][0]['nasa_id']

    asset_url = asset_url_template.format(nasa_id=nasa_id)
    asset_response = requests.get(asset_url)
    asset_data = asset_response.json()

    files = asset_data['collection']['items']

    image_url = ""
    for file in files:
        if file['href'].endswith('.jpg'):
            image_url = file['href']
            break

    if image_url:
        img_response = requests.get(image_url)
        filename = f"mars_photo{i + 1}.jpg"

        with open(filename, "wb") as f:
            f.write(img_response.content)