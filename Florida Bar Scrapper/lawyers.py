import requests
from bs4 import BeautifulSoup as bs


def deCFEmail(fp):
    try:
        r = int(fp[:2],16)
        email = ''.join([chr(int(fp[i:i+2], 16) ^ r) for i in range(2, len(fp), 2)])
        return email
    except (ValueError):
        pass


Base_Url = "https://www.floridabar.org/"

cat = "directories/find-mbr/?sdx=N&eligible=N&deceased=N&pracAreas=C18&pageSize=50"
url = Base_Url + cat + "&pageNumber=1"
next_link = True
names_list = []
firstname_list = []
lastname_list = []
emails_list = []
bar_tags_list = []
companies_list =[]
address_list = []
phone_list = []
io1 = 'HOA22'

while next_link:

    response = requests.get(url)
    soup = bs(response.text, "lxml")
    name_tags = soup.find_all("p", {"class": "profile-name"})
    names = [name.text for name in name_tags if '"' not in name.text]
    names_list+=names

    email_tags = soup.find_all("a", {"class": "icon-email"})
    emails = [str(email) for email in email_tags]
    for x in range(0, len(emails)):
        emails[x] = emails[x].replace('a class="icon-email" href="/cdn-cgi/l/email-protection#', '')
        index = emails[x].find('"')
        emails[x] = emails[x][1:index]
        emails[x] = deCFEmail(emails[x])
    emails_list+=emails

    bar_tags = soup.find_all("p", {"class": "profile-bar-number"})
    bars = [bar.text[5:] for bar in bar_tags]
    bar_tags_list += bars

    contact_tags = soup.find_all("div", {"class": "profile-contact"})
    contacts = [str(contact.find("p")) for contact in contact_tags]
    for x in range(0,len(contacts)):
        contacts[x] = contacts[x].split('<br/>')
        companies_list.append(contacts[x][0][3:])
        address_list.append(contacts[x][1])
        phones = [phone.find("a")['href'][4:] for phone in contact_tags]
        phone_list+= phones

    link = soup.body.find("a", title="next page")
    if link:
        url = Base_Url + link['href']
        print(url)
    else:
        next_link = False
