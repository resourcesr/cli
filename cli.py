from src.parser import Parser
from src.general import get_and_display_data
import ssl

p = Parser()
conn = p.conn()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn.menu("main")
ch = input(" => ")
if ch.lower() == "e" :
    print("\nGoodBye !")
    quit()
try : choice = int(ch)
except : print("Enter Just Numbers !")
if choice == 1 :
    get_and_display_data("computing")
elif choice == 2 :
    get_and_display_data("physics")
elif choice == 3 :
    get_and_display_data("media_sciences")
elif choice == 4 :
    get_and_display_data("management_sciences")
elif choice == 5 :
    get_and_display_data("biomedical_engineering")
elif choice == 6 :
    get_and_display_data("electrical_engineering")
elif choice == 7 :
    get_and_display_data("pharmaceutical_sciences")
elif choice == 8 :
    get_and_display_data("dental_sciences")
elif choice == 9 :
    get_and_display_data("medical_sciences")
elif choice == 10 :
    get_and_display_data("mathematics_statistics")
elif choice == 11 :
    get_and_display_data("public_policy")
elif choice == 12 :
    get_and_display_data("social_science")
elif choice == 13 :
    get_and_display_data("game_design_production")
else :
    print("\nInvalid Input !")
