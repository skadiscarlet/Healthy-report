#! /bin/bash
# health report 
# Date: 15:01 2021-8-25
var=`sudo python ~/Health-report/weixin.py 2>~/e.txt`
if test 'success' = $var
then
	echo "上报成功" | mail -s "健康打卡成功" 1375446341@qq.com
else
	echo $var
fi

