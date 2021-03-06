from maltreatment_nlp.patterns import ALL_PATTERNS


def run(text, **metadata):
    for name, pat in ALL_PATTERNS.items():
        for m in pat.finditer(text):
            yield metadata | {
                'pre_context': ' '.join(text[max(m.start() - 100, 0): m.start()].split()).strip(),
                'post_context': ' '.join(text[m.end(): m.end() + 100].split()).strip(),
                'term': m.group(),
                'pattern': name,
            }


def get_keys(**metadata):
    """Get all keys, e.g., for creating a csv file with csv.dictwriter"""
    return ['pre_context', 'term', 'post_context', 'pattern'] + list(metadata.keys())
