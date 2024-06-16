生成中文pdf

jupyter nbconvert --to latex 中文.ipynb

add 
```
\usepackage{fontspec,xunicode,xltxtra}
\setmainfont{Microsoft YaHei}
\usepackage{ctex}
```

xelatex  中文.tex



auto convert 
jupyter nbconvert --to latex "机器学习八股文 Variance and Bias.ipynb"
python add_chinese.py "机器学习八股文 Variance and Bias.tex"