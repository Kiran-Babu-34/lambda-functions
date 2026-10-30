add=lambda a,b,c:a+b+c
print(add(10,2,14))

# even or odd number
# =======================
even=lambda a:"even" if a%2==0 else "odd"
print(even(2))

# vote eligible or not
# =======================
vote=lambda a: "elegible" if a>=18 else "not eligible"
print(vote(18))


     # cubes 
# ==========================
cubes=lambda a:a**3
print(cubes(3))


# leap year
# ===============

year=lambda a: "leap yaer" if a%400==0 or( a%4==0 and  a%100!=0) else "not a leap year"
print(year(2024))

# divisible by 5 and 10
# ============================

divisible=lambda a:"divisible" if a%5==0 and  a%10==0 else "not divisible"
print(divisible(20))

# enter pin and user name valid or not
pin=lambda a:"valid" if a==1234 else "invalid"
print(pin(123))

# check person is failed or passed
marks=lambda a:"pass" if a>=25 else "fail"
print(marks(25))

# enter digits r multiple or not
is_multi_digit = lambda num: abs(num) >= 10

print(is_multi_digit(5))     

# prime number
prime_number = lambda a: "prime number" if a > 1 and sum(1 for i in range(1, a + 1) if a % i == 0) == 2 else "not a prime"

print(prime_number(2))