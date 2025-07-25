
def load_captions(filepath):
    mapping = {}
    with open(filepath, 'r') as file:
        for line in file:
            tokens = line.strip().split('\t')
            if len(tokens) != 2:
                continue
            image_id, caption = tokens
            image_id = image_id.split('#')[0]
            if image_id not in mapping:
                mapping[image_id] = []
            mapping[image_id].append(caption)
    return mapping
