# -*- coding: utf-8 -*-


import base64
import xlrd
from odoo import models, fields, api

from odoo.exceptions import ValidationError

class ProductImport(models.Model):
    _name = 'product.import'
    _description = 'Importación de Productos'

    name = fields.Char(string="Nombre de la Importación", required=True)
    import_file = fields.Binary(string="Archivo Excel", required=True)
    file_name = fields.Char(string="Nombre del Archivo")
    import_date = fields.Datetime(string="Fecha de Importación", default=fields.Datetime.now)
    product_ids = fields.One2many('product.import.line', 'import_id', string="Productos Importados")

    def process_file(self):
       
        if not self.import_file:
            raise ValueError("Debe subir un archivo para procesar.")

       
        file_data = base64.b64decode(self.import_file)
        workbook = xlrd.open_workbook(file_contents=file_data)
        sheet = workbook.sheet_by_index(0)
        for row_idx in range(1, sheet.nrows):
            product_name = sheet.cell(row_idx, 0).value
            attribute_name = sheet.cell(row_idx, 1).value
            attribute_value_names = str(sheet.cell(row_idx, 2).value).split(',') 

            product = self.env['product.template'].create({'name': product_name})

           
            attribute = self.env['product.attribute'].search([('name', '=', attribute_name)], limit=1)
            if not attribute:
                attribute = self.env['product.attribute'].create({'name': attribute_name})

            value_ids = []
            for value_name in attribute_value_names:
                value_name = value_name.strip()  
                value = self.env['product.attribute.value'].search([
                    ('name', '=', value_name),
                    ('attribute_id', '=', attribute.id),
                ], limit=1)
                if not value:
                    value = self.env['product.attribute.value'].create({
                        'name': value_name,
                        'attribute_id': attribute.id,
                    })
                value_ids.append((4, value.id))

        
            self.env['product.template.attribute.line'].create({
                'product_tmpl_id': product.id,
                'attribute_id': attribute.id,
                'value_ids': value_ids,
            })

        
            for value_id in value_ids:
                self.product_ids.create({
                    'import_id': self.id,
                    'product_template_id': product.id,
                    'attribute_id': attribute.id,
                    'attribute_value_id': value_id[1],
                })




class ProductImportLine(models.Model):
    _name = 'product.import.line'
    _description = 'Detalle de Importación de Productos'

    import_id = fields.Many2one('product.import', string="Importación", ondelete='cascade')
    product_template_id = fields.Many2one('product.template', string="Producto")
    attribute_id = fields.Many2one('product.attribute', string="Atributo")
    attribute_value_id = fields.Many2one('product.attribute.value', string="Valor del Atributo")
