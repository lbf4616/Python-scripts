def filter_out_result(result, score=0):
    """过滤分数小于score的框。

    Args：
        result: y_pred。
    Return:
        过滤后的y_pred。
    """

    cnt1, cnt2 = 0, 0
    result_new = []
    for res in result:
        if res:
            inst_list = []
            for inst in res:
                cnt1 += 1
                if inst[4] >= score:
                    cnt2 += 1
                    inst_list.append(inst)
            result_new.append(inst_list)
        else:
            result_new.append(res)
    print('过滤前和过滤后框的总数分别为：{}, {}。'.format(cnt1, cnt2))
    return result_new