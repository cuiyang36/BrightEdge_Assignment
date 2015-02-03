"""
################################################################
Name: Scraper_main.py

Author: Yang Wang

Email: wangyang19901026@gmail.com

Version: 1.0

Function: main control script

Last updated date: 9-23-2014 20:30

Last updated content:

                    <1> Increase I/O ports for validater class
                    
                    <2> Handle more exception in other classes

                    instead in main script
                    
################################################################
"""
import os

import sys

from Scraper_input_validate import validater

from Scraper_http_connect import httpConnect

from Scraper_parse_worker import parser

from Scraper_result import result

from Scraper_html_maker import htmlMaker

# the webpage header we want to search with
WALMART_HEADER = r"http://www.walmart.com/search/?query="

TMP_DATABASE = r"tmp_database"

# the mode for different inputs
FIRST_MODE = 1

SECOND_MODE = 2


def main(argv):

    
    # set up a validater class for validating input
    vali = validater()

    vali.check(argv)

    mode = vali.getMode()

    url = ""

    # first mode, so only add the *.url para to url
    if mode == FIRST_MODE:

        try: 
            # set the redirect mode to false to prevent redirection
            url = WALMART_HEADER + vali.getUrl() + "&redirect=false"

        except:

            raise Exception("mode and url parameters are not matched!")

            exit()

    # second mode, add the page para to url
    elif mode == SECOND_MODE:

        try:

            page = vali.getPage()

            url = WALMART_HEADER + vali.getUrl() + "&page=" \
                  + page + "&redirect=false"

        except:

            raise Exception("mode and url parameters are not matched!")

            exit()

    else:

        # handle exception, unknown parameter infomation
        raise Exception("Unknown validater return!")

        exit()

    
    # set up a httpConnect class to send url request
    connect = httpConnect()

    connect.sendRequest(url)

    response = connect.getResponse()

    # set up a parser class
    text_parser = parser()

    # output according to the mode request
    if mode == FIRST_MODE:

        text_parser.getParse(mode, response)

        result_number = text_parser.getResultNum()

        print "Number of Results: " + result_number

        return result_number

    else:

        text_parser.setKeyword(vali.getKeyword())

        text_parser.setPage(vali.getPage())

        text_parser.getParse(mode, response)

        result_list = text_parser.getResultList()

        if len(result_list) > 0:

            # print "result_list: " + str(result_list)

            make_docu = raw_input("Make html copy of this page? y/n.\n")
            
            # whether make a html copy of this page?
            while make_docu != 'y' and make_docu != "n":

                make_docu = raw_input("Make html copy of this page? y/n.\n")
                
            # if answer is yes, we make copy under current folder
            if make_docu == 'y':

                curr_path = os.getcwd() + "//" + TMP_DATABASE

                if not os.path.exists(curr_path):

                    os.mkdir(curr_path)

                copy_name = vali.getKeyword() + "#" + vali.getPage() + ".html"

                copy_path = curr_path + "//" + copy_name

                # set up a html maker class
                maker = htmlMaker()

                # make a html format copy in current location
                maker.make(copy_path, result_list)

        print "Number of Results On Selected Page: " + str(len(result_list))
        
        return result_list


if __name__ == "__main__":
    
    main(sys.argv) 
