import requests
from bs4 import BeautifulSoup
import pandas as pd


def getProjectinfo(url, end, start=1) :
    titles = []
    targets = []
    dates = []
    end = end + 1
    for i in range(start, end):
        print( i )
        response = requests.get( url + str(i) )

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            targetBoxes = soup.find_all('div', class_='item-title-box')

            for items in targetBoxes :
                titleSelect = items.select_one('.item-title')
                targetSelect = items.select_one('.project_target')
                dateSelect = items.select_one('.project_schedule')
                titles.append( titleSelect.text.strip() )
                targets.append(targetSelect.text.strip())
                dates.append(dateSelect.text.strip())

            df = pd.DataFrame()
            df["titles"] = titles
            df["targets"] = targets
            df["dates"] = dates
        else :
            print( response.status_code )
            return False
    return df

def main():
    url = 'http://ydct.or.kr/projects/?sf_paged='
    results =  getProjectinfo(url, end=15, start=1)
    results.to_csv("./yd_projects.csv")

if __name__ == "__main__":
    main()