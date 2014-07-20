# import library.
import urllib

try: 
  from urllib.request import urlopen
except ImportError:
  from urllib2 import urlopen

# catch google website.  
html = urlopen("http://www.google.com/")
print (html.read())
