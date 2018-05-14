[TOC]

# JQuery

```
jquery是一个函数库，一个js文件，页面用script标签引入这个js文件就可以使用。

jQuery的版本分为1.x系列和2.x、3.x系列，1.x系列兼容低版本的浏览器，2.x、3.x系列放弃支持低版本浏览器

1、http://jquery.com/ 官方网站
2、https://code.jquery.com/ 版本下载
```

## 文档加载完再执行

```javascript
将获取元素的语句写到页面头部，会因为元素还没有加载而出错，jquery提供了ready方法解决这个问题，它的速度比原生的 window.onload 更快。

$(document).ready(function(){     ......
});
//简写                             
$(function(){
......                               
})
```

## 选择元素

### 选择器

```
jquery选择器可以快速地选择元素，选择规则和css样式相同.
$('#myId') //选择id为myId的网页元素
$('.myClass') // 选择class为myClass的元素
$('li') //选择所有的li元素
$('#ul1 li span') //选择id为为ul1元素下的所有li下的span元素
$('input[name=first]') // 选择name属性等于first的input元素
```

### 选择集过滤

```
$('div').has('p'); // 选择包含p元素的div元素
$('div').not('.myClass'); //选择class不等于myClass的div元素
$('div').eq(5); //选择第6个div元素
```

### 选择集转移

```
$('#box').prev(); //选择id是box的元素前面紧挨的同辈元素
$('#box').prevAll(); //选择id是box的元素之前所有的同辈元素
$('#box').next(); //选择id是box的元素后面紧挨的同辈元素
$('#box').nextAll(); //选择id是box的元素后面所有的同辈元素
$('#box').parent(); //选择id是box的元素的父元素
$('#box').children(); //选择id是box的元素的所有子元素
$('#box').siblings(); //选择id是box的元素的同级元素
$('#box').find('.myClass'); //选择id是box的元素内的class等于myClass的元素
```

### 判断是否选中的元素

```
jquery有容错机制，即使没有找到元素，也不会出错，可以用length属性来判断是否找到了元素.
length等于0，就是没选择到元素;
length大于0，就是选择到了元素。
```

## 操作样式

```
# 操作行间样式
// 获取div的样式
$("div").css("width");
$("div").css("color");
//设置div的样式
$("div").css("width","30px");
$("div").css({fontSize:"30px",color:"red"});

注意：选择器获取的多个元素，获取信息获取的是第一个

# 操作样式类名
$("#div1").addClass("divClass2") //为id为div1的对象追加样式divClass2
$("#div1").removeClass("divClass")  //移除id为div1的对象的class名为divClass的样式
$("#div1").removeClass("divClass divClass2") //移除多个样式，中间空格
$("#div1").toggleClass("anotherClass") //重复切换anotherClass样式
```
## 属性操作

```
# html() 取出或设置html内容
// 取出html内容
var $htm = $('#div1').html();
// 设置html内容
$('#div1').html('<span>添加文字</span>');

# prop() 取出或设置元素除了css之外的某个属性的值
// 取出图片的地址
var $src = $('#img1').prop('src');
// 设置图片的地址和alt属性
$('#img1').prop({src: "test.jpg", alt: "Test Image" });
```
## 链式调用
```
jquery对象的方法会在执行完后返回这个jquery对象，所有jquery对象的方法可以连起来写.
$('#div1') // id为div1的元素
.children('ul') //该元素下面的ul子元素
.slideDown('fast') //高度从零变到实际高度来显示ul元素
.parent()  //跳到ul的父元素，也就是id为div1的元素
.siblings()  //跳到div1元素平级的所有兄弟元素
.children('ul') //这些兄弟元素中的ul子元素
.slideUp('fast');  //高度实际高度变换到零来隐藏ul元素
```

## 绑定事件

