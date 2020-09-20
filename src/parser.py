"""parser.py: General Functions."""
__author__ = "Muhammad Umer Farooq"
__license__ = "GPL-3"
__version__ = "1.0.0"
__administrator__ = "Muhammad Umer Farooq"
__developers__ = ("Muhammad Usman Naeem", "Muhammad Umer Farooq")
__email__ = ("usman.naeem2212@gmail.com", "contact@muhammadumerfarooq.me")
__status__ = "Production"

from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup

class Parser:

    @staticmethod
    def conn():
        '''
        Establishes Connection with class
        Args:
            None
        Returns:
            class
        Raises:
            None.
        '''
        return Parser

    @staticmethod
    def get_html(url) :
        '''
        Gets Html from a webpage
        Args:
            url: url of the page to be opened
        Returns:
            BeautifulSoup version of html parsed from webpage
        Raises:
            None.
        '''
        html = urlopen(Request(url, headers={'User-Agent': 'PYTHON/3.8'})).read().decode()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    @staticmethod
    def get_program(html) :
        '''
        Gets name of programs offered in a course's page html
        Args:
            html: html of the webpage of that course
        Returns:
            List of Programs
        Raises:
            None.
        '''
        links = []
        tags = html('a')
        for tag in tags:
            link = tag.get('href')
            if link != None :
                if link.startswith("/program") :
                    l = link[9:]
                    link = l.split("-")
                    for l in link :
                        try :
                            li = int(l)
                            continue
                        except :
                            if l == link[0] :
                                lin = l.upper()
                                continue
                            lin += " " + l.upper()
                    links.append(lin)
        return(links)

    @staticmethod
    def get_faculty(html) :
        '''
        Gets name of faculty in a program offered in a course's page html
        Args:
            html: html of the webpage of that course
        Returns:
            List of Faculty Members
        Raises:
            None.
        '''
        members = html.find_all('div',{'class':'views-field views-field-field-full-name'})
        return members

    @staticmethod
    def get_contact(html) :
        '''
        Gets contacts of a program from given html
        Args:
            html: html of the webpage of that course
        Returns:
            List of Contact Details
        Raises:
            None.
        '''
        tags = html("p")
        data = []
        for tag in tags :
            x = re.findall("^<p>UAN.*", str(tag))
            for v in x :
                if v != None : data.append(v[3:(len(v)-4)])
            y = re.findall("^<p>Ph.+", str(tag))
            for v in y :
                if v != None : data.append(v[3:(len(v)-4)])
            z = re.findall("^<p><strong>.+", str(tag))
            for v in z :
                if v != None : data.append(v[11:(len(v)-13)])
        return data

    @staticmethod
    def menu(para) :
        '''
        Gets level of menu and Dispays Menu In accordance, returns user's selection
        Args:
            para: Level of Menu
        Returns:
            Choice of User in menu / error (if any)
        Raises:
            None.
        '''
        if para == "main" :
            print("------------------------------\nChoose a Department from Below :\n------------------------------")
            choice = input("\n- FC\tFaculty of Computing\n- P\tPhysics\n- E \tExit.\n  => ")
            if choice.lower() == "fc" :
                return choice.lower()
            elif choice.lower() == "p" :
                return choice.lower()
            elif choice.lower() == "e" :
                print("\nGoodBye.")
                quit()
            else :
                return "error"

        elif para == "second" :
            print("-----------------------------\nChoose an Option from Below :\n-----------------------------")
            choice = input("\n- P\tPrograms\n- F\tFaculty Members\n- C\tContact\n- E \tExit.\n  => ")
            if choice.lower() == "p" :
                return choice.lower()
            elif choice.lower() == "f" :
                return choice.lower()
            elif choice.lower() == "c" :
                return choice.lower()
            elif choice.lower() == "e" :
                quit()
            else :
                return "error"