import requests
import json
import os
import exifread
import pytesseract
import face_recognition
import hashlib
from bs4 import BeautifulSoup

def search_username(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "GitHub": f"https://github.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Medium": f"https://medium.com/@{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Discord": f"https://discordapp.com/users/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}/",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Kick": f"https://kick.com/{username}",
        "OnlyFans": f"https://onlyfans.com/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Badoo": f"https://badoo.com/en/{username}",
        "VK": f"https://vk.com/{username}",
        "OK.ru": f"https://ok.ru/{username}",
        "Pornhub": f"https://www.pornhub.com/users/{username}",
        "XVideos": f"https://www.xvideos.com/profiles/{username}",
        "NexusMods": f"https://www.nexusmods.com/users/{username}",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
        "Minecraft": f"https://namemc.com/search?q={username}",
        "Fiverr": f"https://www.fiverr.com/{username}",
        "Upwork": f"https://www.upwork.com/freelancers/~{username}",
    }

    results = {}
    for site, url in platforms.items():
        response = requests.get(url)
        if response.status_code == 200:
            results[site] = url
    return results if results else f"No results found for {username}."

def check_email(email):
    api_key = "YOUR_HIBP_API_KEY"
    headers = {"hibp-api-key": api_key}
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    return f"Email {email} not found in breaches."

# ---- SHODAN API (IP Address OSINT) ----
def check_ip(ip_address):
    api_key = "YOUR_SHODAN_API_KEY"
    url = f"https://api.shodan.io/shodan/host/{ip_address}?key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return f"IP {ip_address} not found in Shodan database."

# ---- IMAGE METADATA EXTRACTION ----
def extract_image_metadata(image_path):
    metadata = {}
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
        for tag, value in tags.items():
            metadata[tag] = str(value)

    # OCR (Text from image)
    text = pytesseract.image_to_string(Image.open(image_path))
    if text.strip():
        metadata["Extracted Text"] = text.strip()
    
    return metadata

# ---- FACE RECOGNITION (Find Similar Faces) ----
def find_similar_faces(target_image_path, dataset_folder="face_database"):
    known_image = face_recognition.load_image_file(target_image_path)
    known_encoding = face_recognition.face_encodings(known_image)[0]

    results = []
    for filename in os.listdir(dataset_folder):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(dataset_folder, filename)
            test_image = face_recognition.load_image_file(img_path)
            test_encoding = face_recognition.face_encodings(test_image)[0]

            matches = face_recognition.compare_faces([known_encoding], test_encoding)
            if matches[0]:
                results.append(filename)
    
    return results if results else "No matching faces found."

# ---- REVERSE IMAGE SEARCH (Manual Upload Required) ----
def reverse_image_search(image_path):
    search_urls = [
        "https://www.google.com/searchbyimage/upload",
        "https://yandex.com/images/search",
        "https://www.bing.com/visualsearch"
    ]
    results = []
    for url in search_urls:
        files = {"encoded_image": open(image_path, "rb")}
        response = requests.post(url, files=files)
        results.append(f"Check: {url}")
    return results

def extract_document_metadata(file_path):
    metadata = {}
    if file_path.endswith(".pdf"):
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        metadata = reader.metadata
    elif file_path.endswith(".docx"):
        from docx import Document
        doc = Document(file_path)
        metadata["Text Content"] = "\n".join([para.text for para in doc.paragraphs])
    return metadata if metadata else "No metadata found."

def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

#replace api keys :)
