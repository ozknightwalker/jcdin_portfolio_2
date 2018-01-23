from __future__ import unicode_literals

import gzip


class Compressor(object):

    def __init__(self, app):
        self.app = app
        self.attachMiddleWares()

    def attachMiddleWares(self):

        @self.app.middleware('response')
        async def compress_response(request, response):
            uncompressed_body_length = len(response.body)
            content_type = self.get_content_type(response)
            minimum_size = self.app.config.get('COMPRESS_MIN_SIZE')
            if uncompressed_body_length > minimum_size and \
                    self.gzip_allowed(request) and \
                    self.allowed_content_type(response):

                compressed_body = self.compress(response.body)
                compressed_body_length = len(compressed_body)

                # modify the request headers to use the new compressed content
                response.body = compressed_body
                response.headers['Content-Encoding'] = 'gzip'
                response.headers['Vary'] = 'Accept-Encoding'
                response.headers['Content-Length'] = compressed_body_length

        @self.app.middleware('request')
        async def compress_request(request):
            if 'Content-Encoding' in request.headers and \
                    request.headers['Content-Encoding'] == "gzip":
                request.body = gzip.decompress(request.body)

    def compress(self, body):
        return gzip.compress(
            body, compresslevel=self.app.config.get('COMPRESS_LEVEL'))

    def gzip_allowed(self, request):
        return 'gzip' in request.headers['Accept-Encoding']

    def get_content_type(self, response):
        content_type = response.content_type
        if ';' in response.content_type:
            content_type = content_type.split(';')[0]
        return content_type

    def allowed_content_type(self, response):
        return self.get_content_type(response) in self.app.config.get(
            'COMPRESS_MIMETYPES')
