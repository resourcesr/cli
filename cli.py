from src._config import get_config
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

"""ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE"""

heads = {'User-Agent': 'python'}
url = "https://www.riphah.edu.pk/faculty/ict-computing" #get_config("url")
req = Request(url, headers={'User-Agent': 'PYTHON/3.8'})
response = urlopen(req)
html = response.read().decode()

soup = BeautifulSoup(html, 'html.parser')

print(soup)
