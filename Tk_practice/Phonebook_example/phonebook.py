"""
After I had already started copying this horrible code from this book,
I realized that they do not include any of the GUI code here. So, After
I figure out how to properly write a GUI, I have to come back to here and
add the GUI code. BULLSHIT!
"""

import tkinter
import sqlite3

class Phonebook:
    def __init__(self, master):
        # all widgets got here
        pass

    def create_record(self):
        name = self.namefield.get()
        num = self.numfield.get()
        if name == "":
            self.msg["text"] = "Please enter name"
            return
        if num == "":
            self.msg["text"] = "Please enter number"
            return

        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute("INSERT INTO contacts VALUES (NULL, ?, ?)", (name,
                num))
        conn.commit()
        self.namefield.delete(0, END)
        self.numfield.delete(0, END)
        self.msg['text'] = "Phone Record of %s Added" % name

    def view_records(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        list = c.execute("SELECT * FROM contacts ORDER BY name desc")

        for row in list:
            self.tree.insert("", 0, text=row[1], values=row[2])
        c.close()

    def delete_record(self):
        self.msg['text'] = ""
        conn = sqlite3.connect("phonebook.db")
        c = conn.cursor()
        name = self.tree.item(self.tree.selection())['text']
        query = "DELETE FROM contacts WHERE name = '%s';" % name
        c.execute(query)
        conn.commit()
        c.close()
        self.msg['text'] = 'Phone record for %s Deleted' % name

    def update_record(self, newphone, oldphone, name):
        conn = sqlite3.connect("phonebook.db")
        c = conn.cursor()
        c.execute("UPDATE contact SET contactnumber=? WHERE contactnmber=? AND name=?", (newphone, oldphone, name))
        c.close()
        self.t1.destroy()
        self.msg['text'] = "Phone Number of %s modified" % name