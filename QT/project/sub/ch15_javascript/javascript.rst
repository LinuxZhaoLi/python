==========
JavaScript
==========


    The source code for this chapter can be found in the `assets folder <../assets>`_.
    本章的源代码可以在

JavaScript is the lingua-franca on web client development. It also starts to get traction on web server development mainly by node js. As such it is a well-suited addition as an imperative language onto the side of declarative QML language. QML itself as a declarative language is used to express the user interface hierarchy but is limited to express operational code. Sometimes you need a way to express operations, here JavaScript comes into play.
JavaScript是web客户端开发中的通用语言。它还开始吸引主要通过node js进行的web服务器开发。因此，它是作为命令式语言添加到声明性QML语言的一种非常适合的添加。QML本身作为声明性语言用于表示用户界面层次结构，但仅限于表示操作代码。有时您需要一种表示操作的方法，这里需要使用JavaScript。
.. note::

  There is an open question in the Qt community about the right mixture about QML/JS/QtC++ in a modern Qt application. The commonly agreed recommended mixture is to limit the JS part of your application to a minimum and do your business logic inside QtC++ and the UI logic inside QML/JS.

  This book pushes the boundaries, which is not always the right mix for a product development and not for everyone. It is important to follow your team skills and your personal taste. In doubt follow the recommendation.
  在现代Qt应用程序中，QML/JS/QtC+的正确组合是Qt社区中的一个公开问题。通常推荐的混合方法是将应用程序的JS部分限制到最小，在QtC++中执行业务逻辑，在QML/JS中执行UI逻辑。
这本书突破了界限，它并不总是适合产品开发，也不适合所有人。遵循你的团队技能和个人品味是很重要的。如有疑问，请遵照建议。

Here a short example of how JS used in QML looks like::

  Button {
    width: 200
    height: 300
    property bool checked: false
    text: "Click to toggle"

    // JS function
    function doToggle() {
      checked = !checked
    }

    onTriggered: {
      // this is also JavaScript
      doToggle();
      console.log('checked: ' + checked)
    }
  }

所以JavaScript可以作为一个独立的JS函数出现在QML的很多地方，作为一个JS模块，它可以出现在属性绑定的每个右侧。
::

  import "util.js" as Util // import a pure JS module

  Button {
    width: 200
    height: width*2 // JS on the right side of property binding

    // standalone function (not really useful)
    function log(msg) {
      console.log("Button> " + msg);
    }

    onTriggered: {
      // this is JavaScript
      log();
      Qt.quit();
    }
  }

在QML中声明用户界面，使用JavaScript使其具有功能。那么你应该写多少JavaScript呢?这取决于你的风格以及你对JS开发的熟悉程度。JS是一种松散类型的语言，这使得它很难发现类型缺陷。此外，函数期望所有的参数变化，这可能是一个非常讨厌的缺陷。发现缺陷的方法是严格的单元测试或验收测试。因此，如果您在JS中开发真正的逻辑(而不是一些粘合的代码行)，您应该真正开始使用测试优先的方法。在通常的混合团队(Qt/ c++和QML/JS)中，当他们将前端作为领域逻辑的JS数量最小化，而在后端用Qt c++来完成繁重的工作时，他们是非常成功的。然后后端应该经过严格的单元测试，以便前端开发人员能够信任代码并专注于所有这些小的用户界面需求。
.. note::

一般来说:后端开发人员是功能驱动的，前端开发人员是用户故事驱动的。

Browser/HTML vs QtQuick/QML
===========================

JavaScript比HTML多得多。浏览器内的Javascript是一个标准的ECMAScript环境，带有一些额外的浏览器api。浏览器内典型的JS环境中有一个全局对象命名为“窗口”用于与浏览器窗口(标题、URL位置,DOM树等)浏览器提供函数来访问DOM节点的id、类等。(这是使用jQuery提供CSS选择器),最近也通过CSS选择器(“querySelector ' ', ' ' querySelectorAll ' ')。此外，还可以在一定时间后调用函数(' ' setTimeout ' ')并重复调用它(' ' setInterval ' ')。除了这些(和其他浏览器api)之外，该环境类似于QML/JS。
另一个区别是JS如何出现在HTML和QML中。在HTML中，你只能在初始页面加载或事件处理程序(例如页面加载，鼠标按下)中执行JS。例如，你的JS通常在页面加载时初始化，这相当于' '组件。在QML oncomplete ' '。默认情况下，不能在浏览器中使用JS进行属性绑定(AngularJS增强了DOM树以允许进行属性绑定，但这与标准的HTML相去甚远)。
在QML中，JS更像是一流的公民，并且更深入地集成到QML渲染树中。这使得语法更具可读性。除了这些不同之外，开发过HTML/JS应用程序的人使用QML/JS会觉得很自在。

