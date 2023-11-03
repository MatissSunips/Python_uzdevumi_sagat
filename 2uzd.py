""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.
1)RSS?
2)plūsmu no google.lv
Satura agregators- tas ir sistēma, kas ļauj abonēt interesojošos avotus (Sekošana, abonēšana.)
Kā dabūt RSS plūsmu iekš VSC?
"""
import feedparser

# URL uz RSS plūsmu

rss_url='https://news.google.com/home?hl=lv&gl=LV&ceid=LV:lv'

# iegūstam RSS plūsmas datus un veicam analīzi
kkk=feedparser.parse(rss_url)

# noformēšana....
for entry in kkk.entries:
    print("Virsraksts", entry.title)
    print("Saite:", entry.link)
    print("Publicēšanas datums:", entry.published)
    print("\n")