from tkinter import *
from tkinter import ttk# набор улучшенных виджетов
from PIL import Image, ImageTk # т. к. работаем с изображениями
import requests
from io import BytesIO # позволяет работать с 1 и 0

# Список доступных тегов (спящий. прыгающий, дерущийся, черный,белый, бенгальский, сиамский, милый)
ALLOWED_TAGS = ['sleep', 'jump', 'smile', 'fight', 'black', 'white', 'red', 'siamese', 'bengal']


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

def open_new_window():# открыть новое окно
    tag = tag_combobox.get()
    # самый простой способ склейки f строки. Если поле ввода пустое то
    # 'https://cataas.com/cat' (без последнего слеша)
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_with_tag)


    img = load_image(url)
    if img:
        # Создаем новое вторичное окно
        new_window = Toplevel()# Toplevel-высший уровень
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")

        # Добавляем изображение в новое окно
        label = Label(new_window, image=img)
        label.image = img  # Сохраняем ссылку на изображение
        label.pack()


    # Устанавливаем изображение в метку
        label.config(image=img)
        label.image = img
def exit():
    window.destroy()


window = Tk()# создаем главное окно
window.title("Cats!")# назвавние
window.geometry("600x520")# размер


# Создаем меню
menu_bar = Menu(window)# создаем меню в окне window
window.config(menu=menu_bar)

# Добавляем пункты меню
file_menu = Menu(menu_bar, tearoff=0)# чтобы меню не отклеивалась
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)



url = 'https://cataas.com/cat'# адрес в интернете, по которому будем искать
# Вызываем функцию для установки изображения в метку


# Метка "Выбери тег"
tag_label = Label(text="Выбери тег")
tag_label.pack()

tag_combobox = ttk.Combobox(values=ALLOWED_TAGS)# values=ALLOWED_TAGS- разрешонные значения
tag_combobox.pack()

# Кнопка для загрузки изображения с тегом (с текстом)
load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()


window.mainloop()
