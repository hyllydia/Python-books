#coding:utf-8
import random
def generate_code(code_len=4):
    """
        生成指定长度的验证码

        :param code_len: 验证码的长度(默认4个字符)

        :return: 由大小写英文字母和数字构成的随机验证码
        """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1  #last_pos=61
    code = ''
    for _ in range(code_len):
        #randint(), 0~61都可以取到
        index = random.randint(0, last_pos)
        print(index)
        code += all_chars[index]
    return code
if __name__=="__main__":
    code = generate_code()
    print(code)