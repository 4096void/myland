> 原文：https://medium.freecodecamp.org/react-s-jsx-the-other-side-of-the-coin-2ace7ab62b98

# 硬币反面：JSX
React 刚发布的时候，很多人看了一眼然后有点接受不了。JavaScript 里的那些尖括号是干啥用的？！淦，说好的分离呢？Facebook 到底有没有从社区学到教训？



跟很多人一样，我一开始对于 [React's JSX](https://facebook.github.io/react/docs/jsx-in-depth.html) 的这种做法到底有没有效，也是将信将疑，这点还是可以肯定的。但现在我已经爱上 JSX 了，每当我向新人推荐它，都感觉像在炫耀自己长得一点都不好看的儿子。



这里有一张作者儿子的照片，还是很可爱的。（我是图片）
![son](https://cdn-images-1.medium.com/max/1600/1*RBTfDZzW0N5TzHg_pqWmSg.png)


出了标签和 JavaScript 混写以外，我也知道 JSX 也不是一个彻底的方案。实际上，它就是硬币的另一面，事物发展到某种程度总会出现的东西一样。想知道为什么，搬好椅子，我要开始讲（zhuang）课（bi）了。



## 第一阶段：无存在感的 JavaScript（[Unobtrusive JavaScript](https://en.wikipedia.org/wiki/Unobtrusive_JavaScript)）



还记得过去 jQuery 的大好时光吗？到处都是选择器和 DOM 操作。这时，标签是单纯的标签，脚本是单纯的脚本。嗯，这感觉还不错。



我们像这样写标签：

```html
<a class="hide">click to hide me</a>
```

像这样写脚本：

```javascript
$('.hide').click(function() {$(this).hide();})
```



这样就可以下班了？并没有。



似乎是个不错的方案。我们的标签很纯粹！问题随之而来，我怎么在脚本里找关于这个标签的所有逻辑呢？答：通读脚本，一行不漏。在某些极端条件下，你都不能随便动 DOM tree 的结构，可能导致某些选择器失效，除非你通读代码。看到没，分离没有想象中的简单。脚本和标签的确是在各自的文件里，而实际上它们已经紧紧相拥在一起。新的维护人员必须看懂以前的人写的所有代码，否则容易炸。



严格遵守分离原则，带来的只有痛苦的维护和 debug 体验。每次你想改内容，都得担心会不会又有哪个选择器失效了。或许从一开始就走错了方向，如果我们放下对分离原则的偏执，就能更愉快地开发？



## 第二阶段：双向绑定



当前端们在 Knockout 和 Angular 里第一次见到双向绑定，好比约伯受尽千辛万苦见到耶稣。我们之中很多人毫不犹豫立刻抛弃了对分离原则宗教般的信仰，投奔声明式绑定的怀抱（直接在标签里声明）。数据层变，UI 也跟着变。UI 变，数据层也跟着变。很干净，很明了。



每个库或框架都有它自己用来实现双向绑定的方式，但本质上做的。都是同一件事情。先看看下面这几个来自比较流行的框架里的遍历数组的例子：

```javascript
// Angular

<div ng-repeat="user in users">

// Ember

{{#each user in users}}

// Knockout

data-bind="foreach: users
```



这里发生了一些有趣的事。很少人意识到这个根本问题：我们正努力地把脚本嵌进标签里，而不是分离。这几个例子实现的都是同一件事情：通过添加额外的属性来增强原生标签，由脚本来解析实现。现在，我们能愉快地把脚本和标签以这种方式写在一起了，是时候介绍 React 硬币的反面了。



## 第三阶段：JSX

React 的 JSX 转变得不够彻底，它也不过是以下想法所产生的成果之一：我们已经达成了一个行业共识，标签和脚本本应该放在一起。诚然，我们的宣传不够广泛。但只要你用过 Angular，Knockout，Ember 就能了解这个新方向了。像我上面所演示的，数据绑定式的标签写法就是不断地把脚本写到标签里。既然已经选择脚本标签混写，为什么还要增加像 HTML 这种不严谨、松散、软弱无力的技术呢？从一开始，浏览器对 HTML 的解析就很宽容，也不严谨。那么 HTML 还有实现声明数据绑定，变量遍历，逻辑判断的基础吗？



Facebook 认识到这一点，JavaScript 更有逻辑，也是一项不错的技术来解决这两者混写时遇到的问题。这时候，顿悟显现出来了：



Angular，Ember 和 Knockout 把 JavaScript 放到 HTML 里，React 把 HTML 放到 JavaScript 里



这一举措带来的益处是多方面的，直到你用上了 React 和 JSX 之后才能深刻体会到。React 的 JSX 完胜阶段二里提到的所有技术，因为以下理由：



编译时报错



当你在 HTML 里打错字，你根本不知道哪里是有问题的。很多情况下，就是个运行时错误。例如：用 Angular 的时候，你把 ng-repeat 写成 n-repeat，什么都没有发生；用 Knockout 时，把 data-bind 写成 data-bnd 也一样。它们能跑起来，但没有报错。有时候挺让人沮丧的。



相反，如果你在 JSX 里拼错一个字，它就编译不了。忘记关闭 li 标签？你难道不像在写 HTML 的时候获得更丰富的反馈吗？



JSX 让这种必要的反馈信息成为了现实！这个举措的重要性怎么强调也不过分。快速的反馈大幅提升生产力。像我在 [Clean Code](https://www.pluralsight.com/courses/writing-clean-code-humans) 课上讲到的：越好的解决方案，越快报错。



解放 JavaScript 的所有潜能



把标签和脚本组合在一起，意味着你能够享受 JavaScript 带来的所有便利来写更严谨的标签，不像以 HTML 为中心的框架，类似Angular（应该指 1.0 版本）和 Knockout 那样只提供部分功能。



客户端框架不应该需要学习额外的语法来作循环声明以及条件判断。（虽然都是类似的）



React 避免了这一点。阶段二提到的技术，各有各的语法。与此相反，JSX 看起来跟 HTML 挺像的，除了它用的是原生的 JavaScript 写法（刚开始看起来，确实有点不适应）。在一个以 JavaScript 为核心的生态圈里，不用学习全新语法确实不错。



对这种写法，很多 IDE 已经有智能提示。想想以 HTML 为主的很多框架还不能做到这一点



## 最后



JSX 的产生并不是无中生有，它是自然演进的过程，所以不要逃避。



JSX 并不是革命，它是进化。



像很多进化形式，它也很重要。



想了解更多？请看 [Building Applications with React and Flux](http://www.pluralsight.com/author/cory-house)​​​​
