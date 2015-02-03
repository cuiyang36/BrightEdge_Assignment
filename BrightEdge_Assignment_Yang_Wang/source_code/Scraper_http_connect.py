
"""
################################################################
Name: Scraper_http_connect.py

Author: Yang Wang

Email: wangyang19901026@gmail.com

Version: 1.0

Function: send http request to server and handle response

Last updated date: 9-23-2014 20:30

Last updated content:

                    <1> Change response to class parameter
                    
                    <2> Change the connection mode to: 3 times

                    trial
                    
################################################################
"""

import urllib2

import time

# HACK_HEADER to go across the blocking of the request
HACK_HEADER = 'UserAgent#Ruel.ME Walmart Scraper'

# the maximum connection trial times
REQUEST_NUMBER = 3


class httpConnect():

    def __init__(self):

        self.response = None

    # get the response parameter
    def getResponse(self):

        return self.response

    
    def sendRequest(self, url):

        # encapsule a request instance
        req = urllib2.Request(url)

        # split the HACK_HEADER to different parts
        hack_header = HACK_HEADER.split("#")

        # add header to the request instance
        req.add_header(hack_header[0], hack_header[1])

        # first try...
        try_time = 1

        while True:

            print "The " + str(try_time) + " try to connect..."

            if try_time > REQUEST_NUMBER:

                break
            
            try:

                self.response = urllib2.urlopen(req)

                # we successfully get a valid response
                if self.response != None:

                    break

            # handle HTTP exception
            except urllib2.HTTPError, e:

                print 'The server could not fulfill the request.'

                print 'Error code: ', e.code

            # handle url exception
            except urllib2.URLError, e:

                print 'We failed to reach a server.'

                print 'Reason: ', e.reason

            try_time += 1
            
            # sleep for 10 seconds for another trial
            time.sleep(10)

        # we try for three times and finally give up...
        if try_time > REQUEST_NUMBER:

            raise Exception("We could not connect with the server.")

            exit()

        # else, we successfully connect
        print "We have successfully get the response from the server!"

        return

        

            

            

            

            

            
