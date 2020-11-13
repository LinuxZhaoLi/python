#ifndef ROLEENTRYMODEL_H
#define ROLEENTRYMODEL_H

#include <QtCore>
#include <QtGui>

class RoleEntryModel : public QAbstractListModel
{

    Q_OBJECT

public:
    enum RoleNames {
        NameRole = Qt::UserRole,
        HueRole = Qt::UserRole+2,
        SaturationRole = Qt::UserRole+3,
        BrightnessRole = Qt::UserRole+4
    };
   explicit RoleEntryModel(QObject *parent = 0);
    ~RoleEntryModel();
public:
    virtual int rowCount(const QModelIndex &parent) const override;
    virtual QVariant data(const QModelIndex &index, int role) const override;

protected:
    virtual QHash<int, QByteArray> roleNames()const override;
private:
    QList<QColor> m_data;
    QHash<int,QByteArray> m_roleNames;
};

#endif // ROLEENTRYMODEL_H
