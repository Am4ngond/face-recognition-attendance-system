def calculate(n1,n2,op):
 if op == '+':
  return n1 + n2
 elif op == '-':
  return n1 - n2
 elif op == '*':
  return n1 * n2
 elif op == '/':
  return n1 / n2
 else:
  return "Invalid operator"

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculate(num_1, num_2, operator)

print(result)
