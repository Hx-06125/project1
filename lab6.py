import re
import jieba
import numpy as np
from PIL import Image
import wordcloud
import matplotlib.pyplot as plt
bookcomments=''
r='[。，,！.?&!;？*；、  （）( )《》]+'
with open('bookcomments-1.txt','r') as file:
    bookcomments=file.read()
comments_data=re.sub(r,'',bookcomments)
comments=comments_data.split('\n')
comments_tuple=tuple(comments)
with open('bookcomments_new.txt','w') as file:
    for con in comments_tuple:
        file.write(con+'\n')
rule=lambda x:len(set(x))/len(x)>0.6
result=filter(rule,comments_tuple)
with open('bookcomments_new2.txt','w') as file:
    for con in result:
        file.write(con+'\n')
d=dict()
with open('bookcomments_new2.txt','r') as file:
    while True:
        con =file.readline()
        if con:
            comments_list_exact=jieba.cut(con,cut_all=False)
            for key in comments_list_exact:
                d[key]=d.get(key,0)+1
        else :
            break
sorted_d=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
del sorted_d['\n']
wc=wordcloud.WordCloud(
font_path='C:/Windows/Fonts/simhei.ttf',
width=500,height=400,
mask=np.array(Image.open('D:\hx-python\胡贤-lab2\实验二/beijing.png')),
max_words=200,
max_font_size=100,
background_color='white',
font_step=3,
random_state=False,
prefer_horizontal=0.9)
wc.generate_from_frequencies(sorted_d)
mask = np.array(Image.open('D:\hx-python\胡贤-lab2\实验二/beijing.png'))
image_colors = wordcloud.ImageColorGenerator(mask)
wc.recolor(color_func=image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()