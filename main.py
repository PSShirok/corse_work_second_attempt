from utils import load_operations, sort_operation_by_data, get_operation_last_x, print_check, masked_number

card_operations = load_operations()

sort_operations = sort_operation_by_data(card_operations)

last_operations = get_operation_last_x(sort_operations, 5)

for operation in last_operations:
    if "from" in operation:
        operation["from"] = masked_number(operation["from"])
    operation["to"] = masked_number(operation["to"])

show_check = print_check(last_operations)

for operation in show_check:
    print(operation)
