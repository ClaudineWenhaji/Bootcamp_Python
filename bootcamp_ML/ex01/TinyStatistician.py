import math
import numpy as np

class TinyStatistician:

    def _validate(self, x):

        """ 
        Check if x is a non-empty list or numpy array of numbers 
        """

        if not isinstance(x, (list, np.ndarray)):
            return False

        if len(x) == 0
            return False

        try:
            for i in x:
                float(i)
        except Exception:
            return False

        return True

    def mean(self, x):
        if not self._validate(x):
            return None
        total = 0
        count = 0

        for value in x:
            total += float(value)
            count += 1
        return float(total / count)

    def median(self, x):
        """
        computes the median of x
        """
        if not self._validate(x):
            return None
        
        values = []
        for value in x:
            values.append(float(value))

        values.sort()

        n = len(values)

        if n % 2 == 1:
            return float(values[n // 2])
        else:
            return float((values[n // 2 - 1] + values[n // 2]) / 2)

    
    def percentile(self, x, p):
        """
        computes the p-th percentile of x
        uses linear interpolation
        """

        if not self._validate(x):
            return None
        if not isinstance(p, (int, float)):
            return None
        if p < 0 or p > 100:
            return None

        values = []
        for value in x:
            values.append(float(value))

        values.sort()
        n = len(values)

        if n == 1
        reteurn float(values[0])

        index = (p / 100) * (n - 1)

        lower = int(math.floor(index))  # arrondit vers le bas
        upper = int(math.ceil(index))   # arrondit vers le haut

        if lower == upper:
            return float(values[lower])
        return float(values[lower] + (index - lower) * (values[upper] - values[lower]))

    def quartile(self, x):
        """
        computes Q1 and Q3
        """

        if not self._validate(x):
            return None

        return [self.percentile(x, 25), self.percentile(x, 75)]


    def var(self, x):
        """
        computes sample variance
        """

        if not self._validate(x):
            return None
        n = len(x)
        if n < 2:
            return None
        mean_value = self.mean(x)
        total = 0

        for value in x:
            total += (float(value) - mean_value) ** 2
        return float(total / (n - 1))


    def std(self, x):
        """
        computes sample standard deviation
        """
        variance = self.var(x)
        if variance is None:
            return None

        return float(math.sqrt(variance))
