[TOC]

# JavaScript基础

语言特定

```
解释性语言
基于对象
事件驱动，可以直接读用户或客户输入做出相应，无需经过Web服务程序
跨平台，依赖浏览器本身，与操作环境无关
安全性，不允许访问本地的硬盘，也不允许将数据存入服务器，不允许对网络文档进行修改和删除，只能通过浏览器实现信息浏览和动态交互

```

页面行为


```
部分动画效果、页面与用户的交互、页面功能
```

## 嵌入页面的方式

```javascript
# 行间事件
<input type="button" name="" onclick="alert('ok！');">
# 页面script标签嵌入
<script type="text/javascript"> alert('ok！');</script>
# 外部引入
<script type="text/javascript" src="js/index.js"></script>
```

## 加载执行

```javascript
注意：若把javascript写在元素的上面，就会出错，因为页面上从上往下加载执行的，javascript去页面上获取元素div1的时候，元素div1还没有加载，解决方法有两种：
第一种方法：将javascript放到页面最下边；
第二种方法：将javascript语句放到window.onload触发的函数里面,获取元素的语句会在页面加载完后才执行。
window.onload = function(){
        var oDiv = document.getElementById('div1');
    }
```

## 调试程序的方法

```
1、alert(变量名)			弹窗显示，会暂停程序运行
2、console.log(变量名)		浏览器控制台显示，不中断
3、document.title=变量名	页面标题显示，不中断
4、断点调试				   在浏览器的sources中设置断点
```

## 操作元素属性

```javascript
操作元素属性 
读取属性		var 变量 = 元素.属性名 
改写属性		元素.属性名 = 新属性值 
注意：用js读取元素的属性必须是在行间已有赋值的，否则为空


属性名在js中的写法 
1、html的属性和js里面属性写法一样
2、“class” 属性写成 “className”
3、“style” 属性里面的属性，有横杠的改成驼峰式，比如：“font-size”，改成”style.fontSize”

innerHTML 
innerHTML可以读取或者写入标签包裹的内容
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
        //读取
        var sTxt = oDiv.innerHTML;
        alert(sTxt);
        //写入
        oDiv.innerHTML = '<a href="http://www.itcast.cn">传智播客<a/>';
    }
</script>
......
<div id="div1">这是一个div元素</div>
```

## 语言基础

### 数据类型

- 数值型

```javascript
0		//十进制
Oxff	//十六进制
0366	//八进制
3.14	//浮点型
6e+3	//科学计数浮点型
Infinity//无限大
NaN		//非数字
```

- 字符串

```
"你好"
'hello'
"nice to meet 'you'!"
'hello "everyone"'
```

转义

```
\b		//退格
\n		//换行符
\t		//水平制表符
\f		//换页
\'		//单引号，在单引号嵌套时需用
\"		//双引号，在双引号嵌套时需用
\v		//垂直制表符
\r		//回车符
\\		//反斜杠
\OOO	//八进制整数
\xHH	//十六进制整数
\uhhh	//十六进制编码的Unicode字符
```

- 布尔型

```
true
false
```

- undefined

```
变量声明未初始化，它的值就是undefined
```

- null

```
表示空对象，如果定义的变量将来准备保存对象，可以将变量初始化为null,在页面上获取不到对象，返回的值就是null
```

### 常量与变量

- 常量

```
在程序运行过程中保持不变的数据
```

- 变量

```
指程序中一个已经命名的存储单元，主要作用是为数据操作提供存放信息的容器。
有变量名和变量值
```

> 命名

```
变量、函数、属性、函数参数命名规范
1、区分大小写
2、第一个字符必须是字母、下划线（_）或者美元符号（$）
3、其他字符可以是字母、下划线、美元符或数字
4、不能包含空格或+、-等符号
5、不能使用关键字

匈牙利命名风格：
对象o Object 比如：oDiv
数组a Array 比如：aItems
字符串s String 比如：sUserName
整数i Integer 比如：iItemCount
布尔值b Boolean 比如：bIsComplete
浮点数f Float 比如：fPrice
函数fn Function 比如：fnHandler
正则表达式re RegExp 比如：reEmailCheck
```

> 声明

```
//弱类型语言，变量类型由它的值来决定。 定义变量需要用关键字 'var'
var iNum = 123;
//同时定义多个变量可以用","隔开，公用一个‘var’关键字
var iNum = 45,sTr='qwe',sCount='68';
```

> 赋值

