from employee import Employee

def test_give_default_raise():
    emp = Employee('John', 'Doe', 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000

def test_give_custom_raise():
    emp = Employee('Jane', 'Smith', 60000)
    emp.give_raise(10000)
    assert emp.annual_salary == 70000