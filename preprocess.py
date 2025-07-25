
import re

def clean_caption(caption):
    caption = caption.lower()
    caption = re.sub(r"[^a-z ]", "", caption)
    return caption
