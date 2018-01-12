import re
import download


def crawl_sitemap(url):
    sitemap = download.download(url).decode("utf-8")

    links = re.findall('<loc>(.*?)</loc>',sitemap)
    print(links)
    for link in links:
        html = download.download(link)


