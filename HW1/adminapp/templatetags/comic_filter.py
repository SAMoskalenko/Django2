from django import template

register = template.Library()


def comic(text):
    result = text.title()
    new_result = result[:-1]
    new_result += result[-1].upper()
    return new_result


register.filter('comic', comic)


def get_python_type(product):
    result = type(product)
    return result


register.filter('get_python_type', get_python_type)

# if __name__ == '__main__':
#     print(comic('дом'))
#     print(comic('Гараж'))
#
#     print(get_python_type([]))
