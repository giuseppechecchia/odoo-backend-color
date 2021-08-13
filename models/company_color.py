#!/usr/bin/python
###############################################################################
# Copyleft (K) 2020-2022
# Developer: Giuseppe Checchia @eldoleo (<https://github.com/giuseppechecchia>)
###############################################################################

from odoo import models
import logging

_logger = logging.getLogger(__name__)


class OdooBackendColor(models.AbstractModel):

    _name = 'odoo.backend.color'

    _description = """Odoo Backend Custom Color"""

    def change_current_main_color(self):

        _logger.info("""
            To change your main color you need to
            modify it on /odoo_backend_color/static/src/scss/theme_style.scss
        """
                     )
