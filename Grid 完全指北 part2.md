Grid 完全指北 part2

建议：grid 里面有相当大一部分功能与 flexbox 类似，先看 flexbox 再看 grid，效果更佳
原文：https://css-tricks.com/snippets/css/complete-guide-grid/

## 适用于容器
### display
把容器定义为 grid container 并为它的元素提供 grid formatting context

值：
* grid - 块级 grid
* inline-grid - 行内 grid
* subgrid - 被定义的 grid 被嵌套在另外一个 grid 时，可设置此值，同时声明占另外一个 grid 多少行/列的空间

```CSS
.container {
    display: grid | inline-grid | subgrid;
}
```
注意：对于 grid container `column` `float` `clear` `verticle-align` 无效

### grid-template-columns & grid-template-rows
定义 grid container 的 rows & columns，值由 grid line 分隔开。数值表示 track 的宽度，数值之间的其他部分表示 grid line。

值：
* `<track-size>` - 任意长度单位，百分比 或 `fr`
* `<line-name>` - 任意名称

```CSS
.container {
    grid-template-columns: <track-size> ... | <line-name> <track-size> ...;
    grid-template-rows: <track-size> ... | <line-name> <track-size> ...;
}
```

例子：
```CSS
.container {
    grid-template-columns: 40px 50px auto 50px 40px;
    grid-template-rows: 25% 100px auto;
}
```
![上面的例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-numbers.png)

同时你也可以明确指定 grid line 的名称，像下面的例子那样写在中括号里：
```CSS
.container {
    grid-template-columns: [first] 40px [line2] 50px [line3] auto [col4-start] 50px [five] 40px [end];
    grid-template-rows: [row1-start] 25% [row1-end] 100px [third-line] auto [last-line];
}
```
![上面的例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-names.png)

注意，grid line 能有多个名称，下面例子的第二条 grid line 有两个名称：`row1-end` 和 `row2-start`：
```CSS
.container {
    grid-template-rows: [row1-start] 25% [row1-end row2-start] 25% [row2-end];
}
```

通过 `repeat()` 可以精简重复部分：
```CSS
.container {
    grid-template-columns: repeat(3, 20px [col-start]) 5%;
}
```

等价于：
```CSS
.container {
    grid-template-columns: 20px [col-start] 20px [col-start] 20px [col-start] 5%;
}
```

`fr` 可用于代表 grid container 里剩余空间的份额，以下例子表示每一列各占 1/3：
```CSS
.container {
    grid-template-columns: 1fr 1fr 1fr;
}
```

`fr` 仅仅对 grid container 「剩余空间」进行换算，以下例子换算部分不包括 `50px`：
```CSS
.container {
    grid-template-columns: 1fr 50px 1fr 1fr;
}
```


### grid-template-areas
通过引用定义好的 grid area 来定义 grid template，连续的 grid area 视为同一区域，`.` 则表示 empty cell，语法本身已经很直觉地把 grid template 表示出来。

值：
* `<grid-area-name>` - 相关 grid area 已经定义好的名称
* `.` - empty cell
* none - 未定义区域

```CSS
.container {
    grid-template-areas:
        "<grid-area-name> | . | none | ..."
        "...";
}
```

例子：
```CSS
.item-a {
    grid-area: header;
}
.item-b {
    grid-area: main;
}
.item-c {
    grid-area: sidebar;
}
.item-d {
    grid-area: footer;
}

.container {
    grid-template-columns: 50px 50px 50px 50px;
    grid-template-rows: auto;
    grid-template-areas:
        "header header header header"
        "main main . sidebar"
        "footer footer footer footer";
}
```

上面的例子会生成一个 4 × 3 的 grid，第一行为 header，第二行包括 main sidebar，最后一行为 footer
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-template-areas.png)

定义里每一行的项目个数必须与列数一致。

任意数量连续的实心句号跟一个句号都表示一个 empty cell

grid-template-areas 不能指定 grid line 的名称，同时 grid area 四端的 grid line 将被自动命名为 area-name-start(row & column) & area-name-end(row & column)，同一条 grid line 将拥有不止一个名称：上面例子中最左边的 gird line 的名称为 header-start, main-start, footer-start。


### grid-template
`<grid-template-rows>` `<grid-template-columns>` `<grid-template-areas>` 的复合简写。

值：
* none 都设置为初始值
* subgrid 把 `grid-template-rows` 和 `grid-template-columns` 设置给 subgrid，grid-template-areas 设置为初始值
* `<grid-template-rows>` / `<grid-template-columns>` 设置对应的 rows & columns 并将 `grid-template-areas` 设置为 none

