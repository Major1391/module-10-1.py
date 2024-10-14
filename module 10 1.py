from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файле {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Время работы функции {time_res}')
'''После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции 
к домашнему заданию.'''
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))
time_start1 = datetime.now()
thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()
thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(f'Время работы потоков {time_res1}')