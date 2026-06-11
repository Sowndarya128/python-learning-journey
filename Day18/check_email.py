import re
email = "test@gmail.com"
if re.search("@",email):
    print("Valid")
else:
    print("Invalid")