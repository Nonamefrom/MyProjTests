testdata = ['invalid @mail.ru'                       # лишний пробел
            , 'invalid_mail.ru'                      # нет @
            , 'invalid_ @mail.ru'                    # лишний пробел кейс символ + пробел
            , 'invalid_ _mail@ya.ru'                 # лишний пробел кейс символ + пробел + символ
            , 'invalid _mail@ya.ru'                  # лишний пробел кейс пробел + символ
            , 'Abc.google.com'                       # нет @
            , 'A@b@c@google.com'                     # много @
            , 'a"b(c)d,e:f;g<h>i[j\k]l@mail.ru'      # спецсимволы
            , 'just"not"right@example.com'           # слово в двойных кавычках
            , 'this is"not\allowed@example.com'      # пробел кавычка и бекслеш
            , 'this\ still\"notallowed@example.com'  # пробел кавычка и бекслеш




            ]
