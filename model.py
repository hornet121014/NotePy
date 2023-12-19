import view


class Model(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def loadNotes(self):
        notes = self.model.readFile()
        self.view.printNotes(notes)

    def addNote(self, note):
        flag = self.model.addNote(note)
        self.view.addNote(flag)

    def loadNote(self, id):
        note = self.model.loadNote(id)
        self.view.printNote(note)

    def updateNote(self, id, note):
        flag = self.model.updateNote(id, note)
        self.view.updateNote(flag)
    def delNote(self, id):
        flag = self.model.delNote(id)
        self.view.delNote(flag)

    def delNotes(self):
        flag = self.model.delNotes()
        self.view.delNotes(flag)

    def idExist(self, id):
        if self.model.idExist(id):
            return True
        else:
            view.notIdExist(id)
