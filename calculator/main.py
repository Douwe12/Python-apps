import tkinter as tk



class BugdetCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("budget calculator")                                                              #importing + creating the main window
        self.geometry("240x600")


        self.current_numbers = [0]
        self.lbl_top = tk.Label(self, text = self.current_numbers)
        self.lbl_top.place(x = -50, y = 30, width = 320, height = 20)    



        self.btn1 = tk.Button(self, text = "1", command = lambda : self.enter_number(1))
        self.btn2 = tk.Button(self, text = "2", command = lambda : self.enter_number(2))
        self.btn3 = tk.Button(self, text = "3", command = lambda : self.enter_number(3))
        self.btn4 = tk.Button(self, text = "4", command = lambda : self.enter_number(4))
        self.btn5 = tk.Button(self, text = "5", command = lambda : self.enter_number(5))
        self.btn6 = tk.Button(self, text = "6", command = lambda : self.enter_number(6))
        self.btn7 = tk.Button(self, text = "7", command = lambda : self.enter_number(7))                                #creating all buttons
        self.btn8 = tk.Button(self, text = "8", command = lambda : self.enter_number(8))
        self.btn9 = tk.Button(self, text = "9", command = lambda : self.enter_number(9))
        self.btn0 = tk.Button(self, text = "0", command = lambda : self.enter_number(0))
        self.btn_delete = tk.Button(self, text = "del")
        self.btn_clear = tk.Button(self, text = "clear")
        self.btn_addittion = tk.Button(self, text = "+")
        self.btn_equal = tk.Button(self, text = "=")
        self.btn_multiplication = tk.Button(self, text = "x")
        self.btn_division = tk.Button(self, text = "/")
        self.btn_subtraction = tk.Button(self, text = "-")
        self.btn_comma = tk.Button(self, text = ".")

        self.btn_comma.place(x = 30, y = 100, width = 60, height = 60)
        self.btn_multiplication.place(x = 30, y = 400, width = 60, height = 60)
        self.btn_division.place(x = 90, y = 400, width = 60, height= 60)
        self.btn_subtraction.place(x = 150, y = 400, width = 60, height = 60)
        self.btn_equal.place(x = 150, y = 340, width = 60, height = 60)
        self.btn_addittion.place(x = 30, y = 340, width = 60, height = 60)
        self.btn_clear.place(x = 90, y = 100, width = 60, height = 60)
        self.btn_delete.place(x = 150, y = 100, width = 60, height = 60)
        self.btn1.place(x = 30, y = 160, width = 60, height = 60)
        self.btn2.place(x = 90, y = 160, width = 60, height = 60)
        self.btn3.place(x = 150, y = 160, width = 60, height = 60)
        self.btn4.place(x = 30, y = 220, width = 60, height = 60)                                           #all button placement
        self.btn5.place(x = 90, y = 220, width = 60, height = 60)
        self.btn6.place(x = 150, y = 220, width = 60, height = 60)
        self.btn7.place(x = 30, y = 280, width = 60, height = 60)
        self.btn8.place(x = 90, y = 280, width = 60, height = 60)
        self.btn9.place(x = 150, y = 280, width = 60, height = 60)
        self.btn0.place(x = 90, y = 340, width = 60, height = 60)

    def display_number(self):
        self.lbl_top.config(text = self.current_numbers)



    def enter_number(self, number):
        print(self.current_numbers)
        if len(self.current_numbers == 1) and self.current_numbers[0] == 0:
            self.current_numbers = [number]
        else:
            self.current_numbers.append(number)
        self.display_number() 





if __name__ == '__main__':
    app = BugdetCalculator()
    app.mainloop()
    print(app.current_numbers)