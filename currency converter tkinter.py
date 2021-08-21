import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('600x650')

times = []
fontStyle2 = tkFont.Font(size = 60)

def converter(value1, value2, currency):
    times.append('.')
    print(len(times))
    def euroToPound():
        if len(times) > 2:
            curr = 'Euros'
            currency1 = value1
            currency2 = 0.85882368
            converter(currency1, currency2, curr)
        else:
            currency1 = 0.85882368
            currency2 = 0
            converter(currency1, currency2, currency)
    def usdToPound():  
        if len(times) > 2:
            curr = 'USD'
            currency1 = value1
            currency2 = 0.73403392
            converter(currency1, currency2, curr)
        else:
            currency1 = 0.73403392
            currency2 = 0
            converter(currency1, currency2, currency)
        
    def cadToPound():
        if len(times) > 2:
            curr = 'CAD'
            currency1 = value1
            currency2 = 0.572519
            converter(currency1, currency2, curr)
        else:
            currency1 = 0.572519
            currency2 = 0
            converter(currency1, currency2, currency)
    def nzdToPound():
        if len(times) > 2:
            curr = 'NZD'
            currency1 = value1
            currency2 = 0.50179509
            converter(currency1, currency2, curr)
        else:
            currency1 = 0.50179509
            currency2 = 0
            converter(currency1, currency2, currency)
    def rupToPound():
        if len(times) > 2:
            curr = 'Rupees'
            currency1 = value1
            currency2 = 0.0098747659
            converter(currency1, currency2, curr)
        else:
            currency1 = 0.0098747659
            currency2 = 0
            converter(currency1, currency2, currency)
    def naiToPound():
        if len(times) > 2:
            curr = 'Naira'
            currency1 = value1
            currency2 = 0.0017829498
            converter(currency1, currency2, curr)
        else:
            currency1 = 0.0017829498
            currency2 = 0
            converter(currency1, currency2, currency)
    def yenToPound():
        if len(times) > 2:
            curr = 'Yen'
            currency1 = value1
            currency2 = 0.0066863553
            converter(currency1, currency2, curr)
        else:
            currency1 = 0.0066863553
            currency2 = 0
            converter(currency1, currency2, currency)
    def poundToPound():
        if len(times) > 2:
            curr = 'Pounds'
            currency1 = value1
            currency2 = 1
            converter(currency1, currency2, curr)
        else:
            currency1 = 1
            currency2 = 0
            converter(currency1, currency2, currency)
    if len(times) == 2:
        for widget in root.winfo_children():
            widget.destroy()
        label = tk.Label(root, text = 'What currency would you like to convert from?')
        label.grid(row = 1, column = 1)
    elif len(times) == 3:
        for widget in root.winfo_children():
            widget.destroy()
        label = tk.Label(root, text = 'What currency would you like to convert to?')
        label.grid(row = 1, column = 1)
    pounds = Image.open('Currency Converter/pounds.png')
    pounds1 = pounds.resize((200, 100), Image.ANTIALIAS)
    pounds2 = ImageTk.PhotoImage(pounds1)
    pbutton = tk.Button(root, image = pounds2, command = poundToPound)
    pbutton.Image = pounds2
    pbutton.grid(row = 2, column = 1, padx = 50, pady = 10)

    label = tk.Label(root, text = 'Pounds')
    label.grid(row = 3, column = 1)

    euros = Image.open('Currency Converter/euros.png')
    euros1 = euros.resize((200, 100), Image.ANTIALIAS)
    euros2 = ImageTk.PhotoImage(euros1)
    ebutton = tk.Button(root, image = euros2, command = euroToPound)
    ebutton.Image = euros2
    ebutton.grid(row = 2, column = 2, padx = 50, pady = 10)

    label = tk.Label(root, text = 'Euros')
    label.grid(row = 3, column = 2)

    usd = Image.open('Currency Converter/usd.png')
    usd1 = usd.resize((200, 100), Image.ANTIALIAS)
    usd2 = ImageTk.PhotoImage(usd1)
    ubutton = tk.Button(root, image = usd2, command = usdToPound)
    ubutton.Image = usd2
    ubutton.grid(row = 4, column = 1, padx = 50, pady = 10)

    label = tk.Label(root, text = 'USD')
    label.grid(row = 5, column = 1)

    cad = Image.open('Currency Converter/cad.png')
    cad1 = cad.resize((200, 100), Image.ANTIALIAS)
    cad2 = ImageTk.PhotoImage(cad1)
    cbutton = tk.Button(root, image = cad2, command = cadToPound)
    cbutton.Image = cad2
    cbutton.grid(row = 4, column = 2, padx = 50, pady = 10)

    label = tk.Label(root, text = 'CAD')
    label.grid(row = 5, column = 2)

    nzd = Image.open('Currency Converter/nzd.png')
    nzd1 = nzd.resize((200, 100), Image.ANTIALIAS)
    nzd2 = ImageTk.PhotoImage(nzd1)
    nzbutton = tk.Button(root, image = nzd2, command = nzdToPound)
    nzbutton.Image = nzd2
    nzbutton.grid(row = 6, column = 1, padx = 50, pady = 10)

    label = tk.Label(root, text = 'NZD')
    label.grid(row = 7, column = 1)

    rupees = Image.open('Currency Converter/rupees.png')
    rupees1 = rupees.resize((200, 100), Image.ANTIALIAS)
    rupees2 = ImageTk.PhotoImage(rupees1)
    rbutton = tk.Button(root, image = rupees2, command = rupToPound)
    rbutton.Image = rupees2
    rbutton.grid(row = 6, column = 2, padx = 50, pady = 10)

    label = tk.Label(root, text = 'Rupees')
    label.grid(row = 7, column = 2)

    naira = Image.open('Currency Converter/naira.png')
    naira1 = naira.resize((200, 100), Image.ANTIALIAS)
    naira2 = ImageTk.PhotoImage(naira1)
    nbutton = tk.Button(root, image = naira2, command = naiToPound)
    nbutton.Image = naira2
    nbutton.grid(row = 8, column = 1, padx = 50, pady = 10)

    label = tk.Label(root, text = 'Naira')
    label.grid(row = 9, column = 1)

    yen = Image.open('Currency Converter/yen.png')
    yen1 = yen.resize((200, 100), Image.ANTIALIAS)
    yen2 = ImageTk.PhotoImage(yen1)
    ybutton = tk.Button(root, image = yen2, command = yenToPound)
    ybutton.Image = yen2
    ybutton.grid(row = 8, column = 2, padx = 50, pady = 10)

    label = tk.Label(root, text = 'Yen')
    label.grid(row = 9, column = 2)

    if len(times) < 2:
        converter(value1, value2, currency)
    elif len(times) > 3:
        def presentResult():
            num = entry.get()
            final_result = round(result * float(num), 2)
            for widget in root.winfo_children():
                widget.destroy()
            answer = [str(final_result), currency]
            label = tk.Label(root, text = ' '.join(answer), font = fontStyle2)
            label.pack()
        print(value1)
        print(value2)
        result = value1/value2
        for widget in root.winfo_children():
            widget.destroy()
        label = tk.Label(root, text = 'How many would you like to convert?')
        label.grid(padx = 180)
        entry = tk.Entry(root)
        entry.grid()
        button = tk.Button(root, text = 'Enter', command = presentResult)
        button.grid()

converter(value1 = 2, value2 = 3, currency = 0)
root.mainloop()