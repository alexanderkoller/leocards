import urllib
from lxml import etree

url =  "http://www.example.com/servlet/av/ResultTemplate=AVResult.html"
response = urllib.urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
tree.xpath("x")