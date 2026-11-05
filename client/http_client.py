import requests


class HttpClient:

    def __init__(self, base_url, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)

        return self.session.request(
            method=method,
            url=url,
            **kwargs
        )

    def close(self):
        self.session.close()