from tkinter import *
import unittest

def fizzbuzz(num:int):
    if num == 0:
        return str(0)
    elif num %3== 0 and num % 5 ==0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)
    
def fizzbuzzlist():
    textsum = ""
    for i in range(100):
        textsum = textsum + fizzbuzz(i+1) +"\n"
    textfield = Text(myframe)
    textfield.grid(column=1, row=1)
    textfield.config(width=20, height=10)
    scrolltext = Scrollbar(myframe,command = textfield.yview)
    scrolltext.grid(column=2, row=1, sticky='nesw')
    textfield.config(yscrollcommand = scrolltext.set)
    textfield.insert(1.0,textsum)
    textfield.configure(state='disabled')

ventana = Tk()

ventana.title('Application')
ventana.geometry('300x300')
ventana.resizable(False,False)
ventana.config(bg='blue')
myframe = Frame()
myframe.config(width=300, height=300)
myframe.config(bg='blue')
myframe.pack()

buttonfizz= Button(myframe, text="FizzBuzz", command=fizzbuzzlist)
buttonfizz.grid(row=0, column=1,padx=10,pady=10)

ventana.mainloop()



class TestFizzBuzz(unittest.TestCase):
    
    def testfizzbuzzfunction(self):
        self.assertEqual(fizzbuzz(1),str(1))
        self.assertEqual(fizzbuzz(4),str(4))
        self.assertEqual(fizzbuzz(3),'Fizz')
        self.assertEqual(fizzbuzz(5),'Buzz')
        self.assertEqual(fizzbuzz(15),'FizzBuzz')
        self.assertEqual(fizzbuzz(99),'Fizz')
        self.assertEqual(fizzbuzz(100),'Buzz')
        self.assertEqual(fizzbuzz(0),str(0))

if __name__ == '__main__':
    unittest.main()



