from src._config import get_config
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get(url) :          #Gets and parses html from url
    html = urlopen(Request(url, headers={'User-Agent': 'PYTHON/3.8'})).read().decode()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def data(html, what) :            #Gets data from html
    links = []
    tags = html('a')
    for tag in tags:
        link = tag.get('href')
        if link != None :
            if link.startswith(what) :
                l = link[9:]                    #Gets Rid of UseLess Data (line 22 - 32)
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

def menu(para):             #Displays Menu
    if para == "main" :
        print("------------------------------\nChoose a Department from Below :\n------------------------------")
        choice = input("\n- FC\tFaculty of Computing\n- P\tPhysics\n- E \tExit.\n  => ")
        if choice.lower() == "fc" :
            return choice.lower()
        elif choice.lower() == "p" :
            return choice.lower()
        elif choice.lower() == "e" :
            quit()
        else :
            print("Invalid Input ! Try Again\n")
            menu("main")
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
            print("Invalid Input ! Try Again\n")
            menu("second")

choice = menu("main")
if choice == "fc" :
    url = "https://www.riphah.edu.pk/faculty/ict-computing/programs" #get_config("computing_url")
    html = get(url)

    print("\nOffered Programs :")
    p = data(html, "/program")
    for programs in p :
        print(programs)

    print("\nFaculty Members :")
    html = get("https://www.riphah.edu.pk/faculty/ict-computing/faculty-members")
    print(html.find('div',{'class':'views-field views-field-field-full-name'}).text) #gets field-content    -    This line just gets first one, Umer please solve this issue

    '''
                Above Taken from Following Example :
        source_code = <span class="UserName"><a href="#">Martin Elias</a></span>
        soup = BeautifulSoup(source_code)
        print soup.find('span',{'class':'UserName'}).text
    '''



elif choice == "p" :
    url = "https://www.riphah.edu.pk/faculty/ict-physics/programs" #get_config("physics_url")
    html = get(url)

    print("\nOffered Programs :")
    p = data(html, "/program")
    for programs in p :
        print(programs)

    print("\nFaculty Members :")
    html = get("https://www.riphah.edu.pk/faculty/ict-computing/faculty-members")
    print(html.find('div',{'class':'views-field views-field-field-full-name'}).text) #gets field-content    -    This line just gets first one, Umer please solve this issue


#choice = menu("second")
#if choice == "p" :
#    data(html, "/program")
#if choice == "f" :
#    data(html, "/faculty-member")
#if choice == "c" :
#    data(html, "/contact")
