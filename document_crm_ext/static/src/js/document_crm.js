odoo.define('documents_crm_ext.DocumentsInspector', function (require) {

    var documentInspector = require("documents.DocumentsInspector");
    const fileUploadMixin = require('web.fileUploadMixin');
    const documentInspectorMixin = require('documents.controllerMixin')

    var originalFunc = documentInspectorMixin._makeFileUploadFormDataKeys

    documentInspector.include({
        start: function(){
            this.__parentedParent._makeFileUploadFormDataKeys = function({recordID}){
                const context = this.model.get(this.handle, { raw: true }).getContext();
                return {
                    folder_id: this.searchModel.get('selectedFolderId'),
                    owner_id: context && context.default_owner_id,
                    partner_id: context && context.default_partner_id,
                    crm_id: context && context.default_crm_id
                };
            }
            return this._super.apply(this, arguments)
        },
        _renderFields: function(){
            const options = {mode: 'edit'};
            const proms = [];
            if (this.records.length === 1) {
                proms.push(this._renderField('name', options));
                if (this.records[0].data.type === 'url') {
                    proms.push(this._renderField('url', options));
                }
                proms.push(this._renderField('partner_id', options));
                proms.push(this._renderField('crm_id', options));
            }
            if (this.records.length > 0) {
                proms.push(this._renderField('owner_id', options));
                proms.push(this._renderField('folder_id', {
                    icon: 'fa fa-folder o_documents_folder_color',
                    mode: 'edit',
                }));
            }
            return Promise.all(proms);
        },
    });
});
