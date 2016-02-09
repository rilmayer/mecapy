# -*- coding: utf-8 -*-
 
class Mecab:
    """mecab-pythonのインストールに挫折した人用
    """
 
    def __init__(self, string=""):
        self.ma_list = self.cmd_mecab(string)
 
    def wakachi(self):
        """分かち書きの結果を返す(list)
        """
        wakachi_list = []
        for word_ma in self.ma_list:
            wakachi_list.append(word_ma.split('\t')[0])
        return wakachi_list
 
    def futsu_hyouki(self):
        """普通表記の結果を返す(list)
        """
        futsu_hyouki_list = []
        for word_ma in self.ma_list:
            word, ma_info = word_ma.split('\t')
            futsu_hyouki_info = ma_info.split(',')[6]
            word_futsu = ''
            if futsu_hyouki_info == '*':
                word_futsu = word
            else:
                word_futsu = futsu_hyouki_info
            futsu_hyouki_list.append(word_futsu)
        return futsu_hyouki_list
 
    def cmd_mecab(self, string='', opt=''):
        """
        Shell経由でmecabを実行して結果を取得
        (引き数)
          string str： 解析したい文字列
          opt str： mecabの解析オプション
        (返り値)
          words_with_ma_info list： 解析した結果を改行で分割したリスト
        """
        import subprocess
        cmd = 'echo %s | mecab' % string.replace('\n', '')
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_data, stderr_data = p.communicate()
        stdout = str(stdout_data, encoding='Shift-JIS')
        words_with_ma_info = stdout.split("\r\n")
        words_with_ma_info.remove('EOS')
        words_with_ma_info.remove('')
        return words_with_ma_info
