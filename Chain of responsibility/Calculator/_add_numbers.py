from chain_parent import Chain
from build_request import CalculationRequest


class AddNumbers(Chain):
    def __init__(self):
        self._next_chain = None

    def set_next_chain(self, _next_chain: Chain):
        self._next_chain = _next_chain

    def calculate(self, calculation_request: CalculationRequest):
        if calculation_request.get_calculation_method() == "add":
            print(f"{calculation_request.get_number1()}+{calculation_request.get_number2()} = "
                  f"{calculation_request.get_number1()+calculation_request.get_number2()}")
        elif self._next_chain:
            self._next_chain.calculate(calculation_request)
        else:
            return None
