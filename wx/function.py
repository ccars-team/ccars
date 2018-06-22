## -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from dss.Serializer import serializer
from wx.sql import Sql

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