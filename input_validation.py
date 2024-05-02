import logging


def validate_input(term: str = 'término', input_value: int|float|str = None) -> float:
    while True:
        if not input_value:
            input_value = input(f"Por favor introduce un valor para '{term}': ")
        try:
            valid_input = float(input_value)
        except ValueError:
            print(f"Por favor, introduzca un valor para '{term}' en formato numérico que no sea negativo.")
            logging.info('invalid format')

        if valid_input < 0:
            logging.info('negative number')
        else:
            return valid_input
        
        
if __name__ == '__main__':
    validate_input()
    