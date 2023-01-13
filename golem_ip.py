import requests
from urllib.parse import urljoin
import time

host = "http://ports.golem.network/"

response = requests.post(
    urljoin(host, 'ping-me'),
    data={
        'ports': [8080],
        'timestamp': time.time()
    },
    timeout=10.0,
)
result = response.text
print('Ping result: ', result)

