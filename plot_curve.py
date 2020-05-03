import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    font = {'family': 'Times New Roman',
            'style': 'normal',
            'weight': 'normal',
            'color': 'black',
            'size': 12
            }
    plt.rc('font', family='Times New Roman')
    plt.figure()

    file_path = r'C:\Users\Tiger\OneDrive - stu.scu.edu.cn\Papers\Mine\Graduate\table\chapter5\loss_study_rdn_rnn2'
    file_list = ['3layer3iter', 'addavgloss']
    for file_name in file_list:
        result = pd.read_csv(file_path+'\\'+file_name+'.csv')
        data = result['psnr']
        plt.plot(data, label=file_name+'        ')

    plt.xlabel('Epoch', fontdict=font)
    plt.ylabel('PSNR', fontdict=font)
    plt.legend(loc='lower right')
    plt.show()