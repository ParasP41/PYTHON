'''#requests module#'''

import requests
from bs4 import BeautifulSoup 
# response=requests.get("https://www.google.com/");
# print(response.text)

# url="https://jsonplaceholder.typicode.com/posts"
# data = {
#     'key1': 'value1',
#     'key2': 'value2'
# }
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Bearer YOUR_TOKEN_HERE'
# }

# res = requests.post(url, headers=headers, json=data);
# print(res.text);



url="https://www.codewithharry.com/blogpost/django-cheatsheet/";
res=requests.get(url);
# print(res.text);

soup=BeautifulSoup(res.text,"html.parser");

for heading in soup.find_all("h2"):
    print(heading.text);

# print(soup.prettify());