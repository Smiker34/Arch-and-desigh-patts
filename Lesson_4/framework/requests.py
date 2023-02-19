class GetRequests:

    @staticmethod
    def parse_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        query_string = environ['QUERY_STRING']
        request_params = GetRequests.parse_data(query_string)
        return request_params


class PostRequests:

    @staticmethod
    def parse_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_data(env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        print(content_length)

        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data

    def parse_wsgi_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            print(f'строка после декод - {data_str}')
            result = self.parse_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_data(environ)
        data = self.parse_wsgi_data(data)
        return data
