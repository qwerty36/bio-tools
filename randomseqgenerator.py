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