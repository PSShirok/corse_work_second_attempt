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
    sort_by_date = sorted(date_operations, key=lambda x: operation["date"])
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
    for operation in last_operations:
        date_operation = datetime.datetime.strptime(operation["date"], '%Y-%m-%dT%H:%M:%S.%f')
        print(f"""{date_operation.strftime("%d.%m.%Y")} {operation["description"]}
{operation["from"] if 'from' in operation else ""} -> {operation["to"]}
{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n""")

# def print_operations():
#     """
#     :return: вывод статистики в нужном формате
#     """
#     date_operations = get_date_sort()
#     date_operations.reverse()
#     for payment_date in date_operations:
#         for operation in card_operations:
#             if "date" in operation:
#                 if operation['date'] == payment_date:
#                     date_operation = datetime.datetime.strptime(payment_date, '%Y-%m-%dT%H:%M:%S.%f')
#                     print(f"""{date_operation.strftime("%d.%m.%Y")} {operation["description"]}
# {format_from(operation["from"]) if 'from' in operation else ""} -> {format_from(operation["to"])}
# {operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n""")