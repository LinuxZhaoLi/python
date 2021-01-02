#ifndef AUDIOOUTPUT_H
#define AUDIOOUTPUT_H
// 音频输出类
#include <math.h>
#include <QAudioOutput>
#include <QByteArray>
#include <QComboBox>
#include <QIODevice>
#include <QLabel>
#include <QMainWindow>
#include <QObject>
#include <QPushButton>
#include <QSlider>
#include <QTimer>

class Generator: public QIODevice
{
    Q_OBJECT
public:
    // 生成器
    Generator(const QAudioFormat &format,qint64 durationUs, int sampleRate,QObject *parent);
    ~Generator();
    void start();
    void stop();
    qint64 readData(char *data,qint64 maxlen);
    qint64 writeData(const char* data, qint64 len);
    qint64 bytesAbailable()const;

private:
    void generateData(const QAudioFormat &format, qint64 durationUs, int sampleRate);

private:
    qint64 m_pos;
    QByteArray m_buffer;

};

class AudioTest : public QMainWindow
{
    Q_OBJECT
public:
    AudioTest();
    ~AudioTest();
private:
    void initializeWindow();
    void initializeAudio();
    void createAudioOutput();
private :
    QTimer *m_pushTimer;
    QPushButton *m_suspendResumeButton;
    QComboBox* m_deviceBox;
    QLabel* m_volumeLabel;
    QSlider* m_volumeSlider;

    QAudioDeviceInfo m_device;
    Generator *m_generator;
    QAudioOutput *m_audioOutput;
    QIODevice *m_output;
    QAudioFormat m_format;

    bool m_pushMode;
    QByteArray m_buffer;

private slots:
    void pushTimerExpired();
    void toggleMode();
    void toggleSuspendResum();
    void deviceChanged(int index);
    void volumeChange(int);

};

#endif // AUDIOOUTPUT_H
