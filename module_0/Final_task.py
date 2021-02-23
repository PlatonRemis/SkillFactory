import numpy as np

def score_game(game_core):
    #Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    
    return print("Ваш алгоритм угадывает число в среднем за {} попыток".format(score))

def game_core_v3(number):
    count = 1
    predict = 50  #Начинать угадывать будем с середины
    floor = 1     #Нижняя граница ряда чисел
    ceiling = 100 #Верхняя граница, эти переменные понадобятся для выполнения тела функции
    
    while number!=predict:
        count+=1
        
        if predict<number:   #Если загаданное чило больше
            floor = predict  #Мы сдвигаем нижнюю границу вверх
            if round((ceiling-floor)/2)==0: #Защита от бесконечного цикла, когда number = ceiling
                predict = ceiling
            else:
                predict = floor + round((ceiling-floor)/2) #И наша новая догадка становится на середине
                                                           #Оставшегося ряда чисел (округляя вниз)
        elif predict>number: #То же самое, но двигаемся вниз
            ceiling = predict
            if round((ceiling-floor)/2)==0: #Защита от бесконечного цикла, когда number = floor
                predict = floor
            else:
                predict = ceiling - round((ceiling-floor)/2)
                
    return count

score_game(game_core_v3)
