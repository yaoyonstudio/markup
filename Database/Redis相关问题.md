# Redis简介

## 作用

Redis是一个开源的内存中的数据结构存储系统，它可以用作：**数据库、缓存和消息中间件**。

Redis不使用表，他的数据库不会预定义或者强制去要求用户对Redis存储的不同数据进行关联。

## 数据结构

它支持多种类型的数据结构，如字符串（String），散列（Hash），列表（List），集合（Set），有序集合（Sorted Set或者是ZSet）与范围查询，Bitmaps，Hyperloglogs 和地理空间（Geospatial）索引半径查询。**其中常见的数据结构类型有：String、List、Set、Hash、ZSet这5种。**

Redis 内置了复制（Replication），LUA脚本（Lua scripting）， LRU驱动事件（LRU eviction），事务（Transactions） 和不同级别的磁盘持久化（Persistence），并通过 Redis哨兵（Sentinel）和自动分区（Cluster）提供高可用性（High Availability）。

## 持久化存储

Redis也提供了持久化的选项，这些选项可以让用户将自己的数据保存到磁盘上面进行存储。根据实际情况，可以每隔一定时间将数据集导出到磁盘（ROB快照），或者追加到命令日志中（AOF只追加文件），他会在执行写命令时，将被执行的写命令复制到硬盘里面。您也可以关闭持久化功能，将Redis作为一个高效的网络的缓存数据功能使用。

## 工作模式

数据库的工作模式按存储方式可分为：硬盘数据库和内存数据库。Redis 将数据储存在内存里面，读写数据的时候都不会受到硬盘 I/O 速度的限制，所以速度极快。

## 单线程模型

Redis客户端对服务端的每次调用都经历了发送命令，执行命令，返回结果三个过程。其中执行命令阶段，由于Redis是单线程来处理命令的，所有每一条到达服务端的命令不会立刻执行，所有的命令都会进入一个队列中，然后逐个被执行。并且多个客户端发送的命令的执行顺序是不确定的。但是可以确定的是不会有两条命令被同时执行，不会产生并行问题，这就是Redis的单线程基本模型。

## 速度快/处理高并发原因

1、完全基于内存，绝大部分请求是纯粹的内存操作，非常快速。数据存在内存中，类似于HashMap，HashMap的优势就是查找和操作的时间复杂度都是O(1)；

2、数据结构简单，对数据操作也简单，Redis中的数据结构是专门进行设计的；

3、采用单线程，避免了不必要的上下文切换和竞争条件，也不存在多进程导致的切换而消耗 CPU，不用去考虑多线程各种锁的问题，不存在加锁释放锁操作，没有因为可能出现死锁而导致的性能消耗；由于单线程无法发挥多核CPU性能，不过可以通过在单机开多个Redis实例来完善

4、使用多路I/O复用模型，非阻塞IO；

5、使用底层模型不同，它们之间底层实现方式以及与客户端之间通信的应用协议不一样，Redis直接自己构建了VM 机制 ，因为一般的系统调用系统函数的话，会浪费一定的时间去移动和请求；

## redis的其他特点

（1）Redis是单进程单线程的

