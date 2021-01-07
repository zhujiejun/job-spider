import os
import sys

from scrapy.cmdline import execute

# import uuid
# from rediscluster import RedisCluster
# from elasticsearch import Elasticsearch

# startup_nodes = [{"host": "node101", "port": "7001"}]
# elastic_nodes = [{"host": "node101", "port": 9200},
#                  {"host": "node102", "port": 9200},
#                  {"host": "node103", "port": 9200}]

# url = 'https://www.zhipin.com/job_detail/?city=101280600&query=Java'
if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy', 'crawl', 'boss'])
    # rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    # rc.set("foo", "bar")
    # es = Elasticsearch(elastic_nodes)
    # es.index(index="job_test_index", id=uuid.uuid1(), body={'name': 'zhujiejun', 'age': 18})

    # driver = tool().driver
    # driver.get(url)
    # driver.execute_async_script('send_xml_request()')
    # html = driver.page_source
    # file_handle = open('/home/cat/Downloads/common/zhipin.html', mode='w')
    # file_handle.write(html)
    # driver.save_screenshot('/home/cat/Downloads/common/zhipin.png')
    # print(f'{html}')

    # salary = '15-25K'
    # salary = '15-25K·13薪'
    # pattern = re.compile(r'K(·(\d)+薪)?$')
    # salary = pattern.sub('', salary)
    # res = salary.split('-')
    # temp = []
    # for x in res:
    #     temp.append(int(x) * 1000)
    # for item in temp:
    #     print(item)
