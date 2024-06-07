from itemloaders.processors import TakeFirst, Identity
from scrapy.loader import ItemLoader


class OfferLoader(ItemLoader):
    default_output_processor = TakeFirst()
    tags_out = Identity()