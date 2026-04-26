from pyscript import display, document 



class Classmates: # creating the class
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    
    def line(self):
        return f"Hi! I am {self.name} from {self.section}! My favorite subject is {self.subject}"
    


currentclassmates = [
    Classmates("Calvin", "Topaz", "Math"),
    Classmates("Ashley", "Emerald", "Science"),
    Classmates("Enzo", "Ruby", "P.E"),
    Classmates("Phoebe", "Topaz", "English"),
    Classmates("Vito", "Sapphire", "P.E")
]

Globallist = []

def newclassmate(e):
    document.getElementById('output').innerHTML = ''
    name = document.getElementById('Input1').value
    section = document.getElementById('Select').value
    subject = document.getElementById('Select2').value

    if name and section and subject:
       classmate = Classmates(name, section, subject)
       currentclassmates.append(classmate)

       display(f'{name} has been added to the list', target = 'output')
       
    else:
       display(f'please fill up the form', target = 'output')

def something(e):
    document.getElementById('output').innerHTML = ''

    if currentclassmates:

        for inside in currentclassmates:
            display(inside.line(), target='output')
    if Globallist:
        for inside in Globallist:
            display(inside.line(), target='output')
    

       


