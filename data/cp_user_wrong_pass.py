# набор валидных логинов и невалидных паролей для проверки авторизации в ПУ


testdata = [
    ('admin@svrauto.ru', '123456789')
   ,('admin@svrauto.ru', 'somewrongpass')
   ,('admin@svrauto.ru', 'parol')
   ,('admin@svrauto.ru', 'admin@svrauto.ru')
   ,('admin@svrauto.ru', 'qwerty')
   ,('admin@svrauto.ru', 'password')
   ,('admin@svrauto.ru', 'skgjalksdjfhalsdjfhk')
            ]