```
var lesson = "English"
//或者
var lesson;
lesson = "English"
```

> 共有特性

```
所有变量都拥有可以读取和更新的特性
value		属性值，其为默认属性
writable	若属性被更新， 将其设置为true
enumerable	在枚举对象成员时，若该属性应被包括在内，设置为true
configurable若属性可以被删除，且该特性可以被修改，设置为true
```

### 运算符

> 算数运算符

| 运算符 | 描述 | 示例       |
| ------ | ---- | ---------- |
| +      | 加   | 3+6        |
| -      | 减   | 6-2        |
| *      | 乘   | 2*3        |
| /      | 除   | 12/3       |
| %      | 求模 | 7%4        |
| ++     | 自增 | i=6; j=i++ |
| --     | 自减 | i=6; j=i-- |

> 字符串运算符

| 运算符 | 描述                               | 示例                          |
| ------ | ---------------------------------- | ----------------------------- |
| +      | 连接两个字符串                     | 'a'+'b'                       |
| +=     | 连接两个字符串，并将结果赋给第一个 | var name = 'a'<br>name += 'b' |

> 比较运算符

| 运算符 | 描述                     | 示例      |
| ------ | ------------------------ | --------- |
| <      | 小于                     | 1<6       |
| >      | 大于                     | 4>3       |
| <=     | 小于等于                 | 10<=10    |
| >=     | 大于等于                 | 10>=10    |
| ==     | 等于，判断值不判断类型   | '5'==5    |
| ===    | 绝对等于，判断值和类型   | '5'==='5' |
| !=     | 不等于，判断值不判断类型 | 4 != 5    |
| !==    | 不绝对等于，判断值和类型 | '4'!=4    |

> 赋值运算符

| 运算符 | 描述       | 示例  |
| ------ | ---------- | ----- |
| =      | 赋值       | a =10 |
| +=     | 求和后赋值 | a+=10 |
| -=     | 求差后赋值 | a-=10 |
| *=     | 求乘后赋值 | a*=10 |
| /=     | 求除后赋值 | a/=10 |
| %=     | 求模后赋值 | a%=10 |

> 逻辑运算符

| 运算符 | 描述 | 示例   |
| ------ | ---- | ------ |
| &&     | 与   | a&&b   |
| \|\|   | 或   | a\|\|b |
| ！     | 非   | !a     |

> 条件运算符

```
表达式？结果1：结果2
```

> 其他运算符

逗号

```
// 逗号将多个表达式排在一起，整个表达式的值为最后一个表达式的值
var a,b,c,d;
a=(b=3,c=4,d=5)
```

typeof

```
// 判断操作数的数据类型，返回一个字符串
typeof 操作数
```

new

```
// 创建一个新的内置对象实例
对象实例名称 = new 对象类型(参数)
对象实例名称 = new 对象类型
```
### 注释

```
javascript语句开始可缩进也可不缩进，缩进是为了方便代码阅读，一条javascript语句应该以“;”结尾;

// 单行注释
/*  
    多行注释
    1、...
    2、...
*/
```

## 基本语句

### 条件语句

> if

```
//if语句
if(){}
//if...else
if(){}
else{}
//多重if else语句
if(){}
else if(){}
else if(){}
else{}
//嵌套
if(){
    if(){}
    else{}
}
else{
    if(){}
    else{}
}
```

> switch

```
switch(表达式){
    case 常量表达式1：
    	语句1；
    	break；
    case 常量表达式2：
    	语句2；
    	break;
    ...
    default:
    	语句n;
    	break
}
```

### 循环语句

> while

```
# while循环
while(条件){循环体}


```

> do…while

```
do{
    语句
}while(表达式)
```

> for

```
for（var i=0;i<len;i++）{循环体}
```

### 跳转语句

> continue

```
只能用于while、for、do...while
跳过本次循环，并开始下一次循环
```

> break

```
通常用于while、for、do...while
跳出循环
```

### 异常处理

`try…catch…finally`

```
try{
    语句
}catch(exception){
    语句
}finally{
   	语句
}
```

Error对象属性

```
name	异常类型字符串
message	实际的异常信息
```

throw抛异常

```
throw new Error("自定义异常信息")
```
eg

```javascript
try{
    var x = 5;
    var y = 0;
    if (y == 0){
        throw("Can't divide by zero")
    }
    console.log(x/y);
}
catch(e){
    console.log("Error:" + e);
}
finally{
    console.log("Finally block executed");
}
```

## 函数

### 定义

