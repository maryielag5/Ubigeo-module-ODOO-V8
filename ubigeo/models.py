# -*- coding: utf-8 -*-

from openerp import models, fields


class Country_district(models.Model):
    _name = 'res.country.district'
    _description = 'Country State Province Districts'
    province_id = fields.Many2one('res.country.province', 'Province', required=True)
    name = fields.Char('District Name', size=64, required=True)
    code = fields.Char('District Code', size=8, required=True)
    _sql_constraints = [
        ('code_uniq', 'unique(code)', ('The code of the district must be unique !'))
    ]


class Country_province(models.Model):
    _name = 'res.country.province'
    _description = 'Country State Provinces'
    state_id = fields.Many2one('res.country.state', 'State', required=True)
    name = fields.Char('Province Name', size=64, required=True)
    code = fields.Char('Province Code', size=6, required=True)
    district_ids = fields.One2many('res.country.district', 'province_id', 'Districts')
    _sql_constraints = [
        ('code_uniq', 'unique(code)', ('The code of the province must be unique !'))
    ]


class Country_state(models.Model):
    _inherit = 'res.country.state'
    _description = 'Country States'
    province_ids = fields.One2many('res.country.province', 'state_id', 'Provinces')
