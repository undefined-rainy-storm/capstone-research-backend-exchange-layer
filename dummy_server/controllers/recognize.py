from ..entities.image import ImageEncoded

class RecognizeController:
    def handle_request(request):
        image = ImageEncoded(request['content'], del_after_decode=False)
        return image.width, image.height
