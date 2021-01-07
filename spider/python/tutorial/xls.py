import xlrd
import xlwt
from xlutils import copy


class tool:
    # 设置表格样式
    def set_stlye(self, name, height, bold=False):
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

    def init_execel(self):
        wb = xlwt.Workbook()
        job = wb.add_sheet(u'job', cell_overwrite_ok=True)
        title = [u'company_name', u'address', u'position_id', u'position_name',
                 u'salary', u'describe', u'work_year', u'educational', u'create_time']
        for i in range(0, len(title)):
            job.write(0, i, title[i], set_stlye("Time New Roman", 220, True))
        wb.save('/home/cat/Downloads/common/job.xls')

    def write_excel(self, data):
        # 打开文件
        rbook = xlrd.open_workbook(r'/home/cat/Downloads/common/job.xls')
        rsheet = rbook.sheet_by_index(0)
        # 获取所有sheet的名字
        # print(rbook.sheet_names())
        wbook = copy.copy(rbook)
        # 获取第1个sheet的表
        wsheet = wbook.get_sheet(0)
        for c in range(0, len(data)):
            wsheet.write(rsheet.nrows + 1, c, data[c], self.set_stlye("Time New Roman", 220, True))
        wbook.save('/home/cat/Downloads/common/job.xls')
