from utils import load_operations, sort_operation_by_data, get_operation_last_x, print_check

card_operations = load_operations()

sort_operations = sort_operation_by_data(card_operations)

last_operations = get_operation_last_x(sort_operations, 5)

print_check(last_operations)