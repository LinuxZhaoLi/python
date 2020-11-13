#include "roleentrymodel.h"

RoleEntryModel::RoleEntryModel(QObject *parent)
    :QAbstractListModel(parent)
{
    // QHash<int,>
    m_roleNames[NameRole] = "name";
    m_roleNames[HueRole] = "hue";
    m_roleNames[SaturationRole] = "saturation";
    m_roleNames[BrightnessRole] = "brightness";
    for(const QString &name : QColor::colorNames())
        m_data.append(QColor(name));
}

RoleEntryModel::~RoleEntryModel()
{

}

int RoleEntryModel::rowCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return m_data.count();
}
// 返回的是一个 m_roleNames
QVariant RoleEntryModel::data(const QModelIndex &index, int role) const
{
    int row = index.row();
    if(row < 0 || row >= m_data.count())
        return QVariant();
    const QColor &color = m_data.at(row);
    switch(role){
        case NameRole:
        return color.name();
    case HueRole:
        return color.hueF();
    case SaturationRole:
        return color.saturation();
    case BrightnessRole:
        return color.lightnessF();


    }
    return QVariant();
}

QHash<int, QByteArray> RoleEntryModel::roleNames() const
{
    return m_roleNames;
}
