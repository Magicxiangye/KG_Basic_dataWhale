#新建的项目包
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