/*

import QtQuick 2.5
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.2
import QtQuick.Window 2.2
import "Jsconsole.js" as Util



ApplicationWindow {
    id:root
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    menuBar: MenuBar{  // 菜单栏

        Menu{
            title: qsTr("File")
            MenuItem{
                text: qsTr("Exit")
                onTriggered: Qt.quit()
            }
        }
    }



    ColumnLayout{  // 列布局

        anchors.fill: parent
        anchors.margins: 9
        RowLayout{  // 行布局
            Layout.fillWidth: true
            TextField{
                id: input
                Layout.fillWidth: true
                focus: true
                onAccepted: {
                    root.jsCall(input.text)
                }

            }
            Button {
                text: qsTr("Send")
                onClicked:{
                    root.jsCall(input.text)
                }
            }
        }

        Item{
            Layout.fillWidth: true
            Layout.fillHeight: true
            Rectangle{
                anchors.fill: parent
                color: "#333"
                border.color: Qt.darker(color)
                opacity: 0.2
                radius: 2

            }

            ScrollView{  // 提供另一项内的滚动视图
                id: scrollview
                anchors.fill: parent
                anchors.margins: 9
                ListView{  // 列表
                    id: resultView
                    model: ListModel{
                        id: outputModel
                    }
                    delegate: ColumnLayout{  // 代理
                        width: ListView.view.width
                        Label{
                            Layout.fillWidth: true
                            color: 'green'
                            text: "> " + model.expression
                        }
                        Label{
                            Layout.fillWidth: true
                            color: 'blue'
                            text: "" + model.result

                        }
                        Rectangle{  // 分割线
                            height: 1
                            Layout.fillWidth: true
                            color: "#333"
                            opacity: 0.2
                        }
                    }
              }
            }
        }
    }
    function jsCall(exp)  // 输入表达式， 添加到输出结果中
    {
        var data = Util.call(exp)
        outputModel.insert(0,data);
    }
}


*/


import QtQuick 2.5
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.2
import QtQuick.Window 2.2
import "Jsconsole.js" as Util

ApplicationWindow {
    id: root
    title: qsTr("JSConsole")
    width: 640
    height: 480

    Component.onCompleted: {

        var arr = [1,2,3,4,5,6,7,8,9,90]
        var r = Util.get_primes(arr)
        Util.printList(r)

        var str = "1元";
        if(str.match("元"))
            {
        console.log("匹配")
        }else{
            console.log("不匹配")
        }
    }

    menuBar: MenuBar {
        Menu {
            title: qsTr("File")
            MenuItem {
                text: qsTr("Exit")
                onTriggered: Qt.quit();
            }
        }
    }

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
                    root.jsCall(input.text)
                }
            }
            Button {
                text: qsTr("Send")
                onClicked: {
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
                    delegate: ColumnLayout { // 布局方式自动 计算宽高

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



    function jsCall(exp) {
        var data = Util.call(exp);
        outputModel.insert(0, data)
    }


}

