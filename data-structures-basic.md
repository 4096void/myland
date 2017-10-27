# 数据结构常识
https://www.interviewcake.com/article/python/data-structures-coding-interview
## RAM

RAM 就是「你写的程序」中所有变量、函数、字符串、对象存放的地方，AKA working memory or just memory，我们也叫它「内存」

与内存相对的就是「外存」，存放文档、图片、视频、应用程序，AKA storage sometimes called persistent storage or disc，我们也叫它「硬盘」

内／外存有啥特点？内存快，但容量小；外存慢，但容量大
例如：「你的手提电脑」硬盘容量有 500G 内存才只有 8G

bit 是能表示 0/1 的单位
8 bit = 1 byte

内存里最小的单位就是 byte，而且每一 byte 都有自己的编号，AKA address

内存，也只是「存储」，「实际的数据处理」发生在处理器 AKA processor
而，processor 和 memory 之间的数据读写交互是由「内存控制器」实现的，AKA memory controller

内存控制器对内存有「byte 细度」的直接的「控制／管制」，无比快速高效
That’s why we call it Random Access Memory.
例如：读完地址 64 里的数据，能立刻去读 9927 里的数据

为什么外存读的速度那么慢？
外存没有类似的「外存控制器」来直接控制每 byte，只能等「读／写头」AKA reader 旋转到对应位置才能执行读写

实际上我们写的程序（变量、函数、字符串、对象 etc）对应的内存地址是「连续」的，如果处理器读取数据时也同样能以「连续」的方式去读，就能带来明显的「性能」提升

落实到具体实现，处理器通过内存控制器获取某一地址里的数据时，内存控制器不仅返回目标地址里的数据，还返回「目标地址附近」的数据，并将它们加入自己的「缓存（AKA cache）」里

例如：处理器读取 1230 里的数据后，下一次它需要 1231 里的数据，直接从自己的缓存里就能读取到，比从 RAM 读取快一个数量级

用二进制表示数字

生活中我们使用的数字系统称为十进制 AKA base 10 decimal
因为由 0 数到 9，一共用了十个数字

计算机只有两位 0 1 AKA binary

