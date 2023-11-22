import webbrowser

def open_url(url):
    chrome_path = 'C:\Program Files\Google\Chrome\Application\Chrome.exe'
    webbrowser.open(chrome_path, url)


url = input("Enter url: ")
open_url(url)