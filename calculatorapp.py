help_screen = '''   CALCULATOR
    Input must be formatted as: {number} {operator} {number} with whitespaces in between each part
    type quit to exit
    type help to view this text again'''
index_error_ouput = 'Input must be formatted as (number) (operator) (number) with a whitespace between each part'


def calculate(first_number, calculation_mode, second_number):
    if calculation_mode == '+':
        return f'{first_number} + {second_number} = {(float(first_number) + float(second_number))}'
    elif calculation_mode == '-':
        return f'{first_number} - {second_number} = {(float(first_number) - float(second_number))}'
    elif calculation_mode == '*':
        return f'{first_number} * {second_number} = {(float(first_number) * float(second_number))}'
    elif calculation_mode == '/':
        return f'{first_number} / {second_number} = {(float(first_number) / float(second_number))}'
    else:
        return 'Invalid Operator'


print(help_screen)
while True:
    user_input = input('Calculate: ')
    try:
        if user_input == 'quit':
            break
        elif user_input == 'help':
            print(help_screen)
        else:
            try:
                print(calculate(user_input.split(' ')[0], user_input.split(' ')[1], user_input.split(' ')[2]))
            except IndexError:
                print(index_error_ouput)
    except ValueError:
        print('Invalid Number')
