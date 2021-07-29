## pyTape

-----

“pyTape”模块加入了一个叫做“Tape”的数据类型，“Tape”包含了一条很长的“带子”用来记录信息，另外还有一枚“指针”指向带子上面任意的位置，操作上面的数据。

这个模块原来是为上课的时候摸鱼，尝试brainfxxk这样思路清奇语法有趣的语言而准备的。~~使用方法“exce()”开启新世界。~~



### 安装与使用

-----

```pip install pyTape``` 或者进入dist目录直接选择whl安装

导入模块使用```from pyTape import pyTape```或者可以为了使用方便，写成```from pyTape import pyTape as pt```

script/dist目录下有两个文件，可以在windows或linux环境中执行一些brainfxxk指令。

> 使用方法：```cpl {文件名} {文件名}```

接受若干个文件名作为参数，此时，这些文件里储存的brainfxxk指令将逐条地在命令行里执行

若没有提供任何文件名，cpl则会开始交互式brainfxxk编程，用“q”或“exit()”退出



### 关于列表的操作

-----

记录信息的“带子”用一个列表实现，截取列表里面的某一段信息可以使用这样的表达:

> ```{实例名}[下标]``` =等同于= ```{实例名}.reg[下标]```

获取列表里所含元素的数量可以使用这样的表达:

> ```len({实例名})``` =等同于= ```len({实例名}.reg)```

输出列表可以使用这样的表达:

> ```print({实例名})``` =等同于= ```print({实例名}.reg)```

列表里面最小的元素值为0，类型全部为整数，也就是说列表里不会出现负数，只会出现正整数。



### exce()实现brainfxxk语法

-----

~~exce()需要两个参数，其中一个是self~~，另外一个参数作为brainfxxk指令，以字符串的形式传递，如：

> ```{实例名}.exce(<brainfxxk指令>)```或者```{实例名}(<brainfxxk指令>)```



### 关于brainfxxk指令

-----

这个模块暂时只支持```+ - < > [ ] , .```几种运算

#### 运算符"+"

使指针所指元素的值+1

#### 运算符"-"

使指针所指元素的值-1

#### 运算符"<"

指针指向左边一个元素

#### 运算符">"

指针指向右边一个元素

#### 运算符"["与"]"

两个中括号括起来的运算作为循环体，指针所指元素作为while循环的条件

#### 运算符","

请求一个输入，覆盖指针所指元素原来的值

#### 运算符"."

将指针所指元素转换成字符类型输出



### 其他操作

-----

#### 运算符"("与")"

用括号括起来的部分循环n遍，n作为一个正整数紧贴在左边的括号外

> 如```+>+>+>```可以写成```3(+>)```

若需要循环的部分为单个运算符（"("除外），则可以直接省略括号

> 如```+++```可以写成```3+```

#### 运算符"?"

输出一个整数，指针指向元素的下标

#### 运算符"&"

输出一个整数，指针所指元素的值

#### 运算符"*"

重置列表

#### 运算符"!"

将指针指向元素的值为n，则将指针重新指向列表中下标为n的元素

#### Tape的加法

加法符号左右必须都是Tape类型数据，加法的结果为两个列表的元素各自相加

#### Tape的减法

减法符号两边必须是Tape类型数据，左边为被减数右边为减数，结果是两个列表的元素各自相减取绝对值(因为列表里面不能存在负数)

#### Tape的乘法

乘法符号左右必须都是Tape类型数据，结果为两个列表的元素各自相乘

#### Tape的除法

除法符号两边必须是Tape类型数据，左边为被除数右边为除数，结果是两个列表的元素各自相除取整(因为列表里面只能有正整数)

#### Tape取模

%两边必须是Tape类型数据，左边为被除数右边为除数，结果是两个列表的元素各自取模



#### 更新

----

##### 0.0.5

调整了运算符"[]","]"使循环嵌套可能

改掉一些小问题
