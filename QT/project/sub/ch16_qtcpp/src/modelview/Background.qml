import QtQuick 2.5

Rectangle {
    id: root
    anchors.fill: parent
    gradient: Gradient {   // 渐变
//        GradientStop { position: 0.0; color: "#4a4a4a" }
        GradientStop { position: 0.0; color: "#4a4a4a" }

        GradientStop { position: 1.0; color: "#2b2b2b" }
    }
}
//位置和颜色属性描述了渐变中给定位置所使用的颜色，如渐变停止符所示。
//默认位置为0.0;默认颜色是黑色。
//Rectangle {
//      width: 400; height: 800
//      rotation: 270
//      gradient: Gradient {
//          GradientStop { position: 0.0; color: "red" }
//          GradientStop { position: 0.33; color: "yellow" }
//          GradientStop { position: 1.0; color: "green" }
//      }
//  }
