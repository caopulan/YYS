import random
import matplotlib.pyplot as plt
import numpy as np

def jieyuan():
    return random.choices([1,2,3,4],k=1)[0]

if __name__ == "__main__":
    """
    结缘可简单看作两个式神的情况，式神数量不影响其分布
    """
    result_list = []
    imitate_time = 10000000
    for i in range(imitate_time): # 模拟10000次
        fail_time = 0 # 失败次数
        total_time = 1 # 单次模拟的总轮次
        situation = [0,jieyuan()] # 两个式神初始化
        # print(situation)
        while fail_time < 5: # 失败五次跳出循环
            total_time += 1
            situation[total_time%2] = jieyuan()
            # print(total_time%2,situation)
            if situation[0] != situation [1]:
                fail_time += 1
            else:
                fail_time = 0
        result_list.append(total_time)

    # 写入文件
    fp = open("jieyuan_result.txt", "w")
    for i in result_list:
        fp.writelines(str(i) + "\n")
    fp.close()

    # 输出结果
    result1_list = [i // 10 for i in result_list]
    result1_list = [i if i <= 5 else 6 for i in result1_list]
    print("平均退条轮数：{:.2f}".format((sum(result_list)/len(result_list))))
    print("6-10轮频率：{:.2f}%".format(result1_list.count(0)/imitate_time*100))
    print("10-20轮频率：{:.2f}%".format(result1_list.count(1)/imitate_time*100))
    print("20-30轮频率：{:.2f}%".format(result1_list.count(2)/imitate_time*100))
    print("30-40轮频率：{:.2f}%".format(result1_list.count(3)/imitate_time*100))
    print("40-50轮频率：{:.2f}%".format(result1_list.count(4)/imitate_time*100))
    print("50-60轮频率：{:.2f}%".format(result1_list.count(5)/imitate_time*100))
    print("大于60轮频率：{:.2f}%".format(result1_list.count(6)/imitate_time*100))


    # 绘制
    count_num = []
    time_list = []
    for i in range(66):
        if result_list.count(i + 1):
            count_num.append(result_list.count(i + 1)/imitate_time)
            time_list.append(i + 1)

    p2 = plt.bar(time_list, count_num, 0.45, label="num", color="#87CEFA")
    plt.xticks(np.arange(5, 65, 5))
    plt.show()