```
# 给元素绑定click事件，可以用如下方法：
$('#btn1').click(function(){
    // 内部的this指的是原生对象
    // 使用jquery对象用 $(this)
})

# 获取元素的索引值 
获得匹配元素相对于其同胞元素的索引位置，此时用index()

# jquery事件
blur() 				元素失去焦点
focus() 			元素获得焦点
click() 			鼠标单击
mouseover() 		鼠标进入（进入子元素也触发）
mouseout() 			鼠标离开（离开子元素也触发）
mouseenter() 		鼠标进入（进入子元素不触发）
mouseleave() 		鼠标离开（离开子元素不触发）
hover() 			同时为mouseenter和mouseleave事件指定处理函数
ready() 			DOM加载完成
submit() 			用户递交表单
```

## 动画与特殊效果

```
通过animate方法可以设置元素某属性值上的动画，可以设置一个或多个属性值，动画执行完成后会执行一个函数。
$('#div1').animate({
    width:300,
    height:300
},1000,'swing',function(){
    alert('done!');
});
animate参数：
参数一：要改变的样式属性值，写成字典的形式
参数二：动画持续的时间，默认400，单位为毫秒，一般不写单位
参数三：动画曲线，默认为‘swing’，缓冲运动，还可设置‘linear’，匀速运动
参数四：动画回调函数，动画完成后执行的匿名函数

# 特殊效果是对常用的动画进行了函数的封装，参数取animate的后三个
fadeIn() 淡入
fadeOut() 淡出
fadeToggle() 切换淡入淡出
hide() 隐藏元素
show() 显示元素
toggle() 切换元素的可见状态
slideDown() 向下展开
slideUp() 向上卷起
slideToggle() 依次展开或卷起某个元素
```

## 循环

```
对jquery选择的对象集合分别进行操作，需要用到jquery循环操作，此时可以用对象上的each方法：
$(function(){
    $('.list li').each(function(){
        $(this).html($this.index());
    })
})
```

## 事件冒泡

```
在一个对象上触发某类事件，无论是否有这个对象的时间处理程序，不仅自己执行，还会向这个对象的父级对象传播，从里到外，父级对象所有同类事件都将被激活，直到到达了对象层次的最顶层，即document对象（body/html）。

阻止事件冒泡
执行函数有参数event，且执行
event.stopPropagation();

阻止默认行为
执行函数有参数event，且执行
event.preventDefault();

合并阻止写法：
return false;
```

## 事件委托

```
事件委托就是利用冒泡的原理，把事件加到父级上，通过判断事件来源的子集，执行相应的操作，事件委托首先可以极大减少事件绑定次数，提高性能；其次可以让新加入的子元素也可以拥有相同的操作。

# 一般写法：
$(function(){
    $ali = $('#list li');
    $ali.click(function() {        		$(this).css({background:'red'});
    });
})		
# 委托写法
$(function(){
    $list = $('#list');
    $list.delegate('li', 'click', function() {        				$(this).css({background:'red'});
    });
})
```

## 节点操作

```
元素节点操作指的是改变html的标签结构，它有两种情况：
1、移动现有标签的位置
2、将新创建的标签插入到现有的标签中

创建新标签
var $div = $('<div>'); //创建一个空的div
var $div2 = $('<div>这是一个div元素</div>');

移动或者插入标签的
父元素.append(子元素)：当前元素的内部后面放入另外一个元素
子元素.appendTo(父元素)：当前元素放置到另一元素的内部的后面
父元素.prepend(子元素):当前元素的内部的前面放入另外一个元素
子元素.prepend(父元素)：当前元素放置到另一元素的内部的前面
元素.after(元素)：当前元素的后面放入另一个元素
元素.insertafter(元素)：当前元素放置到另一元素的后面
元素.before(元素)：当前元素的前面放入另一个元素
元素.insertbefore(元素)：当前元素放置到另一元素的前面

删除元素
元素.remove()
```

## 表单验证（正则）

