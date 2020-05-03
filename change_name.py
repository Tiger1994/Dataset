import os


def main():
    desk_top = r'C:\Users\Tiger\Desktop'
    for method in os.listdir(desk_top):
        method_path = desk_top+'\\'+method
        if os.path.isdir(method_path):
            for set in os.listdir(method_path):
                set_path = method_path+'\\'+set
                for image in os.listdir(set_path):
                    name = image.split('.')[0]
                    tmp = name.split('_')
                    if len(tmp) >= 3:
                        new = ''
                        for s in tmp[:-1]:
                            new = new+s+'_'
                        new = new[:-1]
                        old_name = set_path + '\\' + image
                        new_name = set_path + '\\' + new + '.png'
                        os.rename(old_name, new_name)
    a = 0


if __name__ == '__main__':
    main()
