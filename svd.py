import recsys.algorithm
recsys.algorithm.VERBOSE = True
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data
from recsys.evaluation.decision import PrecisionRecallF1
from recsys.evaluation.prediction import RMSE, MAE
import sys

class Recommender():
    def __init__(self, train, test):
        recsys.algorithm.VERBOSE = True
        self.train = train
        self.test = test
        self.svd = SVD()
        self.svd.set_data(train)

    def set_train(self, train):
        self.train = train

    def set_test(self, test):
        self.test = test

    def get_train(self):
        return self.train

    def get_test(self):
        return self.test

    def get_alluserid(self, dataset):
        userid_list = []
        for rating, item_id, user_id in dataset.get():
            if user_id not in userid_list:
                userid_list.append(user_id)
        return userid_list

    def get_allitemid(self, dataset):
        itemid_list = []
        for rating, item_id, user_id in dataset.get():
            if item_id not in itemid_list:
                itemid_list.append(item_id)
        return itemid_list

    def eval_rmse(self):
        # Evaluation using prediction-based metrics
        rmse = RMSE()
        mae = MAE()
        for rating, item_id, user_id in self.test.get():
            try:
                pred_rating = self.svd.predict(item_id, user_id)
                rmse.add(rating, pred_rating)
                mae.add(rating, pred_rating)
            except KeyError:
                continue
        print 'RMSE=%s' % rmse.compute()
        print 'MAE=%s' % mae.compute()

    def recommend(self, N=10, only_unknowns=False, is_row=True):
        rec_list = {}
        for rating, item_id, user_id in self.test.get():
            if user_id in self.get_alluserid(self.train):
                rec_list[user_id] = self.svd.recommend(user_id, n=N, only_unknowns=False, is_row=False)
                print rec_list[user_id]
        return rec_list

    def precisionRecall(self, rec_list2, test_dict):
        print "Start calculate precision and recall..."
        hit = 0
        n_recall = 0
        n_precision = 0
        for user, items in test_dict.items():
             if user not in self.get_alluserid(self.train):
                 continue
             rec_list = self.svd.recommend(user, n=30, only_unknowns=False, is_row=False)
             r = [i[0] for i in rec_list]
             print 'rec_list', r
             hit += len(list(set(r) & set(items.keys())))
             n_recall += len(items)
             n_precision += 30
        return [hit / (1.0 * n_recall), hit / (1.0 * n_precision)]

def file_to_dict(path):
    dataset = {}
    for line in open(path, 'r').readlines():
        #print line
        user_id, item_id, rate = int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2])
        dataset.setdefault(user_id)
        if dataset[user_id] == None:
            dataset[user_id] = {}
        #dataset[user_id].setdefault(item_id)
        dataset[user_id][item_id] = {'rate':rate}
    return dataset

def main():
    # Load train and test Dataset
    train = Data()
    test = Data()
    train.load('./dataset/train.csv', force=True, sep=',', format={'col':0, 'row':1, 'value':2, 'ids':int})
    test.load('./dataset/test.csv', force=True, sep=',', format={'col':0, 'row':1, 'value':2, 'ids':int})
    test_dict = file_to_dict('./dataset/test.csv')
    #data = Data()
    #data.load('./ratings.dat', force=True, sep='::', format={'col':0, 'row':1, 'value':2, 'ids':int})
    #train, test = data.split_train_test(percent=80)
    rec = Recommender(train, test)
    rec.svd.compute(k=100, min_values=0.1, pre_normalize=None, mean_center=False, post_normalize=True)
    #rec.eval_rmse()
    #rec_list = rec.recommend()
    rec_list = []
    print rec.precisionRecall(rec_list, test_dict)

if __name__ == '__main__':
    main()
