from tkinter import *
from models import session, Contact
from datetime import datetime, date

class Table:
    def __init__(self, root):
        
        contacts = session.query(Contact).all()

        
        lst = []
        for contact in contacts:
            contact_data = [
                contact.id,
                contact.name,
                contact.number,
                contact.email,
                contact.address,
                contact.created_at,
                contact.updated_at,
            ]
            lst.append(contact_data)

        
        total_rows = len(lst)
        total_columns = len(lst[0])

        
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='black', font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])



root = Tk()
t = Table(root)
root.mainloop()
