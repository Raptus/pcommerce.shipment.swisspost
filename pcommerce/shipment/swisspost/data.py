from pcommerce.core.data import ShipmentData

def SwissPostShipmentData(as_customer=True, address=None):
    data = ShipmentData('pcommerce.shipment.swisspost')
    data.as_customer = as_customer
    data.address = address
    return data
