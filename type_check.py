def type_check(parameter_type):
    def decorator(func):
        def wrapper(param):
            if not isinstance(param, parameter_type):
                return "Bad Type"

            return func(param)
        return wrapper
    return decorator







@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
