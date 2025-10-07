def table_for(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def table_while(n):
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n*i}")
        i += 1

def table_do_while(n):
    i = 1
    while True:
        print(f"{n} x {i} = {n*i}")
        i += 1
        if i > 10:
            break

# Test
num = 2
print("For Loop:")
table_for(num)
print("\nWhile Loop:")
table_while(num)
print("\nDo-While Simulation:")
table_do_while(num)