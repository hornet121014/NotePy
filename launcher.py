from datetime import datetime

import view
from cs import CS
from jsonservice import JSONService
from model import Model
from note import Note
from view import View


def init():
    fname = "notes.json"
    run = Model(JSONService(fname), View())
    try:
        while True:
            print('\nГлавное меню:')
            choice = input(
                '0. закрыть приложение\n'
                '1. загрузить все заметки\n'
                '2. добавить заметку\n'
                '3. загрузить заметку\n'
                '4. обновить заметку\n'
                '5. удалить заметку\n'
                '6. удалить все заметки\n\n'
                'выберите команду: '
            )
            if choice == '0':
                break
            elif choice == '1':
                run.loadNotes()
            elif choice == '2':
               run.addNote(getNoteData())
            elif choice == '3':
               run.loadNote(getId())
            elif choice == '4':
                id = getId()
                if run.idExist(id):
                    run.updateNote(id, getNoteData())
            elif choice == '5':
                id = getId()
                if run.idExist(id):
                    run.delNote(id)
            elif choice == '6':
                run.delNotes()
            else:
                CS.msgError("\nВведите корректные данные.")
    except:
        print()


def getDateStamp():
    return datetime.now().strftime("%Y.%m.%d %H:%M:%S")

def getNoteData():
    print("\nЗаполните данные заметки ")
    title = input("- введите заголовок: ")
    body = input("- введите содержание: ")
    date = getDateStamp()
    idn = 0
    return Note(idn, title, body, date)

def getId():
    try:
        numid = input("\nВведите id заметки: ")
        return int(numid)
    except:
        return numid