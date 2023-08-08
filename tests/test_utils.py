from ..utils import sort_operation_by_data, get_operation_last_x, masked_number, print_check

test_list = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]
def test_sort_operation_by_data():
  assert sort_operation_by_data(test_list) == [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]

def test_get_operation_last_x():
  assert get_operation_last_x(test_list, 1) == [{'date': '2019-08-26T10:50:58.294041',
  'description': 'Перевод организации',
  'from': 'Maestro 1596837868705199',
  'id': 441945886,
  'operationAmount': {'amount': '31957.58',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 64686473678894779589'}]

def test_masked_number():
  assert masked_number("Maestro 1596837868705199") == 'Maestro 1596 37** **** 5199'
  assert masked_number("Счет 15968378687056445199") == 'Счет ** 5199'

def test_print_check():
  assert print_check(test_list) == ['26.08.2019 Перевод организации\n'
 'Maestro 1596837868705199 -> Счет 64686473678894779589\n'
 '31957.58 руб.\n',
 '03.07.2019 Перевод организации\n'
 'MasterCard 7158300734726758 -> Счет 35383033474447895560\n'
 '8221.37 USD\n']
