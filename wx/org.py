## -*- coding: utf-8 -*-
# from wx.function import *
from wx.data import DBMysqlHelp
import json
from django.http import HttpResponse
from django.shortcuts import render
from dss.Serializer import serializer
from wx.sql import Sql
import pymysql
import math




def org(request):
    # 获取页数
    page_num = request.GET.get('page', '0')
    # 获取地理位置
    # 纬度
    show_latitude = request.GET.get('show_latitude', '0')
    # 经度
    show_longitude = request.GET.get('show_longitude', '0')
    page_nu = (int(page_num) - 1) * 3;
    if float(show_latitude) == 0 or float(show_longitude)== 0:
        sql_do = "select c_oid,c_name,c_start,c_img,c_dis,longitude,latitude,address from c_org limit %s,%s " % (page_nu, 3)
    else:
        # 获取地理位置信息
        local_info = getLocalOrg(lat=float(show_longitude),lon=float(show_latitude),raidus=2000)
        sql_do = "select c_oid,c_name,c_start,c_img,c_dis,longitude,latitude,address from c_org WHERE  longitude between %s  AND   %s  AND  latitude between %s  AND   %s  limit %s,%s " % (local_info['minLat'],local_info['maxLat'],local_info['maxLng'],local_info['minLng'],page_nu, 3)


    model = DBMysqlHelp()
    data_all = model.fetchall(sql_do)

    objects_list = []
    if data_all:
        i = 1;
        for row in data_all:
            d = {}
            d['c_oid'] = row[0]
            d['c_name'] = row[1]
            d['c_start'] = row[2]
            d['c_img'] = row[3]
            d['c_dis'] = row[4]
            d['longitude'] = str(row[5])
            d['latitude'] = str(row[6])
            d['address'] = row[7]
            d['c'] = i
            i = i+1
            objects_list.append(d)
        if(objects_list):
            data = {
                "code":1000,
                "msg":"成功",
                "data": objects_list,
            }
        else:
            data = {
                "code":1001,
                "msg":"失败"
            }
    else:
        if int(page_num)==1:
            data = {
                "code": 1002,
                "msg": "你的周边暂时没有商家"
            }
        else:
            data = {
                "code": 1001,
                "msg": "失败"
            }
    jsondatar = json.dumps(data, ensure_ascii=True)

    return  response_as_json(jsondatar,foreign_penetrate=False)

'''
返回json数据
'''
def response_as_json(data, foreign_penetrate=False):
    # jsonString = serializer(data=data, output_type="json", foreign=foreign_penetrate)
    response = HttpResponse(
        data,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response




'''
 * 计算经纬度范围 
 * lat 纬度 
 * lon 经度 
 * raidus 半径(米) 
'''
def getLocalOrg(lat=0,lon=0,raidus=3000):
    PI = 3.14159265;
    latitude = lat;
    longitude = lon;
    degree = (24901 * 1609) / 360.0;
    raidusMile = raidus;
    dpmLat = 1 / degree;
    radiusLat = dpmLat * raidusMile;
    minLat = latitude - radiusLat;
    maxLat = latitude + radiusLat;

    mpdLng = degree * math.cos(latitude * (PI / 180));
    dpmLng = 1 / mpdLng;
    radiusLng = dpmLng * raidusMile;
    minLng = longitude - radiusLng;
    maxLng = longitude + radiusLng;
    data = {
        "maxLat":maxLat,
        "minLat": minLat,
        "maxLng": maxLng,
        "minLng": minLng,
    }
    return data;  


