import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
from time import sleep

def check_recent_articles():
    response = requests.get("https://medium.com")
    # response.content
    soup = BeautifulSoup(response.content, 'html.parser')
    # title_elements = soup.select("h2.ui-h4")
    main_containers = soup.select("div.extremeHero-postContent")


    names= []
    # for element in title_elements:
    #     names.append(element.string)
    
    for container in main_containers:
        print("Title: ", container.select_one(".u-marginBottom4").string)
        print("Author: ", container.select_one("a.postMetaInline--author").string)
        print("Summary: ", container.select_one("div.ui-summary").string)
    
    # return tuple(names)
    # names =[element.string for element in title_elements]
        # print (element.string)

def notify(article_title, text="Nothing yet"):
    toaster = ToastNotifier()
    toaster.show_toast(article_title, text, duration=3)

# def main():
#     article_titles= check_recent_articles()
    
#     for article_title in article_titles:
#         notify(article_title, "Some Content")
#         sleep(3)


if __name__=="__main__":
    check_recent_articles()

# notify("Hello There", "Just Wanted to see how you are")
# print(len(soup.select("h2.ui-h4")))
# print(response.content)
