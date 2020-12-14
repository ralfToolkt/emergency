# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    token = fields.Char(
        string='token',
    )

class Location(models.Model):
    _name = 'location'
    _description = 'Location that send by the emergency button'

    
    date_time = fields.Datetime(
        string='Date Time',
        default=fields.Datetime.now,
    )
    
    
    user_id = fields.Many2one(
        string='user',
        comodel_name='location',
    )
    
    
    longitude = fields.Float(
        string='longitude',
    )
    
    latitude = fields.Float(
        string='latitude',
    )
    
    city = fields.Char(
        string='city',
    )
    
    country = fields.Char(
        string='country',
    )
    
    district = fields.Char(
        string='district',
    )
    
    isoCountryCode = fields.Char(
        string='isoCountryCode',
    )
    
    name = fields.Char(
        string='name',
    )
    
    postalCode = fields.Char(
        string='postalCode',
    )
    
    region = fields.Char(
        string='region',
    )
    
    street = fields.Char(
        string='street',
    )

    
    
    

class emergency(models.Model):
    _name = 'emergency'
    _description = 'emergency table'

    name = fields.Char()
    longitude = fields.Float()
    latitude = fields.Float()
    accuracy = fields.Float()

