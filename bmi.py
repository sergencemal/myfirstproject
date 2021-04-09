
class BMI:
    def __init__(self, height: float, weight: float):
        self._height = float(height)
        self._weight = float(weight)

    def calculate(self) -> float:
        return self._weight / ((self._height / 100) ** 2)

    def category(self) -> str:
        bmi = self.calculate()
        if bmi < 18.5:
            return "underweight"

        if 18.5 <= bmi < 25:
            return "healthy"

        if 25 <= bmi < 30:
            return "overweight"

        return "obese"
