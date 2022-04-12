# -*- coding:utf-8 -*-

import os
import re
import pandas as pd
from glob import glob


def get_file_list(data_path: str = './') -> list:
    file_path = os.path.join(data_path, "*.txt")
    file_list = glob(file_path)
    for _ in file_list:
        if 'requirements' in _:
            file_list.remove(_)
    file_list.sort()
    return file_list


def read_file(file_name: str):
    try:
        file_open = open(file_name, encoding="utf-8")
    except Exception as e:
        print(e)
        return ''

    content = file_open.read()
    file_open.close()
    return content


def format_data(data: str):
    pattern1 = '(\d{1,})\..*'
    pattern2 = '\d{1,}\.(\s*[^甲乙丙丁1-9]*\s*纺*平*[^甲乙丙丁1-9]*\s*)([甲乙丙丁]{0,1}\d{1,4}号{0,1}[甲乙丙丁]{0,1})-{0,1}\s*(\d{3,4})室{0,1}\D*\s*([0-9一二三四五六七八九十Il\|]{1,})[份套斤瓶个]{0,1}.*'
    convert_dict = {
        '一': '1',
        'I': '1',
        'l': '1',
        '|': '1',
        '二': '2',
        '三': '3',
        '四': '4',
        '五': '5',
        '六': '6',
        '七': '7',
        '八': '8',
        '九': '9',
        '十': '10',
    }
    data_failed = []
    data_success = []
    for item_data in re.finditer(pattern=pattern1, string=data):
        item_num = item_data.group(1)
        item_analyze = re.search(pattern=pattern2, string=item_data.group())

        if item_analyze is None:
            data_to_rec = [item_num, item_data.group()]
            data_failed.append(data_to_rec)
            continue

        part_num = item_analyze.group(2)
        if '纺平' in item_analyze.group(1) or not re.search(pattern='\d{4}', string=item_analyze.group(3)) is None:
            part_num = '纺平大厦' + item_analyze.group(2)

        if re.search(pattern='[甲乙丙丁]', string=part_num):
            part_num = re.search(pattern='\d{1,}', string=part_num).group() + '号' + re.search(pattern='[甲乙丙丁]', string=part_num).group()

        if '号' not in part_num:
            part_num = part_num + '号'

        room_num = item_analyze.group(3) + '室'
        amount = item_analyze.group(4)

        if re.search(pattern='\d{1,}', string=amount) is None:
            amount = convert_dict[amount]

        amount = int(amount)
        data_to_add = [item_num, part_num, room_num, amount]
        data_success.append(data_to_add)

    data_to_write = pd.DataFrame(data_success, columns=['序号', '栋号', '房间号', '数量'])
    data_to_write.set_index(['序号'], inplace=True)
    data_to_write.sort_values(by=['栋号', '房间号'], axis=0, inplace=True)
    data_out = pd.DataFrame(data_failed, columns=['序号', '原始数据'])
    data_out.set_index(['序号'], inplace=True)
    return data_to_write, data_out


def main() -> None:
    file_list = get_file_list()
    for file in file_list:
        content = read_file(file_name=file)
        data_ok, data_bad = format_data(data=content)
        file_name = './' + file.split("/")[-1].split("\\")[-1][:-4] + '.xlsx'

        data_writer = pd.ExcelWriter(file_name)
        data_ok.to_excel(data_writer, sheet_name='整理好的数据')
        data_bad.to_excel(data_writer, sheet_name='无法识别数据')

        data_writer.save()
        data_writer.close()

    return


if __name__ == '__main__':
    main()
