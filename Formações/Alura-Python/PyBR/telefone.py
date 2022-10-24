import re

class TelefonesBr:
    def __init__(self, phone):
        if self.verify_phone(phone):
            self.number = phone
        else:
            raise ValueError('Número invalido!')
    
    def verify_phone(self, phone):
        pattern = "([0-9]{2,3}?)?([0-9]{2})([9]?[0-9]{4})([0-9]{4})"
        answer = re.search(pattern, phone)
        if answer:
            return True
        else:
            return False

    def format_num(self):
        pattern = "([0-9]{2,3}?)?([0-9]{2})([9]?[0-9]{4})([0-9]{4}$)"
        answer = re.search(pattern, self.number)
        if answer.group(1) is None:
            num_format = f'({answer.group(2)}) {answer.group(3)}-{answer.group(4)}'
        else:
            num_format = f'+{answer.group(1)} ({answer.group(2)}) {answer.group(3)}-{answer.group(4)}'
        return num_format

    def __str__(self):
        return self.format_num()