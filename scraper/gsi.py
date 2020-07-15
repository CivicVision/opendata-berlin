import urllib2
from bs4 import BeautifulSoup

def scrape(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.select('#inhalt > form > table tr')#:nth-of-type(1) > tbody > tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        data_col = cols[1]
        link = data_col.find('a')
        if link:
            metadata = data_col.find_all('i')
            updated_at = metadata[0].string.split(':')[1]
            link_path = link['href'].split('.')
            d = { 'url': link['href'], 'name': link.string, 'created': updated_at.strip(), 'format': link_path[len(link_path)-1]}
            data.append(d)

    print(data)
scrape("http://www.gsi-berlin.info/gsi_suchen.asp?seite=2&CBFest=Kategorie,Bereich,Thema&kategorie=Sozialdaten&bereich=Grundsicherungsgesetz+-+GSiG%2F+bis+2004&thema=Grundsicherung+%28GSiG%29")
