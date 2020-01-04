import ssl
from xmlrpc.client import ServerProxy

ssl._create_default_https_context = ssl._create_unverified_context

s = ServerProxy('https://127.0.0.1:15000', allow_none=True)
s.set('foo','bar')
s.set('spam',[1,2,3])
print('s.keys[]',s.keys())
print("s.get('foo'):")
s.delete('spam')
print("s.exists('spam'):",s.exists('spam')) 

