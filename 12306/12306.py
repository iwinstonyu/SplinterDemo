#coding=utf-8

from splinter import Browser
b = Browser(driver_name="chrome")
b.visit("https://mail.126.com")
b.fill("email","windpenguin")
b.fill("password","123!")

