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
import firebase_admin
import os
from firebase_admin import credentials, firestore


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

    def get_faculty(html, para) :
        '''
        Gets name of faculty in a program offered in a course's page html
        Args:
            html: html of the webpage of that course
            para: Parameter
        Returns:
            List of Faculty Members
        Raises:
            None.
        '''
        if para == "username" :
            usernames = {}
            tags = html('a')
            i = 0
            for tag in tags:
                username = tag.get('href')
                if username != None :
                    if username.startswith("https://www.riphah.edu.pk/users") :
                        i += 1
                        usernames.update( {str(i) : str(username[31:])} )
            return usernames
        if para == "name" :
            usernames = {}
            Name = html.findAll("div", {"class" : "views-field views-field-field-full-name"})
            i = 0
            for n in Name:
                i += 1
                tags = n('div')
                for tag in tags:
                    result = re.split(">", str(tag))
                    name = str(result[2])[:(len(str(result[2])))-3]
                    usernames.update( {str(i) : name} )
            return usernames

    def faculty_details(self, username, url):
        '''
        Returns Details of Faculty members from website
        Args:
            username = usernames of faculty-members
            url = base url of website
        Returns:
            Dictionary
        Raises:
            None.
        '''
        data = {}
        url += username
        html = self.get_html(url)
        tags = html('img')
        for tag in tags:
            link = tag.get('src')
            if link != None :
                if link.startswith("https://www.riphah.edu.pk/sites/default/files/styles/photo_gallery_front_210x210_/public/pictures") :
                    image = str(link)
        name_temp = str(html.find("div", {"class":"personal_info_full_name"}))
        name = name_temp[37:(len(name_temp)-6)]
        data.update( {"name" : str(name)} )
        designation_temp = str(html.find("div", {"class":"personal_info_desig_title"}))
        designation = designation_temp[39:(len(designation_temp)-6)]
        data.update( {"designation" : str(designation)} )
        level_temp = str(html.find("div", {"class":"personal_info_level_edu"}))
        level = level_temp[37:(len(level_temp)-6)]
        data.update( {"level" : str(level)} )
        #email_temp = str(html.find("div", {"class" : "personal_info_email"}))
        email = ""  #email_temp[42:(len(email_temp)-26)]
        data.update( {"email" : str(email)} )
        return (json.dumps(data, indent=2))

    @staticmethod
    def decode(string):
        # Todo
        return string
>>>>>>> d9111015a5ef0431024878c5b6888a0ccd687a93

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
        Gets level of menu and Dispays Menu In accordance
        Args:
            para: Level of Menu
        Returns:
            None
        Raises:
            None.
        '''
        if para == "main" :
            print("------------------------------\nChoose a Department from Below :\n------------------------------")
            print("\n- 1\tFaculty of Computing\n- 2\tPhysics\n- 3\tMedia Sciences\n- 4\tManagement Sciences\n- 5\tBiomedical Engineering\n- 6\tElectrical Engineering\n- 7\tPharmaceutical Sciences\n- 8\tDental Sciences\n- 9\tMedical Sciences\n- 10\tMathematics Statistics\n- 11\tPublic Policy\n- 12\tSocial Science\n- 13\tGame Design Production\n- E \tExit.")

        elif para == "second" :
            print("-----------------------------\nChoose an Option from Below :\n-----------------------------")
            print("\n- P\tPrograms\n- F\tFaculty Members\n- C\tContact\n- E \tExit.")

    @staticmethod
    def initialize_firebase() :
        '''
        Initializes firebase sdk and firestore instance
        Args:
            None
        Returns:
            None
        Raises:
            None.
        '''
        cred = credentials.Certificate("apps.json")
        firebase_admin.initialize_app(cred)

    @staticmethod
    def write_on_firebase(department, attribute, data) :
        '''
        Writes data on firebase
        Args:
            program: (Name of Collection) program that user wants to see data of
            attribute: (Name of Document) Programs / Faculty-Members / Contact
            data: Dictionary of data to insert in firebase
        Returns:
            None
        Raises:
            None.
        '''
        firestore_db = firestore.client()
        firestore_db.collection(department).document(attribute).set(data)


    @staticmethod
    def read_from_firebase(program, attribute) :
        '''
        Reads data from firebase
        Args:
            program: (Name of Collection) program that user wants to see data of
            attribute: (Name of Document) Programs / Faculty-Members / Contact
        Returns:
            List of data file from firebase
        Raises:
            None.
        '''
        dat = list()
        firestore_db = firestore.client()
        data = firestore_db.collection(program).document(attribute).get().to_dict()
        if data == None :
            return dat
        for i in sorted (data) :
            dat.append(str(data[i]))
        return dat

    @staticmethod
    def create_folder(name, path) :
        '''
        Creates a folder in given path of given name
        Args:
            name: name of folder
            path: path where folder is to be created
        Returns:
            None
        Raises:
            None.
        '''
        path = os.path.join(path, name)
        try : os.mkdir(path)
        except : return

    @staticmethod
    def file_exists(file) :
        '''
        Checks if file exists
        Args:
            file: location / filename
        Returns:
            Bool: True/False
        Raises:
            None.
        '''
        try :
            my_file = open(file)
            my_file.close()
            return True
        except :
            return False
