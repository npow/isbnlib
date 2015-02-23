#!/usr/bin/env python

from textwrap import fill

from .dev.webservice import query as wsquery

UA = "isbntools (gzip)"


def goo_desc(isbn):
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn+{isbn}"\
          "&fields=items/volumeInfo(description)"\
          "&maxResults=1".format(isbn=isbn)
    content = wsquery(url, user_agent=UA)
    try:
        content = content['items'][0]['volumeInfo']['description']
        return fill(content, width=75)
    except:
        return
