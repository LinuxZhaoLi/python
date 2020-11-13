#include "dataentrymodel.h"
#include <QDebug>
DataEntryModel::DataEntryModel(QObject *parent)
    :QAbstractListModel(parent)
{
    m_data = QColor::colorNames();
    qDebug()<<"colorNames";
    qDebug()<<m_data;
}

DataEntryModel::~DataEntryModel()
{

}

int DataEntryModel::rowCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return m_data.count();

}

QVariant DataEntryModel::data(const QModelIndex &index, int role) const
{
    // 索引返回所请求的行和列信息。
    //我们忽略列，只使用行信息
    int row = index.row();
    if(row < 0 || row > m_data.count())
        return QVariant();

    //模型可以返回不同角色的数据。
    //默认角色为显示角色。
    //可以在QML中通过“model.display”访问它
    switch(role)
    {
        case::Qt::DisplayRole:
        qDebug()<<Qt::DisplayRole;
        return m_data.value(row);

    }
    return QVariant();
}
