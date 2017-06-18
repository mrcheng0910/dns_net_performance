### 基于多因素测量和分析用户到本地DNS递归服务器的网络性能

本作业从北京和山东两个网络探测点，分别对大量北京和山东的 DNS 递归服务器进行网络性能测量，模拟用户设置不同 DNS 服务器。
分别从网络时延、时延抖动、丢包率、平均路径长度多个因素测量用户到 DNS 递归服务器的网络性能， 并从多个维度对数据进行分析。

#### 项目文件介绍
* net_result_sd_sd.sql   
数据库结构文件，直接导入即可使用。目前所有数据所在数据库3服务器上cyn_test数据库中。

* 基于***网络性能.pdf   
对已有数据进行的简单分析和总结，并且写出待改进地方。

*  database.py  
数据库操作文件

* netState.py  
读取要查询的DNS服务器IP进行测量

* source_ip  
保存原始dns数据的目录

* result  
保存结果目录

* insert2db.py  
将结果数据存入数据库，并且添加地理位置、运营商等信息

* ztfb.py  
简单的去除异常数据，z-score大于3或小于-3的去掉。读取`test.txt`中的数据。

* DNS_track.py   
验证dns是否可正常解析域名，该程序自己未使用，后续可能会用到

* ip_location  
ip地理位置确认

#### 运行命令

`python netState.py ip_source.txt result.txt` 
* ip_source.txt 为要探测的DNS数据
* result.txt 为保存的结果文件

#### 注意事项

根据论文中的描述进行相关地方的改进。
* 山东到北京，北京到山东的路径长度差这么多，why