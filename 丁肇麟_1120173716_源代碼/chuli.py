import pandas as pd
import numpy as np
import xlwt
import re
#消除修饰词空格，枕区优势节律
# # X = ' 9-10Hz ɑ节律 调节/调幅良好 低波幅 双侧对称 睁眼抑制完全 插入性慢波少量 '
# def func2(x):
#     list_split = x.strip().split(' ')
#     len_list = len(list_split)
#     i = 0
#     while i < len_list:
#         if len_list > 1:
#             if (re.search('调节', list_split[i]) != None and re.search('欠佳', list_split[i]) != None) or \
#                     (re.search('调节', list_split[i]) != None and re.search('差', list_split[i]) != None) or \
#                     (re.search('调节', list_split[i]) != None and re.search('尚可', list_split[i]) != None) or \
#                     (re.search('调节', list_split[i]) != None and re.search('良好', list_split[i]) != None) :
#                 pass
#             elif re.search('调节', list_split[i]) != None and re.search('调幅', list_split[i]) != None :
#                 list_split[i] += list_split[i + 1]
#                 del list_split[i + 1]
#             elif re.search('睁眼',list_split[i]) != None:
#                 list_split[i] += list_split[i+1]
#                 del list_split[i+1]
#             elif re.search('插入性慢波',list_split[i]) != None:
#                 list_split[i] += list_split[i+1]
#                 del list_split[i+1]
#         len_list = len(list_split)
#         i += 1
#     return ' '.join(list_split)
# # def func(x):
# #     list_split = x.strip().split(' ')
# #     len_list = len(list_split)
# #     i = 0
# #     j = 0
# #     res = [None,None,None,None,None,None,None]
# #     for i in range(len_list):
# #         if re.search('波幅', list_split[i]) != None:
# #             res[0] = list_split[i]
# #         elif re.search('Hz', list_split[i]) != None:
# #             res[1] = list_split[i]
# #         elif re.search('节律', list_split[i]) != None or re.search('活动', list_split[i]) != None:
# #             res[2] = list_split[i]
# #         elif re.search('调节', list_split[i]) != None or re.search('调幅', list_split[i]) != None:
# #             res[3] = list_split[i]
# #         elif re.search('对称', list_split[i]) != None:
# #             res[4] = list_split[i]
# #         elif re.search('睁眼', list_split[i]) != None:
# #             res[5] = list_split[i]
# #         elif re.search('慢波', list_split[i]) != None:
# #             res[6] = list_split[i]
# #         else:
# #             res.append(None)
# #         i += 1
# #     return res
# # df = pd.read_excel("data.xls")
# # df["枕区优势节律"] = df["枕区优势节律"].map(func2)
# # df_join = df["枕区优势节律"].map(func).to_list()
# # print(df_join)
# # df_join = pd.DataFrame(df_join, columns=['1','2','3','4','5','6','7','8'])
# # print(df_join)
# # df_to_excel = df.join(df_join)
# # df_to_excel.to_excel("data3.xls")
# #
# def func3(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return 2
# df = pd.read_excel("data_r.xls")
# df["8"] = df["8"].map(func3)
# df_join = df["8"].to_list()
# print(df_join)
# df_join = pd.DataFrame(df_join, columns=['5555'])
# print(df_join)
# df_to_excel = df.join(df_join)
# df_to_excel.to_excel("data3.xls")
#
#发作间期癫痫样放电
# # def func4(x):
# #     list_split = x.strip().split(' ')
# #     res = []
# #     if re.search('未见',list_split[0]) != None:
# #         res.append(0)
# #     else:
# #         res.append(1)
# #     return res
# # df = pd.read_excel("data.xls")
# # df1 = df['发作间期癫痫样放电'].map(func4)
# # df1_join = df1.to_list()
# # print(df1_join)
# # df1_join = pd.DataFrame(df1_join, columns=['9'])
# # print(df1_join)
# # df_to_excel = df.join(df1_join)
# # df_to_excel.to_excel("data2.xls")
#
#年龄
# # def func5(x):
# #     list_split = x.strip().split('岁')
# #     len_list = len(list_split)
# #     res = []
# #     if(len_list == 1):
# #         if(re.search('月',list_split[0])) or re.search('天',list_split[0]):
# #             res.append(0)
# #         elif(int(list_split[0])>=18):
# #             res.append(1)
# #         else:
# #             res.append(0)
# #     else:
# #         if(int(list_split[0])>=18):
# #             res.append(1)
# #         else:
# #             res.append(0)
# #     return res
# # df = pd.read_excel("data.xls")
# # df1 = df['年龄'].map(func5)
# # df1_join = df1.to_list()
# # print(df1_join)
# # df1_join = pd.DataFrame(df1_join, columns=['10'])
# # print(df1_join)
# # df_to_excel = df.join(df1_join)
# # df_to_excel.to_excel("data2.xls")
#
# res = []
# def func6(x):
#     global res
#     new_list = []
#     list_split = ' '.join(x.strip().split())
#     if '，' in list_split:
#         list_split = list_split.strip().split('，')
#     elif '、' in list_split:
#         list_split = list_split.strip().split('、')
#         if '、' in list_split:
#             list_split = list_split.strip().split('、')
#     else:
#         list_split = list_split.strip().split(' ')
#
#     for str in list_split:
#         split = str.split()
#         if len(split) > 1:
#             for i in split:
#                 new_list.append(i)
#         else:
#             new_list.append(str)
#     list_split = new_list.copy()
#     for i in list_split:
#         res.append(i.upper())
#         res = list(set(res))
#     # len_list = len(list_split)
#     # i = 0
#     # flag = 0
#     # while(i < len_list):
#     #     j = 0
#     #     len_res = len(res)
#     #     if (len_res == 0):
#     #         res.append(list_split[i])
#     #         len_res = len(res)
#     #     else:
#     #         while(flag == 0 and j < len_res):
#     #             if(list_split[i] == res[j]):
#     #                flag = 1
#     #             j += 1
#     #         if(flag == 0):
#     #             res.append(list_split[i])
#     #     i += 1
#
#
# df = pd.read_excel("data3.xls")
# df1 = df['临床用药2'].map(func6)
# print(res)
# print(len(res))
# res_length = len(res)
# i = 0
# cnt_zy = 0
# cnt_shlq = 0
# cnt_lpms = 0
# cnt_kpl = 0
# # while(i<res_length):
# #     if re.search('未',res[i])!=None or re.search('不详',res[i])!=None or re.search('无',res[i])!=None or re.search('停药',res[i])!=None:
# #         del res[i]
# #         res_length = len(res)
# #     elif re.search('ML',res[i]) != None or re.search('不明',res[i]) != None:
# #         del res[i]
# #         res_length = len(res)
# #     elif re.search('中药',res[i])!= None or re.search('中成药', res[i])!=None:
# #         if(cnt_zy == 0):
# #             res[i] = '中成药'
# #             i += 1
# #             cnt_zy += 1
# #         else:
# #             del res[i]
# #             res_length = len(res)
# #     elif re.search('水合氯醛', res[i])!=None:
# #         if(cnt_shlq == 0):
# #             res[i] = '水合氯醛'
# #             i += 1
# #             cnt_shlq += 1
# #         else:
# #             del res[i]
# #             res_length = len(res)
# #     elif re.search('诱导睡眠', res[i])!=None:
# #         del res[i]
# #         res_length = len(res)
# #     elif re.search('雷帕霉素',res[i])!=None:
# #         if(cnt_lpms == 0):
# #             res[i] = '雷帕霉素'
# #             i += 1
# #             cnt_lpms += 1
# #         else:
# #             del res[i]
# #             res_length = len(res)
# #     elif re.search('氯硝西泮、开浦兰', res[i]) != None:
# #         del res[i]
# #         res_length = len(res)
# #
# #     else:
# #         i += 1
# # res = sorted(res)
# # # del res[0]
# # print(res)
# # print(len(res))
# # df1_join = pd.DataFrame(df1_join, columns=['10'])
# # print(df1_join)
# # df_to_excel = df.join(df1_join)
# # df_to_excel.to_excel("data2.xls")
#