The Language
============

This chapter will not give you a general introduction to JavaScript. There are other books out there for a general introduction to JavaScript, please visit this great side on `Mozilla Developer Network <https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript>`_.

On the surface JavaScript is a very common language and does not differ a lot from other languages::

  function countDown() {
    for(var i=0; i<10; i++) {
      console.log('index: ' + i)
    }
  }

  function countDown2() {
    var i=10;
    while( i>0 ) {
      i--;
    }
  }

But be warned JS has function scope and not block scope as in C++ (see `Functions and function scope <https://developer.mozilla.org/it/docs/Web/JavaScript/Reference/Functions_and_function_scope>`_).

The statements ``if ... else``, ``break``, ``continue`` also work as expected. The switch case can also compare other types and not just integer values::

  function getAge(name) {
    // switch over a string
    switch(name) {
    case "father":
      return 58;
    case "mother":
      return 56;
    }
    return unknown;
  }

JS knows several values which can be false, e.g. ``false``, ``0``, ``""``, ``undefined``, ``null``). For example, a function returns by default ``undefined``. To test for false use the ``===`` identity operator. The ``==`` equality operator will do type conversion to test for equality. If possible use the faster and better ``===`` strict equality operator which will test for identity (see `Comparison operators <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators>`_.

Under the hood, javascript has its own ways of doing things. For example arrays::

  function doIt() {
    var a = [] // empty arrays
    a.push(10) // addend number on arrays
    a.push("Monkey") // append string on arrays
    console.log(a.length) // prints 2
    a[0] // returns 10
    a[1] // returns Monkey
    a[2] // returns undefined
    a[99] = "String" // a valid assignment
    console.log(a.length) // prints 100
    a[98] // contains the value undefined
  }

Also for people coming from C++ or Java which are used to an OO language JS just works differently. JS is not purely an OO language it is a so-called prototype based language. Each object has a prototype object. An object is created based on his prototype object. Please read more about this in the book `Javascript the Good Parts by Douglas Crockford <http://javascript.crockford.com>`_ or watch the video below.

.. youtube:: hQVTIJBZook


To test some small JS snippets you can use the online `JS Console <http://jsconsole.com>`_ or just build a little piece of QML code::


  import QtQuick 2.5

  Item {
    function runJS() {
      console.log("Your JS code goes here");
    }
    Component.onCompleted: {
      runJS();
    }
  }


JS Objects
==========

While working with JS there are some objects and methods which are more frequently used. This is a small collection of them.

* ``Math.floor(v)``, ``Math.ceil(v)``, ``Math.round(v)`` - largest, smallest, rounded integer from float
* ``Math.random()`` - create a random number between 0 and 1
* ``Object.keys(o)`` - get keys from object (including QObject)
* ``JSON.parse(s)``, ``JSON.stringify(o)`` - conversion between JS object and JSON string
* ``Number.toFixed(p)`` - fixed precision float
* ``Date`` - Date manipulation

You can find them also at: `JavaScript reference <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference>`_

Here some small and limited examples of how to use JS with QML. They should give you an idea how you can use JS inside QML

.. rubric:: Print all keys from QML Item

::

  Item {
    id: root
    Component.onCompleted: {
      var keys = Object.keys(root);
      for(var i=0; i<keys.length; i++) {
        var key = keys[i];
        // prints all properties, signals, functions from object
        console.log(key + ' : ' + root[key]);
      }
    }
  }


.. rubric:: Parse an object to a JSON string and back

::

  Item {
    property var obj: {
      key: 'value'
    }

    Component.onCompleted: {
      var data = JSON.stringify(obj);
      console.log(data);
      var obj = JSON.parse(data);
      console.log(obj.key); // > 'value'
    }
  }

.. rubric:: Current Date

::

  Item {
    Timer {
      id: timeUpdater
      interval: 100
      running: true
      repeat: true
      onTriggered: {
        var d = new Date();
        console.log(d.getSeconds());
      }
    }
  }


.. rubric:: Call a function by name

::

  Item {
    id: root

    function doIt() {
      console.log("doIt()")
    }

    Component.onCompleted: {
      // Call using function execution
      root["doIt"]();
      var fn = root["doIt"];
      // Call using JS call method (could pass in a custom this object and arguments)
      fn.call()
    }
  }


Creating a JS Console
=====================

As a little example, we will create a JS console. We need an input field where the user can enter his JS expressions and ideally there should be a list of output results. As this should more look like a desktop application we use the QtQuick Controls module.


.. note::

  A JS console inside your next project can be really beneficial for testing. Enhanced with a Quake-Terminal effect it is also good to impress customers. To use it wisely you need to control the scope the JS console evaluates in, e.g. the currently visible screen, the main data model, a singleton core object or all together.


.. figure:: assets/jsconsole.png


We use Qt Creator to create a Qt Quick UI project using QtQuick controls. We call the project `JSConsole`. After the wizard has finished we have already a basic structure for the application with an application window and a menu to exit the application.

For the input, we use a TextField and a Button to send the input for evaluation. The result of the expression evaluation is displayed using a ListView with a ListModel as the model and two labels to display the expression and the evaluated result.

::

  // part of JSConsole.qml
  ApplicationWindow {
    id: root

    ...

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 9
        RowLayout {
            Layout.fillWidth: true
            TextField {
                id: input
                Layout.fillWidth: true
                focus: true
                onAccepted: {
                    // call our evaluation function on root
                    root.jsCall(input.text)
                }
            }
            Button {
                text: qsTr("Send")
                onClicked: {
                    // call our evaluation function on root
                    root.jsCall(input.text)
                }
            }
        }
        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Rectangle {
                anchors.fill: parent
                color: '#333'
                border.color: Qt.darker(color)
                opacity: 0.2
                radius: 2
            }

            ScrollView {
                id: scrollView
                anchors.fill: parent
                anchors.margins: 9
                ListView {
                    id: resultView
                    model: ListModel {
                        id: outputModel
                    }
                    delegate: ColumnLayout {
                        width: ListView.view.width
                        Label {
                            Layout.fillWidth: true
                            color: 'green'
                            text: "> " + model.expression
                        }
                        Label {
                            Layout.fillWidth: true
                            color: 'blue'
                            text: "" + model.result
                        }
                        Rectangle {
                            height: 1
                            Layout.fillWidth: true
                            color: '#333'
                            opacity: 0.2
                        }
                    }
                }
            }
        }
    }
  }


