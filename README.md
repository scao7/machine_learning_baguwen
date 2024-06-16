生成中文pdf

jupyter nbconvert --to latex 中文.ipynb

add 
```
\usepackage{fontspec,xunicode,xltxtra}
\setmainfont{Microsoft YaHei}
\usepackage{ctex}
```

xelatex  中文.tex


一建转换pdf
python add_chinese.py baguwen_variance_bias.ipynb

