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
        if len(links) != 0 :
            return links
        else :
            return "none"

    @staticmethod
    def get_faculty(html):
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
        
        if len(members) != 0:
            return members
        else :
            return "none"

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
        if len(data) != 0 :
            return data
        else :
            return "none"

    @staticmethod
    def get_input() :
        '''
        Gets Inout from user and returns Answer
        Args:
            None
        Returns:
            output: Output
        Raises:
            None.
        '''
        output = input(" => ")
        return output

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
            print("\n- 1\tFaculty of Computing\n- 2\tPhysics\n- 3\tMedia Sciences\n- 4\tManagement Sciences\n- 5\tBiomedical Engineering\n- 6\tElectrical Engineering\n- 7\tPharmaceutical Sciences\n- 8\tDental Sciences\n- 9\tMedical Sciences\n- 10\tMathematics Statistics\n- 11\tPublic Policy\n- 12\tSocial Science\n- 13\tGame Design Production\n- E \tExit.")

        elif para == "second" :
            print("-----------------------------\nChoose an Option from Below :\n-----------------------------")
            print("\n- P\tPrograms\n- F\tFaculty Members\n- C\tContact\n- E \tExit.")
