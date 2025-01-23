def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return "Unhandled TypeError"
        else:
            return "Invalid input types"

#Example of the uncommon error
print(function_with_uncommon_error(10,0)) #Division by zero
print(function_with_uncommon_error(10,'a')) #Invalid input types
print(function_with_uncommon_error(10,2)) #5.0
print(function_with_uncommon_error('a',2)) #Invalid input types
print(function_with_uncommon_error(10,0.0)) #Division by zero
print(function_with_uncommon_error(10.0,0.0)) #Division by zero
print(function_with_uncommon_error(10.0, 2)) #5.0
print(function_with_uncommon_error(10, 2.0)) #5.0