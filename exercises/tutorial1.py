
start = 1
end = 10

a,b,c = 0,1,0
fib_values = []

for i in range(start,end):
    c = a + b
    a = b
    b = c

    if c == 0:
        fib_values.append(i)
    else:
        fib_values.append(c)

print(fib_values)

