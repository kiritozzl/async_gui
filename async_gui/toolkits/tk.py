#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..engine import Engine


class TkEngine(Engine):
    def update_gui(self):
        self.main_app.update()
