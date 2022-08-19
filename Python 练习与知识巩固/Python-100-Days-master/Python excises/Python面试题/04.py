"""
写出生成从m到n公差为k的等差数列的生成器。
"""
def generate():
    for i in range(m,n+1,k):
        yield i
if __name__=="__main__":
    print(generate())