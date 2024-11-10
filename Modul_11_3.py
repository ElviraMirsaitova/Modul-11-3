import inspect

class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def voice(self):
        print(self.sound)


obj = Horse()
obj.voice()


def introspection_info(obj):
    info = {'тип': type(obj).__name__, 'атрибуты': obj.__dict__, 'методы': dir(obj),
            'модуль': inspect.getmodule(obj)}
    return print(info)

print(introspection_info(obj))

