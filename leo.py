import codecs

import sys

import lxml
import urllib3
from urllib.parse import quote

from collections import defaultdict
from lxml import etree
from lxml.html.soupparser import fromstring

import conf

http = urllib3.PoolManager()

fromlang_xpath = '//*/table/tbody/tr[*]/td[5]/samp'
fromlang_text_xpath = "(.|.//*)/text()"

tolang_xpath   = '//*/table/tbody/tr[*]/td[8]/samp'
tolang_text_xpath   = fromlang_text_xpath

sections = ['section-phrase', 'section-praep', 'section-example', 'section-subst', 'section-adjadv', 'section-verb']


def extract_words(tree, xpath, text_xpath):
    d = defaultdict(list)
    for a in tree.xpath(xpath):
        words = [w.strip() for w in a.xpath(text_xpath)]
        samp = " ".join([w for w in words if w])

        clazz = a.xpath("../../../../../@id")[0]

        d[clazz].append(samp)

    return d

def lookup(word):
    eurl = conf.make_leo_path(quote(word))
    print(eurl)

    response = http.request("GET", eurl)
    htmlparser = etree.HTMLParser()
    tree = etree.fromstring(response.data)

    with open("response.txt", "w") as f:
        print(etree.tostring(tree), file=f)

    from_dict = extract_words(tree, fromlang_xpath, fromlang_text_xpath)
    to_dict = extract_words(tree, tolang_xpath, tolang_text_xpath)

    return from_dict, to_dict
