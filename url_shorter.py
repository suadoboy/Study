## LIBRARIES
import hashlib
## FUNCTION TO SHORTEN THE URL
def shorter_url(url):
    return hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
## VARIABLES
original_url = input("Enter the URL: ")
SHORTERD_URL = shorter_url(original_url)
## PRINTING THE RESULT
print("Shorter URL: ", SHORTERD_URL)
print("Original URL: ", original_url)
## AUTHOR: suadob0y