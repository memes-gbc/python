#imports all of the juicy stuff and making the variables
# -*- coding: utf-8 -*-
import feedparser
import random
import ssl
import os

def clear():
    x = 0
    while x <= 3:
        print('\n')
        x = x + 1

def feed():
#does a little magic to make sure feedparser does its thing correctly
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

#notices feeds owo whats this
    feeds = [ #entitledparents
             'https://www.reddit.com/r/entitledparents.rss?sort=new',
              #choosingbeggars
             'https://www.reddit.com/r/ChoosingBeggars/search.rss?q=self%3Ayes&restrict_sr=on&include_over_18=on&sort=relevance&t=all',
              #pettyrevenge
             'https://www.reddit.com/r/pettyrevenge.rss?sort=new',
              #stories
             'https://www.reddit.com/r/stories.rss?sort=new'
            ]
#prints all of the feed urls
    x = 0
    feedThingy = 0
    for i in feeds:
        x = x + 1
        feedThingy = feeds[x - 1].replace('https://www.reddit.com/','')
        feedThingy = feedThingy.replace('/search','')
        feedThingy = feedThingy.split('.rss')
        feedThingy = feedThingy[0]
        print('%d) %s' % (x,feedThingy))
#asks which feed do you want
    subreddit = int(input('choose a subreddit (type the num): ')) - 1

#gets feed
    feed = feedparser.parse(feeds[subreddit])
    entries = len(feed['entries'])
    clear()
    x = 0
    n = 0

    for x in feed['entries']:
        n = n + 1
        print('%d) %s' % (n,x['title']))
    print('\n')
    itemChosen = str(input('type the item number you would like to read: '))
    if itemChosen == 'random':
        itemChosen = random.randint(0,entries)
    else:
        itemChosen = int(itemChosen) - 1

#throws out all of the ugly tags and unecessary things
    replacement = str(feed['entries'][itemChosen]['summary'].replace('<p>',' '))
    replacement = str(replacement.replace('&#39;','\''))
    replacement = str(replacement.replace('&#32;',':'))
    replacement = str(replacement.replace(': submitted by :',''))
    replacement = str(replacement.replace(feed['entries'][itemChosen]['author'],''))
    replacement = str(replacement.replace('[link] : [comments]',''))
    replacement = str(replacement.replace('&quot;','"'))
    replacement = str(replacement.replace('&amp;','&'))
    speakText = str(replacement.replace('</p>',' '))
    replacement = str(replacement.replace('</p>','\n\n'))
    while True:
        locationOpen = replacement.find('<')
        if locationOpen != -1:
            locationClose = replacement.index('>') + 1
            replacement = replacement[0:locationOpen] + replacement[locationClose:len(replacement)]
        else:
            break

#feedBody = finalReplacement
    clear()

#gets all of the details of the post
    feedAuthor = feed['entries'][itemChosen]['author']
    feedAuthorURL = feed['entries'][itemChosen]['authors'][0]['href']
    feedURL = feed['entries'][itemChosen]['link']
    feedTitle = feed['entries'][itemChosen]['title']

    print(feedTitle)
    print('posted by: %s (%s)' % (feedAuthor,feedAuthorURL))
    print('post url: %s' % feedURL)
    print('\n')
    print(replacement)
feed()



