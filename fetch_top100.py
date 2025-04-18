import requests
from bs4 import BeautifulSoup

def fetch_top_100():
    url = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    addresses = []
    for link in soup.select("td div div span.addr"):
        addr = link.text.strip()
        if addr:
            addresses.append(addr)

    with open("wallets_top100.txt", "w") as f:
        for addr in addresses:
            f.write(f"{addr}\n")

    print(f"Saved {len(addresses)} addresses to wallets_top100.txt")

if __name__ == "__main__":
    fetch_top_100()
