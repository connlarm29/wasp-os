# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Daniel Thompson
"""Example of any automatically discovered application.

Any python file (``.py`` or ``.mpy``) discovered in the ``apps/``
directory will be automatically added to the Software application.
"""

import wasp
import gc

class sysInfoApp():
    NAME = "sysInfo"

    def __init__(self):
        '''init area'''
        self._getInfo()

    def _draw(self):
        draw = wasp.watch.drawable
        draw.fill()
        draw.string("~", 0, 32, width=240)
        draw.string("PineTime Info", 0, 64, width=240)
        draw.string(f"Battery: {self.battLvl}%", 0, 96, width=240)
        draw.string(f"Voltage: {self.battVtlg}mV", 0, 128, width=240)
        draw.string(f"Free Mem: {self.freeMem}kB",0,128+32,width=240)
        draw.string("~", 0, 128+64, width=240)

    def foreground(self):
        self._getInfo()
        self._draw()

    def _getInfo(self):
        self.battLvl = wasp.watch.battery.level()
        self.battVtlg = (wasp.watch.battery.voltage_mv())/1000.0
        if wasp.watch.free:
            self.freeMem = gc.mem_free()/1000.0
        else:
            self.freeMem = -1
