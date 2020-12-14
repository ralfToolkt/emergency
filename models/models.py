# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    def create_new_user(self, username, password, name):
        new_user = self.create({
            'login': kw['username'],
            'password': kw['password'],
            'name': kw['name'],
            # 'email': kw['email'],
            # 'sel_groups_1_8_9': 9
        })

        return new_user

class emergency(models.Model):
    _name = 'emergency'
    _description = 'emergency table'

    name = fields.Char()
    longitude = fields.Float()
    latitude = fields.Float()
    accuracy = fields.Float()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
