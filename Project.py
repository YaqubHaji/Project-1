import webbrowser

with open('websites.txt') as file:
    links = file.readlines()
    for link in links:
        webbrowser.open(link)