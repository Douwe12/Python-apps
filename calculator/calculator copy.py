import tkinter as tk
import operator as o
import re
root = tk.Tk()
root.title("budget calculator")                                                              #importing + creating the main window
root.geometry("240x600")




btn1 = tk.Button(root, text = "1", command = lambda : top(1))
btn2 = tk.Button(root, text = "2", command = lambda : top(2))
btn3 = tk.Button(root, text = "3", command = lambda : top(3))
btn4 = tk.Button(root, text = "4", command = lambda : top(4))
btn5 = tk.Button(root, text = "5", command = lambda : top(5))
btn6 = tk.Button(root, text = "6", command = lambda : top(6))
btn7 = tk.Button(root, text = "7", command = lambda : top(7))                                #creating all buttons
btn8 = tk.Button(root, text = "8", command = lambda : top(8))
btn9 = tk.Button(root, text = "9", command = lambda : top(9))
btn0 = tk.Button(root, text = "0", command = lambda : top(0))
btn_delete = tk.Button(root, text = "del", command = lambda : delete())
btn_clear = tk.Button(root, text = "clear", command = lambda : clear())
btn_addittion = tk.Button(root, text = "+", command = lambda : addittion())
btn_equal = tk.Button(root, text = "=", command = lambda : equal())
btn_multiplication = tk.Button(root, text = "x", command = lambda : multiplication())
btn_division = tk.Button(root, text = "/", command = lambda : division())
btn_subtraction = tk.Button(root, text = "-", command = lambda : subtraction())
btn_comma = tk.Button(root, text = ".", command = lambda : comma())

btn_comma.place(x = 30, y = 100, width = 60, height = 60)
btn_multiplication.place(x = 30, y = 400, width = 60, height = 60)
btn_division.place(x = 90, y = 400, width = 60, height= 60)
btn_subtraction.place(x = 150, y = 400, width = 60, height = 60)
btn_equal.place(x = 150, y = 340, width = 60, height = 60)
btn_addittion.place(x = 30, y = 340, width = 60, height = 60)
btn_clear.place(x = 90, y = 100, width = 60, height = 60)
btn_delete.place(x = 150, y = 100, width = 60, height = 60)
btn1.place(x = 30, y = 160, width = 60, height = 60)
btn2.place(x = 90, y = 160, width = 60, height = 60)
btn3.place(x = 150, y = 160, width = 60, height = 60)
btn4.place(x = 30, y = 220, width = 60, height = 60)                                           #all button placement
btn5.place(x = 90, y = 220, width = 60, height = 60)
btn6.place(x = 150, y = 220, width = 60, height = 60)
btn7.place(x = 30, y = 280, width = 60, height = 60)
btn8.place(x = 90, y = 280, width = 60, height = 60)
btn9.place(x = 150, y = 280, width = 60, height = 60)
btn0.place(x = 90, y = 340, width = 60, height = 60)




value = []
current_text = ""                                                                             #starting values for some variables that have to be defined outside a function
queue = []
lbl_max = tk.Label(root, text = "You cannot enter more then 15 digits", bg = "blue")
max_reached = False
current_value = 0
op = []
x = 0
start = 0
values = []
current_string = ""




def top(number):
    global current_text, lbl_top, queue

    lbl_max.place_forget()

    text = number                                                                               #setting variables
    text1 = str(text) 

    if max_reached == False:
        current_text = str(current_text) + str(text)    
        lbl_top = tk.Label(root, text = current_text)
        lbl_top.place(x = -50, y = 30, width = 320, height = 20)                                    #creating and placing the main label

    if "0" in current_text:
        if current_text.index("0") == 0 and len(current_text) > 1:                              #remove the "0" when another digit is entered
            current_text = current_text.replace("0", "")
            lbl_top.config(text = current_text)

    max_char()                                   

    if len(current_text) == 0:                                                                  #makes sure theres a "0" character in current_text
        current_text = "0"

    queue.append(text1)                                                                         #keeping the queue up to date for clear
    print(queue)





def clear():
    global current_text, queue, value, op

    current_text = ""                                                                           #resetting the text to 0
    max_char()
    top(0)
    value = []
    queue = []                                                                                  #clearing lists
    op = []



def delete():
    global current_text, queue

    if len(current_text) <= 1:
        current_text = "0"
        lbl_top.config(text = current_text)

    if current_text != "0" and len(current_text) > 1:
        current_text = current_text[:-1]                                                        #the standard del function
        lbl_top.config(text = current_text)

    max_char()

    if queue == True:
        queue.pop()                                                                              #updating queue
        print(queue)

    if len(queue) == 1:                                                                         #if you delete the last character the value goes back to 0(Doesnt work atm)
        top(0)
    


    

