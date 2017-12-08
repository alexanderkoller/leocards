import urllib3

http = urllib3.PoolManager()

headers = urllib3.make_headers(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
url = "https://docs.google.com/forms/d/e/1FAIpQLScnrTr-Rf0j8Hfv5pWmYROhuSxnNMZJk_wV3FZBizl48--37A/formResponse"

def add_vocab(from_word, to_word):
    params = {
        "entry.2045357775": from_word,
        "entry.804661629": to_word
    }

    response = http.request('POST', url, params, headers)
    # print(response.status)
    # print(response.data)
    return response.status


# add_vocab("from", "to")