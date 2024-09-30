from tkinter import *
from tkinter import ttk

def out_values(height=0):
    #принимает int рост от пользователя из entry_get(), где идёт обработка введённой информации
    lbl_overup_info['text'] = 'управляемость     <параметр>   стабильность'
    if height in range(155, 160):#логика относительно составленной таблицы рост-длина
        lbl_info_rich['text'] = '20.25"    <ростовка>    20.4"'
        lbl_info_back['text'] = '12.4"    < перья >     12.6"'
    elif height in range(160, 165):
        lbl_info_rich['text'] = '20.3-20.4"<ростовка>    20.5"'
        lbl_info_back['text'] = '12.44"    < перья >     12.7"'
    elif height in range(165, 170):
        lbl_info_rich['text'] = '20.4"    <ростовка>    20.6"'
        lbl_info_back['text'] = '12.5"    < перья >     12.75"'
    elif height in range(170, 175):
        lbl_info_rich['text'] = '20.5"    <ростовка>    20.7"'
        lbl_info_back['text'] = '12.7"    < перья >     12.75"'
    elif height in range(175, 180):
        lbl_info_rich['text'] = '20.7"    <ростовка>20.8-21"'
        lbl_info_back['text'] = '12.75"    < перья >     13.2"'
    elif height in range(180, 185):
        lbl_info_rich['text'] = '20.7-20.8"<ростовка>      21"'
        lbl_info_back['text'] = '12.8"    < перья >     13.2"'
    elif height in range(185, 190):
        lbl_info_rich['text'] = '20.75"   <ростовка>    21.1"'
        lbl_info_back['text'] = '13.2"    < перья >     13.7"'
        lbl_overdown['text'] = 'если Вы Ирек Ризаев, то вам перья 12.8'
    elif height in range(190, 192):
        lbl_info_rich['text'] = '21.1"+   <ростовка>   21.2"+'
        lbl_info_back['text'] = '13.6"    < перья >     13.75"'

def entry_get():    #обработка введённой информации: преобразование из str в float, проверка, что рост в периоде 155-190
    if entry.get() and str(entry.get()).isdigit():
        if float(str(entry.get()).replace(',', '.')) > 191 or float(str(entry.get()).replace(',', '.')) < 155:
            entry.delete(0, END)
            return 0
        elif len(entry.get()) > 3:
            entry.delete(3, END)
        out_values(int(entry.get()))
    else:
        entry.delete(0, END)

head = Tk() #head всего прилоежния, его интерфейс
head.title('ramnik2') #название окна

lbl_up = ttk.Label(text='подскажу длину bmx рамы для твоего роста').grid(column=1, row=0, columnspan=1, rowspan=2, ipadx=1, ipady=1)#верхний текст, приветствие
entry = ttk.Entry(validate="key", validatecommand=(head.register(lambda x: x.isdigit()), '%S')) #инит поля для ввода роста
entry.grid(column=1, row=2)
btn = ttk.Button(text='рассчитать(↑рост↑)', command=entry_get)
btn.grid(column=1, row=4, columnspan=1, ipadx=1, ipady=1) #потом необходимо изменить текст на "рассчитать"
lbl_overup_info = ttk.Label(text='наиболее подходящее всем')
lbl_overup_info.grid(column=1, row=5, columnspan=1, ipadx=1, ipady=1)    #потом необходимо заменить на "управляемость    <параметр>   стабильность"
lbl_info_rich = ttk.Label(text='20.5"    <ростовка>    20.75"')
lbl_info_rich.grid(column=1, row=6)
lbl_info_back = ttk.Label(text='12.75"    < перья >     12.8"')
lbl_info_back.grid(column=1, row=7)
lbl_overdown = ttk.Label(text=' \n ')
lbl_overdown.grid(column=1, row=8)

head.mainloop()