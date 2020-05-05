try:
    from ..core.exceptions import typeChecker, typeCheckerArray
except ValueError:
    from core.exceptions import typeChecker, typeCheckerArray


class Gradient:
    def __init__(self, colors, minValue, maxValue):
        """
            Initialization - Creates a gradient object

            :param colors: The array of color codes for this gradient
            :param minValue: The minValue for this gradient
            :param maxValue: The maxValue for this gradient
        """
        self.colors = colors
        self.minValue = minValue
        self.maxValue = maxValue

    @property
    def colors(self):
        return self.__colors

    @colors.setter
    def colors(self, colors):
        typeCheckerArray(type(self).__name__, colors, str, "colors")
        self.__colors = []
        for entry in colors:
            self.__colors.append(entry)

    @property
    def minValue(self):
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue):
        typeChecker(type(self).__name__, minValue, int, "minValue")
        self.__minValue = minValue

    @property
    def maxValue(self):
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue):
        typeChecker(type(self).__name__, maxValue, int, "maxValue")
        self.__maxValue = maxValue

    def get_dict(self):
        """
            Converts the currently loaded gradient file into a dict
            :returns: A dict representation of the current gradient object
        """
        return dict(colors=self.__colors, minValue=self.__minValue,
                    maxValue=self.maxValue)
