#include <QAudioDeviceInfo>
#include <QAudioOutput>
#include <QDebug>
#include <qmath.h>
#include <qendian.h>
#include "audiooutput.h"

#define PUSH_MODE_LABEL "Enable push mode"
#define PULL_MODE_LABEL "Enable pull mode"
#define SUSPEND_LABEL "Suspend playback"
#define VOLUME_LABEL "Volume"

const int DuarationSeconds = 1;
const int ToneSampleRates = 600;
const int DataSampleRates = 44100;
const int BufferSize = 32768;

Generator :: Generator(const QAudioFormat &format, qint64 durationUs,int sampleRate, QObject* parent)
    :QIODevice(parent)
    ,m_pos(0)
{
    if(format.isValid())
    generateData(format,durationUs,sampleRate);
}

Generator::~Generator()
{

}

void Generator::start()
{
    open(QIODevice::ReadOnly);
}
void Generator::stop()
{

    m_pos = 0;
    close();
}

void Generator::generateData(const QAudioFormat &format, qint64 durationUs, int sampleRate)
{
    const int  channelBytes = format.sampleSize();
    const int sampleBytes = format.channelCount();

    qint64 length = (format.sampleRate() * format.channelCount() * (format.sampleRate() / 8)) * durationUs / 100000;
    Q_ASSERT(length % sampleBytes == 0);
    Q_UNUSED(sampleBytes)

    m_buffer.resize(length);
    unsigned char *ptr = reinterpret_cast<unsigned char*> (m_buffer.data());


}
