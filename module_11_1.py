import requests
import matplotlib.pyplot as plt
import os
from PIL import Image, ImageOps


"""Модуль REQUESTS"""

print('#' * 10, '-' * 3, 'Модуль REQUESTS', '-' * 3, '#' * 10)
print('-' * 45)

url = 'https://4pda.to'  # url для исследования
print(f'Сведения о сайте: {url}')

try:
    r = requests.get(url)  # выполняем запрос к сайту

    if r.status_code == 200:  # получаем ответ от сайта, что он доступен
        print(f'Код ответа: {r.status_code} - Сайт доступен')

        print(r.headers)
        try:
            print(f'Дата и время сервера: {r.headers['Date']}')
        except:
            print('Не удалось получить дату и время сервера')

        try:
            print(f'Соединение сервера: {r.headers['Connection']}')
        except:
            print('Не удалось получить информацию о соединение сервера')

        try:
            print(f'Тип контента сервера: {r.headers['Content-Type']}')
        except:
            print('Не удалось получить информацию о типе контента сервера')

        try:
            print(f'Дата последнего изменения: {r.headers['Last-Modified']}')
        except:
            print('Не удалось получить дату последнего изменения')

        try:
            print(f'Время ответа сервера: {r.elapsed}')
        except:
            print('Не удается получить время ответа от сервера')

        r = requests.get(url, params={'s': 'xiaomi'})  # формируем запрос поиска
        print(f'Поиск по слову Xiaomi: {r.url}')

        r.encoding = 'windows-1251'  # устанавливаем кодировку для корректного сохранения кода страницы
        with open('Cod_4pda.txt', 'w') as f:  # сохраняем код страницы
            f.write(r.text)
        print('Код сайта сохранен в файл: Cod_4pda.txt')

    elif r.status_code == 404:  # если получен ответ от сервера, что сайт не доступен
        print(r.status_code, '- Сайт не найден')
    else:
        print(r.status_code, '- Неизвестная ошибка')  # другой ошибки мы не знаем
except requests.exceptions.ConnectionError:  # не удалось найти сайт, например неверно указан адрес
    print('Ошибка при выполнении запроса')


"""Модуль PILLOW"""

print()
print()
print('#' * 10, '-' * 3, 'Модуль PILLOW', '-' * 3, '#' * 10)
print('-' * 43)


def info(image):
    img_ = Image.open(image)  # открываем изображение
    file_size = os.path.getsize(image)  # узнаем размер (вес) изображения

    print('Размер файла:', file_size, 'байт')
    print(f'Формат изображения: {img_.format}')
    print(f'Разрешение изображения: {img_.size[0]}x{img_.size[1]}')
    print(f'Цветовая модель изображения: {img_.mode}')


def img_resize(image, image_new, height, width):
    img_ = Image.open(image)
    out = img_.resize((width, height))  # меняем размер изображения
    out.save(image_new)  # сохраняем измененное изображение
    print(f'Измененное изображение сохранено как: {image_new}')


try:
    print('Информация об изображении: nature.jpg')
    print('-' * 40)

    info('nature.jpg')
    print('-' * 40)

    img_resize('nature.jpg', 'nature_new.jpg', 1000, 1000)
    print('-' * 40)

    img = Image.open('nature_new.jpg')  # открываем изображение
    if img.mode == 'RGB':  # проверяем режим модели цветопередачи
        red, green, blue = img.split()  # делим изображения на каналы R, G, B
        red.save('nature_new_red.jpg')  # сохраняем канал R
        green.save('nature_new_green.jpg')  # сохраняем канал G
        blue.save('nature_new_blue.jpg')  # сохраняем канал B
        print('Каналы R, G, B изображения сохранены')
    else:
        print('Изображение не в RGB модели')
    print('-' * 40)

    img = Image.open('nature_new.jpg')
    if img.mode == 'RGB':
        red, green, blue = img.split()
        pustye_pikseli = red.point(lambda _: 0)  # создаем пустые пиксели

        red_image = Image.merge('RGB', (red, pustye_pikseli, pustye_pikseli))  # объединяем каналы заполняя пустые пиксели
        green_image = Image.merge('RGB', (pustye_pikseli, green, pustye_pikseli))
        blue_image = Image.merge('RGB', (pustye_pikseli, pustye_pikseli, blue))

        red_image.save('nature_new_merge_red.jpg')  # сохраняем изображение каждого канала
        green_image.save('nature_new_merge_green.jpg')
        blue_image.save('nature_new_merge_blue.jpg')

        print('Окрашенные каналы R, G, B изображения сохранены!')
        print('-' * 40)

        rgb_image = Image.merge('RGB', (red, green, blue))  # объединяем разделенные каналы исходного изображения
        rgb_image.save('nature_new_merge.jpg')  # сохраняем объединенное изображение
        print('Объединенное изображение сохранено как: nature_new_merge.jpg')
    print('-' * 40)

    img = Image.open('nature_new_blue.jpg')
    colorized = ImageOps.colorize(img, black='red', white='yellow')  # меняем цветопередачу изображения
    colorized.save('nature_colorized.jpg')
    print('Изображение цветного фона сохранено как: nature_colorized.jpg')

except OSError:
    print('Не удалось открыть изображение')


"""Модуль MATPLOTLIB"""

print()
print()
print('#' * 10, '-' * 3, 'Модуль MATPLOTLIB', '-' * 3, '#' * 10)
print('-' * 43)

x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
y = [200, 456, 30, 159, 788, 342, 68, 897, 1098, 37, 543, 801]

print('Построение графика!')
plt.bar(x, y, label='Величина прибыли')  # Параметр label позволяет задать название величины для легенды
plt.xlabel('2024 год')  # Подпись для оси х
plt.ylabel('Прибыль, в млн руб.')  # Подпись для оси y
plt.title('Cтолбчатая диаграмма прибыли за 2024 год')  # Название диаграммы
plt.legend()  # Легенда

print('Демонстрация графика!')
plt.show()

print('Демонстрация графика завершена!')
