tags = [
    {"name": "Tag1"},
    {"name": "Tag2"},
    {"name": "Tag3"},
    {"name": "Tag4"},
    {"name": "Tag5"},
    {"name": "Tag6"},
    {"name": "Tag7"},
]


class Tag:
    raw_tags = tags

    def __init__(self, tagid: int):
        self.id = tagid

        try:
            self.name = self.raw_tags[tagid]["name"]
        except IndexError:
            raise ValueError("Tag ID out of range")

    def __repr__(self):
        id, name = self.id, self.name
        return f"<Tag {id=} {name=}>"

    @classmethod
    def packing(cls, *tags):
        packed = 0

        for tag in tags:
            packed += 1 << tag.id

        return packed

    @classmethod
    def unpacking(cls, packed: int):
        tags = []

        for i in range(len(cls.raw_tags)):
            if packed & (1 << i):
                tags.append(Tag(i))

        return tags
