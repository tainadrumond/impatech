def relatively_prime(num1, num2):
    smallest_num = num1 if num1 < num2 else num2
    numbers_to_evaluate = list(range(2, int(smallest_num/2)+1))
    numbers_to_evaluate.append(smallest_num)
    for i in numbers_to_evaluate:
        if ((num1%i == 0) & (num2%i == 0)):
            return False
    return True
    

are_relatively_prime = relatively_prime(6, 9)
print(are_relatively_prime)
