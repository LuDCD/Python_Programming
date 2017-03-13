#!/usr/bin/python
# -*- coding:utf8 -*-

import datetime

class Note:
    '''
    Represent a note in the notebook. Match against a string in searching and store tags for each note
    '''

    def __init__(self, memo, tags=''):# memo 备忘录
        '''
        initialize a note with memo and optional spase-separated tags. Automatically set the not's creation date
        and unique id.
        :param memo:
        :param tags:
        :return:
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''
        Determine(确定) if this note matches the filter text.Return Ture if it matches,False otherwise(除此之外).

        Search is case sensitive and matches both text and tags.
        case sensitive 区分大小写
        '''
        return filter in self.memo or filter in self.tags


class Notebook:
    '''
    Represent a collection of notes that can be tagged, modified(修改), and search.
    '''

    def __init__(self):
        '''
        Initialize a notebook with an empty list.
        '''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list.
        '''
        self.notes.append(Note(memo,tags))

    def _find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''
        Find the note eith given id and change its memo to the given value.
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False


    def modify_tags(self, note_id, tags):
        '''
        Find the note eith given id and change its tags to the given value.
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = tags
            return True
        return False

    def search(self, filter):
        '''
        Find all note that match the given filter string
        :param filter:
        :return:list
        '''
        return [note for note in self.notes if note.match(filter)]

        # notes = []
        # for note in self.notes:
        #     if note.match(filter):
        #         notes.append(note)