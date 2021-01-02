TEMPLATE = app
TARGET = audiooutput

QT += multimedia widgets

HEADERS = audiooutput.h \
    audiooutput.h
SOURCES = \
	 mian.cpp \
    audiooutput.cpp

target.path = $$[QT_INSTALL_EXAMPLES]/multimedia/audiooutput
message("target path" $$target.path)
INSTALLS += target 