```CSS
.container {
    grid-template: none | subgrid | <grid-template-rows> / <grid-template-columns>;
}
```

同时设置 rows columns areas 的精简写法：
```CSS
.container {
    grid-template:
        [row1-start] "header header header" 25px [row1-end]
        [row2-start] "footer footer footer" 25px [row2-end]
        / auto 50px auto;
}
```

等价于：
```CSS
.container {
    grid-template-rows: [row1-start] 25px [row1-end row2-start] 25px [row2-end];
    grid-template-columns: auto 50px auto;
    grid-template-areas:
        "header header header"
        "footer footer footer";
}
```

注意：`grid-template` 并不会重置 `grid-auto-columns` `grid-auto-rows` `grid-auto-flow`，在多数情况下你都会用到，所以推荐使用 `grid`，而不是 `grid-template`

### grid-column-gap & grid-row-gap
定义 grid line 的宽度，也即是 rows/columns 之间部分的宽度

值：
* `<line-size>` 任意长度单位

```CSS
.container {
    grid-column-gap: <line-size>;
    grid-row-gap: <line-size>;
}
```

例子：
```CSS
.container {
    grid-template-columns: 100px 50px 100px;
    grid-template-rows: 80px auto 80px; 
    grid-column-gap: 10px;
    grid-row-gap: 15px;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-column-row-gap.png)
注意：grid line 只出现在 rows/columns 之间，不包括两端


### grid-gap
`<grid-row-gap>` `<grid-column-gap>` 的精简写法

值：
* `<grid-row-gap>` `<grid-column-gap>` - 任意长度单位

例子：
```CSS
.container {
    grid-template-columns: 100px 50px 100px;
    grid-template-rows: 80px auto 80px; 
    grid-gap: 10px 15px;
}
```
注意：如果 `grid-column-gap` 没有设置，将被默认设置为 `grid-row-gap` 的值

### justify-items
元素内填充内容的对齐方式，justify-items 对应水平轴的对齐方式，align-items 则为垂直轴

值：
* start - 左对齐
* end - 右对齐
* center - 居中
* stretch - 拉伸（默认值）

```CSS
.container {
    justify-items: start | end | center | stretch;
}
```

例子：
```CSS
.container {
    justify-items: start;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-items-start.png)

```CSS
.container{
    justify-items: end;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-items-end.png)

```CSS
.container {
    justify-items: center;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-items-center.png)

```CSS
.container {
    justify-items: stretch;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-items-stretch.png)
注意：单个元素填充内容的水平对齐方式可通过 `justify-self` 设置


### align-items
元素内填充内容的对齐方式，justify-items 对应水平轴的对齐方式，align-items 则为垂直轴

值：
* start - 顶部对齐
* end - 底部对齐
* center - 垂直居中
* stretch - 填充（默认值）

```CSS
.container {
    align-items: start | end | center | stretch;
}
```

例子：

```CSS
.container {
  align-items: start;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-items-start.png)

```CSS
.container {
  align-items: end;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-items-end.png)

```CSS
.container {
  align-items: center;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-items-center.png)

```CSS
.container {
  align-items: stretch;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-items-stretch.png)
注意：单个元素填充内容的垂直对齐方式可通过 `justify-self` 设置


### justify-content
当 grid 内元素的总宽度少于 grid 的宽度时（所有元素的宽度都为非 `fr` 单位），在这种情况下，你可以设置 grid 整体的对齐方式 justify-content 设置水平轴，align-content 设置垂直轴

值：
* start - 左对齐
* end - 右对齐
* center - 水平居中
* stretch - 拉伸
* space-around - 元素之间间隔相等，两端为一半
* space-between - 元素之间间隔先等，两端为 0
* space-evenly - 元素之间以及两端都相等

```CSS
.container {
    justify-content: start | end | center | stretch | space-around | space-between | space-evenly;
}
```

例子：

```CSS
.container {
    justify-content: start;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-content-start.png)

```CSS
.container {
    justify-content: end;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-content-end.png)

```CSS
.container {
    justify-content: center;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-content-center.png)

```CSS
.container {
    justify-content: stretch;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-content-stretch.png)

```CSS
.container {
    justify-content: space-around;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-content-space-around.png)

```CSS
.container {
    justify-content: space-between;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-content-space-between.png)

```CSS
.container {
    justify-content: space-evenly;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-content-space-evenly.png)


