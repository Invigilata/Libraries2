def introspection_info(obj):
    """
    Функция для проведения интроспекции объекта.

    :param obj: объект для интроспекции
    :return: словарь с данными об объекте
    """
    info = {}

    # Тип объекта
    info['type'] = type(obj).__name__

    # Атрибуты и методы объекта
    attributes = []
    methods = []
    for attribute in dir(obj):
        if callable(getattr(obj, attribute)):
            methods.append(attribute)
        else:
            attributes.append(attribute)

    info['attributes'] = attributes
    info['methods'] = methods

    info['module'] = obj.__class__.__module__

    if hasattr(obj, '__doc__'):
        info['docstring'] = obj.__doc__

    if hasattr(obj, '__name__'):
        info['object_name'] = obj.__name__

    if hasattr(obj, '__class__'):
        info['class_name'] = obj.__class__.__name__

    return info


# Пример использования функции
number_info = introspection_info(42)
print(number_info)


# Создание собственного класса для демонстрации
class MyClass:
    """
    Пример пользовательского класса для демонстрации интроспекции.
    """

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return self.value

    @classmethod
    def class_method(cls):
        return "This is a class method."

    @staticmethod
    def static_method():
        return "This is a static method."


# Создание объекта класса MyClass
my_object = MyClass(123)

# Пример использования функции с объектом класса MyClass
object_info = introspection_info(my_object)
print(object_info)
