import random
from tkinter import *
import tkinter as tk
import winsound



def replace_example(event=None):
    global replaces
    replaces += 1
    title__replace.set(f"Смен:  {replaces}")
    example()

def example():
    global answer
    event = random.choice(["Сложение","Вычитание","Умножение","Найти X","Возвести в квадрат","Сравнение","Угадай знак","Модуль числа","Округли число"])
    title__name.set(event)
    a,b = random.randint(1,250),random.randint(1,250)
    
    if event == "Сложение":
        answer = a + b
        sign = "+" 
    elif event =="Вычитание":
        answer = a - b
        sign = "-"
    elif event == "Умножение":
        a,b = random.randint(1,15),random.randint(1,15)
        answer = a * b
        sign = "*"
    elif event == "Найти X":
        answer,b = random.randint(-25,50),random.randint(1,50)
        title__exp.set((f"{b} * x = {answer * b}"))
        return
    elif event == "Возвести в квадрат":
        a = random.randint(1,100)
        answer = a**2
        title__exp.set(f"{a}²")
        return
    elif event == "Сравнение":
        a,b = random.randint(-1000,1000),random.randint(-1000,1000)
        event += " (<,>,=)"
        sign = " ? "
        if a > b:
            answer = ">"
        elif a < b:
            answer = "<"
        else:
            answer = "="
    elif event == "Угадай знак":
        a = random.randint(-200,200)
        b = random.choice([x for x in range(-200, 201) if x != 0])
        answer = random.choice(["*","+","-","/"])
        if answer == "*":
            c = a * b
        elif answer == "+":
            c = a + b
        elif answer == "-":
            c = a - b
        else:
            c = round(a / b, 2)
        title__exp.set(f"{a} ? {b} = {c}")
        title__name.set(f"{event} ( + - * / )")
        return
    elif event == "Модуль числа":
        a,b = random.randint(-100,50),random.randint(-100,50) 
        answer = abs(a - b)
        title__exp.set(f"| {a} - {b} |")
        return
    elif event == "Округли число":
        a = round(random.uniform(1,100),2)
        answer = int(round(a,0))
        title__exp.set(f"{a}")
        return  

    title__exp.set((f"{a} {sign} {b}"))
    return 

def answer_check(event=None): 
    global true_answ, false_answ
    user_input = answerInput.get().strip()
    
    if user_input != "":
        if user_input == str(answer):
            example()
            true_answ += 1 
            title__true.set(f"Правильно: {true_answ}")
            winsound.PlaySound("SystemDefault", winsound.SND_ASYNC | winsound.SND_ALIAS)
            answerInput.configure(bg="#7CFC00", fg="#000000")
        else:
            false_answ += 1
            title__false.set(f"Неправильно: {false_answ}")
            winsound.PlaySound("SystemHand", winsound.SND_ASYNC | winsound.SND_ALIAS)
            answerInput.configure(bg="#FF0000")

        windows.after(300, lambda: answerInput.configure(bg=block_bg))
        
        total_answers = false_answ + true_answ
        correct_pct = round((true_answ / total_answers) * 100, 2)
        wrong_pct = round((false_answ / total_answers) * 100, 2)
        title__stat_R_F.set(f"{correct_pct}% / {wrong_pct}%")

        answerInput.delete(0, END)
    else:
        winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC | winsound.SND_ALIAS)

fond = "#000000"            
block_bg = "#121212"        
text_main = "#FFFFFF"        
text_accent = "#F472B6"      
btn_color = "#1F2937"       
btn_text = "#FFFFFF"        

replaces = 0
false_answ = 0
true_answ = 0

title__name = tk.StringVar() 
title__exp = tk.StringVar()
title__true = tk.StringVar()
title__false = tk.StringVar()
title__stat_R_F = tk.StringVar()
title__replace = tk.StringVar()

title__stat_R_F.set("0%  /  0%")
title__false.set("Неправильно: 0")
title__true.set("Правильно: 0")
title__replace.set("Смен: 0")

windows = Tk()
windows["bg"] = fond
windows.resizable(width=False, height=False)
windows.geometry("325x375")
windows.title("Примеры")

frame_func = Frame(windows, width=1, height=1, bg=fond)
frame_func.place(relx=0.1, rely=0.15, relheight=0.7, relwidth=0.5)

frame_stat = Frame(windows, width=1, height=1, bg=fond)
frame_stat.place(rely=0.15, relx=0.65, relheight=0.7, relwidth=0.75)

answerInput = Entry(frame_func, bg=block_bg, fg=text_main, insertbackground="white", relief="solid", borderwidth=1)
answerInput.place(rely=0.6, relheight=0.1, relwidth=0.9)
answerInput.focus() 

btn_return_answer = Button(frame_func, bg=btn_color, fg=btn_text, text="Поменять пример", command=replace_example, relief="flat")
btn_return_answer.place(relx=-0.001, relheight=0.1, relwidth=0.9)

btn_answer_check = Button(frame_func, bg=btn_color, fg=btn_text, text="Проверить ответ", command=answer_check, relief="flat")
btn_answer_check.place(rely=0.125, relheight=0.1, relwidth=0.9)

title1 = Label(frame_stat, fg=text_main, text="СТАТИСТИКА", bg=fond, font=("Arial", 9, "bold"))
title1.place(relx=0.01, relheight=0.06, relwidth=0.45)

title_exp_name = Label(frame_func, fg=text_accent, textvariable=title__name, bg=fond, font=("Arial", 10, "bold"))
title_exp_name.place(rely=0.3, relwidth=0.9)

title_exp = Label(frame_func, fg=text_main, textvariable=title__exp, bg=block_bg, font="bold", relief="solid", padx=3, pady=3, borderwidth=1)
title_exp.place(rely=0.48, relheight=0.1, relwidth=0.9)

title_answer_stat = Label(frame_stat, bg=fond, fg=text_main, textvariable=title__true, padx=3, pady=3)
title_answer_stat.place(rely=0.1, relheight=0.07, relwidth=0.4)

title_falseanswer_stat = Label(frame_stat, bg=fond, textvariable=title__false, fg=text_main, padx=3, pady=3)
title_falseanswer_stat.place(rely=0.2, relheight=0.07, relwidth=0.45)

title2_stat = Label(frame_stat, bg=fond, fg=text_main, text="Прав. / Неправ.", padx=3, pady=3)
title2_stat.place(rely=0.45, relheight=0.08, relwidth=0.48)

title_stat_t_f = Label(frame_stat, bg=fond, fg=text_main, textvariable=title__stat_R_F, padx=3, pady=3)
title_stat_t_f.place(rely=0.55, relheight=0.08, relwidth=0.4)

title_replace = Label(frame_stat, bg=fond, fg=text_main, textvariable=title__replace, padx=3, pady=3)
title_replace.place(rely=0.3, relheight=0.08, relwidth=0.3)

example()

windows.bind('<Return>', lambda event: answer_check())
windows.bind("<Escape>", lambda event: replace_example())

windows.mainloop()
