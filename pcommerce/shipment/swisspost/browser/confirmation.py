from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from pcommerce.shipment.swisspost.browser.base import SwissPostBase

class SwissPostConfirmation(SwissPostBase):
    template = ViewPageTemplateFile('confirmation.pt')