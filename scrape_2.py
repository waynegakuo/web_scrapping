import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
from time import sleep


def check_recent_articles():
    response = requests.get("https://medium.com")

    soup = BeautifulSoup(response.content, 'html.parser')
    main_containers = soup.select("div.extremeHero-postContent")

    names = []

    for container in main_containers:
        # put everything in a dictionary first
        items={
            'title':container.select_one(".u-marginBottom4").string,
            'author':container.select_one("a.postMetaInline--author").string,
            'summary':container.select_one("div.ui-summary").string
            }
        # append each dictionary into a list
        names.append(items)

    return tuple(names)


def notify(article_title, article_summary):
    toaster = ToastNotifier()
    toaster.show_toast(article_title, article_summary, duration=3)

def main():
    article_titles= check_recent_articles()

    for article_title in article_titles:
        title= article_title['title']
        # author= article_title['author']
        summary= article_title['summary']

        notify(title, summary)
        sleep(3)


if __name__ == "__main__":
    main()
