#coding:utf-8import scrapyfrom ..items import ToutiaocrawlItemclass Toutiao(scrapy.Spider):    name="toutiao"    start_urls=["http://tieba.baidu.com/f?kw=%C8%F5%D6%C7"]    allowed_domains1=["http://tieba.baidu.com"]    MAX_PAGE=10 #最大页数    k=0 #计数    def parse(self,response):        hrefs=response.xpath("//a[@class='j_th_tit ']/@href").extract()        next=response.xpath("//a[@class='next pagination-item ']/@href").extract()        for href in hrefs:            yield scrapy.Request(url=self.allowed_domains1[0]+href,callback=self.content_parse)        self.k+=1        if self.k<self.MAX_PAGE:            yield scrapy.Request(url="http:"+next[0],callback=self.parse)    def content_parse(self,response):        title=response.xpath("//h1[@class='core_title_txt  ']/@title").extract()        content=response.xpath('//*[@id="j_p_postlist"]/div[1]/div[3]/div[1]/cc/div/text()').extract()        item=ToutiaocrawlItem()        try:            item["title"]=title[0]            try:                item["content"] = content[0]            except:                item["content"] = ""            return item        except:            pass