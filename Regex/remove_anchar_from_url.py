"""

Complete the function/method so that it returns the url with anything
after the anchor (#) removed.

Example:

# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1' 
remove_url_anchor('www.codewars.com?page=1') 
"""

import re

def remove_url_anchor(url):
	my_pattern = re.sub('#.*','',url)
	return my_pattern

a = remove_url_anchor('www.codewars.com#about')
print(a)