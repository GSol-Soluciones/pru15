# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import base64


class Document(models.Model):
    _inherit = "documents.document"

    crm_id = fields.Many2one("crm.lead", string="Opportunity")


class CrmLead(models.Model):
    _inherit = "crm.lead"

    document_count = fields.Integer(string='Documents', compute="_compute_document_count")

#    def auto_check_document_exist(self):
#        lead_obj = self.env['crm.lead'].search([('document_count','>',0),('exist_docs','!=',True)])
#        folder_id = self.env['documents.folder'].search([('name', '=', 'Marketing')])
#        for lead in lead_obj:
#             document_ids = self.env['documents.document'].search_count([('crm_id', '=', lead.id),('folder_id','=',folder_id.id)])
#            if document_ids:
#                lead.exist_docs = True

    def _compute_document_count(self):
        for rec in self:
            rec.document_count = self.env['documents.document'].search_count([('crm_id', '=', rec.id)])

    def action_open_crm_documents(self):
        self.ensure_one()
        return {
            'name': _('Documents'),
            'res_model': 'documents.document',
            'type': 'ir.actions.act_window',
            'views': [(False, 'kanban')],
            'view_mode': 'kanban',
            'context': {
                "search_default_crm_id": self.id,
                "default_crm_id": self.id,
                "searchpanel_default_folder_id": False
            },
        }
