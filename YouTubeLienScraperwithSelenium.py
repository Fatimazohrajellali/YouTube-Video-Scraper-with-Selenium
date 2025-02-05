from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

# Chemin vers le ChromeDriver
driver_path = "E:\\driver\\chromedriver.exe"

# Initialiser le navigateur
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Exécuter en mode sans tête

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

def scrape_youtube_videos(search_query, max_videos=10):
    search_url = f"https://www.youtube.com/results?search_query={search_query}"
    driver.get(search_url)
    time.sleep(3)
    
    videos = driver.find_elements(By.XPATH, "//a[@id='video-title']")
    
    scraped_data = []
    for video in videos[:max_videos]:
        title = video.get_attribute("title")
        link = video.get_attribute("href")
        if link:
            scraped_data.append([title, link])
    
    return scraped_data

def save_to_csv(data, filename=r"C:\Users\INKA\Desktop\EfficientNet-B0\youtube_videos1.csv"):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(data)

if __name__ == "__main__":
    query = input("Entrez votre requête de recherche YouTube : ")  # Demander à l'utilisateur d'entrer une requête
    video_data = scrape_youtube_videos(query, max_videos=10)
    save_to_csv(video_data)
    print(f"{len(video_data)} vidéos pour '{query}' ont été ajoutées dans C:\\Users\\INKA\\Desktop\\EfficientNet-B0\\youtube_videos1.csv")

    
    driver.quit()