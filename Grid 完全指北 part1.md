[toc]
## Grid 完全指北 part1
> 建议：grid 里面有相当大一部分功能与 flexbox 类似，先看 flexbox 再看 grid，效果更佳

*原文：https://css-tricks.com/snippets/css/complete-guide-grid/*

### 介绍

CSS grid 可以说是 CSS 里「最强大的布局方案」。flexbox 只能满足一个维度（行或列）里的布局要求，而 grid 能同时满足。与 flexbox 类似，在 container 和 item 上设置相关属性就可以应用 grid 布局。

原文引用 [Chris House's guide](http://chris.house/blog/a-complete-guide-css-grid-layout/)（持续更新中~）

CSS grid 是一套「基于二维网格」的布局系统，完全改变了「基于网格的用户界面」的布局方式。

CSS grid 之前，网页布局主要用 `table` `float` `position` `inline-block` 来实现，但从本质上说，它们都是 hacks（个人理解为：凡与人天生的布局直觉违背），还遗漏了不少「重要的布局痛点」（比如：垂直居中）。

flexbox 部分缓解了这种现状，但它只针对「一维」情况（只有行或者列），而不是「二维」

CSS grid 是第一个针对「二维布局」的 CSS 模块

主要有两个原因，促使我写这份指南。

第一，Rachel Andrew 的 [Get Ready for CSS Grid Layout](http://abookapart.com/products/get-ready-for-css-grid-layout)，全面透彻地介绍了 CSS grid，它是本文的基础，推荐你买来看看。

第二，Chris Coyier 的 [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) 曾经是我学 flexbox 时用到的资料。

它帮过很多人，只要 google flexbox 就能轻松找到它。你会注意到，本文跟它有很多相似地方，（如果你也想要写一份 CSS grid 的指南）why not steal from the best?

本文只介绍「最新规范」里提到的 CSS grid 相关概念，不包括过时的 IE 语法，并且我会尽量定期更新，与最新规范保持一致

## 基础概念 & 浏览器支持状况

总的来说，container `display: grid` 表示应用 grid 布局，`grid-template-columns` 和 `grid-template-rows` 设置行列的宽度； items 设置 `grid-column` 和 `grid-row` 来指定 grid 中的位置。

跟 flexbox 里的 item 设置了 `order` 一样，如果 grid 里的 item 设置了 `grid-column & grid-column`，原来的顺序不影响实际的排列顺序。

也就是仅仅通过 CSS，就能随意变更 items 的排列顺序，跟 media queries 配合使用，效果拔群。

也就是说你只要定义好页面的最初布局，仅需要几行 CSS 代码，就能重新排列 items 的顺序，以适应不同宽度的设备。

grid 就是这么强大的 CSS module

到 2017 三月为止，很多浏览器已经（不带前缀）原生支持 CSS grid 了：Crhome(android Chrome), Firefox, Safari(IOS Safari), Opera.

IE 10/11 支持 CSS grid，但语法已过时，Edge 将会兼容最新 CSS grid 语法。

[戳我看 Caniuse 数据](https://caniuse.com/#feat=css-grid)

除微软以外的大多数浏览器厂商，在 CSS grid 规范成熟之前，都已尽量抑制自己在 CSS grid 具体实现（指具体语法）上++为所欲为的欲望++。

这是一件好事，再也不用学多套语法了。

那么从现在开始「入门到上线」吧！（part2 待填......）
