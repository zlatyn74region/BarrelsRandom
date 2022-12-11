import random
import logging

def input_int(
    msg: str, 
    min: int = None, 
    max: int = None,
) -> int:
    '''
    Берет на ввод у пользователя число с дальнейшей проверкой.
    Параметры:
    msg - Сообщение подающееся на ввод пользователю.
    min - Минимальное значение на ввод.
    max - Максимальное значение на ввод.
    Возврат:
    Корректно введенное число.
    '''
    while True:
        try:
            logging.info(msg)
            num = int(input(msg))
            logging.info('Пользователь ввел: ' + str(num))
            if min != None and num < min or max != None and num > max:
                min_msg = '' if min == None else f' от {min}'
                max_msg = '' if max == None else f' до {max}'
                print(f'Ошибка: нужно ввести число{min_msg}{max_msg}!')
                logging.error(f'Ошибка: нужно ввести число{min_msg}{max_msg}!')
                continue
            logging.info('Корректное значение введенное пользователем: ' + str(num))
            return num
        except:
            logging.error('Ошибка: нужно ввести число!', exc_info=True)
            print('Ошибка: нужно ввести число!')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="logfile.log", filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s")
                            
    amount_barrels = input_int('Введите количество бочек: ', 1)

    barrels = [i for i in range(1, amount_barrels + 1)]

    random.shuffle(barrels)

    while True:
        choice = barrels.pop()
        print("Выпал бочонок №", choice)
        logging.info("Выпал бочонок №" + str(choice))
        if len(barrels) == 0: break

        input("Нажмите enter чтобы вытянуть следующий бочонок >>>" )
        logging.info('Нажмите enter чтобы вытянуть следующий бочонок >>>')