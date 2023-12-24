import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0 # кол-во попыток
    min_number = 1
    max_number = 101
    # цикл в которм компьютер отгадывает число за минимальное число попыток
    while True:
        random_number = np.random.randint(min_number, max_number)
        count +=1
        if random_number > number:
            max_number = random_number
        elif random_number < number:
            min_number = random_number
        else:
            break
    return(count)
if __name__ == '__main__':
    game_core_v3