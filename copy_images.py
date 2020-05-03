import shutil
import os


def main():
    desk_top = r'C:\Users\Tiger\Desktop'
    # for dir_name in os.listdir(desk_top):
    #     dir = desk_top+'\\'+dir_name
    #     if os.path.isdir(dir):
    #         for set_name in os.listdir(dir):
    #             set_dir = dir+'\\'+set_name
    #             old_dir = set_dir+'\\x4'
    #             if os.path.isdir(old_dir):
    #                 for image_name in os.listdir(old_dir):
    #                     old_path = old_dir+'\\'+image_name
    #                     new_path = set_dir+'\\'+image_name
    #                     shutil.copy(old_path, new_path)
    for dir_name in os.listdir(desk_top):
        dir = desk_top+'\\'+dir_name
        if os.path.isdir(dir):
            for set_name in os.listdir(dir):
                set_dir = dir+'\\'+set_name
                old_dir = set_dir+'\\x4'
                if os.path.isdir(old_dir):
                    shutil.rmtree(old_dir)
    a = 0


if __name__ == '__main__':
    main()
