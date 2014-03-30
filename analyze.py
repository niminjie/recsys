import sys
#action_0 = open('./analysis/action_0.tr', 'w')
#action_1 = open('./analysis/action_1.tr', 'w')
#action_2 = open('./analysis/action_2.tr', 'w')
#action_3 = open('./analysis/action_3.tr', 'w')
#action_1or0 = open('./analysis/action_1or0.tr', 'w')

#for line in open('./dataset/t_alibaba_data_sort.csv'):
#    if line.split(',')[2].strip() == '0':
#        action_0.write(line)
#    if line.split(',')[2].strip() == '1':
#        action_1.write(line)
#    if line.split(',')[2].strip() == '2':
#        action_2.write(line)
#    if line.split(',')[2].strip() == '3':
#        action_3.write(line)
#    if line.split(',')[2].strip() == '0' or line.split(',')[2].strip() == '1':
#        action_1or0.write(line)

#action_0.close()
#action_1.close()
#action_2.close()
#action_3.close()
#action_1or0.close()


dis_action_1or0 = open('./analysis/dis_action_1or0.tr', 'w')

tmp_list = []
for line in open('./analysis/action_1or0.tr'):
    dis = line.split(',')[0:2]
    if dis not in tmp_list:
        tmp_list.append(dis)
        dis_action_1or0.write(line)
        sys.stdout.write(line)
dis_action_1or0.close()