```
1、什么是正则表达式： 
能让计算机读懂的字符串匹配规则。

2、正则表达式的写法：
var re=new RegExp('规则', '可选参数');
var re=/规则/参数;

3、规则中的字符 
1）普通字符匹配：
如：/a/ 匹配字符 ‘a’，/a,b/ 匹配字符 ‘a,b’

2）转义字符匹配：
\d 匹配一个数字，即0-9
\D 匹配一个非数字，即除了0-9
\w 匹配一个单词字符（字母、数字、下划线）
\W 匹配任何非单词字符。等价于[^A-Za-z0-9_]
\s 匹配一个空白符
\S 匹配一个非空白符
\b 匹配单词边界
\B 匹配非单词边界
. 匹配一个任意字符

var sTr01 = '123456asdf';
var re01 = /\d+/;
//匹配纯数字字符串
var re02 = /^\d+$/;
alert(re01.test(sTr01)); //弹出true
alert(re02.test(sTr01)); //弹出false
4、量词：对左边的匹配字符定义个数 
? 出现零次或一次（最多出现一次）
+ 出现一次或多次（至少出现一次）
* 出现零次或多次（任意次）
{n} 出现n次
{n,m} 出现n到m次
{n,} 至少出现n次

5、任意一个或者范围 
[abc123] : 匹配‘abc123’中的任意一个字符
[a-z0-9] : 匹配a到z或者0到9中的任意一个字符

6、限制开头结尾 
^ 以紧挨的元素开头
$ 以紧挨的元素结尾

7、修饰参数：
g： global，全文搜索，默认搜索到第一个结果接停止
i： ingore case，忽略大小写，默认大小写敏感

8、常用函数 
test
用法：正则.test(字符串) 匹配成功，就返回真，否则就返回假

正则默认规则 
匹配成功就结束，不会继续匹配，区分大小写

常用正则规则

//用户名验证：(数字字母或下划线6到20位)
var reUser = /^\w{6,20}$/;

//邮箱验证：        
var reMail = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/i;

//密码验证：
var rePass = /^[\w!@#$%^&*]{6,20}$/;

//手机号码验证：
var rePhone = /^1[34578]\d{9}$/;
```

## JSON

```
json是 JavaScript Object Notation 的首字母缩写，单词的意思是javascript对象表示法，这里说的json指的是类似于javascript对象的一种数据格式

两种结构：
1、对象结构
对象结构是使用大括号“{}”括起来的，大括号内是由0个或多个用英文逗号分隔的“关键字:值”对（key:value）构成的。
语法：
{
    "键名1":值1,
    "键名2":值2,
    "键名n":值n
}
说明：
对象结构是以“{”开始，到“}”结束。其中“键名”和“值”之间用英文冒号构成对，两个“键名:值”之间用英文逗号分隔。
注意，这里的键名是字符串，但是值可以是数值、字符串、对象、数组或逻辑true和false。

2、JSON数组结构
JSON数组结构是用中括号“[]”括起来，中括号内部由0个或多个以英文逗号“,”分隔的值列表组成。
语法：
[
    {
        "键名1":值1,
        "键名2":值2
    },
    {
        "键名3":值3,
        "键名4":值4
    },
    ……
]
说明：
arr指的是json数组。数组结构是以“[”开始，到“]”结束，这一点跟JSON对象不同。 在JSON数组中，每一对“{}”相当于一个JSON对象。 
注意，这里的键名是字符串，但是值可以是数值、字符串、对象、数组或逻辑true和false。
```

## AJAX

ajax技术的目的是让javascript发送http请求，与后台通信，获取数据和信息。ajax技术的原理是实例化xmlhttp对象，使用此对象与后台通信。ajax通信的过程不会影响后续javascript的执行，从而实现异步。

**同步和异步** 
现实生活中，同步指的是同时做几件事情，异步指的是做完一件事后再做另外一件事，程序中的同步和异步是把现实生活中的概念对调，也就是程序中的异步指的是现实生活中的同步，程序中的同步指的是现实生活中的异步。

