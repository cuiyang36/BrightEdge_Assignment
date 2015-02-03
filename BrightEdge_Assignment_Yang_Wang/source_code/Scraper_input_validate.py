
"""
################################################################
Name: Scraper_input_validate.py

Author: Yang Wang

Email: wangyang19901026@gmail.com

Version: 1.0

Function: validate the input and parse to different conditions

Last updated date: 9-23-2014 20:30

Last updated content:

                    <1> Fix the magic number of mode
                    
                    <2> Handle exception in check function

                    instead of in *_main script

                    <3> Can return back class parameters to

                    *_main script
                    
################################################################
"""

import urllib

# global variables
SMALLEST_INPUT_NUMBER = 2

LARGEST_INPUT_NUMBER = 3

FIRST_MODE = 1

SECOND_MODE = 2


class validater():

    
    # constructor for validater class
    def __init__(self):

        self.keyword = None

        self.page = None

        self.url = None

        self.mode = None


    # get the keyword parameter
    def getKeyword(self):

        return self.keyword


    # get the page parameter
    def getPage(self):

        return self.page


    # get the url parameter
    def getUrl(self):

        return self.url


    # get the mode parameter
    def getMode(self):

        return self.mode

    
    # judge whether the input page string is a number
    def isNumber(self, num_string):

        if not type(num_string) == str:

            return False

        for char in num_string:

            if not char.isdigit():

                return False

        return True



    # check the input and assign the parameter
    def check(self, argv):

        if argv == None or len(argv) < SMALLEST_INPUT_NUMBER \
                         or len(argv) > LARGEST_INPUT_NUMBER:

            # exception: no input or too many input parameters
            raise Exception("Invalid input!")

            exit()

        # there is only one parameter
        elif len(argv) == SMALLEST_INPUT_NUMBER:

            self.keyword = argv[1]

            self.url = urllib.quote(self.keyword)

            self.mode = FIRST_MODE

        # there are two input parameters
        elif len(argv) == LARGEST_INPUT_NUMBER:

            if not self.isNumber(argv[2]):
                
                # if it's not a number, throw exception
                raise Exception("Invalid input page number!")

                exit()

            else:

                self.page = argv[2]

            self.keyword = argv[1]

            self.url = urllib.quote(self.keyword)

            self.mode = SECOND_MODE

        else:
            
            # unknown error
            raise Exception("Unknown input error!")

            exit()

            

            

            

            