#
#临床用药，remove为处理函数，szh为将药名数字化过程
# def remove(x):
#     if 'ml' in x or '毫升' in x or 'ML' in x or '诱导睡眠' in x:
#         return '水合氯醛'
#     elif '未' in x or '不详' in x or '无' in x or '停药' in x or '不明' in x:
#         return 'None'
#     elif '中药' in x or '中成药' in x:
#         return '中成药'
#     elif '雷帕霉素' in x :
#         return '雷帕霉素'
#     elif '丙戊酸钠' in x or '丙戊酸镁' in x or '德巴金' in x:
#         return 'VPA'
#     elif '劳拉西' in x:
#         return '劳拉西泮'
#     elif '奥卡西平' in x or '曲莱' in x:
#         return 'OXC'
#     elif '喜宝宁'in x or '氨己烯酸' in x or '喜保宁' in x:
#         return 'VGB'
#     elif '左卡尼丁' in x:
#         return '左卡尼汀'
#     elif '开浦兰'in x or '左乙拉西坦' in x:
#         return 'LEV'
#     elif '托吡酯' in x or '妥泰' in x:
#         return 'TPM'
#     elif '卡马西平' in x:
#         return 'CBZ'
#     elif '苯巴比妥' in x or '复方苯巴比妥溴化钠' in x:
#         return 'PB'
#     elif '氯硝西泮' in x:
#         return 'CZP'
#     elif '硝西泮' in x:
#         return 'NZP'
#     elif '地西泮' in x:
#         return 'DZP'
#     elif '苯妥英钠' in x:
#         return 'PHT'
#     elif '乙琥胺' in x:
#         return 'ESM'
#     elif '氯巴占' in x:
#         return 'CLB'
#     elif '唑尼沙胺' in x:
#         return 'ZNS'
#     elif '促肾上腺皮质激素' in x:
#         return 'ACTH'
#     elif '拉考沙胺' in x:
#         return 'LCM'
#     elif '吡仑帕奈' in x:
#         return 'PBR'
#     elif '拉莫三嗪' in x or '利必通' in x:
#         return 'LTG'
#     elif '阿力哌唑' in x or '阿立哌唑' in x :
#         return '阿立哌唑'
#     else:
#         return x.upper()
#
# def szh(x):
#     i = 0
#     global res_list
#     for i in range(len(res_list)):
#         if x == res_list[i]:
#             return i
# df = pd.read_excel("data3.xls")
# data_type = df['临床用药'].str.split(expand=True).stack().reset_index(level = 1,drop = True)
# d2 = df.join(data_type.to_frame(name='临床用药2')).reset_index(drop=True)
# print(d2)
# data_type = df['临床用药2'].str.split('，', expand=True).stack().reset_index(level = 1,drop = True)
# d2 = df.join(data_type.to_frame(name='临床用药3')).reset_index(drop=True)
# data_type_2 = d2['临床用药3'].str.split('、', expand=True).stack().reset_index(level = 1,drop = True)
# df_res = d2.join(data_type_2.to_frame(name='临床用药4')).reset_index(drop=True)
# df_res['临床用药_res'] = df_res['临床用药4'].map(remove)
# res_list = sorted(list(set(df_res['临床用药_res'])))
# del res_list[0]
# df_res['临床用药_final'] = df_res['临床用药_res'].map(szh)
# df_res.to_excel('data_res.xls')
# d2.to_excel('data3.xls')
# # print(d2)