**局部刷新和无刷新** 
ajax可以实现局部刷新，也叫做无刷新，无刷新指的是整个页面不刷新，只是局部刷新，ajax可以自己发送http请求，不用通过浏览器的地址栏，所以页面整体不会刷新，ajax获取到后台数据，更新页面显示数据的部分，就做到了页面局部刷新。

**同源策略** 
ajax请求的页面或资源只能是同一个域下面的资源，不能是其他域的资源，这是在设计ajax时基于安全的考虑。特征报错提示：

```
XMLHttpRequest cannot load https://www.baidu.com/. No  
'Access-Control-Allow-Origin' header is present on the requested resource.  
Origin 'null' is therefore not allowed access.
```

**ajax使用**

```
$.ajax({
    url:'/js/data.json',
    type:'POST', 
    dataType: json,
    data:{name:'wang',age:25},
    async: true,
    success:function(data){
    	alert(data);
     },
	error:function(){
    	alert("出错")
	},
});
参数说明：
url: 请求地址
type: 请求方式，默认为GET，常用的还有POST
dataType: 预期服务器返回的数据类型。如果不指定，jQuery 将自动根据 HTTP 包 MIME 信息来智能判断，比如 XML MIME 类型就被识别为 XML。可为：json/xml/html/script/jsonp/text
data： 发送给服务器的参数
async: 同步或者异步，默认为true，表示异步
timeout: 设置请求超时时间（毫秒）,此设置将覆盖全局设置。
success： 请求成功之后的回调函数
error： 请求失败后的回调函数

新的写法(推荐)：
$.ajax({
    url: 'js/data.json',
    type: 'GET',
    dataType: 'json',
    data:{'aa':1}
})
.done(function(data) {
    alert(data.name);
})
.fail(function() {
    alert('服务器超时，请重试！');
});
// data.json里面的数据： {"name":"tom","age
```

封装方法：

- load

```javascript
# 从服务器加载数据，并把返回的数据放入被选元素中。
$(selector).load(URL,data,callback)
# eg
$("button").click(function(){
  $("#div1").load("demo_test.txt",function(responseTxt,statusTxt,xhr){
    if(statusTxt=="success")
      alert("外部内容加载成功！");
    if(statusTxt=="error")
      alert("Error: "+xhr.status+": "+xhr.statusText);
  });
});
```

- get

```javascript
# 通过 HTTP GET 请求从服务器上请求数据。
$.get(URL,callback)
# eg
$("button").click(function(){
  $.get("demo_test.asp",function(data,status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});
```

- post

```javascript
# 通过 HTTP POST 请求从服务器上请求数据
$.post(URL,data,callback)
# eg
$("button").click(function(){
  $.post("demo_test_post.asp",
  {
    name:"Donald Duck",
    city:"Duckburg"
  },
  function(data,status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});
```

## jsonp

ajax只能请求同一个域下的数据或资源，有时候需要跨域请求数据，就需要用到jsonp技术，jsonp可以跨域请求数据，它的原理主要是利用了`<script>`标签可以跨域链接资源的特性。jsonp和ajax原理完全不一样，不过jquery将它们封装成同一个函数。

```
$.ajax({
    url:'js/data.js',
    type:'get',
    dataType:'jsonp',
    jsonpCallback:'fnBack'
})
.done(function(data){
    alert(data.name);
})
.fail(function() {
    alert('服务器超时，请重试！');
});

// data.js里面的数据： fnBack({"name":"tom","age":18});
```

eg：获取360搜索关键词联想数据

```
$(function(){
    $('#txt01').keyup(function(){
        var sVal = $(this).val();
        $.ajax({
            url:'https://sug.so.360.cn/suggest?',
            type:'get',
            dataType:'jsonp',
            data: {word: sVal}
        })
        .done(function(data){
            var aData = data.s;
            $('.list').empty();
            for(var i=0;i<aData.length;i++)
            {
                var $li = $('<li>'+ aData[i] +'</li>');
                $li.appendTo($('.list'));
            }
        })        
    })
})

//......

<input type="text" name="" id="txt01">
<ul class="list"></ul>
```






