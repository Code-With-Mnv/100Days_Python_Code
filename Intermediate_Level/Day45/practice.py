from bs4 import BeautifulSoup

with open("website.html") as webfile:
    contents = webfile.read()

soup = BeautifulSoup(contents, "html.parser")
#here we have created a soup object using which we can tap into any element of the website

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.li)
print(soup.li.string)
print(soup.a)

all_li_tag = soup.findAll(name="li")
#returns a list

print(all_li_tag)

#when we want only text not the whole tag
#or only href

li_str = []
href_lst = []

for tag in all_li_tag:
    li_str.append(tag.getText())
    href_lst.append(tag.get("href"))

print(li_str)
print(href_lst)

# we can also access a particular tag having a particular "id" or "class" using "id" or "class_" attributes