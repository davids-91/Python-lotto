import lotto

print("Welcome! This is lotto game.")
print("Enter six values in range 1-49.")

number_list = lotto.get_input()

if not(lotto.check_number_count(number_list)):
    print("You should enter exactly six numbers!")
elif not(lotto.check_unique(number_list)):
    print("Numbers are not unique!")
elif not(lotto.check_range(number_list)):
    print("Numbers are not in given range!")
else:
    random_numbers = lotto.generate_random_numbers()
    lotto.compare_results_and_output(random_numbers, number_list)