redis利用队列技术将并发访问变为串行访问，消除了传统[数据库](http://lib.csdn.net/base/mysql)串行控制的开销

（2）读写分离模型

通过增加Slave DB的数量，读的性能可以线性增长。为了避免Master DB的单点故障，集群一般都会采用两台Master DB做双机热备，所以整个集群的读和写的可用性都非常高。
读写分离[架构](http://lib.csdn.net/base/architecture)的缺陷在于，不管是Master还是Slave，每个节点都必须保存完整的数据，如果在数据量很大的情况下，集群的扩展能力还是受限于单个节点的存储能力，而且对于Write-intensive类型的应用，读写分离[架构](http://lib.csdn.net/base/architecture)并不适合。

（3）数据分片模型

为了解决读写分离模型的缺陷，可以将数据分片模型应用进来。

可以将每个节点看成都是独立的master，然后通过业务实现数据分片。

结合上面两种模型，可以将每个master设计成由一个master和多个slave组成的模型。

（4）Redis的回收策略

```
volatile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最少使用的数据淘汰

volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰

volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰

allkeys-lru：从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰

allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰

no-enviction（驱逐）：禁止驱逐数据
```

注意这里的6种机制，volatile和allkeys规定了是对已设置过期时间的数据集淘汰数据还是从全部数据集淘汰数据，后面的lru、ttl以及random是三种不同的淘汰策略，再加上一种no-enviction永不回收的策略。

**使用策略规则：**

　　1、如果数据呈现幂律分布，也就是一部分数据访问频率高，一部分数据访问频率低，则使用allkeys-lru

　　2、如果数据呈现平等分布，也就是所有的数据访问频率都相同，则使用allkeys-random



## 其他问题

**Redis不存在线程安全问题？ **
Redis采用了线程封闭的方式，把任务封闭在一个线程，自然避免了线程安全问题，不过对于需要依赖多个redis操作的复合操作来说，依然需要锁，而且有可能是分布式锁

**Redis为什么是单线程的？**

因为CPU不是Redis的瓶颈。Redis的瓶颈最有可能是机器内存或者网络带宽。（以上主要来自官方FAQ）既然单线程容易实现，而且CPU不会成为瓶颈，那就顺理成章地采用单线程的方案了。关于redis的性能，官方网站也有，普通笔记本轻松处理每秒几十万的请求，参见：[How fast is Redis?](https://link.zhihu.com/?target=https%3A//redis.io/topics/benchmarks)

**如果万一CPU成为你的Redis瓶颈了，或者，你就是不想让服务器其他核闲置，那怎么办？**

那也很简单，你多起几个Redis进程就好了。Redis是keyvalue数据库，又不是关系数据库，数据之间没有约束。只要客户端分清哪些key放在哪个Redis进程上就可以了。redis-cluster可以帮你做的更好。

**单线程可以处理高并发请求吗？**

采用多路 I/O 复用技术可以让单个线程高效的处理多个连接请求（尽量减少网络IO的时间消耗） 
（1）为什么不采用多进程或多线程处理？

> 多线程处理可能涉及到锁 
> 多进程处理会涉及到进程切换而消耗CPU

（2）单线程处理的缺点？

> 无法发挥多核CPU性能，不过可以通过在单机开多个Redis实例来完善

**使用Redis有哪些好处？**

(1) 速度快，因为数据存在内存中，类似于HashMap，HashMap的优势就是查找和操作的时间复杂度都是O(1)

(2) 支持丰富数据类型，支持string，list，set，sorted set，hash

(3) 支持事务，操作都是原子性，所谓的原子性就是对数据的更改要么全部执行，要么全部不执行

(4) 丰富的特性：可用于缓存，消息，按key设置过期时间，过期后将会自动删除

**Redis相比memcached有哪些优势？**

(1) memcached所有的值均是简单的字符串，[redis](http://lib.csdn.net/base/redis)作为其替代者，支持更为丰富的数据类型

(2) redis的速度比memcached快很多

(3) redis可以持久化其数据

(4)Redis支持数据的备份，即master-slave模式的数据备份。

(5)使用底层模型不同
它们之间底层实现方式 以及与客户端之间通信的应用协议不一样。
Redis直接自己构建了VM 机制 ，因为一般的系统调用系统函数的话，会浪费一定的时间去移动和请求。
(6）value大小：redis最大可以达到1GB，而memcache只有1MB

# 主从时注意事项

(1) Master最好不要做任何持久化工作，如RDB内存快照和AOF日志文件

(Master写内存快照，save命令调度rdbSave函数，会阻塞主线程的工作，当快照比较大时对性能影响是非常大的，会间断性暂停服务，所以Master最好不要写内存快照;AOF文件过大会影响Master重启的恢复速度)

(2) 如果数据比较重要，某个Slave开启AOF备份数据，策略设置为每秒同步一次

(3) 为了主从复制的速度和连接的稳定性，Master和Slave最好在同一个局域网内

(4) 尽量避免在压力很大的主库上增加从库

(5) 主从复制不要用图状结构，用单向链表结构更为稳定，即：Master <- Slave1 <- Slave2 <- Slave3...

这样的结构方便解决单点故障问题，实现Slave对Master的替换。如果Master挂了，可以立刻启用Slave1做Master，其他不变。