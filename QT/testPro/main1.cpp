#include <QDebug>
#include <QFileInfo>
#include <QDir>
#include <QStringList>
#include <QFileInfoList>

#define DECLARATIVE_EXAMPLE_MAIN(NAME) int main(int argc, char* argv[]) \
{\
   int a = 0;\
}

void test_Dir_getAllFileName(QString path)
{
    QDir dir;
    if(!dir.exists(path)){
        qDebug() << "目录不存在";
    }else{
        QDir dir(path);
        QStringList list = dir.entryList();
        for(int i=0;i<list.length();i++){
            //除去 . 和 ..
            if(list[i]!="." && list[i]!="..")
                qDebug() << list.at(i);
        }
    }
}

unsigned int test_Dir_getFileSize(QString path)// 获取文件大小
{
    unsigned int size = 0;
    QFileInfo info(path);
    if(info.isFile()){
        size += info.size();
    }

    QDir dir;
    if(!dir.exists(path)){
        qDebug() << "目录不存在";
    }else{
        QDir dir(path);
        QFileInfoList list = dir.entryInfoList();
        for(int i=0;i<list.length();i++){

            //除去 . 和 ..
            if(list[i].fileName()!="." && list[i].fileName()!=".."){
//                qDebug() << list.at(i).absoluteFilePath();
//                size += test_Dir_getFileSize(list.at(i).absoluteFilePath());
            }else{
 qDebug() << "*********";
  qDebug() <<list[i].fileName();

         qDebug() << list.at(i).absoluteFilePath();
            }
        }
    }
//    qDebug() << size;
    return size;
}
#include <QUrl>

//#define DECLARATIVE_EXAMPLE_MAIN(NAME) int main(int argc, char* argv[]) \
//{\
//qDebug()<<QUrl("qrc:///" #NAME ".qml")<<endl;\
//    return 0;\
//}




int main(int argc, char *argv[])
{
    Q_UNUSED(argc)
    Q_UNUSED(argv)
    DECLARATIVE_EXAMPLE_MAIN(ss)

//    qDebug() << test_Dir_getFileSize(path);
//   QDir dir(path);
//  qDebug()<<dir.absolutePath();


//    QString str = "helloworld";
//    QString a = str.mid(0, 5);
//       qDebug()<<a;

//    QString b = str.mid(5);
//    qDebug()<<b;

//    QString str2 = b.append(a);
//    str2 = "worldhello";

//    uint32_t i_t = 0xFFFFFFFE;
//    qDebug()<<"i_t"<<i_t;

     return 0;
}
