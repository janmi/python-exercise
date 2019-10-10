import urllib.parse
import http.client
import json

def main():
	host = "106.ihuyi.com"
	sms_send_url = '/webservice/sms.php?method=Submit'
	params =  urllib.parse.urlencode({'account': 'APIID', 'password': 'APIKEY', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '15977488817', 'format': 'json'})
	print(params)
	headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
	conn = http.client.HTTPConnection(host, port=80, timeout=30)
	conn.request('POST', sms_send_url, params, headers)
	response = conn.getresponse()
	print(response)
	response_str = response.read()
	jsonstr = response_str.decode('utf-8')
	print(json.loads(jsonstr))
	conn.close()


if __name__ == '__main__':
		main()