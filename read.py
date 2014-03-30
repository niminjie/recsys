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

def dict_to_matrix(dataset):
    pass

def split_to_file():
    tst_file = open('./dataset/test.csv', 'w')
    trn_file = open('./dataset/train.csv', 'w')

    for line in open('./analysis/dis_action_1.tr', 'r'):
        time = line.split(',')[3].strip()
        if time <= '2014/8/9' and time >= '2014/7/9':
            tst_file.write(line)
        else:
            trn_file.write(line)
    tst_file.close()
    trn_file.close()

#out_file = open('./test.tr', 'w')
#
#for line in open('./dataset/t_alibaba_data_sort.csv'):
#    if line.split(',')[2].strip() == '0' or line.split(',')[2].strip() == '1':
#        out_file.write(line)
#out_file.close()
split_to_file()
