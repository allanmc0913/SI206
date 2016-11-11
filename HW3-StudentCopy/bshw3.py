# Allan Chen, SI206 Homework 3

# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
import re
from bs4 import BeautifulSoup

base_url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

#for loop to find every instance of "student" and replace it with "AMAZING student".  Regex accounts for when "students" is in the text since "student" is in "students"
#referenced from http://stackoverflow.com/questions/15056633/python-find-text-using-beautifulsoup-then-replace-in-original-soup-variable
findstudent = soup.find_all(text=re.compile("student"))
for word in findstudent:
	fixedtext = word.replace("student", "AMAZING student")
	word.replace_with(fixedtext)

#for loop iterates through every image tag looking for a specifc src (logo2.png).  
for img in soup.find_all('img', src="logo2.png"):
	#replace existing src with new image src.  New src is the UMSI logo saved in given media folder
	img['src'] = 'media/logo.png'

#for loop iterates through every image tag looking for a specific src.  That src is the big image on the webpage.  
for img in soup.find_all('img', src="https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg"):
	#replace existing src with new src.  New src is image of myself saved in same media folder
	img['src'] = 'media/allanchen.jpg' 

#at the end, save HTML output to a new file
with open("BSIadmissionspage.html", "w") as file:
	file.write(soup.prettify())