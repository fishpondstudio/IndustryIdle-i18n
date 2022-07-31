with open('resources.txt') as f:a={i for i in f.read().strip().split('\n')}

def g(file,to,extra):
    with open(to,'w') as f:
        f.write(file.readline().replace('CN',to[3:5]))
        for line in file.readlines():
            f.write('"'.join([line.split('"')[0],extra(line.split('"')[1]),line.split('"')[2]]) if line.strip().split(':')[0] in a else line)


import pypinyin
with open('zh-CN.ts') as f:b=g(f,'zh-PY.ts',lambda x:"".join(x[0] for x in pypinyin.pinyin(x)).upper()+'-'+x)
