import requests
from bs4 import BeautifulSoup

url=input( "enter url")
response=requests.get(url)
# print(type(response))
# print(response.text)
filename="temp.html"
bs=BeautifulSoup(response.text,"html.parser")
formatted_text=bs.prettify()
print(formatted_text)

with open(filename,"w+") as f:
     f.write(formatted_text)


list_imgs=bs.find_all('img')
#  print(list_imgs)

no_of_imgs=len(list_imgs)

list_as=bs.find('a')
no_of_as=len(list_as)

print("number of imgs tags ",no_of_imgs)
print("number of anchor ",no_of_as)