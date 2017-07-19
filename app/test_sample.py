def fun(x):
    return x+1

class BucketListItem(object):
    pass

class Category(object):
    pass

bucket_items = []

#creates a BucketList Item
def createItem(id,createdBy,name,category):
    item = BucketListItem()
    item.id = id;
    item.createdBy = createdBy;
    item.name = name;
    item.category = category;
    bucket_items.append(item)
    return item;

def bucketSize():
    return len(bucket_items)

def test_answer():
    assert fun(3) == 4

def test_answer2():
    assert fun(3) == 5

def test_answer3():
    assert fun(5) == 6

def test_create_item():
    assert createItem(1,'vivian','Travel to Rwanda!!!!','Travel').id == 1

def test_checkItemListSize():
    assert  len(bucket_items) == 1

def test_removeItem():
    del bucket_items[0]
    assert len(bucket_items) == 0
