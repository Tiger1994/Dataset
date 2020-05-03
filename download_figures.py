import re
import os
import urllib.request as url_req


def main():
    method = 'SRCNN'
    set = 'Urban100'
    start = 0
    set_path = r'C:\Users\Tiger\OneDrive - stu.scu.edu.cn\Papers\Mine\Graduate\figure\chapter2\Image_sets'
    set_result = r'C:\Users\Tiger\Desktop' + '\\' + method
    set_url = 'http://vllab.ucmerced.edu/wlai24/LapSRN/results'
    image_path = set_path+'\\'+set
    result_path = set_result+'\\'+set
    if not os.path.isdir(result_path):
        os.makedirs(result_path)
    names = os.listdir(image_path)
    for name_all in names[start:]:
        name = os.path.splitext(name_all)[0]
        if set == 'B100':
            url = set_url+'/BSDS100' + '/x4/'+name+'_x4_'+method+'.png'
        else:
            url = set_url + '/' + set + '/x4/' + name + '_x4_' + method + '.png'
        result_name = result_path+'\\'+name_all
        if os.path.isfile(result_name):
            continue
        url_req.urlretrieve(url, result_name)
        print("Number{}: ".format(start+1) + name+' Complete!')
        start = start+1
        # a = 0


if __name__ == '__main__':
    main()
