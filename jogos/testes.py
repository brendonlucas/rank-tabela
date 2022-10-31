import requests

def main():
    url = "https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl=www.google.com"
    r = requests.get(url)
    print(r.content)

if __name__ == '__main__':
    main()