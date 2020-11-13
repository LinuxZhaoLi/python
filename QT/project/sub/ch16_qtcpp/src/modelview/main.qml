import QtQuick 2.5
import QtQuick.Window 2.2
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.2
import org.example 1.0

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Background { // a dark background
        id: background
    }

    DynamicEntryModel {  // 数据
        id: dynamic
        onCountChanged: {
            // we print out count and the last entry when count is changing
            print('new count: ' + count);
            print('last entry: ' + get(count-1));
        }
    }

    ColumnLayout {  // 列布局
        anchors.fill: parent
        anchors.margins: 8
        ScrollView {  // 滑动界面
            Layout.fillHeight: true
            Layout.fillWidth: true
            ListView {
                id: view
                // set our dynamic model to the views model property
                model: dynamic
                delegate: ListDelegate {
                    width: ListView.view.width
                    // construct a string based on the models proeprties
                    text: 'hsv(' +
                          Number(model.hue).toFixed(2) + ',' +
                          Number(model.saturation).toFixed() + ',' +
                          Number(model.brightness).toFixed() + ')'
                    // sets the font color of our custom delegates
                    color: model.name

                    onClicked: {
                        // make this delegate the current item
                        view.currentIndex = index
                        view.focus = true
                    }
                    onRemove: {
                        // remove the current entry from the model
                        dynamic.remove(index)
                    }
                }
                highlight: ListHightlight { }
                // some fun with transitions :-)
                add: Transition {
                    // applied when entry is added
                    NumberAnimation {
                        properties: "x"; from: -view.width;
                        duration: 250; easing.type: Easing.InCirc
                    }
                    NumberAnimation { properties: "y"; from: view.height;
                        duration: 250; easing.type: Easing.InCirc
                    }
                }
                remove: Transition {
                    // applied when entry is removed
                    NumberAnimation {
                        properties: "x"; to: view.width;
                        duration: 250; easing.type: Easing.InBounce
                    }
                }
                displaced: Transition {
                    // applied when entry is moved
                    // (e.g because another element was removed)
                    SequentialAnimation {
                        // wait until remove has finished
                        PauseAnimation { duration: 250 }
                        NumberAnimation { properties: "y"; duration: 75
                        }
                    }
                }
            }
        }
        TextEntry { //组件
            id: textEntry
            onAppend: {
                // called when the user presses return on the text field
                // or clicks the add button

                var c_list = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "grey", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "transparent", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]
                for(var i =0; i< c_list.length;i++){
                    dynamic.append(c_list[i])

                }
            }

            onUp: {
                // called when the user presses up while the text field is focused
                view.decrementCurrentIndex()
            }
            onDown: {
                // same for down
                view.incrementCurrentIndex()
            }

        }

        }

}
