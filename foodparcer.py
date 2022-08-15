import requests
from bs4 import BeautifulSoup
import os

url = "http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie    "

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0(iPad;CPU OS 110like Mac OSX)AppleWebKit/604.1.34(KHTML,like Gecko)Version/11.0 Mobile/15A5341f Safari/604.1"
}
req = requests.get(url, headers=headers)
src = req.text


soup = BeautifulSoup(src, "lxml")
all_products = soup.find_all(class_="mzr-tc-group-item-href")
all_categories_dist = {}
all_names = []
for item in all_products:
    item_text = item.text
    item_href = "http://health-diet.ru" + item.get("href")
    all_categories_dist[item_text] = item_href
    all_names.append(item_text)

while True:
    for item in all_names:
        print(item, end=", ")

    factory_name = input("\n\nName - ")

    url = all_categories_dist[factory_name]
    print(url)

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0(iPad;CPU OS 110like Mac OSX)AppleWebKit/604.1.34(KHTML,like Gecko)Version/11.0 Mobile/15A5341f Safari/604.1"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")

    all_information = soup.find(
        class_="uk-overflow-container").find("tbody").find_all("tr")
    filename = (f"{factory_name}.txt")

    if " " in filename:
        filename = filename.replace(" ", "_")

    with open(filename, "w", encoding="utf-8") as file:
        for item in all_information:
            try:
                table_cell = item.find_all("td")
                product_name = table_cell[0].text.strip()
                cal = table_cell[1].text.strip()
                squirrels = table_cell[2].text.strip()
                fats = table_cell[3].text.strip()
                carb = table_cell[4].text.strip()
                structure = item.find("a").get("href")
                
            except Exception as exp:
                print(f"error \n{exp}")

            info = (
                f"\n{product_name} - http:/health-diet.ru{structure} \n{cal} \n{squirrels} Белки \n{fats} Жиры \n{carb} Углеводы\n")

            print(info)
            file.write(info)

    os.system(f"start {filename}")
