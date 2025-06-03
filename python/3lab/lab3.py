import datetime
import time

#1 задание: декоратор для логирования
def log_decorator(func):
    def wrapper(*args, **kwargs):
        #запись времен начала выполнения программы
        start_time = datetime.datetime.now()
        start_msg = f"[{start_time}] Функция '{func.__name__}' вызвана с аргументами: {args}\n"
        
        #записываем в файлик
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(start_msg)
        
        #вызов функции и отсчет времени
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        #запись времени завершения
        end_msg = f"[{datetime.datetime.now()}] Функция '{func.__name__}' завершена. Время выполнения: {end - start:.1f} сек.\n"
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(end_msg)
        
        return result
    return wrapper

@log_decorator #используем декоратор от ф-ии calculate
def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        raise ValueError("Неподдерживаемая операция")

calculate(10, 5, '+')

#2 задание: декоратор для ограничения вызовов
def rate_limit(max_calls, period):
    def decorator(func):
        calls = []
        
        def wrapper(*args, **kwargs):
            now = time.time()
            #удаляем старые вызовы (старше period секунд)
            calls[:] = [call for call in calls if now - call <= period]
            
            if len(calls) >= max_calls:
                print("Превышен лимит вызовов. Попробуйте позже.")
                return
            
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, period=60)
def send_message(message):
    print(f"Сообщение отправлено: {message}")

for _ in range(5):
    send_message("Привет!")

#3 задание: декоратор для кэширования
def cache_decorator(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  #первый вызов вычисляется
print(fibonacci(10))  #второй берется из кэша