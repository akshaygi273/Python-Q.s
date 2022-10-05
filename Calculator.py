# 1. Provide a program for the calculator from terminal.
# • Make sure it do not ask questions but when you press enter. it displays the result.
# • Amount and formula has to be in one line.
# e.g 456 - 12
# 564/ 10
# 456*1234+09-12



while True:
    try: 
        exp=input('Enter the expression  ')

        print(eval(exp))
    
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    except Exception as e:
        print(e)
    