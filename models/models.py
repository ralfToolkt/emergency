# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    token = fields.Char(
        string='token',
    )

    # def create_new_user(self, username, password, name):
    #     new_user = self.create({
    #         'login': username,
    #         'password': password,
    #         'name': name,
    #     })

    #     return new_user

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
