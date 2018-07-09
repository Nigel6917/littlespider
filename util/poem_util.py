# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 
# @Author  : LIYUAN134
# @File    : poemUtil.py
# @Comment :
#            
poem_arr = [
    '而今才道当时错，心绪凄迷', '红泪偷垂，满眼春风百事非', '情知此后来无计，强说欢期', '一别如斯，落尽梨花月又西',
    '严宵拥絮频惊起，扑面霜空', '斜汉朦胧，冷逼毡帷火不红', '香篝翠被浑闲事，回首西风', '数尽残钟，一穟灯花似梦中',
    '冷香萦遍红桥梦，梦觉城笳', '月上桃花，雨歇春寒燕子家', '箜篌别后谁能鼓，肠断天涯', '暗损韶华，一缕茶烟透碧纱',
    '嫩烟分染鹅儿柳，一样风丝', '似整如欹（qi），才著春寒瘦不支', '凉侵晓梦轻蝉腻，约略红肥', '不惜葳蕤（ wēirui)，碾取名香作地衣',
    '桃花羞作无情死，感激东风', '吹落娇红，飞入窗前伴懊侬', '谁怜辛苦东阳瘦，也为春慵', '不及芙蓉，一片幽情冷处浓',
    '拨灯书尽红笺也，依旧无聊', '玉漏迢迢，梦里寒花隔玉箫', '几竿修竹三更雨，叶叶萧萧', '分付秋潮，莫误双鱼到谢桥',
    '凉生露气湘弦润，暗滴花梢', '帘影谁摇，燕蹴风丝上柳条', '舞鵾镜匣开频掩，檀粉慵调', '朝泪如潮，昨夜香衾觉梦遥',
    '相逢不语，一朵芙蓉著秋雨', '小晕红潮，斜溜鬟心只凤翘', '待将低唤，直为凝情恐人见', '欲诉幽怀，转过回阑叩玉钗',
]

import random


def random_poem():
    rt_poem = []
    size = 4
    length = len(poem_arr)
    for index in range(0, size):
        s_poem = poem_arr[random.randint(0, length - 1)]
        rt_poem.append(s_poem)
    return rt_poem


if __name__ == '__main__':
    print ''.join(random_poem())