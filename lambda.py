#def square(num): return num ** 2
#square = lambda num: num ** 2
numbers = [1,3,5,9,10,4]

#result = list(map(square, numbers))
#for item in map(square, numbers):
#     print(item)

#def check_even(num): return num%2==0

#result = list(filter(check_even, numbers))

check_even = lambda num: num%2==0
#result = list(filter(lambda num: num%2==0, numbers))
# result = square(3)
result = list(filter(check_even, numbers))

result = check_even(numbers[2])

print(result)