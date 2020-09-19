from src.general import general
from src.general import get_and_display_data
import ssl

g = general()
conn = g.conn()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

choice = conn.menu("main")

if choice == "fc" :
    get_and_display_data("computing")

elif choice == "p" :
    get_and_display_data("physics")
