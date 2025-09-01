import urllib
import urllib.request

try:
    user_website = str(input("Enter a website URL: "))
    site = urllib.request.urlopen("http://" + user_website)
    print(f'Website {site.geturl()} is up and running.')

except urllib.error.URLError:
    print("Failed to retrieve webpage.")