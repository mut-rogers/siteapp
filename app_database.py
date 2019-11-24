'''This module saves data to an SQLite Database,
        Tables: materials, labor, expenses, misc, contacts, project details

        Methods: save_materials(), save_labor(), save_expense(), save_misc(), create_new(project)

        '''



import sqlite3 as sq
from sqlite3 import Error
import os.path 
from os.path import exists
from kivymd.uix.dialog import MDDialog

project_files = 'project.txt'



def create_new_project(projectName, projectType, startDate, projectedCost, completionDate):
    '''This method creates a new project together with it database;
            Requires: projectName, projectType, startDate, projectedCost, completionDate'''

    project_database_name = projectName + '.db'
    projects_file = 'project.txt'

    conn = sq.connect(project_database_name)
    cur = conn.cursor()

    try:
        #create tables
        cur.execute('CREATE TABLE IF NOT EXISTS "project_details" (project_id INTEGER PRIMARY KEY AUTOINCREMENT, project_name TEXT NOT NULL, project_type TEXT NOT NULL, projected_cost INTEGER NOT NULL, stard_date TEXT, estimated_date_of_completion TEXT)')
        cur.execute('CREATE TABLE IF NOT EXISTS "materials" (item_id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT NOT NULL, quantity INTEGER NOT NULL, unit_price INTEGER NOT NULL, date TEXT NOT NULL)')
        cur.execute('CREATE TABLE IF NOT EXISTS "labor" (labor_id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT NOT NULL, labor_number INTEGER NOT NULL, wage INTEGER NOT NULL, date TEXT NOT NULL)')
        cur.execute('CREATE TABLE IF NOT EXISTS "expenses" (expense_id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT NOT NULL, amount INTEGER NOT NULL, date TEXT NOT NULL)')
        cur.execute('CREATE TABLE IF NOT EXISTS "misc" (misc_id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT NOT NULL, date TEXT NOT NULL, amount INTEGER NOT NULL)')
        cur.execute('CREATE TABLE IF NOT EXISTS "contacts" (contact_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, contact TEXT NOT NULL)')
        cur.execute('INSERT INTO "project_details" (project_name, project_type, projected_cost, stard_date, estimated_date_of_completion) VALUES(?, ?, ?, ?, ?)', (str(projectName), str(projectType), int(projectedCost), str(startDate), str(completionDate)))

        if not exists(projects_file):
            file_handle = open(projects_file, 'w' )
            file_handle.write(project_database_name)
            file_handle.close()
        else:
            file_handle = open(projects_file, 'a')
            file_handle.write('\n' + project_database_name)
            file_handle.close()
    except Error as err:
        pass

    finally:
        if conn:
            conn.commit()
            cur.close()
            conn.close()



def save_materials(itemName, quantity, unitPrice, date):
    '''This methods saves material records to the App database;
            args>>> itemName, quantity, unitPrice, date'''

    db_name = open(project_files, 'r')
    data = db_name.readlines()    

    conn = sq.connect(data[-1])
    cur = conn.cursor()

    try:        
        if quantity == '' or unitPrice == '':
            quantity = 0
            unitPrice = 0

        cur.execute('INSERT INTO "materials" (item_name, quantity, unit_price, date) VALUES (?,?,?,?)', (str(itemName), int(quantity), int(unitPrice), str(date)))
        
    except Error as err:
        pass
    finally:
        if conn:
            conn.commit()
            cur.close()
            conn.close()
            db_name.close()


def save_labor(category, number, wage, date):
    ''' This method saves labor records to the App database;
            args>>> category, number, wage, advances '''

    db_name = open(project_files, 'r')
    data = db_name.readlines()
    
    conn = sq.connect(data[-1])
    cur = conn.cursor()

    try:
        if number == '' or wage == '' or date == '':
            number = 0
            wage = 0
            date = '2019-01-01'
        
        cur.execute('INSERT INTO "labor" (category, labor_number, wage, date) VALUES(?,?,?,?)', (str(category), int(number), int(wage), str(date)))
        

    except Error as err:
        print (err)

    finally:
        if conn:
            conn.commit()
            cur.close()
            conn.close()
            db_name.close()


def save_expenses(_type, date, amount):

    ''' saves expenses'''
    
    db_name = open(project_files, 'r')
    data = db_name.readlines()

    conn = sq.connect(data[-1])
    cur = conn.cursor()

    try:        
        if amount == '':
            amount = 0

        cur.execute('INSERT INTO "expenses" (type, amount, date) VALUES(?,?,?)', (str(_type), str(date), int(amount)))
        print ('saved successfully')

    except Error as err:
        print (err)

    finally:
        if conn:
            conn.commit()
            cur.close()
            conn.close()
            db_name.close()


def save_misc(_type, amount, date):
    ''' This method saves misclenious expenses:
            args >>>>_type, amount, date 
             '''

    db_name = open(project_files, 'r')
    data = db_name.readlines()

    conn = sq.connect(data[-1])
    cur = conn.cursor()

    try:
        if amount == '':
            amount = 0

        cur.execute('INSERT INTO "misc" (type, date, amount) VALUES(?,?,?)', (str(_type), str(date), int(amount)))
        print ('saved successfully')

    except Error as err:
        print (err)

    finally:
        if conn:
            conn.commit()
            cur.close()
            conn.close()
            db_name.close()


def save_contact(name, contact):
    '''This method saves a new contact:
            args>>> name, contact '''

    db_name = open(project_files, 'r')
    data = db_name.readlines()

    conn = sq.connect(data[-1])
    cur = conn.cursor()

    try:
        cur.execute('INSERT INTO "contacts" (name, contact) VALUES(?,?)', (str(name), str(contact)))

    except Error as err:
        print (err)

    finally:
        if conn:
            conn.commit()
            cur.close()
            conn.close()
            db_name.close()            