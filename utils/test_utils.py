import numpy as np
from sklearn.metrics import multilabel_confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd

import pprint
pp = pprint.PrettyPrinter()

y_true = np.array([[1, 1, 1, 0], [0, 1, 1, 0]])
y_pred = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
mcm = multilabel_confusion_matrix(y_true, y_pred)
print("----------------------mcm---------------------------")
print(mcm)


def init_tp_fp_matrix():
    num_categories = 4
    matrix = []
    for row in range(num_categories):
        matrix.append([0 for column in range(num_categories)])
    return matrix

tp_fp_matrix = init_tp_fp_matrix()
for i in range(len(y_true)):
    # print(y_true[i])
    # print(y_pred[i])
    ground_truth = y_true[i]
    prediction = y_pred[i]
    ground_truth_dp_category_indices = []
    for j in range(len(ground_truth)):
        dp_category_index = j
        if(ground_truth[dp_category_index] == 1):
            ground_truth_dp_category_indices.append(dp_category_index)
            is_tp = (ground_truth[dp_category_index] == 1 and prediction[dp_category_index] == 1)
            if(is_tp):
                tp_fp_matrix[dp_category_index][dp_category_index] += 1

    for k in range(len(ground_truth)):
        # print(j)
        dp_category_index = k
        is_fp = (ground_truth[dp_category_index] == 0 and prediction[dp_category_index] == 1)
        if(is_fp):
            samplewise_mcm = multilabel_confusion_matrix(y_true, y_pred, samplewise=True)
            # print("dp_category_index", dp_category_index)
            # num_tp = samplewise_mcm[0][1][1]
            fp_share = 1 / len(ground_truth_dp_category_indices)
            for row_dp_category_index in ground_truth_dp_category_indices:
                tp_fp_matrix[row_dp_category_index][dp_category_index] += fp_share

print("----------------------------tp_fp_matrix----------------------------")
# pp.pprint(tp_fp_matrix)

numpy_tp_fp_matrix = np.array(tp_fp_matrix)
pp.pprint(numpy_tp_fp_matrix)
# print(numpy_tp_fp_matrix[:,0])
# print(numpy_tp_fp_matrix[:,1])
# print(numpy_tp_fp_matrix[:,2])
# print(numpy_tp_fp_matrix[:,3])

dp_categorywise_tp_plus_fp = []
for dp_category_index in range(len(numpy_tp_fp_matrix)):
    # print(numpy_tp_fp_matrix[:,dp_category_index])
    # print(sum(numpy_tp_fp_matrix[:,dp_category_index]))
    dp_categorywise_tp_plus_fp.append(sum(numpy_tp_fp_matrix[:,dp_category_index]))
numpy_dp_categorywise_tp_plus_fp = np.array(dp_categorywise_tp_plus_fp)
print(numpy_dp_categorywise_tp_plus_fp)
print(numpy_tp_fp_matrix / numpy_dp_categorywise_tp_plus_fp)


# x = np.array([[1.055,2,3,4],
#               [2,3,np.nan,5],
#               [np.nan,5,2,3]])
# print(np.argwhere(np.isnan(x)))
# np.nan_to_num(x, copy=False, nan=0.0)
# print(x)
# y = np.round(x, 2)
# print(y)


class_bin_index_to_dp = {
    "0": "ACTIVITY MESSAGE"
    , "1": "HIGH DEMAND MESSAGE"
    , "2": "LOW STOCK MESSAGE"
    , "3": "LIMITED TIME MESSAGE"
    , "4": "COUNTDOWN TIMER"
    , "5": "ATTENTION DISTRACTION"
    , "6": "DEFAULT CHOICE"
    , "7": "FRIEND SPAM"
    # , "8": "FORCED ENROLLMENT"
    , "8": "DISGUISED ADS"
    , "9": "SOCIAL PYRAMID"
    , "10": "PRIVACY ZUCKERING"
    , "11": "INTERMEDIATE CURRENCY"
    , "12": "NAGGING"
    , "13": "GAMIFICATION"
    , "14": "ROACH MOTEL"
    , "15": "FORCED CONTINUITY"
    , "16": "NO DP"
}

def print_tp_fp_distribution(tp_fp_distribution_rounded):
    category_rows = []
    for i in range(len(tp_fp_distribution_rounded)):
        # print(class_bin_index_to_dp[str(i)])
        # print(tp_fp_distribution_rounded[i])
        row = []
        category = class_bin_index_to_dp[str(i)]
        category_row = tp_fp_distribution_rounded[i]
        row.append(category)
        for item in category_row:
            row.append(item)
        category_rows.append(row)

    category_columns = []
    category_columns.append("category")
    for i in range(len(tp_fp_distribution_rounded)):
        category = class_bin_index_to_dp[str(i)]
        category_columns.append(category)

    # panda dataframes
    results = pd.DataFrame(category_rows, columns=category_columns)
    print("::::::::::::::::::::Results::::::::::::::::::::")
    print(results)

tp_fp_distribution = numpy_tp_fp_matrix / numpy_dp_categorywise_tp_plus_fp
np.nan_to_num(tp_fp_distribution, copy=False, nan=0.0)
tp_fp_distribution_rounded = np.round(tp_fp_distribution, 2)
print_tp_fp_distribution(tp_fp_distribution_rounded)
