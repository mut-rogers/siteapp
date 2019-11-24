import sqlite3 as sq 
from sqlite3 import Error 

'''Home Screen Update:::
        This module updates homescreen labels i.e;
            >>project cost
            >>material cost
            >>labor cost
            >>expense cost
            '''
            
project_files = 'project.txt'




def update_material():

    '''This method returns a string of the total amount
    spent on materials'''


    current_db = open(project_files, 'r')
    data = current_db.readlines()

    conn = sq.connect(data[-1])
    cur = conn.cursor()

    total_material_cost = 0
    
    try:
        cur.execute('SELECT * FROM "materials"')
        data = cur.fetchall()

        for record in data:
            quantity = record[2]
            unit_price = record[3]

            buying_price = quantity * unit_price
      
            total_material_cost += buying_price
    
    except Error as err:
        print (err)

    finally:
        if conn:
            cur.close()
            conn.close()
            current_db.close()

    return ('{:,}'.format(total_material_cost))



def update_labor():

    '''This method updates the labor label in home screen with the total amount spent on labor'''

    current_db = open(project_files, 'r')
    data = current_db.readlines()

    conn = sq.connect(data[-1])
    cur = conn.cursor()

    total_labor_cost = 0

    try:
        cur.execute('SELECT * FROM "labor"')
        data = cur.fetchall()
        
        for record in data:
            number = record[2]
            wage = record[3]

            total = number * wage
            total_labor_cost += total

    except Error as err:
        print (err)

    finally:
        if conn:
            cur.close()
            conn.close()
            current_db.close()

    return ('{:,}'.format(total_labor_cost))


def update_expenses():
    '''This method updates the expenses Label with the total amount spent on expenses'''

    current_db = open(project_files, 'r')
    data = current_db.readlines()

    conn = sq.connect(data[-1])
    cur = conn.cursor()

    total_expenses_cost = 0

    try:
        cur.execute('SELECT * FROM "expenses"')

        data = cur.fetchall()
        
        for record in data:
            amount = record[3]

            total_expenses_cost += int(amount)

    except Error as err:
        print (err)

    finally:
        if conn:
            cur.close()
            conn.close()
            current_db.close()
    
    return ('{:,}'.format(total_expenses_cost))




def update_total_project_cost():

    '''This method will update the total Project Cost Label in Home Screen
            by summing up the cost of materials, expenses, labor and misclenious costs'''


    current_db = open(project_files, 'r')
    data = current_db.readlines()

    conn = sq.connect(data[-1])
    cur = conn.cursor()

    material_cost = 0
    labor_cost = 0
    expenses_cost = 0
    misc_cost = 0

    try:
        cur.execute('SELECT * FROM "materials"')
        mat_records = cur.fetchall()
        for record in mat_records:
            qty = record[2]
            unit_price = record[3]

            total = qty * unit_price
            material_cost = material_cost + total

        cur.execute('SELECT * FROM "labor"')
        lab_records = cur.fetchall()
        for record in lab_records:
            number = record[2]
            wage = record[3]

            total = number * wage 
            labor_cost = labor_cost + total

        cur.execute('SELECT * FROM "expenses"')
        exp_records = cur.fetchall()
        for record in exp_records:
            total = record[3]
            expenses_cost = expenses_cost + int(total)

        cur.execute('SELECT * FROM "misc"')
        misc_records = cur.fetchall()
        for record in misc_records:
            total = record[3]
            misc_cost = misc_cost + total



        return ('{:,}'.format(material_cost + labor_cost + expenses_cost + misc_cost))

    except Error as err:
        print (err)

    finally:
        if conn:
            cur.close()
            conn.close()
            current_db.close()
            
        

