import urllib3

import conf

http = urllib3.PoolManager()

headers = urllib3.make_headers(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')

def add_vocab(from_word, to_word):
    params = {
        conf.gf_from_id: from_word,
        conf.gf_to_id: to_word
    }

    response = http.request('POST', conf.gf_url, params, headers)
    # print(response.status)
    # print(response.data)
    return response.status


# add_vocab("from", "to")