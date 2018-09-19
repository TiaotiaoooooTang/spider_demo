import requests
from retrying import retry

@retry(stop_max_attempt_number=3)
def get_data():
    print('*' * 50)
    url = 'http://www.zhihu.com'
    response = requests.get(url,timeout=0.005)
    print(response.status_code)

get_data()