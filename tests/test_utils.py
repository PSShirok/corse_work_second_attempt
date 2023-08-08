from utils import sort_operation_by_data, get_operation_last_x, masked_number

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
  assert  masked_number(test_list) == [{'date': '2019-08-26T10:50:58.294041',
  'description': 'Перевод организации',
  'from': 'Maestro 1596 37** **** 5199',
  'id': 441945886,
  'operationAmount': {'amount': '31957.58',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет ** 9589'},
 {'date': '2019-07-03T18:35:29.512364',
  'description': 'Перевод организации',
  'from': 'MasterCard 7158 00** **** 6758',
  'id': 41428829,
  'operationAmount': {'amount': '8221.37',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет ** 5560'}]

def print_check():
  assert print_check(test_list)
