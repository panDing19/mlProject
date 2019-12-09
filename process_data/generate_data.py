import jieba
import pandas as pd
import re

name = 'two_movies_test.csv'
generate_name = 'processed_data_two_movies.txt'
rule = re.compile(u'[^\u4E00-\u9FA5]')
if __name__ == '__main__':
    #读入影评+评分数据
    data = pd.read_csv(name, encoding = 'gb18030')
    comment = list(data.iloc[:, 0])
    score = list(data.iloc[:, 1])
    movie = list(data.iloc[:, 2])
    # with open(name, 'rb') as f:
    #     text = f.read()


    with open(generate_name, 'w') as f:
        # for i in range(len(data)):
        #     if type(comment[i]) != float:
        #         tmp_com = comment[i]
        for tmp_com, tmp_sco, tmp_mov in zip(comment, score, movie):
            if(type(tmp_com)==float):
                continue
            if len(tmp_com) < 6:
                continue
            if bool(re.search('[a-z]', tmp_com)):
                continue
            tmp_com = tmp_com.strip()
            tmp_com = tmp_com.replace('\r\n', '')
            tmp_com = tmp_com.replace('\r', '')
            tmp_com = tmp_com.replace('\n', '')
            tmp_com = ''.join(tmp_com.split())

            punctuation = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""
            re_punctuation = "[{}]+".format(punctuation)
            new_com = re.sub(re_punctuation, "", tmp_com)
            ret = rule.match(new_com)
            if(ret!=None):
                continue

            if type(tmp_com) == float:
                continue
            seg_list = jieba.cut(tmp_com, cut_all=False)
            f.write(' '.join(seg_list))
            f.write(' </d> ')
            f.write(tmp_mov)
            f.write(' ')
            tmp_sco = int(tmp_sco)
            if tmp_sco == 1:
                f.write('一星级')
            elif tmp_sco == 2:
                f.write('二星级')
            elif tmp_sco == 3:
                f.write('三星级')
            elif tmp_sco == 4:
                f.write('四星级')
            else:
                f.write('五星级')
            f.write('\n')