import asyncio
import json

from .rnis import RNIS


class Munic:
    def __init__(self):
        self.login_rnis = 'Karpenko'
        self.password_rnis = 'H7DneQW3'
        self.token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJSTklTIiwiYXVkIjoiaHR0cDpcL1wvcm5pcy5jb20iLCJpYXQiOjE3MTExMDAxMjYsIm5iZiI6MTcxMTAxNDAyNiwiaW5mbyI6IntcInVzZXJcIjp7XCJ1dWlkXCI6XCI1N2FjOTMyMC05OWI5LTExZWUtOTNhOS0wMmE1MjBkYTE4NWJcIixcImxvZ2luXCI6XCJTaGVwZWxldlwiLFwiY29tcG9uZW50XCI6XCJvcGVyYXRvclwiLFwiaXNfc3lzdGVtXCI6ZmFsc2UsXCJpc19zdXBlcnZpc29yXCI6ZmFsc2UsXCJpc19zZW1pX2NvbmZpcm1lZFwiOmZhbHNlLFwiaXNfbm90aWZpY2F0ZWRcIjpmYWxzZSxcImluZm9cIjp7XCJ1bml0X3V1aWRcIjpcImU2ZmExZjA0LWNiOTMtMTFlYS1iMWZlLTAyZjQyYjA0MzZlMVwifX19In0.BWzWSVcudo0w9UkyQNQ_-ChbXmc9MO4zuBaH8DY2XK0'

    async def __aenter__(self):
        self.data = await self.get
        return self

    async def __aexit__(self, *args, **kwargs):
        pass

    def normolize_name(self, name):
        replace_list = ['МО', 'Городской округ', 'в настоящее время - ', 'городской округ']
        for replace in replace_list:
            name = name.replace(replace, '')
        return name.strip()

    @property
    async def get(self):
        async with RNIS(login=self.login_rnis, 
                        password=self.password_rnis, 
                        token=self.token
                        ) as rnis:
            dictionary = await rnis.API.Dictionary.to_list(
                dictionary='communal_municipalities',
                retries=2,
                error_print=True,
            )
            dictionary = dictionary['payload'][0]['documents']
            dictionary = {
                self.normolize_name(item['name']):item['uuid'] 
                for item in dictionary
            }
            dictionary = dict(sorted(dictionary.items()))
            return dictionary

    