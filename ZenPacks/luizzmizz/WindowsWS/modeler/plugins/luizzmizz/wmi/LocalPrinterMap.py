import re
from ZenPacks.community.WMIDataSource.WMIPlugin import WMIPlugin

class LocalPrinterMap(WMIPlugin):

    maptype = "LocalPrinterMap"
    compname = "os"
    relname = "localprinter"
    modname = "ZenPacks.luizzmizz.WindowsWS.LocalPrinter"

    tables = {
        "Win32_Printer": (
            "Win32_Printer",
            None,
            "root/cimv2",
            {
                'Caption':'caption',
                'DriverName':'driverName',
                'HorizontalResolution':'resx',
                'VerticalResolution':'resy',
                'PortName':'portName',
                'EnableBIDI':'local',
                'Default':'default',
                'DeviceID':'deviceId'
            }
        ),
    }

    def process(self, device, results, log):
        """collect WMI information from this device"""
        log.info('Processing %s for device %s', self.name(), device.id)
        rm = self.relMap()
        for instance in results.get("Win32_Printer", []):
            try:
                om = self.objectMap(instance)
                om.id = self.prepId(om.deviceId)
                om.local = (re.search('^[0-9]',om.portName)<0)
                rm.append(om)
            except AttributeError:
                continue
        return rm
