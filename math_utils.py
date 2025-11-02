def find_max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
      return (num 1)
    elif num2> num3 and num2 > num3:
      return (num 2)
    else:
      return (num3)

def find_mean(num1, num2, num3):
    find_mean = (num1 + num2 + num3) / 3
    return find_mean

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    find_mean_std = (((num1 - mean_value)**2 + (num2 - mean_value)**2 + (num3 - mean_value)**2) / 3) **0.5
    return (mean, find_mean_std)
