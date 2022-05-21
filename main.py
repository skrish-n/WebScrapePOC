# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
from bs4 import BeautifulSoup

def crawl_for_zip(zip_code):
    # Use a breakpoint in the code line below to debug your script.

    URL = "https://www.yelp.com/search?find_desc=Apartments&find_loc="+zip_code
    #print(URL)
    page = requests.get(URL).text
    #print('request done')
    soup = BeautifulSoup(page, 'lxml')
    listing = soup.find_all('div', class_='child__09f24__EJUma')
    #print(soup)
    json_list = []
    for i in range(len(listing)):
        name = listing[i].find('img').get('alt')
        url = 'https://www.yelp.com'+listing[i].find('a').get('href')
        img_src = listing[i].find('img').get('src')
        curr_dict = {'Name':name,'ListingURL':url,'ImageURL':img_src}
        json_list.append(curr_dict)
        '''
        print(name)
        print(url)
        print(img_src)
        '''
    json_string = json.dumps(json_list, indent=4)
    #print(json_string)
    f = open("output.txt", "w")
    f.write(json_string)
    f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zip_code = input('Enter your Zipcode:\n')
    print(zip_code)
    crawl_for_zip(zip_code)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
