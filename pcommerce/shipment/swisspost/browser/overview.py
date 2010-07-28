from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from pcommerce.shipment.swisspost.browser.base import SwissPostBase

class SwissPostOverview(SwissPostBase):
    template = ViewPageTemplateFile('overview.pt')