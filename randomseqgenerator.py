###################################################################
##Richard Jansen, HAN University of Applied sciences, 14-03-2015###
##Application to randomize FASTA formatted sequences.           ###
##  OPEN FILE WINDOW MIGHT OPEN IN THE BACKGROUND!!!            ###
###################################################################

from tkinter import *
from tkinter import filedialog
import random
niets=Tk()
file = filedialog.askopenfile()
niets.destroy()
niets.mainloop()

raw_data = ""
startReading = False
for regel in file:
    if startReading:
        raw_data += regel[10:]
    if ">" in regel:
        startReading = True
sequence = raw_data.replace(' ','').replace('\n','').replace('\r','')

y = len(sequence)
d =[random.choice(sequence) for x in range(y)]
s = "".join(d)
print (s)