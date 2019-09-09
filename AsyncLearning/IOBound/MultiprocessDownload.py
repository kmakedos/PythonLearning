import requests
import multiprocessing
import time


session = None


# This creates a session for each process (not for each function call)
def get_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}: Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with multiprocessing.Pool(initializer=get_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == '__main__':
    sites = [
        "http://www.in.gr",
    ] * 80

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

# It took 18" with 20 workers
