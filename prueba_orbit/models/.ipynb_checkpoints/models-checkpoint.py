# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class prueba_orbit(models.Model):
#     _name = 'prueba_orbit.prueba_orbit'
#     _description = 'prueba_orbit.prueba_orbit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import fields, models


class CRM(models.Model):
    _inherit = 'crm.lead'

    # ('category_id.name', '=', 'Cliente')
    partner_id = fields.Many2one(
        'res.partner', string='Customer', index=True, tracking=10,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id), ('customer_rank','>', 0)] ",
        help="Linked partner ...")
        
    contact_id = fields.Many2one('res.partner', string='Contact')
