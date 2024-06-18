import base64


def load_image_and_convert_to_base64(image_path: str):
    with open(image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read())
    return encoded_image.decode("utf-8")


def extract_image_title_from_path(image_path: str) -> str:
    filename = image_path.split("/")[-1]
    title = filename.split(".")[0]
    return title.replace("-", " ").replace("_", " ")
