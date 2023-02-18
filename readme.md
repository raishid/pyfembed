# Pyfembed

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Script to upload Videos to Fembed via API

# Requeriments
Python >=3.6

# Usage

    pip install pyfembed

    import pyfembed import Pyfembed

    pyfembed = Pyfembed(client_id, client_secret)
    upload_url = pyfembed.get_upload_url()
    uploaded = pyfembed.upload(
        file_path=filepath, 
        url_upload=upload_url.data.url, 
        token=upload_url.data.token
    )
    video_id = pyfembed.get_video_id(uploaded['fingerprint'])

And ready, the file is uploaded to share