#
#
# def funcBofu(x):
#     if(re.search('低波幅',str(x)) !=None):
#         return 1
#     elif re.search('低-中波幅',str(x)) != None:
#         return 2
#     elif re.search('中波幅',str(x)) != None:
#         return 3
#     elif re.search('中-高波幅',str(x)) != None:
#         return 4
#     elif re.search('高波幅',str(x)) != None:
#         return 5
#     else:
#         return 0;
# df = pd.read_excel('data_res.xls')
# df1 = df['1'].map(funcBofu)
# df1_join = df1.to_list()
# df1_join = pd.DataFrame(df1_join, columns=['1_fin'])
# df_toexcel = df.join(df1_join)
# df_toexcel.to_excel('data_res1.xls')

# def funcHz(x):
#     list_split = str(x).split('-')
#     if re.search('8Hz', list_split[0]) != None:
#         return 6
#     elif float(list_split[0]) < 4 and float(list_split[0]) >0:
#         return 1
#     elif float(list_split[0]) >=4 and float(list_split[0]) <5:
#         return 2
#     elif float(list_split[0]) >=5 and float(list_split[0]) <6:
#         return 3
#     elif float(list_split[0]) >=6 and float(list_split[0]) <7:
#         return 4
#     elif float(list_split[0]) >=7 and float(list_split[0]) <8:
#         return 5
#     elif float(list_split[0]) >=8 and float(list_split[0]) <9:
#         return 6
#     elif float(list_split[0]) >=9 and float(list_split[0]) <10:
#         return 7
#     elif float(list_split[0]) >= 10:
#         return 8
#     else:
#         return 0
# df = pd.read_excel('data_res.xls')
# df['2'] = df['2'].fillna(0)
# df1 = df['2'].map(funcHz)
# df1_join = df1.to_list()
# df1_join = pd.DataFrame(df1_join, columns=['2_fin'])
# df_toexcel = df.join(df1_join)
# df_toexcel.to_excel('data_res1.xls')

