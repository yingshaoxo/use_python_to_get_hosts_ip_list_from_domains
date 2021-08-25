domains = [
"api.binance.com"
]

import socket
import sys
print("\n\n")
for url in domains:
    ip = socket.gethostbyname(url)
    print(f"{ip} {url}")

#curl -X GET "https://api.binance.com/api/v3/exchangeInfo"
