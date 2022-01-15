# -*- coding: utf-8 -*-
#????????????????????????????????????????????????????????????????????????????
#?                                                                          ?
#?           ,o888888o.      d888888o.       ,o888888o.     8 8888          ?
#?          8888     `88.  .`8888:' `88.  . 8888     `88.   8 8888          ?
#?       ,8 8888       `8. 8.`8888.   Y8 ,8 8888       `8b  8 8888          ?
#?       88 8888           `8.`8888.     88 8888        `8b 8 8888          ?
#?       88 8888            `8.`8888.    88 8888         88 8 8888          ?
#?       88 8888             `8.`8888.   88 8888         88 8 8888          ?
#?       88 8888   8888888    `8.`8888.  88 8888        ,8P 8 8888          ?
#?       `8 8888       .8'8b   `8.`8888. `8 8888       ,8P  8 8888          ?
#?          8888     ,88' `8b.  ;8.`8888  ` 8888     ,88'   8 8888          ?
#?           `8888888P'    `Y8888P ,88P'     `8888888P'     8 888888888888  ? 
#?                                                                          ?
#?     SOFTWARE DEVELOPED AND SUPPORTED BY GSol Soluciones Informácas       ?
#?                       COPYRIGHT (C) 2020 - TODAY                         ?
#?                           http://www.gsol.es                             ?
#?                                                                          ?
#????????????????????????????????????????????????????????????????????????????
{
    'name': "Documents CRM",

    'summary': """
	Add Crm to the Documents module
    """,

    'description': """
        Add Crm to the Documents module:
        • User can add documents by opportunity
        • Added smart button in Opportunity View to show and add Documents
        • Added textbox at Documents module to assign Opportunity to documents
        • Search by Opportunity at Documents module
    """,

    'author': "GSol Soluciones Informaticas",
    'website': "https://www.gsol.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Documents',
    'version': '14.1.4',

    'depends': ['base', 'documents', 'crm'],

    'data': [
        #'data/cron.xml',
        'views/templates.xml',
        'views/crm_lead.xml'
    ],
}