import os
from urllib.parse import quote

leo_lang = os.environ["LEO_LANG"]
gf_url = os.environ["GF_URL"]
gf_from_id = os.environ["GF_FROM_ID"]
gf_to_id = os.environ["GF_TO_ID"]




def make_leo_path(word):
    return "https://dict.leo.org/%s/%s" % (quote(leo_lang), quote(word))

