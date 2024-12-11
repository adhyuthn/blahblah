import random
import datetime

fd = open("README.txt", "a")
text = "## NEW " + str(datetime.datetime.now())
fd.write(text)
fd.close()
