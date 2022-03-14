import requests
import sys

def db_setup(url, db_addr):
    r = requests.get(url, allow_redirects=True)
    open(db_addr, 'wb').write(r.content)

if __name__ == "__main__":
    url = 'https://github.com/lzy2022/S2022_EC530_Project2/raw/main/Code/DB/Project_2_back.db'
    db_addr = sys.argv[1]
    db_setup(url, db_addr)