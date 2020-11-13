#include <QtGui>
#include <QtQml>
#include "dataentrymodel.h"
#include "roleentrymodel.h"
#include "dynamicentrymodel.h"

int main(int argc, char* argv[])
{
    QGuiApplication app(argc,argv);
DataEntryModel dd;

    qmlRegisterType<DataEntryModel>("org.examplr",1,0,"DataEntryModel");
    qmlRegisterType<RoleEntryModel>("org.example",1,0,"RoleEntryModel");
    qmlRegisterType<DynamicEntryModel>("org.example",1,0,"DynamicEntryModel");
    QQmlApplicationEngine engine;
//    engine.load(QStringLiteral("qrc:/main.qml"));
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();

}
/*
("aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque",
"black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood",
"cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk",
 "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray",
"darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen",
"darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen",
"darkslateblue", "darkslategray", "darkslategrey", "darkturquoise",
"darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue",
"firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite",
 "gold", "goldenrod", "gray", "green", "greenyellow", "grey", "honeydew",
"hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush",
"lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan",
"lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink",
"lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "
lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen",
"magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid",
 "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen",
"mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose",
"moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange",
"orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise",
 "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum",
"powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown",
"salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver",
"skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen",
"steelblue", "tan", "teal", "thistle", "tomato", "transparent",
 "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow",
 "yellowgreen")

*/
