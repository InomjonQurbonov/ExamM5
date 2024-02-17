#1-variant:1-savol
def generate_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        son = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(son)
        yield son

n = int(input("Insert N Please:"))

print(f"Fibonachchi sonlari {n} ta elementi:")
for son in generate_fibonacci(n):
    print(son)
