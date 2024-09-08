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




window = Tk()# создаем главное окно
window.title("Cats!")# назвавние
window.geometry("600x480")# размер

# Создаем метку без изображения
label = Label()
label.pack()# размещаем

# Добавляем кнопку для обновления изображения
update_button = Button(text="Обновить", command=set_image)
# command=set_image- вызывает load_image и установливает изображение в метку
update_button.pack() # update-обновление,


url = 'https://cataas.com/cat'# адрес в интернете, по которому будем искать
# Вызываем функцию для установки изображения в метку
set_image()# чтобы появилась первая картинка при запуске проекта



window.mainloop()