The evaluation function ``jsCall`` does the evaluation not by itself this has been moved to a JS module (``jsconsole.js``) for clearer separation.

::

  // part of JSConsole.qml

  import "jsconsole.js" as Util

  ...

  ApplicationWindow {
    id: root

    ...

    function jsCall(exp) {
        var data = Util.call(exp);
        // insert the result at the beginning of the list
        outputModel.insert(0, data)
    }
  }

为了安全起见，我们不使用JS中的' ' ' eval ' '函数，因为这会允许用户修改本地作用域。我们使用函数构造函数在运行时创建一个JS函数，并将我们的作用域作为这个变量传递进来。由于每次创建函数时，它不充当闭包并存储自己的作用域，因此我们需要使用' ' this。a = 10 ' '将值存储在函数的这个范围内。这个范围由脚本设置为scope变量。
::

  // jsconsole.js
  .pragma library

  var scope = {
    // our custom scope injected into our function evaluation
  }

  function call(msg) {
      var exp = msg.toString();
      console.log(exp)
      var data = {
          expression : msg
      }
      try {
          var fun = new Function('return (' + exp + ');');
          data.result = JSON.stringify(fun.call(scope), null, 2)
          console.log('scope: ' + JSON.stringify(scope, null, 2) + 'result: ' + result)
      } catch(e) {
          console.log(e.toString())
          data.error = e.toString();
      }
      return data;
  }

调用函数返回的数据是一个带有result、expression和error属性的JS对象:' ' data: {expression: {}， result: {}， error:{}} ' '。我们可以直接在ListModel中使用这个JS对象，然后从委托访问它。“模型。expression ' '给我们输入表达式。为了简单起见，我们忽略了误差结果。