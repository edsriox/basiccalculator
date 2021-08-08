import tkinter
import tkinter as t
from tkinter import Label
window = t.Tk()
window.geometry('500x500')
window.title('Hesap Makinesi')
label1 = t.Label(  text = 'Basit İşlem Uygulaması:' , font = ' verdana 22 bold')
label1.place( x = 8 , y = 20)

def toplama():
    x = int(E1.get())
    y = int(E2.get())
    sonuc = x + y
    yazi = t.Label(text = sonuc , font = 'italic 30 bold' )
    yazi.place(x = 250 , y = 290)
    sonuçgösterge = t.Label(text = 'Sonuç = ' , font = 'italic 20 bold' )
    sonuçgösterge.place(x = 50 , y = 290)

def cıkarma():
    x = int(E1.get())
    y = int(E2.get())
    sonuc = x - y
    yazi = t.Label(text = sonuc , font = 'italic 30 bold' )
    yazi.place(x = 250 , y = 290)
    sonuçgösterge = t.Label(text = 'Sonuç = ' , font = 'italic 20 bold' )
    sonuçgösterge.place(x = 50 , y = 290)

def delete():

    E1.delete(0)
    E2.delete(0)



def newwindow():
    window2 = t.Tk()
    window2.geometry('500x500')
    window2.title('Diğer İşlemler')
    L1 = t.Label(window2 , text = 'İşlem Seçin:' , font = 'verdana 25 bold')
    L1.place(x = 25 , y = 30)

    def bölme():
        z = int(E3.get())
        c = int(E4.get())
        sonuc1 = z / c
        if z % c == 0:
            sonuc1 = int(sonuc1)
        else:
            sonuc1 = float(sonuc1)
        yazi = t.Label(window2 , text= sonuc1, font='italic 30 bold')
        yazi.place(x=250, y=290)
        sonuçgösterge1 = t.Label(window2 , text='Sonuç = ', font='italic 20 bold')
        sonuçgösterge1.place(x=50, y=290)
    def carpma():
        x = int(E3.get())
        y = int(E4.get())
        sonuc2 = x * y
        yazi = t.Label(window2 , text=sonuc2, font='italic 30 bold')
        yazi.place(x = 250, y = 290)
        sonuçgösterge1 = t.Label(window2 , text='Sonuç = ', font='italic 20 bold')
        sonuçgösterge1.place(x=50, y=290)

    def delete2():

        E3.delete(0)
        E4.delete(0)

    deletebutton = t.Button(window2 , text='Tümünü Temizle', font='verdana 13 bold', bg='red', command=delete2)
    deletebutton.place(x=168, y=450)

    bölmebutonu = t.Button(window2 , text = 'Bölme' , bg = 'skyblue' , font = 'verdana 19 bold' , command = bölme)
    bölmebutonu.place(x = 120 , y = 380)
    carpmabutonu = t.Button(window2, text='Çarpma', bg='goldenrod', font='verdana 19 bold', command = carpma)
    carpmabutonu.place(x=260, y= 380)

    E3 = t.Entry(window2, font='italic 13 bold', )
    E3.place(x=170, y=150)

    E4 = t.Entry(window2, font='italic 13 bold', )
    E4.place(x=170, y=200)

    labelsayigiriniz3 = t.Label(window2, text='Sayi Giriniz: ', font='verdana 12 ')
    labelsayigiriniz3.place(x=60, y=145)

    labelsayigiriniz4 = t.Label(window2 , text='Sayi Giriniz: ', font='verdana 12 ')
    labelsayigiriniz4.place(x=60, y=198)






    window2.mainloop()


deletebutton = t.Button(text = 'Tümünü Temizle' , font = 'verdana 13 bold' , bg = 'red', command = delete)
deletebutton.place(x =60 , y = 450 )

toplamabutton = t.Button(bg = 'blue'  , text = 'Toplama' , font = 'verdana 20 bold' , command = toplama)
toplamabutton.place(x = 75 , y = 370)

cıkarmabutton = t.Button(bg = 'green'  , text = 'Çıkarma' , font = 'verdana 20 bold' , command = cıkarma )
cıkarmabutton.place(x = 250 , y = 370)

labelsayigiriniz1 = t.Label (text = 'Sayi Giriniz: ' , font = 'verdana 12 ' )
labelsayigiriniz1.place(x = 65 , y = 95)

labelsayigiriniz2 = t.Label (text = 'Sayi Giriniz: ' , font = 'verdana 12 ' )
labelsayigiriniz2.place(x = 65 , y = 195)

farkliislemlerbutonu = t.Button(text = 'Farklı İşlemler' , font = 'verdana 13 bold', bg = 'purple' , command = newwindow )
farkliislemlerbutonu.place(x = 260 , y = 450)

E1 = t.Entry(window, font = 'italic 13 bold' , bg = 'yellow' )
E1.place(x = 170 , y = 100)

E2 = t.Entry(window, font = 'italic 13 bold' , bg = 'yellow' )
E2.place(x = 170 , y = 200)







window.mainloop()

