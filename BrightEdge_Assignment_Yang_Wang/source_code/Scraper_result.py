"""
################################################################
Name: Scraper_result.py

Author: Yang Wang

Email: wangyang19901026@gmail.com

Version: 1.0

Function: the result class for providing item information

Last updated date: 9-23-2014 20:30

Last updated content:

                    <1> add keyword and page paras as class paras
                    
################################################################
"""

class result:

    def __init__(self):

        self.keyword = None

        self.page = None

        self.title = None

        self.price = None


    # output the important info of result object
    def toString(self):

        product_title = "Product Name: "

        product_price = "Price: "

        if self.keyword != None:

            product_title += self.title

        if self.price != None:

            product_price += self.price

        return product_title + "\n" + product_price + "\n"
        
        

    # set the value of keyword para
    def setKeyword(self, keyword):

        self.keyword = keyword


    # set the value of page para
    def setPage(self, page):

        self.page = page


    # set the value of title para
    def setTitle(self, title):

        self.title = title


    # set the value of price para
    def setPrice(self, price):

        self.price = price


    # get the value of keyword para
    def getKeyword(self):

        return self.keyword


    # get the value of page para
    def getPage(self):

        return self.page


    # get the value of title para
    def getTitle(self):

        return self.title


    # get the value of price para
    def getPrice(self):

        return self.price

    
            

            

            

            
