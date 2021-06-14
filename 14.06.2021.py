zakaz = []
for number in range(10):
      print('Список доступных марок инструментов в продаже:\n 1. Casio,\n 2. Yamaha\n 3. Roland\n 4. Tesler')
      musical_instrument = ['Casio','Yamaha', 'Roland', 'Tesler']
      print('Введите номер производителя инструмента, который вы хотите приобрести')
      mark = int(input())
      print('Тип инструмента:\ 1.Кейтар ,\n 2.Синтезато\n 3.Рабочая станция, \n 4.Цифровое пианино')
      kind_instrument = ['Кейтар','Синтезатор', 'Рабочая станция', 'Цифровое пианино']
      kind = int(input())
      print('Выберите количество клавиш: от 13 до 88')
      keys = input()
      print('Выберите цвет из списка:\n 1. Черный\n 2. Белый\n 3. Бежевый\n 4. Серый')
      color_instr = ['черный', 'белый', 'бежевый', 'серый']
      color = int(input())
      number = " Модель инструмента: " + musical_instrument[mark-1] + "; Тип инструмента: " + kind_instrument[kind-1] + "; Количество клавиш: " + keys + "; Цвет: " + color_instr[color-1]
      zakaz.append(number)
      print('Хотите продолжить покупки? (да/нет)')
      qst = input()
      if qst != 'да':
            break
print('Ваш заказ:')
print('\n'.join(zakaz))
print("Спасибо за то, что выбрали наш магазин,\nчерез 10 минут с вами свяжется наш менеджер,\nдля дальнейшего оформления заказа")
