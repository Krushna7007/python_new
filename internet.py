import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
print( 'connected' if connect() else 'no internet!' ) #single line if else in python 3