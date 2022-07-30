from bs4 import BeautifulSoup
import requests

class Search:
    def __init__(self, entry, comments, points):
        self.entry = entry
        self.comments = comments
        self.points = points
    
    def __repr__(self):
        return "Entry: " +str(self.entry)+ "    -   Comments: " +str(self.comments)+ "  - Points: " +str(self.points) + "\n"

class List:
    def __init__(self):
        self.list_search = list_search

    # Filter Comments
    def filter_comments_major5(self):
        filter_comments = list()
        temp_list = list()

        for element_list in self:
            if len(element_list.entry.split()) > 6:
                num_comments = element_list.comments.split()[0]
                if (num_comments.isdigit()):
                    num_comments = int(num_comments)
                    if len(filter_comments) == 0:
                        filter_comments.append(element_list)
                    else:
                        count = 0
                        controlInsert = False

                        for comments_list in filter_comments:
                            if(num_comments > int(comments_list.comments.split()[0])):
                                filter_comments.insert(count, element_list)
                                controlInsert = True
                                break
                            count += 1
                else:
                    temp_list.append(element_list)

        filter_comments.extend(temp_list)
        return filter_comments

    # Filter Points
    def filter_points_minor5(self):
        filter_points = list()
        temp_list = list()

        for element_list in self:
            if len(element_list.entry.split()) <= 6:
                num_points = element_list.points.split()[0]
                if (num_points.isdigit()):
                    num_points = int(num_points)
                    if len(filter_points) == 0:
                        filter_points.append(element_list)

                    else:
                        count = 0
                        controlInsert = False

                        for comments_list in filter_points:
                            if(num_points > int(comments_list.points.split()[0])):
                                filter_points.insert(count, element_list)
                                controlInsert = True
                                break
                            count += 1
                else:
                    temp_list.append(element_list)

        filter_points.extend(temp_list)
        return filter_points

page = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(page.content, 'html.parser')

id = soup.find_all('tr', class_='athing')
list_search = list()
count = 0

for i in id:
    if count < 30:
        entries = soup.find_all('tr', id=i['id'])
        comments = soup.find_all('a', href='item?id=' + i['id'])
        points = soup.find_all('span', id='score_' + i['id'])
        if(len(comments) == 1 and len(points) == 0):
            list_search.append(
                Search(entries[0].text, 'No comments', 'No points'))
        elif (comments[1].text.find('comments') < 0):
            list_search.append(
                Search(entries[0].text, 'No comments', points[0].text))
        elif(len(points) == 0):
            list_search.append(
                Search(entries[0].text, comments[1].text, 'No points'))
        else:
            list_search.append(
                Search(entries[0].text, comments[1].text, points[0].text))
    else:
        break
    count += 1

while(True):
    value = input('What do you want to print in the therminal: 1-Ordered by comments 2-Ordered by points or 3-Print all the list?')
    print(value)
    if (value == '1'):
        print(List.filter_comments_major5(list_search))
    elif (value == '2'):
        print(List.filter_points_minor5(list_search))
    elif (value == '3'):
        print(list_search)