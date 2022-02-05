import re
import tkinter as tk

def DisplayStrength(canvas):
    password = textField.get()

    def testPasswordStrength(password):
        

            eightCharsLongRegex = re.compile(r'[\w\d\s\W\D\S]{8,}')
            upperCaseRegex = re.compile(r'[A-Z]+')
            lowerCaseRegex = re.compile(r'[a-z]+')
            oneOrMoreDigitRegex = re.compile(r'\d+')
            SpecialcharecterRegex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not SpecialcharecterRegex.search(password):
                return False
            if not eightCharsLongRegex.search(password):
                return False
            elif not upperCaseRegex.search(password):
                return False
            elif not lowerCaseRegex.search(password):
                return False
            elif not oneOrMoreDigitRegex.search(password):
                return False

            return True
    info = testPasswordStrength(password)
    if info == 0:
        label1.config(text = "False")
    if info == 1:
        label1.config(text = "True")

canvas = tk.Tk()
canvas.geometry("600x300")
canvas.title("Password App")
canvas.configure(bg = 'pink')

f = ("TimesNewRoman", 12, "bold")

textField = tk.Entry(canvas, font = f)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', DisplayStrength)

label1 = tk.Label(canvas, font = f)
label1.pack()
label1.configure(bg = "white")

label2 = tk.Label(canvas, font = f)
label2.config(text = "If strong password, program returns True" + "\n" + "If not, program returns False")
label2.pack()
label2.configure(bg = "white")


canvas.mainloop()   