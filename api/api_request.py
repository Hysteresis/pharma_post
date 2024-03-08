import requests

url = 'http://127.0.0.1:8000/api/'
headers = {
    # 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5ODk0NDQwLCJpYXQiOjE3MDk4OTQxNDAsImp0aSI6ImM5OTliNWUwNGJjZjRhOWZhZmU5MWFkNDRiOTc0YTI1IiwidXNlcl9pZCI6MX0.EyxjTmPyBI4wl_1wbYp8KQ1xkptoYExi_UcmhiSLM9c'
}
response = requests.get(url, headers=headers)

print(response.text)

