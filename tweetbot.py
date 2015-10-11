from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import optparse
import json
import smtplib
import sys
from elasticsearch import Elasticsearch
from datetime import datetime
import re

consumer_key="P0RTduLx45x0xQOaFL7N50NYX"
consumer_secret="k6GhrA21iPV0yZIEyx7g8XFQfzMFsaANJZB9HqQRAiubuNZ6LA"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="16852719-jFd88Pues05XSygDLmDirIkIx06qwIOFKVsnXClw6"
access_token_secret="PpDuZrGjF4PY4byiSaJ0pntTpupF5umrQwxfb1TQPWy3q"

#Go to google settings and enable access for less secure apps
senderemail = "upgoingstaaar@gmail.com"
senderpass = "123shubham"

#Pick up the arguments.
parser = optparse.OptionParser()
parser.add_option('-k', '--keyword', action="store", dest="keyword", help="What do you want to check, sire?", default="spam")
parser.add_option('-m', '--mail', action="store", dest="mail", help="Give your gmail userid. ", default="spam")
parser.add_option('-e', '--elastdetails', action="store", dest="elastdetails", help="Details of Elasticsearch instance, eg. ip_address:port", default="spam")
options, args = parser.parse_args()

#all the major action
class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        list_data = json.loads(data)
        #print(list_data)
        tweet = (list_data["text"])
        username = list_data["user"]["screen_name"]
        print('>>' + username + ' posted: ' + tweet)
        msg = "Subject: Twitter Bot for keyword - " + options.keyword.upper() + "\n\nHey Man\nYour Twitter Bot just wanted to send you an update.\n<b>" + username + "</b> just posted a new tweet: \n<i>" + tweet +"</i>"
        if (options.mail != 'spam'):
            p = re.compile("^([0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$")
            m = p.match(options.mail)
            if m:
                mailer(msg.encode('utf8'), options.mail)
            else:
                print('Email ID is wrong. Please enter valid one.')
        list_data['timestamp'] = datetime.now()
        if (options.elastdetails != 'spam'):
            ip = options.elastdetails.split(":")[0]
            port = options.elastdetails.split(":")[1]
            dumpToElastic(list_data, ip, port)
        return True

    def on_error(self, status):
        print(status)

#Code for searching the Twitter streaming api.
def search(xyz):
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=[xyz])

#Code for sending mail.
def mailer(msg, emailid):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senderemail, senderpass)
        server.sendmail(senderemail, emailid, msg)
        server.quit()
        print("[+] Mail sent to concerned authorities.")
    except:
        print("[+] I am sorry, Wasn't able to perform my job well. Code for sending the mail got fucked up.")

#Code for dumping the data into ElasticSearch.
def dumpToElastic(bodydata, ip, port):
    ES_HOST = {'host': ip, 'port': port}
    es = Elasticsearch(hosts = [ES_HOST])
    es.index(index='twitter', doc_type="trial", id = 1, body=bodydata)
    #print(es['created'])

#Program kicks off.
print("----- Twitter bot kicked off ------")
if (options.keyword != 'spam'):
    search(options.keyword)
