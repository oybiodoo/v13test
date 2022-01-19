#-*- coding: utf-8 -*-

import logging

from odoo import models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class PosConfig(models.Model):
    _inherit = 'pos.config'

    def open_backend_cashdrawer(self):
        """Open the cashdrawer associated with this pos.config"""

        _logger.info('Opening Cashdrawer: Sending signal to printer...')

        if not self:
            return False
        if not self.epson_printer_ip:
            raise ValidationError('No EPSON printer configured on this PoS Terminal. Please configure the printer in this station\'s Settings.')
        elif not self.iface_cashdrawer:
            raise ValidationError('The Cashdrawer option is not selected. Please configure the PoS settings accordingly if you wish to open the cashbox.')

        return {
            'type': 'ir.actions.client',
            'tag': 'pos_cashbox_oybi.cashbox_backend',
            'params': {'ip': self.epson_printer_ip}
        }
