import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    for length in [4, 8, 12, 16, 20]:
        password = generate_password(length)
        assert len(password) == length

def test_passwords_are_different():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(20)
    password2 = generate_password(20)
    assert password1 != password2