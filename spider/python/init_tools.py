import os
import sys
# import uuid
from scrapy.cmdline import execute
# from rediscluster import RedisCluster
# from elasticsearch import Elasticsearch

import xlrd
import xlwt


# 设置表格样式
def set_stlye(name, height, bold=False):
    # 初始化样式
    style = xlwt.XFStyle()
    # 创建字体
    font = xlwt.Font()
    font.bold = bold
    font.colour_index = 4
    font.height = height
    font.name = name
    style.font = font
    return style


def init_execel():
    wb = xlwt.Workbook()
    job_sheet = wb.add_sheet(u'job', cell_overwrite_ok=True)
    title = [u'company_name', u'address', u'position_id', u'position_name',
             u'salary', u'describe', u'work_year', u'educational', u'create_time']
    for i in range(0, len(title)):
        job_sheet.write(0, i, title[i], set_stlye("Time New Roman", 220, True))
    wb.save('/home/cat/Downloads/common/job.xls')


def read_excel():
    # 打开文件
    wb = xlrd.open_workbook(r'/home/cat/Downloads/common/job.xls')
    # 获取所有sheet的名字
    print(wb.sheet_names())
    # 获取第二个sheet的表明
    sheet = wb.sheet_by_index(0)
    return sheet


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

    # init_execel()
    # sheet = read_excel()
    # print(sheet.nrows)
