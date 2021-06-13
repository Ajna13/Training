zakaz = []
for number in range(10):
      print('Список доступных марок ноутбуков в продаже:\n 1. Lenovo,\n 2. Asus\n 3. Apple\n 4. HP')
      notebook_mark = ['Lenovo','Asus', 'Apple', 'HP']
      print('Введите номер ноутбука, который вы хотите приобрести')
      mark = int(input())
      print('Список доступных диагоналей экранов:\n-15.6\n-14.0\n-13.3\n-17.3\n-14.1')
      print('Введите диагональ экрана ноутбука')
      diag_display_nb = input()
      print('Список доступных процессоров:\n 1. Core-i5\n 2. Core-i7\n 3. Ryzen 5\n 4. Core-i3\n 5. Pentium Gold')
      proc_nb = ['Core-i5', 'Core-i7', 'Ryzen 5', 'Core-i3', 'Pentium Gold']
      print('Введите номер выбранного процессора:')
      proc = int(input())
      print('Выберите и введите объем оперативной памяти: от 4 гб до 32 гб')
      ram_nb = input()
      print('Выберите номер модели видеокарты из списка:\n 1. Intel\n 2. NVIDIA\n 3. AMD\n 4. Apple')
      gc_nb = ['Intel', 'NVIDIA', 'AMD', 'Apple']
      gc = int(input())
      number = " Модель ноутбука: " + notebook_mark[mark-1] + "; Диагональ экрана: " + diag_display_nb + "; Процессор: "+ proc_nb[proc-1] + "; Объем оперативной памяти: " + ram_nb + "; Модель видеокарты: " + gc_nb[gc-1]
      zakaz.append(number)
      print('Хотите продолжить покупки? (да/нет)')
      qst = input()
      if qst != 'да':
            break
print('Ваш заказ:')
print('\n'.join(zakaz))
print("Спасибо за то, что выбрали наш магазин,\nчерез 10 минут с вами свяжется наш менеджер,\nдля дальнейшего оформления заказа")

#print('Ваш заказ\n'
#      + '\n-----------------------------'
#      + "\nМодель ноутбука: " + notebook_mark[n-1]
#     + "\nДиагональ экрана: " + diag_display_nb
#    + "\nПроцессор: "+ proc_nb[proc-1]
#      + "\nОбъем оперативной памяти: " + ram_nb
#      + "\nМодель видеокарты: " + gc_nb[gc-1]
#      + "\n-----------------------------"
#     )
