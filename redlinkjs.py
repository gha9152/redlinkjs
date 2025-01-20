import requests
import re
import argparse
import subprocess
import os

def find_urls_and_endpoints(js_content):
    pattern = r'(["\'])((https?:\/\/)?([a-zA-Z0-9\-\.]+)(\/[a-zA-Z0-9\-\/]*)*)\1'
    urls = re.findall(pattern, js_content)
    endpoints = [url[1] for url in urls if url[1]]
    return endpoints

def process_js_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"JS file successfully loaded from: {url}")
        js_content = response.text
        endpoints = find_urls_and_endpoints(js_content)
        if endpoints:
            print("\nAll extracted endpoints and links:")
            for endpoint in endpoints:
                print(endpoint)
        else:
            print("No endpoints or links found.")
    else:
        print(f"Error loading JS file, status: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract endpoints and links from a JS file.')
    parser.add_argument('-u', '--url', type=str, required=True, help='URL of the JS file')
    args = parser.parse_args()
    install_requirements_from_github()
    process_js_file(args.url)
