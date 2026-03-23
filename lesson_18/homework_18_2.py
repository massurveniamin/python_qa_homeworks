import requests

BASE_URL = "http://127.0.0.1:8080"
FILENAME = "image.jpg"

with open(FILENAME, 'rb') as f:
    r_post = requests.post(f"{BASE_URL}/upload", files={'image': f})

data = r_post.json()
image_url = data.get("image_url")
server_filename = image_url.split('/')[-1]

r_get = requests.get(
    f"{BASE_URL}/image/{server_filename}",
    headers={"Content-Type": "text"})
print(f"GET response: {r_get.json()}")

r_del = requests.delete(f"{BASE_URL}/delete/{server_filename}")
print(f"DELETE response: {r_del.json()}")