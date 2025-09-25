total = 0

for num in range(100,501):
    if num > 1:
        is_prime = True
        for i in range(2,int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
            if is_prime:
                total += num

                print("sum of prime numbers between 100 and 500 is:", total)
                 

