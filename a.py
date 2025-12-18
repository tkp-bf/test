import requests

response = requests.get('https://g6n9nqfq6nt2cgfn3cmplk5gn7tyhp8dx.bf.gy/rce')
print(response.status_code)  # HTTP status code
print(response.json())       # JSON response (if applicable)
