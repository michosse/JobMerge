# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from typing import Optional
from dataclasses import dataclass, field

@dataclass
class JobOfferItem:
    title: Optional[str] = field(default=None)
    company: Optional[str] = field(default=None)
    image: Optional[str] = field(default=None)
    tags: list[str] = field(default_factory=list)
    link: Optional[str] = field(default=None)