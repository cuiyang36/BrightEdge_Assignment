"""
################################################################

Name: Scraper_parse_worker.py

Author: Yang Wang

Email: wangyang19901026@gmail.com

Version: 1.0

Function: parser to parse the response for different requires

Last updated date: 9-23-2014 20:30

Last updated content:

                    <1> connect with result class

                    <2> change the response not to be class para
                    
################################################################
"""

import urllib2

import re

from bs4 import BeautifulSoup

from Scraper_result import result


# summary container that contains number of results info
SUMMARY_CLASS = "result-summary-container"

# item container that has all individual product info
ITEM_CLASS = "js-tile tile-landscape"

# price container that has all price info
PRICE_CLASS = "item-price-container"

# title container that has all title info
TITLE_CLASS = "js-product-title"

# different mode according to the request
FIRST_MODE = 1

SECOND_MODE = 2


class parser():

    def __init__(self):

        self.soup = None

        self.result_number = None

        self.curr_result_number = None

        self.result_list = []

        self.keyword = None

        self.page = None


      
    # set the value of keyword para
    def setKeyword(self, keyword):

        self.keyword = keyword



    # set the value of page para
    def setPage(self, page):

        self.page = page


    # get the list of result objects
    def getResultList(self):

        return self.result_list
   

    # get the total number of results
    def getResultNum(self):

        return self.result_number



    # get the value of keyword para
    def getKeyword(self):

        return self.keyword



    # get the value of page para
    def getPage(self):

        return self.page



    # get the value of current page result number
    def getCurrResultNum(self):

        return self.curr_result_number

    
 
    # make soup object according to the input response
    def makeSoup(self, response):

        try:

            self.soup = BeautifulSoup(response)

        except:

            raise Exception("The response is failed to make soup!")

            exit()

        
    # parse out the number of results
    def parseResultNum(self, response):

        # try to make soup object according to the response
        self.makeSoup(response) 

        try:

            summary_tag = self.soup.find_all('div', \
                                             attrs = {'class': SUMMARY_CLASS})

        except:

            raise Exception("The soup is invalid when parsing!")

            exit()

        if summary_tag == None or len(summary_tag) < 1:

            raise Exception("Error, no static about the number of results.")

            exit()

        # there should be at most one summary container in one page
        if len(summary_tag) > 1:

            print "Warning! There exists multiple summary on single page!"

        summary_content = summary_tag[0]

        pattern = re.compile("Showing\s(\d+)\s(of)\s(\d+)\s(results)")

        # search for the matched result
        match = pattern.search(str(summary_content))

        if match:

            self.curr_result_number = match.group(1)

            self.result_number = match.group(3)

            # print "The number of results is: " + str(self.result_number)

            # print "The current page number is: " + str(self.curr_result_number)

        else:

            # we cannot find number of results in the container
            raise Exception("Empty content in summary tag!")

            exit()

        return summary_content
    


    # combine all valid string in the tag content
    def combineString(self, tag_content):

        if tag_content == None:

            return ""

        elif not hasattr(tag_content, "contents"):

            return tag_content.string

        else:

            result = ""

            for element in tag_content.contents:

                result += self.combineString(element)

            return result
                

    # set up a result object
    def makeResultObject(self, title, price):

        new_result = result()

        new_result.setTitle(title)

        new_result.setKeyword(self.keyword)

        new_result.setPage(self.page)

        new_result.setPrice(price)

        return new_result

    

    # get result according to the response with soup method
    def getParse(self, mode, response):

        summary_content = self.parseResultNum(response)

        # if first mode, directly return the number of results
        if mode == FIRST_MODE:

            return

        # if second mode, return number plus result object
        elif mode == SECOND_MODE:

            # if the number of results in this page is 0, directly return
            if self.getCurrResultNum() == 0:

                return
            
            # else, let's traverse, make result object and add to list
            curr = self.soup.find('div', attrs = {'class': ITEM_CLASS})

            # start number
            item_index = 1

            while curr:

                print ""

                print "------------- item " + str(item_index) + \
                      "---------------"

                try:

                    title_tag = curr.find_next('a', \
                                               attrs = {'class': TITLE_CLASS})

                    price_tag = curr.find_next('div', \
                                               attrs = {'class': PRICE_CLASS})

                except:

                    print "A error in title and price parsing process!"

                    title_tag = None

                    price_tag = None

                title = self.combineString(title_tag).strip()

                price = self.combineString(price_tag).strip()

                new_result = self.makeResultObject(title, price)

                self.result_list.append(new_result)

                print new_result.toString()

                curr = curr.find_next('div', attrs = {'class': ITEM_CLASS})

                # continue traversing
                item_index += 1

                print "------------------------------------"

            return

        else:

            raise Exception("Invalid mode!")

            exit()
        

        

        

            

            

            

            

            
