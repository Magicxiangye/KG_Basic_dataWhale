---
title: "KG_Basic_dataWhale学习笔记（一）"
tag: "KnowledgeGraph"
date: 2021-01-10
---

# KG_Basic_dataWhale学习笔记（一）

## Task01---知识图谱的简介和认识

### 一、知识图谱的简介

知识图谱是由 Google 公司在 2012 年提出来的一个新的概念。从学术的角度，我们可以对知识图谱给一个这样的定义：“**知识图谱本质上是语义网络（Semantic Network）的知识库”**。但这有点抽象，所以换个角度，**从实际应用的角度出发其实可以简单地把知识图谱理解成多关系图（Multi-relational Graph）**。

#### 1.什么是图（Graph）

图（Graph）**是由节点（Vertex）和边（Edge）来构成**（和数据结构中的理解很像），**多关系图一般包含多种类型的节点和多种类型的边**。实体（节点）指的是现实世界中的事物比如人、地名、概念、药物、公司等，关系（边）则用来表达不同实体之间的某种联系，比如人-“居住在”-北京、张三和李四是“朋友”、逻辑回归是深度学习的“先导知识”等等。

![image.png](https://gitee.com/magicye/blogimage/raw/master/img/ZNWkgnrPpjoHlzq.png)

#### 2.什么是 Schema

知识图谱另外一个很重要的概念是 Schema:

- 介绍：限定待加入知识图谱数据的格式；**相当于某个领域内的数据模型，包含了该领域内有意义的概念类型以及这些类型的属性**
- 作用：**规范结构化数据的表达**，一条数据必须满足Schema预先定义好的实体对象及其类型，才被允许更新到知识图谱中， **一图胜千言**
  - 图中的DataType限定了知识图谱节点值的类型为文本、日期、数字（浮点型与整型）
  - 图中的Thing限定了节点的类型及其属性（即图1-1中的边）
- 举例说明：基于下图Schema构建的知识图谱中仅可含作品、地方组织、人物；其中作品的属性为电影与音乐、地方组织的属性为当地的商业（eg：饭店、俱乐部等）、人物的属性为歌手
- **tips：本次组队学习不涉及schema的构建**

<img src="https://gitee.com/magicye/blogimage/raw/master/img/zxMLupBIewb2jFR.png" alt="Schema定义.PNG" style="zoom:150%;" />

#### 3.知识图谱的价值

![学科概念.PNG](https://gitee.com/magicye/blogimage/raw/master/img/5eFvYZ3rnKDWVNt.png)

知识图谱是人工智能很重要的一个分支, 人工智能的目标为了让机器具备像人一样理性思考及做事的能力

**包含的关系**：在符号主义的引领下，知识工程（核心内容即建设专家系统）取得了突破性的进展 ->
  在整个知识工程的分支下，知识表示是一个非常重要的任务 ->
  而知识图谱又恰恰是知识表示的重要一环

### 二、如何构建

构建的前提是需要把数据从不同的数据源中抽取出来。

对于垂直领域的知识图谱来说，它们的**数据源主要来自两种渠道**：

- **第一种：业务本身的数据**。这部分数据通常包含在公司内的数据库表并**以结构化的方式存储**，一般只需要简单预处理即可以作为后续AI系统的输入；
- **第二种：网络上公开、抓取的数据**。这些数据通常是以网页的形式存在**所以是非结构化的数据**，**一般需要借助于自然语言处理等技术来提取出结构化信息。**

小例子：比如在下面的搜索例子里，Bill Gates和Malinda Gate的关系就可以从非结构化数据中提炼出来，比如维基百科等数据源。

![image.png](https://gitee.com/magicye/blogimage/raw/master/img/XOtDiVkMIE965GZ.png)

#### 1.信息的抽取

**信息抽取的难点在于处理非结构化数据。**

左边是一段非结构化的英文文本，右边是从这些文本中抽取出来的实体和关系。来进行信息的结构化抽取

![image.png](https://gitee.com/magicye/blogimage/raw/master/img/HDa36LRxTv7EN9l.png)

#### 2.构建所需要的知识

在构建类似的图谱过程当中，主要涉及以下几个方面的自然语言处理技术： 

1. **实体命名识别（Name Entity Recognition）**
2. **关系抽取（Relation Extraction）**
3. 实体统一（Entity Resolution）
4. 指代消解（Coreference Resolution）
5. ...

##### 实体命名识别（Named Entity Recognition）

实体命名识别（英语：Named Entity Recognition），简称NER

- 目标：**就是从文本里提取出实体并对每个实体做分类/打标签**；
- 举例说明：比如从上述文本里，我们可以提取出实体-“NYC”，并标记实体类型为 “Location”；我们也可以从中提取出“Virgil's BBQ”，并标记实体类型为“Restarant”。
- 这种过程称之为实体命名识别，这是一项相对比较成熟的技术，有一些现成的工具可以用来做这件事情。

##### 关系抽取（Relation Extraction）

关系抽取（英语：Relation Extraction），简称 **RE**

- 介绍：通过关系抽取技术，把**实体间的关系**从文本中**提取出来**；
- 举例说明：比如实体“hotel”和“Hilton property”之间的关系为“in”；“hotel”和“Time Square”的关系为“near”等等。

![image.png](https://gitee.com/magicye/blogimage/raw/master/img/X7OqhWL6IZbNcke.png)

##### 实体统一（Entity Resolution）

实体统一（英语：Entity Resolution），简称 **ER**

- 介绍：**对于有些实体写法上不一样，但其实是指向同一个实体**；
- 举例说明：比如“NYC”和“New York”表面上是不同的字符串，但其实指的都是纽约这个城市，需要合并。
- 价值：**实体统一不仅可以减少实体的种类，也可以降低图谱的稀疏性（Sparsity）**；

##### 指代消解（Disambiguation）

指代消解（英语：Disambiguation）

- 介绍：**文本中出现的“it”, “he”, “she”这些词到底指向哪个实体**（就是找到文本中的代词到底是指向哪一个的实体），比如在本文里两个被标记出来的“it”都指向“hotel”这个实体。

像是：

![image.png](https://gitee.com/magicye/blogimage/raw/master/img/xUVbWp32ZRjHLa8.png)

### 三、知识图谱的存储

主要有两种存储方式：

- 一种是**基于RDF的存储**；
- 另一种是**基于图数据库的存储**。

![image.png](https://gitee.com/magicye/blogimage/raw/master/img/kZlqe8f2JMNgGTu.png)

RDF**以三元组的方式来存储数据而且不包含属性信息。**

**图数据库一般以属性图为基本的表示形式**，所以实体和关系可以包含属性，这就意味着更容易表达现实的业务场景。

Neo4j系统目前仍是使用率最高的图数据库，但唯一的不足就是不支持准分布式。

相反，OrientDB和JanusGraph（原Titan）支持分布式。

如果选择使用RDF的存储系统，Jena或许一个比较不错的选择。

### 四、Neo4J的介绍和安装

首先在 [Neo4J官网](https://neo4j.com/download/) 下载 Neo4J。

- Neo4J分为社区版和企业版：
  - 企业版：收费，在横向扩展、权限控制、运行性能、HA等方面都比社区版好，适合正式的生产环境；
  - 社区版：**免费**，普通的学习和开发采用免费社区版就好。

这里我装的是Desktop版的，目前还没有遇到什么奇怪的情况，在使用的时候，有的话，后期补充。（安装Neo4J的前提是，要有java的开发环境才能正常的安装使用。）

打开浏览器，:localhost:7474,连接上数据库后，进入交互式的输入框

或者使用的是自带的Browers也可以正常的使用。

![image](https://gitee.com/magicye/blogimage/raw/master/img/wtkmLaIjiWDlRh4.png)

#### 1.Cypher查询语言

Cypher：

- 介绍：是Neo4J的**声明式图形查询语言**，允许用户不必编写图形结构的遍历代码，就可以对图形数据进行高效的查询。
- 设计目的：**类似SQL，适合于开发者以及在数据库上做点对点模式（ad-hoc）查询的专业操作人员**。
- 其具备的能力包括： 
  - 创建、更新、删除节点和关系 
  - 通过模式匹配来查询和修改节点和关系 - 管理索引和约束等

### 五、Neo4J实战

实践的节点包括的是：人物和人物之间有朋友、夫妻等关系，人物和城市之间有出生地的关系

- Person-Friends-PERSON
- Person-Married-PERSON
- Person-Born_in-Location

#### 1.创建节点

删除数据库中以往的图，**确保一个空白的环境进行操作**【注：慎用，如果库内有重要信息的话】：

![image.png](https://gitee.com/magicye/blogimage/raw/master/img/3q4LDMCyZ2Hwemf.png)

```s
 #删除的操作
 MATCH (n) DETACH DELETE n
```

MATCH为匹配的操作、n是创建每个节点什么的设定的标识符（个人的理解）

使用语句来创建节点

```
CREATE (n:Person {name:'John'}) RETURN n
#多创造几个
  CREATE (n:Person {name:'Sally'}) RETURN n
  CREATE (n:Person {name:'Steve'}) RETURN n
  CREATE (n:Person {name:'Mike'}) RETURN n
  CREATE (n:Person {name:'Liz'}) RETURN n
  CREATE (n:Person {name:'Shawn'}) RETURN n
```

CREATE是创建操作，Person是标签，代表节点的类型。

**花括号{}代表节点的属性，属性类似Python的字典。**

这个语句的动作是：创建一个标签为Person的节点，该节点具有一个name属性，属性值是John。

RETURN   n : 创建完成后会返回一下n这个节点的图

创建其他的节点（不同标签的节点）

```s
#也是一样的CREATE方法
#节点类型为Location，属性包括city和state。
CREATE (n:Location {city:'Miami', state:'FL'})
```

多创造几个人物节点的图会变为：

![image](https://gitee.com/magicye/blogimage/raw/master/img/W4RwifuO7MhDjdI.png)

地区和人物节点的合图

![image](https://gitee.com/magicye/blogimage/raw/master/img/uGaBt1MQ7jksXnE.png)

#### 2.创建关系

关系的创建语句：

像是朋友关系

```
 MATCH (a:Person {name:'Liz'}), 
        (b:Person {name:'Mike'}) 
  MERGE (a)-[:FRIENDS]->(b)
```

**方括号 [ ]即为关系，FRIENDS为关系的类型。**

注意这里的**箭头-->是有方向的**，表示是从a到b的关系。 这样，Liz和Mike之间建立了FRIENDS关系。

要**增加关系类型的属性**

```
 MATCH (a:Person {name:'Shawn'}), 
        (b:Person {name:'Sally'}) 
  MERGE (a)-[:FRIENDS {since:2001}]->(b)#合并
```

**不同类型的节点之间的关系创建**

```
 MATCH (a:Person {name:'John'}), (b:Location {city:'Boston'}) MERGE (a)-[:BORN_IN {year:1978}]->(b)
```

这里的关系是BORN_IN，表示出生地，同样有一个属性，表示出生年份。

同样的，也可以在节点创建的是时候，就设置好对应的关系

```
CREATE (a:Person {name:'Todd'})-[r:FRIENDS]->(b:Person {name:'Carlos'})
```

**换行：shift+回车**

#### 3.图数据的查询操作

像是：查询下所有在Boston出生的人物的语句

```
MATCH (a:Person)-[:BORN_IN]->(b:Location {city:'Boston'}) RETURN a,b
```

还有举例查询所有对外关系的节点

```
MATCH(a)--() RETURN a
#查询所有有关系的节点
MATCH (a)-[r]->() RETURN a.name, type(r)
#返回的是开始节点的名字、以及关系的类型
#查询所有有结婚关系的节点
MATCH (n)-[:MARRIED]-() RETURN n
```

![有关系的节点.png](https://gitee.com/magicye/blogimage/raw/master/img/WjCsr4aLnO1kvo7.png)

连接性的查询

**查找某人的朋友的朋友**

比如，查找Mike的朋友的朋友

```
 MATCH (a:Person {name:'Mike'})-[r1:FRIENDS]-()-[r2:FRIENDS]-(friend_of_a_friend) RETURN friend_of_a_friend.name AS fofName
# 这样就得出结果
```

#### 4.删除和修改操作

**增加/修改节点的属性**

**SET表示修改操作**

先用MATCH匹配，再用SET修改

```
  MATCH (a:Person {name:'Liz'}) SET a.age=34
  MATCH (a:Person {name:'Shawn'}) SET a.age=32
  MATCH (a:Person {name:'John'}) SET a.age=44
  MATCH (a:Person {name:'Mike'}) SET a.age=25
```

**删除节点的属性**

**删除属性操作主要通过REMOVE**

```
MATCH (a:Person {name:'Mike'}) SET a.test='test'
MATCH (a:Person {name:'Mike'}) REMOVE a.test
```

**删除节点**

**删除节点操作是DELETE**

```
MATCH (a:Location {city:'Portland'}) DELETE a
```

删除与某个节点有关系的节点

```
 MATCH (a:Person {name:'Todd'})-[rel]-(b:Person) DELETE a,b,rel
```

### 六、 py2neo模块：通过操作python变量，达到操作neo4j的目的

这里我没有试neo4j的库，直接使用的py2neo模块。

使用的方式，大概为：

```python
# 先尝试连接一下数据库
# step 1：导包
from py2neo import Graph, Node, Relationship

if __name__ == '__main__':
    # step 2：连接到图数据库的命令（数据库的用户密码）直连的话没有权限
    g = Graph("bolt://localhost:7687", user="neo4j", password="123")
    # step 3：创建节点
    tx = g.begin()
    a = Node("Person", name="PG")
    tx.create(a)
    b = Node("Person", name="BF")
    # step 4：创建边(关系)
    # 使用字典来添加关系的属性
    properties = {'date': '2019-07-11'}
    # 建立关系的语句
    ab = Relationship(a, "LOVE", b, **properties)
    # step 5：运行
    tx.create(ab)
    tx.commit()
```

### 七、数据导入CSV文件数据

我的Neo4J的**版本是Desktop版本的，所以一些操作都可以可视化。**

将要导入的文件传入数据库相应的import文件夹中，等待读取相应的CSV文件。

![img](https://gitee.com/magicye/blogimage/raw/master/img/11892075-95ef534df01d141e)

通过LOAD CSV  FROM 或者 LOAD CSV WITH HEADERS FROM导入文件。

LOAD CSV  FROM 的方法

```
#对于读入的每一行数据的操作
#有点像str数组的读取方式
LOAD CSV FROM "file:///persons.csv" AS line
CREATE (n:Person {name: line[0]}) RETURN n.value
```

LOAD CSV WITH HEADERS FROM 的方法

```
LOAD CSV WITH HEADERS FROM "file:///persons.csv" AS line
#这里对每一行数据的处理，有点像获取对象的某个属性的方法
CREATE (n:Person {name: line.name}) RETURN n.value
```

![img](https://gitee.com/magicye/blogimage/raw/master/img/11892075-5533b48aa50e618d.png)