# TwitterBot
Keep an eye on specific keywords being posted on Twitter

Ever wondered if you would like to keep an eye on a specific keyword on twitter, eg. "bug bounty" if you would like to be updated with latest bug bounty program updates coming in, or "apt" to keep an eye on upcoming threats with help of data visualization.

Congrats, you have landed safely at the right spot. 

This program lets you define a specific keyword and allows you to:
1. see the updates on console itself.
2. Send an email to a specific email id.
3. Dump the data into elasticsearch.

## Usage: tweepyStreaming.py [options]

Options:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword=KEYWORD
                        What do you want to check, sire?
  -m MAIL, --mail=MAIL  Give your gmail emaild. 
  -e ELASTDETAILS, --elastdetails=ELASTDETAILS
                        Details of Elasticsearch instance, eg. ip_address:port

## Dependencies:
Tweepy library [https://github.com/tweepy/tweepy]<br>
Elasticsearch Library [https://pypi.python.org/pypi/elasticsearch] <br>
Optparse Library [https://docs.python.org/2/library/optparse.html] <br>
Smtplib Library [https://docs.python.org/2/library/smtplib.html]
