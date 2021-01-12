---
title: "KG_Basic_dataWhale学习笔记（二）"
tag: "KnowledgeGraph"
date: 2021-01-12
---

# KG_Basic_dataWhale学习笔记（二）

## Task01---跑程序

### 一、配置程序的坑

#### 1.sklearn模块

sklearn的坑

模型中的sklearn的版本应该是<=0.20.3的

才会集合joblib的模块

现有的版本>=0.24.x以上的版本，joblib是单独分开的一个模块。

降低了模块的版本才可以顺利的使用。

（同时，没安装过机器学习等模块的，要先安装numpy模块、再安装Scipy模块， 最后才能安装sklearn模块）

PS:这个版本的sklearn不匹配python3.8以上的。（巨他妈的坑）

#### 2.其他模块

其他模块的库就是正常的安装

py2neo模块也有一些要提前安装的，但我用的conda虚拟环境安装，会快一点。

### 二、运行的截图

![image-20210112212835011](https://gitee.com/magicye/blogimage/raw/master/img/image-20210112212835011.png)

问答系统的截图

![image-20210112212945820](https://gitee.com/magicye/blogimage/raw/master/img/image-20210112212945820.png)

