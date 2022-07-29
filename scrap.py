from bs4 import BeautifulSoup
import requests

class Search:
    def __init__(self, entry, comments, points):
        self.entry = entry
        self.comments = comments
        self.points = points
    def __str__(self):
        return "Entry: " +str(self.entry)+ "    -   Comments: " +str(self.comments)+ "  - Points: " +str(self.points)

page = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(page.content, 'html.parser')

id = soup.find_all('tr', class_='athing')
list_search = list()
count = 0

for i in id:
    if count < 30:
        entries = soup.find_all('tr', id=i['id'])
        comments = soup.find_all('a', href='item?id='+ i['id'])
        points = soup.find_all('span', id='score_'+ i['id'])
        if(len(comments) == 1 and len(points) == 0):
            list_search.append(Search(entries[0].text, 'No comments', 'No points'))
        elif (comments[1].text.find('comments') < 0):
            list_search.append(Search(entries[0].text, 'No comments', points[0].text))
        elif(len(points) == 0):
            list_search.append(Search(entries[0].text, comments[1].text, 'No points'))
        else:
            list_search.append(Search(entries[0].text, comments[1].text, points[0].text))
    else:
        break
    count += 1

for search in list_search:
    print(search)

