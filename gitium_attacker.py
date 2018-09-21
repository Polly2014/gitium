#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import json
import time
import re
import random


if __name__ == '__main__':
	print "Spider Started..."
	headers = {
		'Connection': 'keep-alive',
		'Content-Type': 'application/json',
		'x-iota-api-version': '1',
		# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) gitium/2.1.3 Chrome/59.0.3071.115 Electron/1.8.2 Safari/537.36',
		'User-Agent': 'gitium-rn/1 CFNetwork/974.2.1 Darwein/18.0.0',
		'AcceptLanguage': 'zh-cn',
		'Accept-Encoding': 'gzip, deflate',
	}
	base_url = 'http://www.gitium.io/gitium/charge/saveCharge'
	page_url = 'http://www.gitium.io/gitium/buySell/getSellCancelListByPage'
	pay_load = {"receivedAddress":"SDIPOLOPSQMKUYODGICMEWHNVNKXIAUDNMJLOBQQWAGRTBBKEJCZJMG9GEOMDKAGVBLJHHVRCDTXBSTMX","currency":"GIT","value":1310787783458,"status":"0","phone":"<script>alert('H');</script>","chargeValue":9,"useCurrency":"Bitcoin","chargeAddress":"SDIPOLOPSQMKUYODGICMEWHNVNKXIAUDNMJLOBQQWAGRTBBKEJCZJMG9GEOMDKAGVBLJHHVRCDTXBSTMX","userPayAddress":"SDIPOLOPSQMKUYODGICMEWHNVNKXIAUDNMJLOBQQWAGRTBBKEJCZJMG9GEOMDKAGVBLJHHVRCDTXBSTMX"}
	payload = {"command":"getNodeInfo"}
	i = 1
	while True:
		resp = requests.post(base_url, data=json.dumps(payload), headers=headers)
		# print resp.status_code
		print "{}-{}".format(i, resp.text)
		i += 1
		# jsonResp = resp.json()
	print "Spider Finished!!!"