#groetjes steven ;)  


character = False


def equal():
    global current_text, value, op, x, current_string, values
    
    answer = 0

    if current_text[-1] == "+" or current_text[-1] == "-" or current_text == "*" or current_text == "/":
        return
    
    else:
        current_value = [index for index, char in enumerate(current_text) if char == "-" and "+" and "*" and "*"]
        searching = None
        operators = ["*", "/", "+", "-"]
        for operator in operators:
            if operator in reversed(current_text):
                searching = operator
                break


        last = len(current_text[current_text.rfind(searching) + 1:])
        count = current_text.count("-") + current_text.count("+") + current_text.count("*") + current_text.count("/")
        once = False
        first = False
        print(last)

        
        for index, items in enumerate(current_text):                                                        #start for loop to loop adding value's to values

            
            if index == 0:
                for item in current_text:
                    if item == "-" or item == "*" or item == "/" or item == "+":                            #adds all the numbers before the first "-" to values
                        values.append(current_string)
                        current_string = ""
                        count1 = 1
                        break
                    else:
                        current_string = current_string + item

            
            elif once == True :                                                                              #breaks if the last set of value's has been added to values
                break
            elif once == True and first == True:
                break
            
            
            elif count == count1:
                    for item in reversed(current_text):
                        if item == "-" or item == "*" or item == "/" or item == "+":                        #adds all the numbers after the last "-" to values
                            values.append(current_string)
                            current_string = ""
                            once = True
                            break
                        else:
                            current_string = current_string + item
            
            
            else:
                end = current_text.rfind(searching)  #searching is incorrect
                start = current_text.find(searching) + 1
                if start - end == 0:
                    current_string = current_string + str(end)
                    values.append(current_string)
                    current_string = ""
                    count1 = count1 + 1
                else:
                    if first == False:
                        for item in current_text[start:] + "*":
                            if item == "-" or item == "*" or item == "/" or item == "+":                    #add everything in between the first and last
                                values.append(current_string)
                                current_string = ""
                                count1 = count1 + 1
                                if current_text.count("+") + current_text.count("/") + current_text.count("*") + current_text.count("-") < 2:
                                        first = True
                                break
                            else:
                                current_string = current_string + item




        if "/" in op or "*" in op:
            index_multi = [index_mul for index_mul, value_mul in enumerate(op) if value_mul == "*"]
            index_divis = [index_div for index_div, value_div in enumerate(op) if value_div == "/"]
            print(index_multi)
            print(index_divis)
        else:
            fst = True
            for item in op:
                if fst == True:
                    answer = item(float(values[0]), float(values[1]))
                    values = values[2:]
                    fst = False
                else:
                    answer = item(answer, float(values[0]))
            print(answer)




                

                


    clear()
    lbl_answer = tk.Label(root, text = answer)
    lbl_answer.place(x = 50, y = 50, width = 320, height = 20)
    max_char()




def addittion():
    global current_text, current_value, value

    max_char()

    if current_text[-1] == "-" or current_text[-1] == "+" or current_text[-1] == "*" or current_text[-1] == "/" or len(current_text) < 1:
        return
    else:
        current_text = current_text + "+"
        lbl_top.config(text = current_text)
        op.append(o.add)


def multiplication():
    global current_text, current_value, value

    max_char()

    if current_text[-1] == "-" or current_text[-1] == "+" or current_text[-1] == "*" or current_text[-1] == "/" or len(current_text) < 1:
        return
    else:
        current_text = current_text + "*"
        lbl_top.config(text = current_text)
        op.append(o.mul)




def division():
    global current_text, current_value, value

    max_char()

    if current_text[-1] == "-" or current_text[-1] == "+" or current_text[-1] == "*" or current_text[-1] == "/" or len(current_text) < 1:
        return
    else:
        current_text = current_text + "/"
        lbl_top.config(text = current_text)
        op.append(o.truediv)



def subtraction():
    global current_text, current_value, value, start

    max_char()

    if current_text[-1] == "-" or current_text[-1] == "+" or current_text[-1] == "*" or current_text[-1] == "/" or len(current_text) < 1:
        return
    else:
        current_text = current_text + "-"
        lbl_top.config(text = current_text)
        op.append(o.sub)


def max_char():
    global max_reached
    if len(current_text) > 25:
        lbl_max.place(x = -30, y = 0, width = 320, height = 20)
        max_reached = True
    else:
        lbl_max.place_forget()
        max_reached = False



def comma():
    global current_text
    max_char()

    if current_text.find(".") == -1:
        current_text = str(current_text) + "."                                                      #comma placement function
        lbl_top.config(text = current_text)








top(0)       #to start with current_text = "0"
root.mainloop()
