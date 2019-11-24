#Site App::: version 1.0.0
#Created on 12 Nov, 2019
#Author Consite Lab:::Rogers M.M

from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivymd.theming import ThemeManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty, StringProperty
import app_database as db
import update_homescreen as home_screen
from kivy.clock import Clock
import time
from datetime import datetime
from os.path import exists


class Controller(FloatLayout):
    materialname = ObjectProperty()
    quantity = ObjectProperty()
    unitprice = ObjectProperty()
    materialdate = ObjectProperty()

    category = ObjectProperty()
    labornumber = ObjectProperty()
    wage = ObjectProperty()
    date = ObjectProperty()

    expensetype = ObjectProperty()
    expensedate = ObjectProperty()
    expenseamount = ObjectProperty()

    misctype = ObjectProperty()
    miscamount = ObjectProperty()
    miscdate = ObjectProperty()

    projectname = ObjectProperty()
    projecttype = ObjectProperty()
    startdate = ObjectProperty()
    completiondate = ObjectProperty()
    estimatedcost = ObjectProperty()

    contactname = ObjectProperty()
    contact = ObjectProperty()

    project_files = StringProperty('project.txt')

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)

        try:
            if not exists(self.project_files):
                self.ids.screen_manager.current = 'home'
            else:            
                self.update_material_label()
                self.update_labor_label()
                self.update_expenses_label()
                self.update_total_project_cost_label()
        except:
            pass       


#--------------------------DATE PICKERS------------------------------------- 
    def date_picker(self, funct):
        picker = MDDatePicker(funct)
        picker.open()

    def get_material_date(self, the_date):
        date = str(the_date)
        self.ids.materialdate.text = date

    def get_expenses_date(self, the_date):
        date = str(the_date)
        self.ids.expensedate.text = date

    def get_misc_date(self, the_date):
        date = str(the_date)
        self.ids.miscdate.text = date

    def get_labor_date(self, the_date):
        date = str(the_date)
        self.ids.labordate.text = date

    def get_new_project_completion_date(self, the_date):
        date = str(the_date)
        self.ids.completiondate.text = date

    def get_new_project_start_date(self, the_date):
        date = str(the_date)
        self.ids.startdate.text = date


#-------------------------SAVES RECORDS TO THE DATABASE---------------------------------------------------------
    def submit_materials(self):
        db.save_materials(self.materialname.text, self.quantity.text, self.unitprice.text, self.materialdate.text)

    def submit_labor(self):
        db.save_labor(self.category.text, self.labornumber.text, self.wage.text, self.date.text)
    
    def submit_expenses(self):
        db.save_expenses(self.expensetype.text, self.expensedate.text, self.expenseamount.text)

    def submit_misc(self):
        db.save_misc(self.misctype.text, self.miscamount.text, self.miscdate.text)

    def create_new_project(self):
        db.create_new_project(self.projectname.text, self.projecttype.text, self.startdate.text, self.estimatedcost.text, self.completiondate.text)

    def submit_contact(self):
        db.save_contact(self.contactname.text, self.contact.text)


#--------------------------------------CLEARS THE TEXTINPUT FIELDS--------------------------------------------------------
    def clear_material_screen(self):
        self.materialname.text = ''
        self.quantity.text = ''
        self.unitprice.text = ''
        self.materialdate.text = ''

    def clear_labor_screen(self):
        self.category.text = ''
        self.labornumber.text = ''
        self.wage.text = ''
        self.date.text = ''

    def clear_expenses_screen(self):
        self.expenseamount.text = ''
        self.expensedate.text = ''
        self.expensetype.text = ''

    def clear_misc_screen(self):
        self.misctype.text = ''
        self.miscamount.text = ''
        self.miscdate.text = ''

    def clear_new_project_screen(self):
        self.projecttype.text = ''
        self.estimatedcost.text = ''
        self.projectname.text = ''
        self.startdate.text = ''
        self.completiondate.text = ''
        self.estimatedcost.text = ''

    def clear_contact_screen(self):
        self.contact.text = ''
        self.contactname.text = ''


#--------------------------------HOME SCREEN METHODS----------------------------------
    def update_material_label(self):
        self.ids.home_material_amount_label.text = home_screen.update_material()

    def update_labor_label(self):
        self.ids.home_labor_amount_label.text = home_screen.update_labor()

    def update_expenses_label(self):
        self.ids.home_expense_amount_label.text = home_screen.update_expenses()

    def update_total_project_cost_label(self):
        self.ids.home_project_amount_label.text = home_screen.update_total_project_cost()


class mainApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    theme_cls.accent_palette = 'Blue'
    theme_cls.theme_style = 'Light'   

    def build(self):
        self.title = 'SiteApp'
        return Controller()          

if __name__ == '__main__':
    mainApp().run()