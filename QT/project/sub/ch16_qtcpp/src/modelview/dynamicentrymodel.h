#ifndef DYNAMICENTRYMODEL_H
#define DYNAMICENTRYMODEL_H

#include <QtCore>
#include <QtGui>

class DynamicEntryModel : public QAbstractListModel
{
   Q_OBJECT
    Q_PROPERTY(int count READ count NOTIFY countChanged)
public:  //定义枚举
    enum RoleNames {
        NameRole = Qt::UserRole,
        HueRole = Qt::UserRole+2,
        SaturationRole = Qt::UserRole+3,
        BrightnessRole = Qt::UserRole+4
    };

    explicit DynamicEntryModel(QObject *parent = 0);
    ~DynamicEntryModel();

    Q_INVOKABLE void insert(int index, const QString& colorValue);
    Q_INVOKABLE void append(const QString& colorValue);
    Q_INVOKABLE void remove(int index);
    Q_INVOKABLE void clear();
    Q_INVOKABLE QColor get(int index);  // 被qml调用

public: // interface QAbstractListModel
    virtual int rowCount(const QModelIndex &parent) const;
    virtual QVariant data(const QModelIndex &index, int role) const;
    int count() const;

signals:
    void countChanged(int arg);
protected:
    // 返回一个类型
    virtual QHash<int, QByteArray> roleNames() const;

private:
    QList<QColor> m_data;
    QHash<int, QByteArray> m_roleNames;  // 相当于字典类型
    int m_count;


};

#endif // DYNAMICENTRYMODEL_H
