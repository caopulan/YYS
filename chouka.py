import random
import matplotlib.pyplot as plt
import multiprocessing



def chouka(p):
    p_len = len(str(p))
    n = 10 ** p_len
    kachi = [0] * int(n*(1-p)) + [1]*int(p*n)
    result = random.choices(kachi, k=1)
    return result[0]



# for i in range(choukatimes): # 模拟10000次抽卡
def single_simulation(i):
    print("正在执行第{}次抽卡".format(i+1))
    piao = 0 # 消耗蓝票
    Up = 3  # 剩余概率up
    for i in range(700):
        piao += 1
        p = p_quantu[i // 500] / 100 if i <= 500 else 1 # 抽到ssr/sp为新式神的概率
        pssr = p_ssr + p_sp if Up <= 0 else 2.5 * (p_ssr + p_sp) # 抽到ssr/sp的概率
        if chouka(pssr) == 1: # 抽到ssr/sp
            Up -= 1
            if chouka(p) == 1: # 抽到新式神
                break
        else:
            pass
    result_list.append(piao)
    average = sum(result_list)/len(result_list)
    return piao

if __name__ == "__main__":
    cpu = 5 # 并行数量
    # 概率
    p_ssr = 0.01
    p_sp = 0.0025
    p_3up = 25 * (p_ssr + p_sp)
    p_quantu = [10 + 5 * i for i in range(7)] + [50, 60, 80, 100]
    times = [50 * i for i in range(11)]
    SSR_SP = 0

    """
    up数值：[10, 15, 20, 25, 30, 35, 40, 50, 60, 80, 100]
    up更新抽数：[0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    """

    choukatimes = 10000
    result_list = []

    times = 0

    # 并行计算
    p = multiprocessing.Pool(cpu)
    result_list = p.map(single_simulation, range(choukatimes))
    p.close()
    p.join()

    # 非并行计算
    for i in range(choukatimes):
        single_result = single_simulation(i)
        result_list.append(single_result)


    # 写入文件
    fp = open("result.txt", "w")
    for i in result_list:
        fp.writelines(str(i) + "\n")
    fp.close()

    # 输出结果
    print("\n\n" + "="*40)
    print("平均消耗蓝票数：{:.2f}".format((sum(result_list)/len(result_list))))


    result1_list = [ i//100 for i in result_list]

    print("1-100抽频率：{:.2f}%".format(result1_list.count(0)/choukatimes*100))
    print("100-200抽频率：{:.2f}%".format(result1_list.count(1)/choukatimes*100))
    print("200-300抽频率：{:.2f}%".format(result1_list.count(2)/choukatimes*100))
    print("300-400抽频率：{:.2f}%".format(result1_list.count(3)/choukatimes*100))
    print("400-500抽频率：{:.2f}%".format(result1_list.count(4)/choukatimes*100))
    print("500-600抽频率：{:.2f}%".format(result1_list.count(5)/choukatimes*100))
    print("600-700抽频率：{:.2f}%".format(result1_list.count(6)/choukatimes*100))
    print("700抽频率：{:.2f}%".format(result1_list.count(7)/choukatimes*100))

    count_num = []
    time_list = []
    for i in range(700):
        if result_list.count(i + 1):
            count_num.append(result_list.count(i + 1))
            time_list.append(i + 1)
    plt.scatter(time_list, count_num, s=20, c="#ff1212", marker='o')
    plt.show()