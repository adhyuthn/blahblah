import random
import datetime

fd = open("README.md", "a")
text = "## NEW " + str(datetime.datetime.now())
fd.write(text)
fd.close()
