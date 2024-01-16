from urllib import request

response = request.urlopen('http://example.com')

print("Status: ", response.status)
print("Get code: ", response.getcode())
print("Msg: ", response.msg)
print("Reason: ", response.reason)
# get header like internal object
print("Headers: ", response.headers)

# get dict of all headers
print("Get headers: ", response.getheaders())

# get selected header
print("Headers get: ", response.headers.get('Content-Type'))
print("Get header: ", response.getheader('Content-Type'))