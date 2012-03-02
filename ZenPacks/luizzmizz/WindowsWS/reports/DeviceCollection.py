import logging
log = logging.getLogger("zen.Reports")

from Products.ZenReports import Utils

class DeviceCollection:
    def run(self, dmd, args):
        report = []

        deviceClass=args.get('DeviceClass','/Server')
        resultset=set(dmd.Devices.getOrganizer(deviceClass).getSubDevices())-set(dmd.Devices.getOrganizer('/Ignore').getSubDevices())
        group=args.get('groups','/Environment/PRO')
        if group!='/':
          resultset=resultset & set(dmd.Groups.getOrganizer(group).getSubDevices())
        system=args.get('Csystems','/')
        if system!='/':
          resultset=resultset & set(dmd.Systems.getOrganizer(system).getSubDevices())
        location=args.get('location','/Devices')
        if location!='/':
          resultset=resultset & set(dmd.Locations.getOrganizer(location).getSubDevices())
        productionState=args.get('productionState','')
        #log.error("list(set(dmd.Devices.getOrganizer('%s').getSubDevices()) & set(dmd.Groups.getOrganizer('%s').getSubDevices()) & set(dmd.Systems.getOrganizer('%s').getSubDevices()) & set(dmd.Locations.getOrganizer('%s').getSubDevices()) )"%(deviceClass,group,system,location))
        for dev in list(resultset):
          if (not productionState) or (productionState==dev.getProdState()):
            report.append(
                    Utils.Record(
                      device = dev.name(),
                      deviceLink = dev.getDeviceLink(),
                      manageIp = dev.manageIp,
                      tag = dev.getHWTag,
                      deviceClassPath = dev.getDeviceClassPath(),
                      deviceClassPathLink = dmd.Devices.getOrganizer(dev.getDeviceClassPath()).getIdLink(),
		      productionState = dev.getProdState()
                      )
                    )

        return report
