import requests

url="https://newsapi.org/v2/everything?q=tesla&from=2024-11-03&sortBy=publishedAt&apiKey=71dbc848d129491588b607a267851f82"
res=requests.get(url);