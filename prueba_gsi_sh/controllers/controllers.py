# -*- coding: utf-8 -*-
# from odoo import http


# class PruebaGsiSh(http.Controller):
#     @http.route('/prueba_gsi_sh/prueba_gsi_sh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba_gsi_sh/prueba_gsi_sh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba_gsi_sh.listing', {
#             'root': '/prueba_gsi_sh/prueba_gsi_sh',
#             'objects': http.request.env['prueba_gsi_sh.prueba_gsi_sh'].search([]),
#         })

#     @http.route('/prueba_gsi_sh/prueba_gsi_sh/objects/<model("prueba_gsi_sh.prueba_gsi_sh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba_gsi_sh.object', {
#             'object': obj
#         })
