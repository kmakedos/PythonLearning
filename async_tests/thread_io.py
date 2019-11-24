import concurrent.futures
import threading
import time
import requests

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=9) as executor:
        executor.map(download_site, sites)


if __name__ == '__main__':
    sites = [
       "https://www.in.gr",
       "https://realpython.com",
       "http://www.dabeaz.com/coroutines/"
    ] * 10

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
