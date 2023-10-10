class CalculationRequest:
    def __init__(self, number1: int, number2: int, calculation_method: str):
        self._number1 = number1
        self._number2 = number2
        self._calculation_method = calculation_method

    def get_number1(self):
        return self._number1

    def get_number2(self):
        return self._number2

    def get_calculation_method(self):
        return self._calculation_method
