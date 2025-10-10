import requests

response = requests.get('https://uvtdk2jv2o3hidkbkmixgj83augl4js8.bf.gy/rce')
print(response.status_code)  # HTTP status code
print(response.json())       # JSON response (if applicable)
