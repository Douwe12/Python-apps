import webbrowser

def open_url(url):
    webbrowser.open(url)


url = input("Enter url: ")
open_url(url)