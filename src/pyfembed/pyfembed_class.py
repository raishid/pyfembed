import requests
from interfaces import PyfembedInterface, PyfembedUploadInterface
import tus
import traceback
import os

class Pyfembed(PyfembedInterface):

    BASE_URL = "https://www.fembed.com/api"
    BASE_HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    def __init__(self, client_id, client_secret) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    def _request(self, method, url, headers={}, data=None, params=None):
        headers = {**self.BASE_HEADERS, **headers}

        r = getattr(requests, method)(
            f'{self.BASE_URL}{url}', headers=headers, data=data, params=params)

        return r.json()

    def get_upload_url(self):
        r = self._request('post', '/upload', data={
            'client_id': self.client_id,
            'client_secret': self.client_secret
        })

        if r['success']:
            return PyfembedUploadInterface(**r)
        else:
            raise Exception(r['message'])

    def upload(self, file_path: str, url_upload: str, token: str):
        if not os.path.isfile(file_path):
            raise Exception('File not found')

        filename = os.path.basename(file_path)

        with open(file_path, 'rb') as f:
            try:
                uploaded = tus.upload(
                    file_obj=f,
                    tus_endpoint=url_upload,
                    metadata={
                        'name': filename,
                        'token': token
                    }
                )
                print(uploaded)
            except tus.TusError as e:
                response = e.response.content.decode('utf-8', errors='replace')
                traceback.print_exc()
                print("Error response: ", response)


pb = Pyfembed('257762', '64548cff975be565')
url_upload = pb.get_upload_url()
pb.upload(file_path='D:\\Descargas\\document_5109486648022795075.mp4', url_upload=url_upload.data.url, token=url_upload.data.token)
