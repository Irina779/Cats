from tkinter import *
from PIL import Image, ImageTk # т. к. работаем с изображениями
import requests
from io import BytesIO # позволяет работать с 1 и 0


window = Tk()# создаем главное окно
window.title("Cats!")# назвавние
window.geometry("600x480")# размер

# Создаем метку без изображения
label = Label()
label.pack()# размещаем


url = 'https://cataas.com/cat'# адрес в интернете, по которому будем искать
img = load_image(url)# создаем функцию загрузки изображения, в которую будем передавать изображение и установливать на метку

if img:# проверка, если не пустая
    # Устанавливаем изображение в метку
    label.config(image=img)
    # Необходимо сохранить ссылку на изображение, чтобы избежать сборки мусора
    label.image = img

window.mainloop()
