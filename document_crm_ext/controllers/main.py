from odoo.addons.documents.controllers.main import ShareRoute
from odoo import http
from odoo.http import request
import json


class ShareRouteExt(ShareRoute):

    @http.route()
    def upload_document(self, **kwargs):
        kwargs.update({'tag_ids':''})
        documents_res = super(ShareRouteExt, self).upload_document(**kwargs)
        documents = json.loads(documents_res.data).get('ids', False)
        documents = documents and request.env['documents.document'].sudo().browse(documents)
        if documents and kwargs.get('crm_id'):
            documents.write({'crm_id': int(kwargs.get('crm_id'))})
        return documents_res