> function

```
function 函数名([参数1，参数2，...]){
    语句
    [return 返回值]
}
```

> 匿名函数

```
var 变量名 = fucntion([参数1，参数2，...]){
    语句
    [return 返回值]
}
```

> Function()

```
var 变量名 = new Function("参数1", "参数2", ... "函数体")
```

### 调用

> 简单调用

```
函数名(传递给函数的参数1，参数2, ...)
```

> 事件响应中

```
<input type="button" value="提交" onClick="函数名(参数)">
```

> 链接中

```
<a href="javascript: 函数名(参数)">
```

### 编译执行

```
# 变量与函数预解析 
JavaScript解析过程分为两个阶段，先是编译阶段，然后执行阶段，在编译阶段会将function定义的函数提前，并且将var定义的变量声明提前，将它赋值为undefined。
```

### 变量作用域

```
变量作用域指的是变量的作用范围，javascript中的变量分为全局变量和局部变量。

全局变量：在函数之外定义的变量，为整个页面公用，函数内部外部都可以访问。
局部变量：在函数内部定义的变量，只能在定义该变量的函数内部访问，外部无法访问。

优先级：在函数内部若使用var新建与全局变量同名的变量，则在函数内部调用时，优先调用内部变量，不对外部变量产生影响
```

### 封闭函数

```javascript
封闭函数是javascript中匿名函数的另外一种写法，
具有如下特性：
1.脚本一旦解析，函数就开始就执行
2.函数不用命名。

封闭函数的作用 
封闭函数可以创造一个独立的空间，在封闭函数内定义的变量和函数不会影响外部同名的函数和变量，可以避免命名冲突，在页面上引入多个js文件时，用这种方式添加js文件比较安全

# 创建封闭函数：
# 方法一：
(function(){
    alert('hello!');
})();
# 方法二
;!function(){
    alert('hello!');
}()
# 方法三
;~function(){
    alert('hello!');
}()
```



### 内置函数

| 函数                 | 用途       | 说明                                           |
| -------------------- | ---------- | ---------------------------------------------- |
| parseInt(sting, [n]) | 数值处理   | 字符转换为整型                                 |
| parseFloat(string)   | 数值处理   | 字符转换为浮点型                               |
| isNaN(num)           | 数值判断   | 是否为NaN                                      |
| ifFinite(num)        | 数值判断   | 是否为无穷大                                   |
| eval(string)         | 字符串处理 | 计算字符串表达式的值，执行其中的JavaScript代码 |
| escape(string)       | 字符串处理 | 将特殊字符进行编码                             |
| unescape(string)     | 字符串处理 | 将编码后的字符串进行解码                       |
| encodeURL(url)       | 字符串处理 | 将URL字符串进行编码                            |
| decodeURL(url)       | 字符串处理 | 对已编码的URL字符串进行解码                    |



## 继承

- 使用原型

`javaScript`通过一种被称为原型继承的方法提供对继承的支持。这意味着一个原型可以拥有`prototype`属性，也可以拥有一个原型。称为原型链

创建一个继承自Item的新对象`SpecialItem`：

1. 创建``SpecialItem()``构造函数

```
function SpecialItem(name){
    this.name = name;
    this.deacribe = function(){
        console.log(this.name + ": color=" + this.color);
    }
}
```

2. 为构建继承关系，设置prototype属性

```
SpecialItem.prototype = new Item();
```

3. 指定其他属性

```
function SpecialItem(name, color, count){
	Item.call(this, color, count);
    this.name = name;
    this.deacribe = function(){
        console.log(this.name + ": color=" + this.color);
    }
}
```

4. 创建对象

```
var special = new SpecialItem("Widget", "Purple", 4);
special.log();
special.describe();
special.log(special);
```

- 使用Create

更改2构建继承关系

```
SpecialItem.prototype = Object.create(Item.prototype);
SpecialItem.prototype.constructor = SpecialIem;
```

- 使用类关键字

```
class Item{
    constructor(color, count){
        this.color = color;
        this.count = count;
        this.log = function(){
            console.log(this.name + ": color=" + this.color);
        };
    }
}

class SpecialItem extends Item{
    constructor(name, color, count){
        super(color, count);
        this.name = name;
        this.describe = function(){
            console.log(this.name + ": color=" + this.color);
        }
    }
}
```

为了保证两种方法解决方案的一致性，增加

```
Item.prototype.isAvailable = true;
Item.prototype.add = function(n){this.count += n;};
```






