

class Notification:
    """Расшифровка значений:
    number=None - Номер набора данных для теста. Обязателен для отслеживания на каком наборе данных упало
    rn=None - перечень РН Партнёров, для позитивных кейсов - только перечень корректного формата. None - пропуск
    checkbox - True = Стоит / False  = не стоит
    level=None - Уровень уведомления. Если указано - выбирать только из существующих вариантов. Иначе - None
    notif_type=None - Тип уведомления. Если указано - выбирать только из существующих вариантов. Иначе - None
    header=None - Заголовок уведомления. Если указано - вводим текст уведомления. Иначе - None
    text=None - Текст уведомления. Если указано - вводим текст уведомления. Иначе - None
    bname=None - Имя кнопки. Если указано - выбирать только из существующих вариантов. Иначе - None
    blink=None - Ссылка на кнопке. Если указано - выбирать только из существующих вариантов. Иначе - None
    """
    def __init__(self, number=None, rn=None, checkbox: bool = False,
                 level=None,
                 notif_type=None,
                 header=None,
                 text=None,
                 bname=None,
                 blink=None,
                 snack=None):

        self.number = number
        self.rn = rn
        self.checkbox = checkbox
        self.level = level
        self.notif_type = notif_type
        self.header = header
        self.text = text
        self.bname = bname
        self.blink = blink
        self.snack = snack

    def __repr__(self):
        return ("%s[%s|%s|%s|%s|%s|%s|%s|%s]" % (self.number, self.rn, self.checkbox, self.level,
                self.notif_type, self.header, self.text, self.bname, self.blink))

    def __eq__(self, other):
        # Закомментировано потому что в уже созданном уведомлении пока нельзя достать значения из текстовых полей
        return (
                # self.rn == other.rn and
                self.checkbox == other.checkbox and
                self.level == other.level and
                self.notif_type == other.notif_type
                # and self.header == other.header
                # and self.text == other.text
                # and self.bname == other.bname
                # and self.blink == other.blink
                )

