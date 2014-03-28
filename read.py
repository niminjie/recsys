def file_to_dict(path):
    dataset = {}
    for line in open(path, 'r').readlines():
        #print line
        user_id, item_id, action, date = line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3].strip()
        item_list = {}
        dataset.setdefault(user_id)
        item_list.setdefault(item_id)
        item_list[item_id] = {'action':action, 'date':date}
        dataset[user_id] = item_list
    return dataset
