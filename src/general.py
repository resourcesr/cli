"""general.py: General Functions."""
__author__ = "Muhammad Umer Farooq"
__license__ = "GPL-3"
__version__ = "1.0.0"
__administrator__ = "Muhammad Umer Farooq"
__developers__ = ("Muhammad Usman Naeem", "Muhammad Umer Farooq")
__email__ = ("usman.naeem2212@gmail.com", "contact@muhammadumerfarooq.me")
__status__ = "Production"

from src.parser import Parser
from src._config import get_config

p = Parser()
conn = p.conn()

def get_and_display_data(program) :
    '''
    Gets data from respective website of the program user wishes to see data of and Displays it
    Args:
        program: Program user wishes to see data of
    Returns:
        Nothing (Displays data)
    Raises:
        None.
    '''
    u = program + "_url"
    url = get_config(u) + "/programs"
    try : html = conn.get_html(url)
    except : print("No Data On Website")
    print("\nOffered Programs :")
    p = conn.get_program(html)
    if p == "none" :
        print("No Programs")
    else :
        for programs in p :
            print(programs)

    print("\nFaculty Members :")
    u = program + "_url"
    url = get_config(u) + "/faculty-members"
    try : html = conn.get_html(url)
    except : print("No Data On Website")
    members = conn.get_faculty(html)
    if members == "none" :
        print("No Members.")
    else :
        for name in members:
            print(name.text)

    print("\nContact :")
    u = program + "_url"
    url = get_config(u) + "/contact"
    try : html = conn.get_html(url)
    except : print("No Data On Website")
    contacts = conn.get_contact(html)
    if contacts == "none" :
        print("No Contacts.")
    else :
        for contact in contacts :
            print(contact)
