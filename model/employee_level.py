from odoo import models, fields,api
from functools import reduce


class EmployeeLevel(models.Model):
    _inherit = 'hr.employee'
    _description = 'EmployeeLevels'

    level_id = fields.Many2one('employee.level', string='Level', readonly=True)
    salary_id = fields.Float(related="level_id.salary", string='Salary',
                             readonly=True)
    hide_button = fields.Boolean(string='Hide')
    count = fields.Integer(default=0)

    def promote(self):
        list= []
        for i in self.env['employee.level'].search([]):
            list.append(i.id)
        self.level_id = list[self.count]
        self.count += 1

        def my_max(x, y):
            if x < y:
                return y
            else:
                return x
        max_height = reduce(my_max, list)
        print(max_height)
        if max_height == self.level_id.id:
            self.hide_button = True


class EmployeeDetails(models.Model):
    _name = 'employee.level'
    _rec_name = "level"

    level = fields.Char(string='Level')
    salary = fields.Float(string='Salary')

    # print(max_value)
    # if self.level_id == max(i):
    #     self.hide_button = True

    # if not self.level_id:
    # print(self.level_id.id)
    # self.level_id = self.level_id.id + 1
    # for i in self.env['employee.level'].search([]):
    #         if not self.level_id:
    #             self.level_id = i.id
    #         else:
    #             self.level_id = self.level_id.id+1```