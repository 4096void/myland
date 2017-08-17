[toc]
## 用递归的方式写动画
> <b>Note</b>: Your callback routine must itself call requestAnimationFrame() if you want to animate another frame at the next repaint.

可以预见有很多渐变操作，实质就是~~某函数的递归调用~~不断计算每一 frame 的样式：每 frame 要 repaint 的样式都由~~递归~~函数计算出来，同时 requestAnimationFrame 返回的 request id 能传进 cancelAnimationFrame 来取消动画  
### DEMO
元素宽度从 0% 到 100%，用时 3 秒（变化不够顺滑）  
```javascript
function largen(elm) {
  var begin = null;
  var action = function(t) {
    if (!begin) begin = t;
    var p = (t - begin) / 3000 * 100;
    if (p <= 100) {
      elm.style.width = p + '%';
      window.requestAnimationFrame(action);
    }
  };
  window.requestAnimationFrame(action);
}
largen(document.querySelector('#target'));
```

让元素在 500px 见方的区域内不断闪现  
```javascript
function flash(elm) {
  var action = function() {
    elm.style.position = 'absolute';
    var l = (Math.random() * 500) + 'px';
    var t = (Math.random() * 500) + 'px';
    elm.style.left = l;
    elm.style.top = t;
    if (!(240 <= l && l <= 260 && 240 <= t && t <= 260)) {
      window.requestAnimationFrame(action);
    }
  };
  window.requestAnimationFrame(action);
}
flash(document.querySelector('#target'));
```

### refs
- https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame
