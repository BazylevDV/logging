import logging


def mul(a,b):
    return a * b
def div(a,b):

    try:
        a / b
        logging.info(f"Successful dividing {a}/{b}")
        return  a / b
    except ZeroDivisionError as err:
        logging.error('na nol ne dely', exc_info=True)
        return 0


def scrt(a):
    return a ** 0.5
def pow(a,b):
    return a ** b

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', format="%(asctime)s | %(message)s")

print(div(3,4))
print(div(3,0))

