# -*- encoding: utf-8 -*-
##############################################################################
#
#    GRAP - Change Precision module for Odoo
#    Copyright (C) 2014 GRAP (http://www.grap.coop)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp.osv.orm import Model
from openerp.osv import fields
from openerp.addons import decimal_precision as dp


class purchase_order_line(Model):
    _inherit = 'purchase.order.line'

    _columns = {
        'price_unit': fields.float(
            'Unit Price', required=True,
            digits_compute=dp.get_precision('GRAP Purchase Unit Price')),
    }
