class Shape:
    def __init__(self):
        if self.__class__.__name__ == 'Shape':
            raise TypeError('Cannot instantiate from base class')

    def area(self):
        raise TypeError('Area is not implemented')

    def perimeter(self):
        raise TypeError('Perimeter is not implemented')
