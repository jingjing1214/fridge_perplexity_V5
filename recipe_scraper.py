import requests
from bs4 import BeautifulSoup

def search_recipes(ingredients):
    query = f"{ingredients} 食譜 site:icook.tw"
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    results = []
    for g in soup.select(".tF2Cxc")[:5]:
        title = g.select_one("h3").text if g.select_one("h3") else "無標題"
        link = g.select_one("a")["href"] if g.select_one("a") else "#"
        snippet = g.select_one(".VwiC3b").text if g.select_one(".VwiC3b") else ""
        results.append((title, link, snippet))
    return results