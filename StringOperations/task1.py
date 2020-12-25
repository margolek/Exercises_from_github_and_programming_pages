"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

"""
import re

def domain_name(url):
	my_pattern = re.compile(r'^(/)')
	my_page = my_pattern.search(url)
	print(my_page.group())




domain_name('http://github.com/carbonfive/raygun')


