from base64 import b64decode
from io import BytesIO
from PIL import Image

class ImageEncoded:
    def __init__(self,
            encoded: str,
            decode: bool=True,
            del_after_decode: bool=True
        ):
        self.encoded = encoded
        self._decoded: Image
        self._width: int
        self._height: int

        if decode:
            self._decoded = Image.open(BytesIO(
                b64decode(encoded)
            ))

        self._width, self._height = self._decoded.size

        if del_after_decode:
            del self._decoded

    @property
    def decoded(self):
        if not self._decoded:
            self._decoded = Image.open(BytesIO(
                b64decode(self.encoded)
            ))
        return self._decoded
    
    @property
    def width(self):
        if not self._width:
            self._width, self._height = self.decoded.size
        return self._width

    @property
    def height(self):
        if not self._height:
            self._width, self._height = self.decoded.size
        return self._height
