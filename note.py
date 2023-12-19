class Note(object):

    def __init__(self, idn, title, body, date):
        self.idn = idn
        self.title = title
        self.body = body
        self.date = date

    def __str__(self):
        return (f'Заметка: {self.idn}\n'
                f'Заголовок: {self.title}\n'
                f'Содержание: {self.body}\n'
                f'Дата последнего изменения: {self.date}\n')
