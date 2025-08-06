#!/usr/bin/env python3
import requests

def main():
    url = "https://wttr.in/Tulcea"
    response = requests.get(url)
    print(response.text)

if __name__ == "__main__":
    main()