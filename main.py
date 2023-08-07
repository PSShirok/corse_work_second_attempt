from utils import load_operations, sort_operation_by_data, get_operation_last_x, print_check, masked_number

card_operations = load_operations()

sort_operations = sort_operation_by_data(card_operations)

last_operations = get_operation_last_x(sort_operations, 5)

masked_account = masked_number(last_operations)

print_check(masked_account)

