from tag import Tag

tag = Tag(0)
print(tag.name)  # Tag1

packed = Tag.packing(Tag(0), Tag(3))
print(packed)  # 9

tags = Tag.unpacking(packed)
print(tags)  # [<Tag id=0 name='Tag1'>, <Tag id=3 name='Tag4'>]
