import requests
from bs4 import BeautifulSoup

url = 'http://www.reddit.com/r/BabyYoda'

response = requests.get(url)
print(response)
print(type(response.cookies))
for cookie in response.cookies:
    print(f'cookie ~~~ {cookie}')

    # provide a string for the name of the parser that iterates over the html
# (there are other options of the parser but in the example we will use html.parser)
parser_name = "html.parser"

#   Instantiate a Web Scraper
# instantiating a web scraper requires the content of the response
# (this content is located in the 'content' attribute of the request object)

soup = BeautifulSoup(response.content, parser_name)
print(f'pretty soup:\n {soup.prettify()}')


# # find all HTML elements with IMG tags - extracts all the tags that match IMG and stores them in a list
# images = soup.find_all("img")
# for img in images:
#     print(f'img ~~~ {img}')
# print(type(images))

# but we don't want all images scraped so we'll filter them out by a dictionary of attributes
# 'alt': 'Post image' - this will only extract images with 'alt' attribute that equals 'Post image'
# meaning only images that are in posts (as opposed to profile image, for instance)
attr_dict = {'alt': 'Post image'}
images = soup.find_all("img", attrs=attr_dict)

# the entire tag is extracted in the form of a dictionary
# from here we need to extract the 'src' or Source attribute in order to download the images

import urllib.request  # so we can download from the source attribute length

counter = 0
print(f'images {images}')
for image in images:
    image_src = image['src']
    print(f'image_src ~~~ {image_src}')
    # image_name = str(counter)
    image_name = f'babYoda{str(counter)}.jpg'
    print(f'image_name ~~~ {image_name}')
    urllib.request.urlretrieve(image_src, image_name)
    counter += 1

print('FIN')

import praw
reddit = praw.Reddit(client_id = '#####',
client_secret = '#####',
username = '#####',
password = '#####',
user_agent = '#####')

columns = { "User":[], "Subreddit":[], "Title":[], "Description":[], "Timestamp":[]}

for submission in reddit.subreddit("BabyYoda").new(limit=100):
    if submission.author in columns['User']: # skip over authors already seen
        continue
    user = reddit.redditor('{}'.format(submission.author))
    user_posts = list(user.submissions.new(limit=100))

    if len(user_posts) <= 5: # skip over users that have less than 5 posts
        continue
    for sub in user_posts:
        columns["User"].append(sub.author)
        columns["Subreddit"].append(sub.subreddit)
        columns["Title"].append(sub.title)
        columns["Description"].append(sub.selftext)
        columns["Timestamp"].append(sub.created)