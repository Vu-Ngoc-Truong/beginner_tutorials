import pydbus
bus= pydbus.SystemBus()
adapter = bus.get('org.bluez','/org/bluez/hci0')
print(dir(adapter))
print(adapter.Name)
# 'NT-137'
print(adapter.Powered)
# True
print(adapter.Address)
# '5C:3A:45:24:8F:E6'
print(adapter.__doc__)
