from tkinter import *
from tkinter import filedialog
import sys, os

def main():   
    root = Tk()
    program_directory = sys.path[0]
    root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "gff.gif")))
    root.title("GFF v0.50 Beta")
    root.geometry("800x420")    
    app = Application(root)
    root.mainloop()
        
class Application(Frame): 
 
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()  
        
    def create_widgets(self):
     
        image1 = PhotoImage(file="background.gif")
        self.label4 = Label(self, image=image1)  
        self.label4.image = image1
        self.label4.grid(row = 1, column = 0, columnspan = 20, rowspan = 6)
              
        self.bttn1 = Button(self, text = "Open file", bg = '#4b599d', command = self.openfile, width = 21)
        self.bttn1.grid(sticky=N+S+E+W, row = 0, column = 0)
        
        self.bttn2 = Button(self, text = "Run formatter", state = DISABLED, bg = '#4b599d', command = self.formatter, width = 21)
        self.bttn2.grid(sticky=N+S+E+W, row = 0, column = 1)

        self.bttn3 = Button(self, text = "Show headers", state = DISABLED, bg = '#4b599d', command = self.results, width = 22)
        self.bttn3.grid(sticky=N+S+E+W, row = 0, column = 2) 
        
        self.bttn4 = Button(self, text = "Write file", state = DISABLED, bg = '#4b599d', command = self.getname, width = 22)
        self.bttn4.grid(sticky=N+S+E+W, row = 0, column = 3)
        
        self.label3 = Label(self, text = "Sequence:")  
        self.label3.grid(row = 1, column = 0, sticky=N+W)
        
        self.output3 = StringVar()
        self.output_label = Label(self, textvariable = self.output3)   
        self.output_label.grid(row = 1, column = 1, columnspan = 5, rowspan = 4, sticky=N+W)
    
        self.label2 = Label(self, text = "Header:")  
        self.label2.grid(row = 3, column = 0, columnspan = 5, rowspan = 4, sticky=N+W)
        
        self.output1 = StringVar()
        self.output_label = Label(self, textvariable = self.output1)   
        self.output_label.grid(row = 3, column = 1, columnspan = 5, rowspan = 4, sticky=N+W)

    def openfile(self):
        self.file = filedialog.askopenfile() 
        self.bttn2.config(state="normal")
        return self.file
        
    def results(self):
        self.output1.set(self.hdata)
        
    def formatter(self):
        file = self.file
        self.data, self.hdata, self.sdata, raw_data = '', '', '', ''
        for line in file:        
            if '>' in line:
                self.data += '\n' + line
                self.hdata += line + '\n' 
                self.sdata += '\n'
                pass
            else:
                raw_data += line          
                seq = raw_data.replace(' ','').replace('\n','').replace('\r','')
                self.data += seq
                self.sdata += seq
                raw_data = ''
        file.close() 
        self.data = self.data[1:]
        self.bttn3.config(state="normal")
        self.bttn4.config(state="normal")
        self.bttn2.config(state="disabled")
        self.identity()
        return self.data, self.hdata

    def identity(self):
        dna, prot, tstring = None, None, ''
        for line in self.sdata.splitlines():
            for char in line:
                if char.upper() in ('R','H','K','D','E','S','T','N','Q','C','G','P','A','V','I','L','M','F','Y','W'):
                    prot = True
                elif char.upper not in ('R','H','K','D','E','S','T','N','Q','C','G','P','A','V','I','L','M','F','Y','W'):
                    prot = False
                    pass
            for char in line:
                if char.lower() in ('a','t','c','g'):
                    dna = True
                elif char.lower() not in ('a','t','c','g'):
                    dna = False
                    pass
            if dna is True and prot is False:
                tstring += 'DNA sequence\n'
            elif prot is True and dna is False:
                tstring += 'Protein sequence\n'
            elif prot is False and dna is False:
                tstring += 'Foreign characters in sequence\n'
        self.output3.set(tstring)
        
    def getname(self):
        toplevel = Toplevel()

        self.label1 = Label(toplevel, text = "File name:")  
        self.label1.grid(row = 0, column = 0, sticky = W)

        self.input1 = Entry(toplevel)        
        self.input1.grid(row = 0, column = 1, sticky = W+E)
        
        self.bttn5 = Button(toplevel, text = "Commit", bg = '#4b599d', command = self.commit)
        self.bttn5.grid(row = 1, column = 0, sticky = W)

        self.bttn6 = Button(toplevel, text = "Close Window", bg = '#4b599d', command = toplevel.destroy)
        self.bttn6.grid(row = 1, column = 1, sticky = W+E)

        self.output2 = StringVar()
        self.output_label = Label(toplevel, textvariable = self.output2)   
        self.output_label.grid(row = 2, column = 0, columnspan = 2, sticky = W+E)
        
    def commit(self):
        with open(os.path.join(os.expanduser('~'),'Documents', self.input1.get()), mode='w') as newfile:   
            newfile.write(self.data)
            self.output2.set('Succes!')        
        newfile.close()

if __name__ == '__main__':
    main()        