#!/usr/bin/env python
# coding: utf-8

import serial
import time
import os
from twython import Twython

print('twitterの認証情報を入力')
CONSUMER_KEY = 'xxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxx'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

print('シリアル通信開始')
#シリアル通信
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

while 1:
	data = ser.readline()#Arduinoからデータの読み込み

	data2 = int(data)#int型に変換
	print('部屋の照明監視中' + time.ctime() + ',' + '照明状況' + ',' + str(data))
	#取得した照度情報をツイート
	if data2 == 2000:
		print('電気がついたよ！')
		api.update_status(status= time.ctime()+'おはよう！')
		time.sleep(1)
	elif data2 == 1000:
		print('電気が消えたよ！')
		api.update_status(status= time.ctime()+'おやすみなさい')
		time.sleep(1)