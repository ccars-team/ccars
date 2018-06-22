## -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from wx.data import DBMysqlHelp

def index(request):
        #return render(request, 'home.html')
	return HttpResponse("https自建 Apache Django1")
def home(request):
        return render(request, 'home.html')
def test(request):
    test1 = DBMysqlHelp()
    sql = "select * from c_org";
    all_info = test1.fetchall(sql,None)
    return HttpResponse(all_info)




