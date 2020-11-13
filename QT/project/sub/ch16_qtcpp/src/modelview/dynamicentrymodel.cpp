#include "dynamicentrymodel.h"

DynamicEntryModel::DynamicEntryModel(QObject *parent)
    :QAbstractListModel(parent)
{
    m_roleNames[NameRole] = "name";
    m_roleNames[HueRole] = "hue";
    m_roleNames[SaturationRole] = "saturation";
    m_roleNames[BrightnessRole] = "brightness";
}

DynamicEntryModel::~DynamicEntryModel()
{

}

void DynamicEntryModel::insert(int index, const QString &colorValue)
{
    if(index < 0 || index > m_data.count())
    {
        return;
    }
    QColor color(colorValue); // 创建一个颜色对象
    if(!color.isValid())
        return;
    emit beginInsertRows(QModelIndex(),index,index); // 发送信号 开始插入
    m_data.insert(index,color);
    emit endInsertRows();  // 发送信号， 结束插入
    emit countChanged(m_data.count()); // 发送信号， 改变数据

}

void DynamicEntryModel::append(const QString &colorValue)
{
    insert(count(),colorValue);
}

void DynamicEntryModel::remove(int index)
{
    if(index < 0 || index >= m_data.count())
        return;
    emit beginRemoveRows(QModelIndex(),index,index);
    m_data.removeAt(index);
    emit endRemoveRows();
    emit countChanged(m_data.count());
}

void DynamicEntryModel::clear()
{
    emit beginResetModel();
    m_data.clear();
    emit endResetModel();

}

QColor DynamicEntryModel::get(int index)
{
    if(index < 0 || index >= m_data.count())
        return  QColor();
    return m_data.at(index);
}

int DynamicEntryModel::rowCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent)
    return m_data.count();
}

QVariant DynamicEntryModel::data(const QModelIndex &index, int role) const
{
    int row = index.row(); //
    if(row < 0|| row >= m_data.count())
        return QVariant();
    const QColor &color = m_data.at(row);
    switch(role)
    {
        case NameRole:
            return color.name();
         case HueRole:
            return color.hueF();
           case SaturationRole:
        return color.saturationF();
    case BrightnessRole:
        return color.lightnessF();


    }
    return QVariant();
}

int DynamicEntryModel::count() const
{
    return rowCount(QModelIndex());
}

QHash<int, QByteArray> DynamicEntryModel::roleNames() const
{
    return m_roleNames;
}

