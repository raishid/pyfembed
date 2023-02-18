from abc import ABCMeta, abstractmethod
from typing import Union

class PyfembedUploadInterface:

    class Data:
        __attrs__ = {
            'url': str,
            'token': str
        }

        def __init__(self, url, token) -> None:
            self.url = url
            self.token = token

    __attrs__ = {
        'success': bool,
        'data': dict,
        'code': int,
    }

    def __init__(self, success, data, code) -> None:
        self.success = success
        self.data = self.Data(**data)
        self.code = code
    

class PyfembedInterface(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
    
    @abstractmethod
    def _request(self, method: str, url: str, headers: Union[dict, None], data: Union[dict, str, None], params: Union[dict, None]) -> Union[dict, None]:
        """
        This method is used to make a request to the Fembed API.
        :param method: The HTTP method to use.
        :param url: The URL to send the request to.
        :param headers: The headers to send with the request.
        :param data: The data to send with the request.
        :param params: The parameters to send with the request.
        """
        pass

    @abstractmethod
    def get_upload_url(self) -> PyfembedUploadInterface:
        """
        This method is used to get the upload URL and token.
        :return: The upload URL and token.
        """
        pass

    @abstractmethod
    def upload(self, file_path: str, url_upload: str, token: str) -> dict:
        """
        This method is used to upload a video to Fembed.
        :param file_path: The path to the video file.
        :param url_upload: The upload URL.
        :param token: The upload token.
        :return: dict with success and fingerprint.
        """
        pass

    @abstractmethod
    def get_video_id(self, fingerprint: str, first_time: bool = True, sleep_time: int = 30) -> str:
        """
        This method is used to get the video ID.
        :param fingerprint: The fingerprint of the video.
        :param first_time: If this is the first time the method is called.
        :param sleep_time: The time to sleep before checking.
        :return: The video ID.
        """
        pass