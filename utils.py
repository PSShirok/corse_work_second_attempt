import json
import datetime


def load_operations():
    """
    берем файл с операциями для работы
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


def sort_operation_by_data(operations):
    """
    принимает файл с операциями, возвращает сортировку по дате
    :param operations: файл с операциями
    :return: сортировка по дате
    """
    date_operations = []
    for operation in operations:
        if "date" in operation:
            date_operations.append(operation)
    sort_by_date = sorted(date_operations, key=lambda x: x["date"], reverse=True)
    return sort_by_date


def get_operation_last_x(operations, how_many_operations):
    """
    :param operations: список словарей с операциями
    :param how_many_operations: какое количество операций
    :return: возвращает количество операций подходящих под условие "EXECUTED"
    """
    last_x_operations = []
    for operation in operations:
        if operation['state'] == "EXECUTED":
            last_x_operations.append(operation)
            if len(last_x_operations) == how_many_operations:
                break
    return last_x_operations


def print_check(last_operations):
    """
    вывод операциии
    :param last_operations: список словарей операций
    :return: возврат статистики в определнном формате
    """
    last_operations_list = []
    for operation in last_operations:
        date_operation = datetime.datetime.strptime(operation["date"], '%Y-%m-%dT%H:%M:%S.%f')
        last_operations_list.append(f"""{date_operation.strftime("%d.%m.%Y")} {operation["description"]}
{operation["from"] if 'from' in operation else ""} -> {operation["to"]}
{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n""")
    return last_operations_list


def masked_number(account):
    mask_number = account.split()[-1]
    mask_is_alpha = ["" if num.isdigit() else num for num in account]
    if len(mask_number) == 20:
        return "".join(mask_is_alpha)+f"** {mask_number[-4:]}"
    else:
        return "".join(mask_is_alpha) + f"{mask_number[:4]} {mask_number[5:7]}** **** {mask_number[-4:]}"
