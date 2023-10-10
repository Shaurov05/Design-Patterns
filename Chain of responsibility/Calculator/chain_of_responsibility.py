from _add_numbers import AddNumbers
from _subtract import SubtractNumbers
from _multiply import MultiplyNumbers
from _divide import DivideNumbers
from build_request import CalculationRequest

if __name__ == '__main__':
    first_chain = AddNumbers()
    second_chain = SubtractNumbers()
    third_chain = MultiplyNumbers()
    fourth_chain = DivideNumbers()

    first_chain.set_next_chain(second_chain)
    second_chain.set_next_chain(third_chain)
    third_chain.set_next_chain(fourth_chain)

    add_request = CalculationRequest(5, 10, "add")
    first_chain.calculate(add_request)

    subtract_request = CalculationRequest(5, 10, "sub")
    first_chain.calculate(subtract_request)

    multiply_request = CalculationRequest(5, 10, "multi")
    first_chain.calculate(multiply_request)

    divide_request = CalculationRequest(5, 10, "div")
    first_chain.calculate(divide_request)
