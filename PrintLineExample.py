
# change above line to point to local 
# python executable

import urllib, urllib.parse, string, time
 

# create URL with desired search parameters

url = "http://archive.stsci.edu/pointings/search.php?"
url = url + "primary=ACS&outputformat=CSV"
url = url + "&pnt_ucountp=%3C5&pnt_icountp=%3E1&bao=and"
url = url + "&galactic=Above&galsearch=75"
url = url + "&action=Search+Exposures"

print('We are testing')
print(url)
### Done!

class TestObject:
    