import requests
import sys
from bs4 import BeautifulSoup
import json
from os import path
import pathlib
import os

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

s = requests.Session()

def main():
    if len(sys.argv) < 2:
        raise ValueError("expected url argument")
    
    url = sys.argv[1]
    
    data = s.get(url, headers=headers)
    
    prod_name, prod_img_links = parse(data.content)

    save_to_dir = path.join(os.getcwd(), "products" , prod_name)
    pathlib.Path(save_to_dir).mkdir(parents=True, exist_ok=True)
    
    img_fps = save_images(prod_img_links, prod_name, save_to_dir)
    
    print(f"SAVED {len(img_fps)} / {len(prod_img_links)} PRODUCT IMAGES FOR ITEM '{prod_name}'")
    print(save_to_dir)
    
    
def parse(data : str) -> [str, [str]]:
    try:
        html = BeautifulSoup(data)
        
        prod_data_str = html.find("script",{"type":"application/ld+json"})
        
        prod_data = json.loads("".join(prod_data_str.contents))
        
        return [prod_data['name'], prod_data['image']]
    except:
        pass
    
def save_images(image_urls : [str], filename : str = "product_image", dir : str = "./"):
    img_saved_to_fps = []
    for [i,url] in enumerate(image_urls):
        res = s.get(url)
        
        if res.status_code < 200 or res.status_code >= 400:
            continue
        
        p = path.join(dir, filename + str(i))
        if not p.endswith(".jpg"):
            p += ".jpg"
        with open(p, "wb") as f:
            f.write(res.content)
            img_saved_to_fps.append(p)
    
    return img_saved_to_fps
        
if __name__ == "__main__":
    main()
    