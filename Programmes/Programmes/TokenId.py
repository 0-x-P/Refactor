from Options.Options import *

import base64

TitrePage("Token Id")

userid = input(f"{couleur.RED}\nVictime ID -> {couleur.RESET}")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n{couleur.RED}Première partie du token: \"{couleur.CYAN}{encodedStr}.{couleur.RED}\"{couleur.RESET}')

input(couleur.RED + "\nFais entrer pour continuer -> " + couleur.RESET)
Reset()