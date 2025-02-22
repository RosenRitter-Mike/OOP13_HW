import time
import logging
from abc import abstractmethod, ABC

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}  running time is {end_time - start_time:.4f} seconds")
        logging.info(f"{func.__name__}  running time is {end_time - start_time:.4f} seconds")

    return wrapper


def password(func):
    def wrapper(*args, **kwargs):
        pword = input("please input the password🔐: ")
        if pword == "1234":
            return func(*args, **kwargs)
        else:
            logging.error(f"function [{func.__name__}] Wrong password: {pword}")
            print("Wrong Password!!!😣")
    return wrapper


def logme(func):
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__}, Started running ")
        func(*args, **kwargs)
        logging.info(f"{func.__name__}, Finished running ")

    return wrapper


@password
def say_hello():
    print('hello...')


@logme
@timer
def star_print(msg):
    print('************', msg)


say_hello()
star_print("Arcturus looks especially bright this night🌠")