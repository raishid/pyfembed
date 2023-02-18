import requests
from .interfaces import PyfembedInterface, PyfembedUploadInterface
import tus
import traceback
import os
from time import sleep

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

    def upload(self, file_path: str, url_upload: str, token: str) -> dict:
        if not os.path.isfile(file_path):
            raise Exception('File not found')

        filename = os.path.basename(file_path)

        with open(file_path, 'rb') as f:
            try:
                file_size = tus._get_file_size(f)
                file_endpoint = tus.create(
                    tus_endpoint=url_upload,
                    file_name=filename,
                    file_size=file_size,
                    metadata={
                        'name': filename,
                        'token': token
                    }
                )
                tus.resume(file_obj=f, file_endpoint=file_endpoint, chunk_size=1024 * 1024 * 10, offset=0)
                return {
                    'success': True,
                    'fingerprint': file_endpoint.split('/')[-1] 
                }
            except tus.TusError as e:
                response = e.response.content.decode('utf-8', errors='replace')
                traceback.print_exc()
                print("Error response: ", response)

    def get_video_id(self, fingerprint: str, first_time: bool = True, sleep_time: int = 30):
        if first_time:
            print('Waiting for fingerprint to be processed...')
            sleep(sleep_time)

        r = self._request('post', '/fingerprint', data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'file_fingerprint': fingerprint
        })

        if r['success']:
            return r['data']['video_id']

        raise Exception(r['message'])
