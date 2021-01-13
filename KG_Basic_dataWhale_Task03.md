---
title: "KG_Basic_dataWhale学习笔记（三）"
tag: "KnowledgeGraph"
date: 2021-01-13
---

# KG_Basic_dataWhale学习笔记（三）

## Task03---Neo4j图数据库导入数据

### 一、知识简介

在计算机科学中，图形作为一种特定的数据结构，用于表达数据之间的复杂关系，如社交关系、组织架构、交通信息、网络拓扑等等。在图计算中，基本的数据结构表达式是：G=(V,E)，V=vertex(节点)，E=edge(边)。图形结构的数据结构一般以节点和边来表现，也可以在节点上增加键值对属性。**图数据库是 NoSQL（非关系型数据库）的一种，它应用图形数据结构的特点（节点、属性和边）存储数据实体和相互之间的关系信息。**

目前使用的是，**Neo4j** ，是当前较为主流和先进的原生图数据库之一，提供原生的图数据存储、检索和处理。它由 Neo Technology支持，从 2003 年开始开发，1.0 版本发布于 2010 年，2.0版本发布于 2013 年。经过十多年的发展，Neo4j 获得越来越高的关注度，它已经从一个 Java 领域内的图数据库逐渐发展成为适应多语言多框架的图数据库。Neo4j 支持ACID、集群、备份和故障转移，具有较高的可用性和稳定性；它具备非常好的直观性，通过图形化的界面表示节点和关系；同时它具备较高的可扩展性，能够承载上亿的节点、关系和属性**，通过 REST 接口或者面向对象的 JAVA API进行访问。**

### 二、Neo4j简介

j使用图相关的概念来描述数据模型，把数据保存为图中的节点以及节点之间的关系。**数据主要由三部分构成**：

- 节点。**节点表示对象实例**，每个节点有唯一的ID区别其它节点，节点带有属性；
- 关系。**就是图里面的边，连接两个节点**，另外这里的关系是有向的并带有属性；
- 属性。**key-value对，存在于节点和关系中**，如图所示。

