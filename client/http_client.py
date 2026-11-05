import requests
from utils.logger import get_logger
from time import perf_counter

class HttpRequestError(Exception):
    def __init__(self, message="发生了自定义错误"):
        self.message = message
        super().__init__(self.message)

class HttpClient:
    def __init__(self,base_url:str,token=None,timeout=10):
        self.logger=get_logger("http_client")
        self.base_url=base_url.rstrip('/')
        self.timeout=timeout
        self.session=requests.session()
        if token:
            headers={
                "Authorization" : f"Bearer {token}"
            }
            self.session.headers.update(headers)

    def request(self,method,path:str,**kwargs):
        url=f"{self.base_url}/{path.lstrip('/')}"
        timeout=kwargs.pop('timeout',self.timeout)
        start = perf_counter()

        try:
            res=self.session.request(method=method,
                                 url=url,
                                 timeout=timeout,
                                 **kwargs
                                 )

            duration = perf_counter() - start
            self.logger.info(
                "HTTP %s %s | status=%s | duration=%.3fs",
                method.upper(),
                path.split("?")[0],
                res.status_code,
                duration,
            )
            return res
        except requests.exceptions.RequestException as e:
            duration = perf_counter() - start

            duration = perf_counter() - start

            self.logger.error(
                "HTTP %s %s | error=%s: %s | duration=%.3fs",
                method.upper(),
                url,
                type(e).__name__,
                e,
                duration
            )

            raise HttpRequestError(f"请求异常,"
                                   f"方式：{method},"
                                   f"url:{url},") from e

    def get(self,path,**kwargs):
        return self.request(method="GET",
                     path=path,**kwargs)
    def post(self,path,**kwargs):
        return self.request(method="POST",
                     path=path,**kwargs)
    def delete(self,path,**kwargs):
        return self.request(method="DELETE",
                     path=path,**kwargs)

    def patch(self, path, **kwargs):
        return self.request(
            method="PATCH",
            path=path,
            **kwargs
        )

    def close(self):
        self.session.close()