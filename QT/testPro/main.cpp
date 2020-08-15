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

bool isValidIP(QString ip){
    QStringList Numlist;
    Numlist = ip.split('.');
    if (Numlist.length() != 4)
    {
        return false;
    }else{

        for(int i = 0;i< 4;i++)
        {
            if(Numlist[i].toInt()>255)
            {
                return false;
            }

        }
        return true;
    }

}
int main( int argc, char **argv )
{
qDebug()<<isValidIP("192.15.12.256");
return 1;
}
