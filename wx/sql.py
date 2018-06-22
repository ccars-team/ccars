## -*- coding: utf-8 -*-
from wx.controller import Controoler
class Sql():
    '''
     name sql Key
     key 关键字
     page 分页偏移量
     limit 每页显示数量
    '''
    def model_org(self,name=False,key=False,page=0,limit=3):
        model_org_sql = {
            "find_sql":"select c_oid,c_name,c_start from c_org limit %s,%s "%(page,limit)
        }
        return  model_org_sql[name]
