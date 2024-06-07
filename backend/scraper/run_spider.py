import os
from scraper.scraper.spiders.job_spider import JobsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings



def run_spider():
    settings = Settings()
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'scraper.scraper.settings'
    settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
    settings.setmodule(settings_module_path,priority="project")
    process = CrawlerProcess(settings)
    process.crawl(JobsSpider)
    try:
        process.start()
        return "Done"
    except Exception as e:
        return "Error"
    