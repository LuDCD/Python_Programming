#!/usr/bin/python
# -*- coding:utf8 -*-

import sys
from parent_directory.notebook import Note,Notebook

class Menu:
    '''
    Display(显示) a menu and respond to(回应) choices when run
    '''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_note,
            '2': self.search_note,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit,
        }

    def display_menu(self):
        print('''
        Notebook Menu

        1.Show all Note
        2.Search Notes
        3.Add Note
        4.Modify Note
        5.Quit
        ''')

    def run(self):
        '''
        Display the menu and respond to choices
        '''
        while True:
            self.display_menu()
            choice = input('Enter an option:')
            action = self.choices.get(choice)
            # print(action )
            # print(type(action))
            if action:
                action()
                # print(1)
            else:
                print('{0} is not a valid choice'.format(choice))

    def show_note(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print('{0}:{1}\n\t{2}'.format(note.id, note.tags, note.memo))

    def search_note(self):
        filter = input("Search for :")
        notes =self.notebook.search(filter)
        self.show_note(notes)


    def add_note(self):
        memo = input('Enter a memo:')
        self.notebook.new_note(memo)
        print('Your note has been added.')

    def modify_note(self):
        id = input('Enter a id:')
        memo = input('Enter a memo:')
        tags = input('Enter tags:')

        if memo:
            self.notebook.modify_memo(memo)
        if tags:
            self.notebook.modify_tags(tags)


    def quit(self):
        print('Thank you for using your notebook today.')
        sys.exit(0)

if __name__ == '__main__':
    # menu = Menu()
    Menu.run()