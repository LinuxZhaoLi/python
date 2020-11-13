import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

Item {
    width: 640
    height: 480
    property alias name: name
    property alias age: age        //property alias 别名：xx
    property alias sex: sexGroup
    property alias spec: speCBox
    property alias hobby: hobbyGrid
    property alias submit: submit
    property alias details: stuInfo
    RowLayout {            //行布局
        x: 50
        y: 35
        spacing: 10
        ColumnLayout {    //列布局
            spacing: 8
            RowLayout {
                spacing: 0
                Label {        //标签
                    text: "name"
                }
                TextField {    //文本框
                    id: name
                    color: "#f57900"
                    renderType: Text.NativeRendering
                    placeholderText: qsTr("Please input...")//水印
                    focus: true
                }
            }
            RowLayout {
                spacing: 13
                Label {
                    text: "age"
                }
                TextField {
                    id: age
                    x: 38
                    color: "#f57900"
                    validator: IntValidator {
                        bottom: 16
                        top: 26
                    }
                }
            }
            GroupBox {                        //组框
                id: group1
                title: qsTr("sex")
                Layout.fillWidth: true
                RowLayout {
                    RadioButton {            //单选按钮
                        id: sexGroup
                        text: qsTr("man")
                        checked: true
                        Layout.minimumWidth: 65
                    }
                    RadioButton {
                        text: qsTr("woman")
                        Layout.minimumWidth: 65
                    }
                }
            }
            RowLayout {
                spacing: 0
                Label {
                    text: "profession"
                }
                ComboBox {                //组合框
                    id: speCBox
                    Layout.fillWidth: true
                    currentIndex: 0
                    model: ListModel {
                        ListElement {
                            text: "computer"
                        }
                        ListElement {
                            text: "Communication engineering"
                        }
                        ListElement {
                            text: "Information network"
                        }
                    }
                    width: 200
                }
            }
            GroupBox {
                id: group2
                title: qsTr("hobby")
                Layout.fillWidth: true
                GridLayout {
                    id: hobbyGrid
                    columns: 3
                    CheckBox {                //复选框
                        text: qsTr("tourism")
                        checked: true
                    }
                    CheckBox {
                        text: qsTr("swim")
                        checked: true
                    }
                    CheckBox {
                        text: qsTr("basketball")
                    }
                    CheckBox {
                        text: qsTr("Sing")
                    }
                    CheckBox {
                        text: qsTr("dance")
                    }
                    CheckBox {
                        text: qsTr("Online shopping")
                    }
                    CheckBox {
                        text: qsTr("Watch TV")
                    }
                    CheckBox {
                        text: qsTr("other")
                        checked: true
                    }
                }
            }
            Button {                //按钮
                id: submit
                anchors.right: group2.right
                text: qsTr("submit")
            }
        }
        ColumnLayout {
            Layout.alignment: Qt.AlignTop
            Label {
                text: "basic information"
                font.pixelSize: 15
                font.bold: true
            }
            TextArea {                //文本域
                id: stuInfo
                Layout.fillHeight: true
                width: 240
                text: "student information..."
                font.pixelSize: 14
            }
        }
    }
}