### align-content
当 grid 内元素的总高度少于 grid 的高度时（所有元素的高度都为非 `fr` 单位），在这种情况下，你可以设置 grid 整体的对齐方式 justify-content 设置水平轴，align-content 设置垂直轴

值：
* start - 顶部对齐
* end - 底部对齐
* center - 垂直居中
* stretch - 拉伸
* space-around - 元素之间间隔相等，两端为一半
* space-between - 元素之间间隔先等，两端为 0
* space-evenly - 元素之间以及两端都相等

```CSS
.container {
    align-content: start | end | center | stretch | space-around | space-between | space-evenly;
}
```

例子：

```CSS
.container {
    align-content: start;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-content-start.png)

```CSS
.container {
    align-content: end;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-content-end.png)

```CSS
.container {
    align-content: center;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-content-center.png)

```CSS
.container {
    align-content: stretch;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-content-stretch.png)

```CSS
.container {
    align-content: space-around;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-content-space-around.png)

```CSS
.container {
    align-content: space-between;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-content-space-between.png)

```CSS
.container {
    align-content: space-evenly;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-content-space-evenly.png)

### grid-auto-columns & grid-auto-rows
当元素的 grid-row/grid-column 超出 grid 定义的范围，可通过该属性指定自动生成的 grid track 的宽高

值：
* `<track-size>` 任意长度单位

```CSS
.container {
    grid-auto-columns: <track-size> ...;
    grid-auto-rows: <track-size> ...;
}
```

想象有以下的 2 × 2 grid
```CSS
.container {
    grid-template-columns: 60px 60px;
    grid-template-rows: 90px 90px
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-auto.png)

现在你又把元素的 grid-comun/grid-row 设置为：
```CSS
.item-a {
    grid-column: 1 / 2;
    grid-row: 2 / 3;
}
.item-b {
    grid-column: 5 / 6;
    grid-row: 2 / 3;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/implicit-tracks.png)
`item-b` 定义在第五列和第六列之间，但我们的 grid 没有这两列，默认情况下会生成 0 宽度的第五列和第六列，也可以通过 grid-auto-columns/grid-auto-rows 来指定它们的宽/高

```CSS
.container {
    grid-auto-columns: 60px;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/implicit-tracks-with-widths.png)

### grid-auto-flow
没有定义 grid-column/grid-row 的元素的自动排列方式

值：
* row - 从左向右，一行一行下来
* column - 从上到下，一行一行往右
* dense - 元素宽/高度从小到大排列
注意：dense 可能会导致元素出现顺序不一致


```CSS
.container {
    grid-auto-flow: row | column | row dense | column dense
}
```

例子：
```HTML
<section class="container">
    <div class="item-a">item-a</div>
    <div class="item-b">item-b</div>
    <div class="item-c">item-c</div>
    <div class="item-d">item-d</div>
    <div class="item-e">item-e</div>
</section>
```

你的 grid 被定义为五列两行：
```CSS
.container {
    display: grid;
    grid-template-columns: 60px 60px 60px 60px 60px;
    grid-template-rows: 30px 30px;
    grid-auto-flow: row;
}
```

有两个元素明确定位：
```CSS
.item-a {
    grid-column: 1;
    grid-row: 1 / 3;
}
.item-e {
    grid-column: 5;
    grid-row: 1 / 3;
}
```

设置为 row 时：
```CSS
.container {
    display: grid;
    grid-template-columns: 60px 60px 60px 60px 60px;
    grid-template-rows: 30px 30px;
    grid-auto-flow: row;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-auto-flow-row.png)

设置为 column 时：
```CSS
.container {
    display: grid;
    grid-template-columns: 60px 60px 60px 60px 60px;
    grid-template-rows: 30px 30px;
    grid-auto-flow: column;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-auto-flow-column.png)


### grid
`grid-template-rows` `grid-template-columns` `grid-template-areas` `grid-auto-rows` `grid-auto-columns` 的精简写法，并且能重置 `grid-column-gap` `grid-row-gap`

值：
* none 初始化所有值
* `grid-template-rows`/`grid-template-columns` 设置/重置对应值
* `grid-auto-flow`[`grid-auto-rows`|[`grid-auto-columns`]] 如果 `grid-auto-columns` 忽略，它的默认与 `grid-auto-rows` 相等，如果都忽略，则为初始值

```CSS
.container {
    grid: none | <grid-template-rows> / <grid-template-columns> | <grid-auto-flow> [<grid-auto-rows> [/ <grid-auto-columns>]];
}
```

例子：
下面两种写法等价：

```CSS
.container {
    grid: 200px auto / 1fr auto 1fr;
}
```

