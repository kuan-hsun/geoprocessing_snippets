import requests
 
payload = {}
response = requests.get("your_api_uri", params=payload)

#只要字串則直接取出 text 值
response_text = response.text
print (response_text)