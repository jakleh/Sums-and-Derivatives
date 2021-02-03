base_num = 0
def calculate_sum(num):
    our_num = num

    if (our_num == 1):
        return our_num
    if (our_num < 1):
        return "Invalid input"
    else:
        item_increase = (2 * our_num) - 1
        our_num -=1
        return item_increase + calculate_sum(our_num)

print(calculate_sum(5))

