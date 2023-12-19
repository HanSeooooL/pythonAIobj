#Closure: Scope를 활용한 테크닉 혹은 버그 원인

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_instance = outer_function(10) # closure_instance에는 x = 10을 기억하고있는 inner_function의 주소가 기억됨
print(closure_instance)
result = closure_instance(5)
print(result)