```CSS
.container {
    grid-template-rows: 200px auto;
    grid-template-columns: 1fr auto 1fr;
    grid-template-areas: none;
}
```

以下两种写法等价：
```CSS
.container {
    grid: column 1fr / auto;
}
```

```CSS
.container {
    grid-auto-flow: column;
    grid-auto-rows: 1fr;
    grid-auto-columns: auto;
}
```

更完整同时也难写的例子：

```CSS
.container {
    grid: [row1-start] "header header header" 1fr [row1-end]
          [row2-start] "footer footer footer" 25px [row2-end]
          / auto 50px auto;
}
```

等价于：

```CSS
.container {
    grid-template-areas:
        "header header header"
        "footer footer footer";
    grid-template-rows: [row1-start] 1fr [row1-end row2-start] 25px [row2-end];
    grid-template-columns: auto 50px auto;
}
```

## 适用于元素
### grid-column-start & grid-column-end & grid-row-start & grid-row-end
指定元素处于 grid 中具体的那一片区域，通过指定四条边来说明：grid-column-start/grid-column-end grid-row-start/grid-row-end

值：
* line - 数字 or grid line 名称
* span <number> - 将跨多少条 grid track
* span <name> - 覆盖直至 <name> grid line
* auto 自动排列

```CSS
.item {
    grid-column-start: <number> | <name> | span <number> | span <name> | auto
    grid-column-end: <number> | <name> | span <number> | span <name> | auto
    grid-row-start: <number> | <name> | span <number> | span <name> | auto
    grid-row-end: <number> | <name> | span <number> | span <name> | auto
}
```

例子：
```CSS
.item-a {
    grid-column-start: 2;
    grid-column-end: five;
    grid-row-start: row1-start
    grid-row-end: 3
}
```

![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-start-end-a.png)


```CSS
.item-b {
    grid-column-start: 1;
    grid-column-end: span col4-start;
    grid-row-start: 2
    grid-row-end: span 2
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/11/grid-start-end-b.png)
注意：如果 `grid-column-end`/`grid-row-end` 没有声明，默认 span 1；z-index 对 item 适用

### grid-column & grid-row
`grid-column-start`/`grid-column-end` `grid-row-start`/`grid-row-end` 的精简写法

值：
* `<start-line>/<end-line>` 同上

```CSS
.item {
    grid-column: <start-line> / <end-line> | <start-line> / span <value>;
    grid-row: <start-line> / <end-line> | <start-line> / span <value>;
}
```

例子：
```CSS
.item-c {
    grid-column: 3 / span 2;
    grid-row: third-line / 4;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-start-end-c.png)
注意：默认 span 1

### grid-area
给元素一个名称，可在 grid container 设置 `grid-template-area` 时引用，同时也可以同时设置：`grid-row-start` `grid-row-end` `grid-column-start` `grid-column-end`

值：
* `<name>` - 任意名称
* `<row-start>`/`<column-end>`/`<row-end>`/`<column-end>` 数字或 grid line 名称

```CSS
.item {
    grid-area: <name> | <row-start> / <column-start> / <row-end> / <column-end>;
}
```

例子：

给元素设置名称
```CSS
.item-d {
    grid-area: header;
}
```

简写例子：
```CSS
.item-d {
    grid-area: 1 / col4-start / last-line / 6
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-start-end-d.png)  

### justify-self
元素内容的水平排列方式

值：
* start - 左对齐
* end - 右对齐
* center - 居中
* stretch - 拉伸（默认值）

```CSS
.item {
    justify-self: start | end | center | stretch;
}
```

例子：

```CSS
.item-a {
    justify-self: start;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-self-start.png)

```CSS
.item-a {
    justify-self: end;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-self-end.png)

```CSS
.item-a {
    justify-self: center;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-self-center.png)

```CSS
.item-a {
    justify-self: stretch;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-justify-self-stretch.png)


### align-self

元素内容的垂直排列方式

值：
* start - 顶部对齐
* end - 底部对齐
* center - 垂直居中
* stretch - 拉伸（默认值）

```CSS
.item {
    justify-self: start | end | center | stretch;
}
```

例子：

```CSS
.item-a {
    align-self: start;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-self-start.png)

```CSS
.item-a {
    align-self: end;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-self-end.png)

```CSS
.item-a {
    align-self: center;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-self-center.png)

```CSS
.item-a {
    align-self: stretch;
}
```
![上面例子](https://cdn.css-tricks.com/wp-content/uploads/2016/03/grid-align-self-stretch.png)
