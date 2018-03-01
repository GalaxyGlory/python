#!/usr/bin/env python
#-*- coding:utf-8 -*-

user = raw_input("请输入用户名： ")
pwd  = raw_input("请输入密码： ")

if user == "galaxy" and pwd == "password":
	print ("登陆成功！")
else:
	print ("登录失败！") 
