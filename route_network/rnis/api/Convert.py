from ..filters import Filters
from ..request import Request


class Convert:
    '''Convert'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def docx_to_pdf(self, **d):
        '''docx_to_pdf | Convert.docx_to_pdf'''
        url  = self.URL.get(self.URL.Convert.docx_to_pdf)
        json = Filters.Convert.docx_to_pdf(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def html_to_pdf(self, **d):
        '''html_to_pdf | Convert.html_to_pdf'''
        url  = self.URL.get(self.URL.Convert.html_to_pdf)
        json = Filters.Convert.html_to_pdf(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def html_to_xls(self, **d):
        '''html_to_xls | Convert.html_to_xls'''
        url  = self.URL.get(self.URL.Convert.html_to_xls)
        json = Filters.Convert.html_to_xls(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def png_to_pdf(self, **d):
        '''png_to_pdf | Convert.png_to_pdf'''
        url  = self.URL.get(self.URL.Convert.png_to_pdf)
        json = Filters.Convert.png_to_pdf(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)