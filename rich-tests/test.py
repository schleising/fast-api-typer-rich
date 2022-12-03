from time import sleep
from urllib.request import urlopen

from rich.progress import wrap_file

response = urlopen("https://www.textualize.io")
size = int(response.headers["Content-Length"])

with wrap_file(response, size) as file:
    for line in file:
        print(line.decode("utf-8"), end="")
        sleep(0.1)