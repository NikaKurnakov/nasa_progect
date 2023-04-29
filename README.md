# Космический телеграмм

Этот проект поможет вам загрузить в телеграмм канал фото от NASA_APOD, spaceX и NASA_EPIC.

### Как получить API-ключ от NASA и  ID от spaceX

Для того, чтобы получить API-ключ от NASA_APOD, Вам нужно зарегестрировать на [сайте](https://api.nasa.gov/#apod). API-ключ отправят Вам на почту. А как его добавлят в переменную окружения, Вы можете прочитать [тут](https://github.com/NikaKurnakov/bitly) в разделе "Переменные окружения".

После вам надо получить API-ключ от NASA_EPIC. Вам также надо зарегестрироваться [здесь](https://api.nasa.gov/#epic). API-ключ Вам так же отправят на почту. Его тоже надо записать в переменную окружения.

ID для spaceX можете использорать вот этот `5eb87d46ffd86e000604b388`. Тип данных ID `str`. Он должен храниться в переменной окружения.
Файл `.env`, в который вы записывали переменные окружения, надо добавить в файл `.gitignore`. 

### Запуск

Затем, когда разобрались с переменными, надо запустить код. Если у вас Windows, то он запускается так:

```
py (название файла).py
```
Если у вас есть ID для spaceX, то запуск будет такой:

```
py get_spaceX.py --id ваш_токен
```

Если у вас Linux, то код будет запускается почти так же, только вместо `py` будет `python`:

```
python (название файла).py
```

Так же и с ID:

```
python get_spaceX.py ваш_токен
```

### Зависимости

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для 
установки зависимостей:

```
pip install -r requirements.txt
```
