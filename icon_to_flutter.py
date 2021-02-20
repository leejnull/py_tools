'''
参数1：需要批量处理的图片文件夹路径

注意：目标路径需要改成项目中使用的路径，在image_scale_path, image_scale_2_path, image_scale_3_path变量中
默认使用的是相对路径
'''
import os
import sys
import shutil

image_scale_path = os.path.abspath(os.path.join(os.getcwd(), '../assets/images'))
image_scale_2_path = os.path.abspath(os.path.join(os.getcwd(), '../assets/images/2.0x'))
image_scale_3_path = os.path.abspath(os.path.join(os.getcwd(), '../assets/images/3.0x'))

def main():
    if len(sys.argv) != 2:
        print('参数缺失：缺少原路径参数|%s' % sys.argv)
        return
    origin_path = sys.argv[1]
    for _, _, filenames in os.walk(origin_path):
        for filename in filenames:
            if 'png' not in filename:
                continue
            des_path = ''
            if '@2x' in filename:
                des_path = os.path.join(image_scale_2_path, filename.replace('@2x', ''))
                print('2倍图：%s' % des_path)
            elif '@3x' in filename:
                des_path = os.path.join(image_scale_3_path, filename.replace('@3x', ''))
                print('3倍图：%s' % des_path)
            else:
                des_path = os.path.join(image_scale_path, filename)
                print('1倍图：%s' % des_path)
            if len(des_path) == 0:
                print('目标路径不能为空')
                return
            source_path = os.path.join(origin_path, filename)
            try:
                shutil.copyfile(source_path, des_path)
            except IOError as e:
                print('复制出错：%s' % e)
            except:
                print('其他错误：', sys.exc_info())

if __name__ == '__main__':
    main()
