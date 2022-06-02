from bs4 import BeautifulSoup
import requests
import os


if not os.path.exists("output"):
    os.mkdir("output")

firstUrl: str = ""

downloadCount: int = 1
pageCount: int = 1
while True:
        
    response = requests.get(f"https://worldflipper.jp/character/?p={pageCount}")

    if response.status_code == 404:
        break

    soup = BeautifulSoup(response.text, "lxml")

    results = soup.find_all("ul", {"class": "char-list"})

    for result in results:
        for character in result.find_all("li"):
            character_name = character.find("a").text.replace("\n", "")
            character_url = character.find("a")["href"]
            character_img = character.find("img")["src"]

            if firstUrl == "":
                firstUrl = character_url
            else:
                if character_url == firstUrl:
                    break

            print(f">>> {character_name} -- {downloadCount} in page({pageCount})")

            response = requests.get(f"https://worldflipper.jp{character_url}")
            soup = BeautifulSoup(response.text, "lxml")
            downloadResults = soup.find_all("a", {"rel": "noopener noreferrer"})

            for downloadLink in downloadResults:

                # href = downloadLink["href"]
                href = downloadLink.get("href")

                if "dot_front" in href:
                    if not os.path.exists(f"output/{downloadCount}_{character_name}_dot_front.png"):
                        print(f"Downloading image file: {href}")
                        imageRequest = requests.get(href)
                        with open(f"output/{downloadCount}_{character_name}_dot_front.png", "wb") as file:
                            file.write(imageRequest.content)
                    else:
                        print(f"Skip: {href}")

                if "illust_0" in href:
                    if not os.path.exists(f"output/{downloadCount}_{character_name}_illust_0.png"):
                        print(f"Downloading image file: {href}")
                        imageRequest = requests.get(href)
                        with open(f"output/{downloadCount}_{character_name}_illust_0.png", "wb") as file:
                            file.write(imageRequest.content)
                    else:
                        print(f"Skip: {href}")

                if "illust_1" in href:
                    if not os.path.exists(f"output/{downloadCount}_{character_name}_illust_1.png"):
                        print(f"Downloading image file: {href}")
                        imageRequest = requests.get(href)
                        with open(f"output/{downloadCount}_{character_name}_illust_1.png", "wb") as file:
                            file.write(imageRequest.content)
                    else:
                        print(f"Skip: {href}")              
                
            downloadCount += 1

    pageCount += 1

exit(0)