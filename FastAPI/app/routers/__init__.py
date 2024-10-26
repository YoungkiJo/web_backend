from configs.config import setting

from concurrent.futures import ThreadPoolExecutor

threads = dict()
executor = ThreadPoolExecutor(max_workers=setting().thread)