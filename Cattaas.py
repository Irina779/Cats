from tkinter import *
from PIL import Image, ImageTk # т. к. работаем с изображениями
import requests
from io import BytesIO # позволяет работать с 1 и 0

def load_image(url):
    try:# обработка исключений
        # Отправляем GET-запрос с использованием requests.get()
        response = requests.get(url)# делаем запрос и получаем ответ,get-команда для получения чего либо

        # Проверяем успешность запроса (код ответа 200)
        response.raise_for_status()# для обработки исключений

        # Читаем байты из ответа в объект BytesIO
        image_data = BytesIO(response.content)# картинка будет приобразована при #помощи BytesIO

        # Открываем изображение с помощью PIL
        img = Image.open(image_data)# img локальная, сокращение от имедж
        # Изменяем размер изображения чтобы была видна кнопка
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        # Image.Resampling.LANCZOS- принцип, по которому будет уменьшаться изображение,
        # чтобы не было большой потери качества


        return ImageTk.PhotoImage(img)# функция вернет img и положит ниже в img = load_image(url)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None # если все хорошо, вернет изображение, если плохо ничего не #вернет

def set_image():
    # Вызываем функцию для загрузки изображения
    img = load_image(url)

    if img:
        # Устанавливаем изображение в метку
        label.config(image=img)
        label.image = img
def exit():
    window.destroy()


window = Tk()# создаем главное окно
window.title("Cats!")# назвавние
window.geometry("600x520")# размер

# Создаем метку без изображения
label = Label()
label.pack()# размещаем

# Добавляем кнопку для обновления изображения, после добавления меню
# она будет не нужна, закомментируем
# update_button = Button(text="Обновить", command=set_image)
# command=set_image- вызывает load_image и установливает изображение в метку
# update_button.pack() # update-обновление

# Создаем меню
menu_bar = Menu(window)# создаем меню в окне window
window.config(menu=menu_bar)

# Добавляем пункты меню
file_menu = Menu(menu_bar, tearoff=0)# чтобы меню не отклеивалась
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=set_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)




url = 'https://cataas.com/cat'# адрес в интернете, по которому будем искать
# Вызываем функцию для установки изображения в метку
set_image()# чтобы появилась первая картинка при запуске проекта



window.mainloop()
