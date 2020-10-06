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
import json
import os

conn = Parser()

def get_and_display_data(program) :
    '''
    Checks if data is in Firebase If it finds it, It displays that data,
    Otherwise Gets data from respective website of the program user wishes to see data of, Displays it and updates the firebase.
    Args:
        program: Program user wishes to see data of
    Returns:
        Nothing (Displays data)
    Raises:
        None.
    '''
    conn.initialize_firebase()

    data = dict()
    programs = conn.read_from_firebase(program, "Programs")
    if len(programs) == 0 :
        print("\nOffered Programs :")
        u = program + "_url"
        url = get_config(u) + "/programs"
        try : html = conn.get_html(url)
        except : print("No Data On Website")
        p = conn.get_program(html)
        if p == "none" :
            print("No Programs")
            data.clear()
            data.update( {"1" : "No Programs"} )
        else :
            data.clear()
            i = 0
            for programs in p :
                i += 1
                data.update( {str(i):programs} )
                print(programs)

        conn.write_on_firebase(program, "Programs", data)
        print("\nUpdated Data on Firebase.")
    else :
        print("\nOffered Programs :")
        for p in programs :
            print(p)


    fMember = conn.read_from_firebase(program, "Faculty Members")
    faculties = {}
    i = 0
    for m in fMember :
        i += 1
        faculties.update( {str(i) : m} )
    if len(faculties) == 0 :
        print("\nFaculty Members :")
        u = program + "_url"
        url = get_config(u) + "/faculty-members"
        try : html = conn.get_html(url)
        except : print("No Data On Website")
        members = conn.get_faculty(html, "name")
        faculties = members.values()
        if faculties == "none" :
            print("No Members.")
            data.clear()
            data.update( {"1" : "No Faculty Members"} )
        for faculty in faculties:
            print(faculty)
        conn.write_on_firebase(program, "Faculty Members", data)
        print("\nUpdated Data on Firebase.")
    else :
        print("\nFaculty Members :")
        for faculty in faculties.values() :
            print(faculty)

    print("\nGetting Details on files")
    directory = "data"
    conn.create_folder(directory, os.getcwd())
    path = os.path.join(os.getcwd(), directory)
    conn.create_folder(program, path)
    for faculty in faculties.values() :
        faculty = faculty.strip()
        conn.create_folder(faculty, os.path.join(path, program))

    # @lablnet Below Code gets the details of faculty members. I am unable to align usernames with names(of files) for successful file write
    '''
    url_2 = get_config("riphah") + "/users"
    u = program + "_url"
    url = get_config(u) + "/faculty-members"
    try : html_1 = conn.get_html(url)
    except : quit()
    name_2 = conn.get_faculty(html_1, "username")
    list = []
    for n in sorted(name_2.keys()) :
        if name_2[n] not in list : list.append(name_2[n])
        else : continue
        print(name_2[n])
        data = conn.faculty_details(name_2[n], url_2)
        for faculty in sorted(faculties.keys()) :
            if faculties[faculty].strip() not in list : list.append(faculties[faculty].strip())
            else : continue
            print(faculty, faculties[faculty].strip())
            print(n, name_2[n])
            if faculty == n :
                faculty = faculties[faculty].strip()
                print(faculty)
                break
        if True :
            continue
        '''
        p = os.path.join(path, program, faculty)
        File = p + "\\" + faculty + ".json"
        with(open(File, "w")) as file:
            file.write(data)
            print(faculty, ": Written on File")


    contacts = conn.read_from_firebase(program, "Contact")
    if len(contacts) == 0 :
        print("\nContact :")
        u = program + "_url"
        url = get_config(u) + "/contact"
        try : html = conn.get_html(url)
        except : print("No Data On Website")
        contacts = conn.get_contact(html)
        if contacts == "none" :
            print("No Contacts.")
            data.clear()
            data.update( {"1" : "No Contacts"} )
        else :
            data.clear()
            i = 0
            for contact in contacts :
                i += 1
                data.update( {str(i) : str(contact)})
                print(contact)

        conn.write_on_firebase(program, "Contact", data)
        print("\nUpdated Data on Firebase.")
    else :
        print("\nContact :")
        for contact in contacts :
            print(contact)
