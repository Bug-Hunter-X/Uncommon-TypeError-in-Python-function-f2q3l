def function_with_uncommon_error_solution(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Invalid input types: a and b must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return str(e)

#Example of the uncommon error
print(function_with_uncommon_error_solution(10,0)) #Division by zero
print(function_with_uncommon_error_solution(10,'a')) #Invalid input types: a and b must be numbers
print(function_with_uncommon_error_solution(10,2)) #5.0
print(function_with_uncommon_error_solution('a',2)) #Invalid input types: a and b must be numbers
print(function_with_uncommon_error_solution(10,0.0)) #Division by zero
print(function_with_uncommon_error_solution(10.0,0.0)) #Division by zero
print(function_with_uncommon_error_solution(10.0, 2)) #5.0
print(function_with_uncommon_error_solution(10, 2.0)) #5.0