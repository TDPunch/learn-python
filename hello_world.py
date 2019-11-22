import requests

# For single line python comments
"""
This is a multiline comment
in Python the quotes are delimiters
"""

print("Hello World!")
print("My name is Tyler")

response = requests.get('https://httpbin.org/ip')

print('Your ip is {0}'.format(response.json()['origin']))
