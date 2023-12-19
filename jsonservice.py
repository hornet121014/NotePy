import json

import os.path
import view
from note import Note


class JSONService(object):

    def __init__(self, fname):
        self.fname = fname
        if self.fileExist(self.fname):
            self.notes = self.readFile()
        else:
            self.notes = list()

    def addNote(self, note):
        try:
            id = 0
            for item in self.notes:
                if item.idn > id:
                    id = item.idn
            idn = id + 1
            note.idn = idn
            self.notes.append(note)
            self.writeFile(self.notes)
            return True
        except:
            return False

    def loadNote(self, id):
        if self.idExist(id):
            for note in self.notes:
                if note.idn == id:
                    return note
        else:
            view.notIdExist(id)

    def updateNote(self, id, note):
        try:
            if self.idExist(id):
                for item in self.notes:
                    if item.idn == id:
                        item.title = note.title
                        item.body = note.body
                        item.date = note.date
                self.writeFile(self.notes)
                return True
            else:
                return False
        except:
            return False

    def delNote(self, id):
        try:
            for i, note in enumerate(self.notes):
                if note.idn == id:
                    del self.notes[i]
            self.writeFile(self.notes)
            return True
        except:
            return False

    def delNotes(self):
        try:
            if self.fileExist(self.fname):
                self.notes.clear()
                self.writeFile(self.notes)
                return True
            else: return False
        except:
            return False

    def writeFile(self, notes):
        mylist = list()
        for note in notes:
            mylist.append({'id': note.idn, 'title': note.title, 'body': note.body, 'date': note.date})
        mynotes = json.dumps(mylist, indent=3, ensure_ascii=False)
        with open(self.fname, "w", encoding='utf-8') as f:
            f.write(mynotes)

    def readFile(self):
        notes = list()
        try:
            with open(self.fname, "r", encoding='utf-8') as f:
                mynotes = f.read()
            data = json.loads(mynotes)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes.append(Note(item['id'], item['title'], item['body'], item['date']))
            return notes
        except:
            # view.emptyNotes()
            return self.notes

    def idExist(self, id):
        try:
            for note in self.notes:
                if note.idn == id:
                    return True
            else:
                return False
        except: return False

    def fileExist(self, fname):
        try:
            if os.path.isfile(fname):
                return True
        except:
            return False

