"""
################################################################
Name: Scraper_html_maker.py

Author: Yang Wang

Email: wangyang19901026@gmail.com

Version: 1.0

Function: making the copy of the results in current page

Last updated date: 9-23-2014 20:30

Last updated content:

                    <1> if found same file name, check whether

                    overwrite
                    
################################################################
"""
import Scraper_result

import os

import time

# templete suffix added when encountering the same file name
TEMPLETE = "_1"

class htmlMaker:

    def __init__(self):

        return


    def make(self, path, results):

        if not path or len(results) < 1:

            return
        
        while os.path.exists(path):

            over_write = raw_input("Overwrite the existed copy? y/n.\n")

            while over_write != 'y' and over_write != 'n':

                over_write = raw_input("Overwrite the existed copy? y/n.\n")

            if over_write == "y":

                break

            else:

                path = path.replace(".html", TEMPLETE + ".html")

        current_number = len(results)

        handler = open(path, 'w+')

        handler.write("<!DOCTYPE html>" + "\n")

        handler.write("<html>" + "\n")

        handler.write("<head>" + "\n")

        html_title = "Walmart Keyword Search Report"

        handler.write("<h1><a id=\"C\"><center>" + html_title + "</center></a></h1>" + "\n")

        handler.write("</head>" + "\n")

        handler.write("<body>" + "\n")

        str_date = time.strftime ("%m_%d_%Y")

        handler.write("<p><b>Time: </b>" + str_date + "</p>" + "\n")

        handler.write("<p><b>Keyword: </b>" + results[0].getKeyword() + "</p>" + "\n")

        handler.write("<p><b>Selected Page: </b>" + results[0].getPage() + "</p>" + "\n")

        handler.write("<p><b>The Result Number of Selected Page: </b>" + str(current_number) + "</p>" + "\n")

        handler.write("<table border=\"4\">" + "\n")

        handler.write("<tr>" + "\n")

        handler.write("<td width=\"2%\"><center><b>No#</b></center></td>" + "\n")
    
        handler.write("<td width=\"5%\"><center><b>Product Name</b></center></td>" + "\n")
    
        handler.write("<td width=\"5%\"><center><b>Price</b></center></td>" + "\n")

        handler.write("</tr>" + "\n")

        for index in xrange(len(results)):

            handler.write("<tr>" + "\n")

            handler.write("<td>" + str(index + 1) + "</td>" + "\n")

            handler.write("<td>" + results[index].getTitle() + "</td>" + "\n")

            handler.write("<td>" + results[index].getPrice() + "</td>" + "\n")

            handler.write("</tr>" + "\n")

        handler.write("</table>" + "\n")

        handler.write('<p><a href=\"#C\">Back To Top</a></p>' + '\n')

        handler.write("</body>" + "\n")

        handler.write("</html>" + "\n")

        handler.close()

        print "The html copy is ready for the following path: "

        print path

        print ""

        

            
    

    

    
            

            

            

            
