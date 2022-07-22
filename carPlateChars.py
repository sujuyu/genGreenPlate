#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 上午10:12
# @Author  : zyx
# @Email   : zhengyixiang2@qq.com

chars = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
         10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'J', 19: 'K',
         20: 'L', 21: 'M', 22: 'N', 23: 'P', 24: 'Q', 25: 'R', 26: 'S', 27: 'T', 28: 'U', 29: 'V',
         30: 'W', 31: 'X', 32: 'Y', 33: 'Z', 34: '京', 35: '沪', 36: '津', 37: '渝', 38: '冀', 39: '晋',
         40: '蒙', 41: '辽', 42: '吉', 43: '黑', 44: '苏', 45: '浙', 46: '皖', 47: '闽', 48: '赣', 49: '鲁',
         50: '豫', 51: '鄂', 52: '湘', 53: '粤', 54: '桂', 55: '琼', 56: '川', 57: '贵', 58: '云', 59: '藏',
         60: '陕', 61: '甘', 62: '青', 63: '宁', 64: '新'}

chars2 = {65: '港',66:'澳',67:'领',68:'使',69:'警',70:'学',71:'挂'}

def chars_dict_to_list():
    c1 = [i for i in chars.values()]
    c2 = [i for i in chars2.values()]
    return c1+c2