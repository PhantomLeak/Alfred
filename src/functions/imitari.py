from PIL import Image
from io import BytesIO
import base64
import re


def reformat_image(image, width, height, format_type):
    buffer = BytesIO()

    image_data = re.sub('^data:image/.+;base64,', '', image)
    decoded_image_data = base64.b64decode(image_data)
    img = Image.open(BytesIO(decoded_image_data))

    formatted_img = img.resize((width, height))
    formatted_img.save(buffer, format_type)
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode()