![图片.png](https://gitee.com/magicye/blogimage/raw/master/img/OGTbAcSw7UMdzHl.png)

#### 1.索引

- 动机：Neo4j使用遍历操作进行查询。为了加速查询，Neo4j会建立索引，并根据索引找到遍历用的起始节点；
- 介绍：默认情况下，相关的索引是由Apache Lucene提供的。但也能使用其他索引实现来提供。
- 操作：用户可以创建任意数量的命名索引。每个索引控制节点或者关系，而每个索引都通过key/value/object三个参数来工作。其中object要么是一个节点，要么是一个关系，取决于索引类型。另外，**Neo4j中有关于节点（关系）的索引，系统通过索引实现从属性到节点（关系）的映射。**
- 作用：
  - 查找操作：系统通过设定访问条件比如，遍历的方向，使用深度优先或广度优先算法等条件对图进行遍历，从一个节点沿着关系到其他节点；
  - 删除操作：Neo4j可以快速的插入删除节点和关系，并更新节点和关系中的属性。

#### 2.优势

- **查询的高性能**

Neo4j是一个原生的图数据库引擎，它存储了原生的图数据，因此，**可以使用图结构的自然伸展特性来设计免索引邻近节点遍历的查询算法，即图的遍历算法设计。**图的遍历是图数据结构所具有的独特算法，即从一个节点开始，根据其连接的关系，可以快速和方便地找出它的邻近节点。这种查找数据的方法并不受数据量的大小所影响，**因为邻近查询查找的始终是有限的局部数据，而不会对整个数据库进行搜索。所以，Neo4j具有非常高效的查询性能**，相比于RDBMS，它的查询速度可以提高数倍乃至数十倍.而且查询速度不会因数据量的增长而下降，即数据库可以经久耐用，并且始终保持最初的活力。不像RDBMS那样，因为不可避免地使用了一些范式设计，所以在查询时如果需要表示一些复杂的关系，势必会构造很多连接，从而形成很多复杂的运算。并且在查询中更加可怕的是还会涉及大量数据，这些数据大多与结果毫无关系，有的可能仅仅是通过ID查找它的名称而已，所以随着数据量的增长，即使查询一小部分数据，查询也会变得越来越慢，性能日趋下降，以至于让人无法忍受。

- **设计的灵活性**

在日新月异的互联网应用中，业务需求会随着时间和条件的改变而发生变化，这对于以往使用结构化数据的系统来说，往往很难适应这种变化的需要。**图数据结构的自然伸展特性及其非结构化的数据格式，让 Neo4j的数据库设计可以具有很大的伸缩性和灵活性。因为随着需求的变化而增加的节点、关系及其属性并不会影响到原来数据的正常使用**，所以使用Neo4j来设计数据库，可以更接近业务需求的变化，可以更快地赶上需求发展变化的脚步。
大多数使用关系型数据库的系统，为了应对快速变化的业务需求，往往需要采取推倒重来的方法重构整个应用系统。而这样做的成本是巨大的。使用Neo4j可以最大限度地避免这种情况发生。虽然有时候，也许是因为最初的设计考虑得太不周全，或者为了获得更好的表现力，数据库变更和迁移在所难免，但是使用Neo4j来做这项工作也是非常容易的，至少它没有模式结构定义方面的苦恼。

- **开发的敏捷性**

**图数据库设计中的数据模型，从需求的讨论开始，到程序开发和实现，以及最终保存在数据库中的样子，直观明了，似乎没有什么变化，甚至可以说本来就是一模一样的。这说明，业务需求与系统设计之间可以拉近距离，需求和实现结果之间越来越接近。**这不但降低了业务人员与设计人员之间的沟通成本，也使得开发更加容易迭代，并且非常适合使用敏捷开发方法。

Neo4j本身可伸缩的设计灵活性，以及直观明了的数据模型设计，以及其自身简单易用的特点等，所有这些优势都充分说明，使用Neo4j很适合以一种测试驱动的方法应用于系统设计和开发自始至终的过程之中，通过迭代来加深对需求的理解，并通过迭代来完善数据模型设计。

- **与其他数据库的比较**

在图数据库领域，除Neo4j外，还有其他如OrientDB、Giraph、AllegroGraph等各种图数据库。与所有这些图数据库相比，Neo4j的优势表现在以下两个方面。

(1)N**eo4j是一个原生图计算引擎**，它存储和使用的数据自始至终都是使用原生的图结构数据进行处理的，**不像有些图数据库，只是在计算处理时使用了图数据库，而在存储时还将数据保存在关系型数据库中。**

(2）**Neo4j是一个开源的数据库**，其开源的社区版吸引了众多第三方的使用和推如开源项目Spring Data Neo4j就是一个做得很不错的例子，同时也得到了更多开发者的拥趸和支持，聚集了丰富的可供交流和学习的资源与案例。这些支持、推广和大量的使用，反过来会很好地推动Neo4j的发展。

- **综合表现**

Neo4j 查询的高性能表现、易于使用的特性及其设计的灵活性和开发的敏捷性，以及坚如磐石般的事务管理特性，都充分说明了使用Neo4j是一个不错的选择。有关它的所有优点，总结起来，主要表现在以下几个方面。

1. **闪电般的读/写速度，无与伦比的高性能表现；**
2. **非结构化数据存储方式，在数据库设计上具有很大的灵活性；**
3. **能很好地适应需求变化，并适合使用敏捷开发方法；**
4. **很容易使用，可以用嵌入式、服务器模式、分布式模式等方式来使用数据库；**
5. **使用简单框图就可以设计数据模型，方便建模；**
6. **图数据的结构特点可以提供更多更优秀的算法设计；**
7. **完全支持ACID完整的事务管理特性；**
8. **提供分布式高可用模式，可以支持大规模的数据增长；**
9. **数据库安全可靠，可以实时备份数据，很方便恢复数据；**
10. **图的数据结构直观而形象地表现了现实世界的应用场景。**

### 三、搭建环境

在上一个任务中已经完成环境的搭建。

- python3.0及以上（还要小于3.8亲测）
- neo4j 3.5.0及以上
- jdk 1.8.0（最先安装的就是这个，因为是基于java的）

neo4j的下载，下载neo4j桌面版或者community版本都可以。

进官方网站：[https://neo4j.com/](https://neo4j.com/)

安装桌面版启动起来更加友好一点，我没用过community版本。

使用桌面版的自带浏览器，查看图数据库也更加的方便。

可以在浏览器中使用[http://localhost:7474/browser/](http://localhost:7474/browser/)网址查看数据库，但是前提是得把桌面的应用程序关掉。

注：记住数据库的用户名和密码，一般默认的是：用户：neo4j, 密码：neo4j。（自己设的数据库用户名一样，密码是自己设置的）

### 四、Neo4j数据导入

#### 1.数据集的介绍

- 数据源：39健康网。包括15项信息，其中7类实体，约3.7万实体，21万实体关系。
- 本次组队搭建的系统的知识图谱结构如下：

![知识图谱结构](https://gitee.com/magicye/blogimage/raw/master/img/TacFAJUnCWfuZXr.png)

**知识图谱实体类型**

![知识图谱实体类型](https://gitee.com/magicye/blogimage/raw/master/img/7zlp2Y9du3Mon1U.png)

**知识图谱实体关系类型**

![知识图谱实体关系类型](https://gitee.com/magicye/blogimage/raw/master/img/QI2tCpk3LuTfoca.png)

**知识图谱疾病属性**

![知识图谱疾病属性](https://gitee.com/magicye/blogimage/raw/master/img/y4repEsqd9bPkSl.png)

**基于特征词分类的方法来识别用户查询意图**

![基于特征词分类的方法来识别用户查询意图](https://gitee.com/magicye/blogimage/raw/master/img/r1ugnS3CPBWfmGk.png)

#### 2.数据的导入

要将 数据 导入 Neo4j 图数据库，首先需要 进入 build_graph.py 类中，在 类 MedicalGraph 中 的**加入 本地 Neo4j 图数据库 的 账号和密码（最好是一个空的数据库）；**

```python
class MedicalGraph:
        def __init__(self):
            ...
            self.graph = Graph("http://localhost:7474", username="neo4j", password="自己的密码")
            ...
```

我是用的pycharm来运行代码，直接运行这个创建数据库文件就行。

Linux或者用命令行的话，运行 以下命令：

```python
python build_graph.py 
```

**注：由于数据量比较大，所以该过程需要运行几个小时** 

####  3.build_graph.py主体代码介绍

**主体类 MedicalGraph 介绍**

```python
class MedicalGraph:
    def __init__(self):
        pass
    
    # 读取文件，获得实体，实体关系
    def read_file(self):
        psss
    # 创建节点
    def create_node(self, label, nodes):
        pass
    # 创建疾病节点的属性
    def create_diseases_nodes(self, disease_info):
        pass
    # 创建知识图谱实体
    def create_graphNodes(self):
        pass
    # 创建实体关系边
    def create_graphRels(self):
        pass
    # 创建实体关系边
    def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
        pass
```

- 获取数据路径

```python
    cur_dir = 
    # 获取的文件夹的绝对路径
    '/'.join(os.path.abspath(__file__).split('/')[:-1])
    self.data_path = os.path.join(cur_dir, 'data/disease.csv')
```

- 链接 Neo4j 图数据库

```python
    self.graph = Graph("http://localhost:7474", username="neo4j", password="自己设定的密码")
```

- 读取文件，获得实体，实体关系

这部分代码的核心就是读取 数据文件，并 **获取实体和实体关系信息。**

- **实体信息(以下的全是实体)：**
  - diseases 疾病
  - aliases  别名
  - symptoms  症状
  - parts  部位
  - departments  科室
  - complications 并发症
  - drugs  药品
- 实体关系：
  - disease_to_symptom  疾病与症状关系
  - disease_to_alias  疾病与别名关系
  - diseases_to_part  疾病与部位关系
  - disease_to_department  疾病与科室关系
  - disease_to_complication  疾病与并发症关系
  - disease_to_drug  疾病与药品关系
- **disease 实体 属性信息**：
  - name
  - age 年龄
  - infection 传染性
  - insurance  医保
  - checklist  检查项
  - treatment  治疗方法

读取传输的文件，分析出实体的信息和关系和属性（Pandas）

```python
def read_file(self):
        """
        读取文件，获得实体，实体关系
        :return:
        """
        # 用pandas做分析
        # cols = ["name", "alias", "part", "age", "infection", "insurance", "department", "checklist", "symptom",
        #         "complication", "treatment", "drug", "period", "rate", "money"]
        # 实体
        diseases = []  # 疾病
        aliases = []  # 别名
        symptoms = []  # 症状
        parts = []  # 部位
        departments = []  # 科室
        complications = []  # 并发症
        drugs = []  # 药品

        # 疾病的属性：age, infection, insurance, checklist, treatment, period, rate, money
        diseases_infos = []
        # 各实体间的关系
        disease_to_symptom = []  # 疾病与症状关系
        disease_to_alias = []  # 疾病与别名关系
        diseases_to_part = []  # 疾病与部位关系
        disease_to_department = []  # 疾病与科室关系
        disease_to_complication = []  # 疾病与并发症关系
        disease_to_drug = []  # 疾病与药品关系

        # pandas读取，编码的格式位置索引（全提取）提取value
        all_data = pd.read_csv(self.data_path, encoding='gb18030').loc[:, :].values
        # 逐行进行操作
        for data in all_data:
            disease_dict = {}  # 疾病信息
            # 疾病（strip()默认去掉开头结尾的空格）
            disease = str(data[0]).replace("...", " ").strip()
            # 疾病属性的字典
            disease_dict["name"] = disease
            # 别名
            # 使用正则表达式的库来操作
            # 取出别名列的属性
            # 具体列数据的提取操作，视情况而定
            line = re.sub("[，、；,.;]", " ", str(data[1])) if str(data[1]) else "未知"
            for alias in line.strip().split():
                aliases.append(alias)
                disease_to_alias.append([disease, alias])
            # 部位
            part_list = str(data[2]).strip().split() if str(data[2]) else "未知"
            for part in part_list:
                parts.append(part)
                diseases_to_part.append([disease, part])
            # 年龄
            age = str(data[3]).strip()
            disease_dict["age"] = age
            # 传染性
            infect = str(data[4]).strip()
            disease_dict["infection"] = infect
            # 医保
            insurance = str(data[5]).strip()
            disease_dict["insurance"] = insurance
            # 科室
            department_list = str(data[6]).strip().split()
            for department in department_list:
                departments.append(department)
                disease_to_department.append([disease, department])
            # 检查项
            check = str(data[7]).strip()
            disease_dict["checklist"] = check
            # 症状
            symptom_list = str(data[8]).replace("...", " ").strip().split()[:-1]
            for symptom in symptom_list:
                # 实体数组和关系数组
                symptoms.append(symptom)
                disease_to_symptom.append([disease, symptom])
            # 并发症
            complication_list = str(data[9]).strip().split()[:-1] if str(data[9]) else "未知"
            for complication in complication_list:
                complications.append(complication)
                disease_to_complication.append([disease, complication])
            # 治疗方法
            treat = str(data[10]).strip()[:-4]
            disease_dict["treatment"] = treat
            # 药品
            drug_string = str(data[11]).replace("...", " ").strip()
            for drug in drug_string.split()[:-1]:
                drugs.append(drug)
                disease_to_drug.append([disease, drug])
            # 治愈周期
            period = str(data[12]).strip()
            disease_dict["period"] = period
            # 治愈率
            rate = str(data[13]).strip()
            disease_dict["rate"] = rate
            # 费用
            money = str(data[14]).strip() if str(data[14]) else "未知"
            disease_dict["money"] = money

            diseases_infos.append(disease_dict)

        # return set()去掉重复项
        return set(diseases), set(symptoms), set(aliases), set(parts), set(departments), set(complications), \
                set(drugs), disease_to_alias, disease_to_symptom, diseases_to_part, disease_to_department, \
                disease_to_complication, disease_to_drug, diseases_infos
```

创建节点

这部分代码**主要是为了创建不包含属性的 节点**

像是，别名、部位什么的

```python
def create_node(self, label, nodes):
        """
        创建节点
        :param label: 标签
        :param nodes: 节点
        :return:
        """
        count = 0
        for node_name in nodes:
            node = Node(label, name=node_name)
            self.graph.create(node)
            count += 1
            print(count, len(nodes))
        return
```

**创建带有属性节点*****(疾病啥的)**

```python
def create_diseases_nodes(self, disease_info):
        """
        创建疾病节点的属性
        :param disease_info: list(Dict)
        :return:
        """
        count = 0
        for disease_dict in disease_info:
            # 创造带有属性的节点
            node = Node("Disease", name=disease_dict['name'], age=disease_dict['age'],
                        infection=disease_dict['infection'], insurance=disease_dict['insurance'],
                        treatment=disease_dict['treatment'], checklist=disease_dict['checklist'],
                        period=disease_dict['period'], rate=disease_dict['rate'],
                        money=disease_dict['money'])
            self.graph.create(node)
            count += 1
            print(count)
        return
```

**创建知识图谱实体**

```python
def create_graphNodes(self):
        """
        创建知识图谱实体
        :return:
        """
        disease, symptom, alias, part, department, complication, drug, rel_alias, rel_symptom, rel_part, \
        rel_department, rel_complication, rel_drug, rel_infos = self.read_file()
        self.create_diseases_nodes(rel_infos)
        self.create_node("Symptom", symptom)
        self.create_node("Alias", alias)
        self.create_node("Part", part)
        self.create_node("Department", department)
        self.create_node("Complication", complication)
        self.create_node("Drug", drug)

        return
```

**创建实体关系边**(为下一步两个实体创建关系做准备)

```python
 def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
        """
        创建实体关系边
        :param start_node:
        :param end_node:
        :param edges:
        :param rel_type:
        :param rel_name:
        :return:
        """
        count = 0
        # 去重处理
        set_edges = []
        for edge in edges:
            set_edges.append('###'.join(edge))
        all = len(set(set_edges))
        for edge in set(set_edges):
            edge = edge.split('###')
            p = edge[0]
            q = edge[1]
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" % (
                start_node, end_node, p, q, rel_type, rel_name)
            try:
                self.graph.run(query)
                count += 1
                print(rel_type, count, all)
            except Exception as e:
                print(e)
        return
```

**创建知识图谱关系**

```python
 def create_graphRels(self):
        disease, symptom, alias, part, department, complication, drug, rel_alias, rel_symptom, rel_part, \
        rel_department, rel_complication, rel_drug, rel_infos = self.read_file()

        self.create_relationship("Disease", "Alias", rel_alias, "ALIAS_IS", "别名")
        self.create_relationship("Disease", "Symptom", rel_symptom, "HAS_SYMPTOM", "症状")
        self.create_relationship("Disease", "Part", rel_part, "PART_IS", "发病部位")
        self.create_relationship("Disease", "Department", rel_department, "DEPARTMENT_IS", "所属科室")
        self.create_relationship("Disease", "Complication", rel_complication, "HAS_COMPLICATION", "并发症")
        self.create_relationship("Disease", "Drug", rel_drug, "HAS_DRUG", "药品")
```

### 五、总结

Neo4j**是一个高性能的,NOSQL图形数据库，它将结构化数据存储在网络上而不是表中**。**Neo4j也可以被看作是一个高性能的图引擎，该引擎具有成熟数据库的所有特性**。Neo4j是一个高度可扩展的本机图形数据库，旨在专门利用数据和数据关系。

。使用Neo4j，开发人员可以构建智能应用程序。