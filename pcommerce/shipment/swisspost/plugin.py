from zope.interface import implements, Interface
from zope.component import adapts

from pcommerce.core import PCommerceMessageFactory as _
from pcommerce.core.interfaces import IShipmentMethod
from pcommerce.shipment.swisspost.interfaces import ISwissPostShipment

class SwissPostShipment(object):
    implements(IShipmentMethod, ISwissPostShipment)
    adapts(Interface)
    
    title = _('SwissPost')
    description = _('Shipment by SwissPost')
    icon = '++resource++pcommerce_shipment_swisspost_icon.gif'
    logo = '++resource++pcommerce_shipment_swisspost_logo.gif'
    
    def __init__(self, context):
        self.context = context
    
    def mailInfo(self, order, lang=None, customer=False):
        data = order.shipmentdata['pcommerce.shipment.swisspost']
        address = data.as_customer and order.address or data.address
        return _('swisspost_mailinfo', default="""SwissPost shipment address
${address}""", mapping=dict(address=address.mailInfo(self.context.REQUEST, lang, customer)))
