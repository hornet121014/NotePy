from cs import CS


class View(object):

    @staticmethod
    def addNote(flag):
        if flag:
            CS.msgTrue("\nЗаметка успешно добавлена")
        else:
            CS.msgError("\nОшибка. Заметка не добавлена")

    @staticmethod
    def printNote(note):
        print(note)

    @staticmethod
    def printNotes(notes):
        if len(notes) != 0:
            for item in notes:
                print(item)
        else:
            emptyNotes()

    @staticmethod
    def updateNote(flag):
        if flag:
            CS.msgTrue("\nЗаметка успешно обновлена")
        else:
            CS.msgError("\nОшибка. Заметка не обновлена")

    @staticmethod
    def delNote(flag):
        if flag:
            CS.msgTrue("\nЗаметка успешно удалена")
        else:
            CS.msgError("\nОшибка. Заметка не удалена")

    @staticmethod
    def delNotes(flag):
        if flag:
            CS.msgTrue("\nВсе заметки успешно удалены")
        else:
            CS.msgError("\nОшибка. Заметки не удалены")
            emptyNotes()


def emptyNotes():
    CS.msgError("\nСписок заметок пуст, либо файла не существует.")


def notIdExist(id):
    CS.msgError(f"\nЗаметки с id = {id} не существует. Проверьте корректность введенных данных")
