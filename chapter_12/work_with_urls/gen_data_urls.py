from urls_utils import gen_from_urls
import pprint

urls = ('http://ya.ru', 'http://twitter.com', 'http://mail.ru')

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)

urls_res = {url: size for size, _, url in gen_from_urls(urls)}
pprint.pprint(urls_res)
