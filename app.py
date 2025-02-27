import requests
from bs4 import BeautifulSoup


def check_links_in_html(file_path):
    
    # open the html file
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        html_content = file.read()

    # parse the html with beautifulsoup
    soup = BeautifulSoup(html_content, "html.parser")

    # find all anchor tags
    links = soup.find_all("a", href=True, )

    for link in links:
        url = link.get("href")
        
        # only external links
        if url.startswith('https://'):
            try:
                response = requests.get(url, timeout=5)  # set a timeout to avoid hanging
                if response.status_code == 200:
                    print(f"Valid: {url}")
                else:
                    print(f"Invalid (Status {response.status_code}): {url}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {url} - {e}")


print("-- index ---")
check_links_in_html("index.html")

print("-- cv ---")
check_links_in_html("cv.html")