# def funcJL(x):
#     if str(x) == '0':
#         return 0
#     elif re.search('ɑ',str(x))!= None:
#         return 1
#     elif re.search('θ',str(x))!= None:
#         return 2
#     elif re.search('混合',str(x))!=None:
#         return 3
#     else:
#         return 4
# df = pd.read_excel('data_res.xls')
# df['3'] = df['3'].fillna(0)
# df1 = df['3'].map(funcJL)
# df1_join = df1.to_list()
# df1_join = pd.DataFrame(df1_join, columns=['3_fin'])
# df_toexcel = df.join(df1_join)
# df_toexcel.to_excel('data_res1.xls')

# def funcTJ(x):
#     if str(x) == '0':
#         return 0
#     elif re.search('差', str(x))!=None:
#         return 1
#     elif re.search('欠佳',str(x))!=None:
#         return 2
#     elif re.search('尚可',str(x))!=None:
#         return 3
#     elif re.search('良好',str(x))!=None:
#         return 4
# df = pd.read_excel('data_res.xls')
# df['4'] = df['4'].fillna(0)
# df1 = df['4'].map(funcTJ)
# df1_join = df1.to_list()
# df1_join = pd.DataFrame(df1_join, columns=['4_fin'])
# df_toexcel = df.join(df1_join)
# df_toexcel.to_excel('data_res1.xls')

# def funcDC(x):
#     if str(x) == '0':
#         return 0
#     elif re.search('双侧对称', str(x))!= None:
#         return 1
#     elif re.search('双侧不对称', str(x))!= None:
#         return 2
# df = pd.read_excel('data_res.xls')
# df['5'] = df['5'].fillna(0)
# df1 = df['5'].map(funcDC)
# df1_join = df1.to_list()
# df1_join = pd.DataFrame(df1_join, columns=['5_fin'])
# df_toexcel = df.join(df1_join)
# df_toexcel.to_excel('data_res1.xls')

# def funcZY(x):
#     if str(x) == '0':
#         return 0
#     elif re.search('不完全',str(x))!=None:
#         return 2
#     elif re.search('完全',str(x))!=None:
#         return 1
#     else:
#         return 2
# df = pd.read_excel('data_res.xls')
# df['6'] = df['6'].fillna(0)
# df1 = df['6'].map(funcZY)
# df1_join = df1.to_list()
# df1_join = pd.DataFrame(df1_join, columns=['6_fin'])
# df_toexcel = df.join(df1_join)
# df_toexcel.to_excel('data_res1.xls')

