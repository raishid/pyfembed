# Pyfembed

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Script to upload Videos to Fembed via API

# Requeriments
Python >=3.6

# Usage

    import pyfembed import Pyfembed

    pfb = Pyfembed(client_id=xxxx, client_secret=xxxx)

    upload_url = pfb.get_upload_url()
    uploaded = pfb.upload(
        file_path=PATH_VIDEO, 
        upload_url.data.url, 
        upload.data.token
    )
    video_id = pfb.get_video_id(uploaded['fingerprint'])

And ready, the file is uploaded to share

