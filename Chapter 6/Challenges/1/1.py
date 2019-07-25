NUM_SQUARES = 9

def ask_number(question, low, high, step = 1):
    """ Asks for a number within a range with a given step """
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    print(response)
    return response

ask_number("Where will you move? 0-8", 0, NUM_SQUARES)
