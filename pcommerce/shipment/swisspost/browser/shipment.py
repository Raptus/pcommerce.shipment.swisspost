from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from pcommerce.core.interfaces import IAddressFactory
from pcommerce.shipment.swisspost.browser.base import SwissPostBase
from pcommerce.shipment.swisspost.data import SwissPostShipmentData

class SwissPostShipment(SwissPostBase):
    template = ViewPageTemplateFile('shipment.pt')
    
    def validate(self):
        self.errors = {}
        haulage_as_customer = self.request.form.get('swisspost_address_as_customer', False)
        if not haulage_as_customer:
            factory = IAddressFactory(self.request)
            self.errors = factory.validate('swisspost_address')
        return len(self.errors) == 0
    
    def process(self):
        self.data = SwissPostShipmentData()
        swisspost_as_customer = self.request.form.get('swisspost_address_as_customer', False)
        if not swisspost_as_customer:
            factory = IAddressFactory(self.request)
            self.data.address = factory.create('swisspost_address')
        self.data.as_customer = swisspost_as_customer
        props = getToolByName(self.context, 'portal_properties').pcommerce_properties
        self.data.pretaxcharge = props.getProperty('swisspost_pretaxcharge', 0.0)
        self.data.posttaxcharge = props.getProperty('swisspost_posttaxcharge', 0.0)
        return self.data