from urllib.request import urlopen, urljoin 
import re 

def download_page(url):
    return urlopen(url).read().decode('utf-8')

def extract_image_locations(page):
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    return img_regex.findall(page)

if __name__ == '__main__':
    target_url = "https://www.debian.org/"
    debian = download_page(target_url)
    image_locations = extract_image_locations(debian)
    for src in image_locations:
        print(urljoin(target_url, src))