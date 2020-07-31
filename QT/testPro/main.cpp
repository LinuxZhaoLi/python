#include <stdio.h>
#include <qdir.h>
#include <QFile>
#include <QFileInfoList>
#include <QFileInfo>
#include <QDebug>
// 遍历map
QVariantMap mySwap(QVariantMap &m,QVariantMap &k)
{

    uint kl = k.keys().length();

    for(uint j = 0;j < kl;j++)
    {
        QString str =  k.keys().value(j);
        uint value = k.values()[j].toUInt();
        if(m.contains(str))
        {
            m.remove(str);
            m.insert(str,value);
        }
    }

    return m;
}
void testPath()
{
    QString str = "/";
    if(str.endsWith('/')){
        qDebug()<<"true";

    }else{

         qDebug()<<"false";
    }

}
int main( int argc, char **argv )
{
Q_UNUSED(argc)
Q_UNUSED(argv)
testPath();
return 1;


}
