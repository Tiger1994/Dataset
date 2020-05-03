import json


def main():
    raw_path = r'C:\Users\Tiger\OneDrive - stu.scu.edu.cn\Papers\Mine\Graduate\figure\chapter3\perceptual'
    file_name = 'position.txt'
    box_size = 55
    file = open(raw_path+'\\'+file_name)
    lines = file.readlines()
    res = {}
    for line in lines:
        line = line[1:]
        line = line.replace('\n', '')
        data = line.split(']')
        coor = data[0].split(', ')
        coor = [int(x) for x in coor]
        name = data[1]

        res[name] = {}
        if name[0:3] == 'img':
            res[name]['dataset'] = 'Urban100'
        elif name.isdigit():
            res[name]['dataset'] = 'B100'
        elif len(name)>=8:
            res[name]['dataset'] = 'Manga109'
        else:
            res[name]['dataset'] = 'Set14'
        res[name]['name'] = name+'.png'
        res[name]['top_left'] = coor
        res[name]['bottom_right'] = [coor[0]+box_size, coor[1]+box_size]

    json_name = 'position.json'
    res_name = raw_path+'\\'+json_name
    with open(res_name, 'w') as f:
        json.dump(res, f, indent=4)
    a = 0


if __name__ == '__main__':
    main()
