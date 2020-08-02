import asyncio
@asyncio.coroutine  # 需要执行的协程  @asyncio.coroutine把一个generator标记为coroutine类型
def wget(host):
    print(f'wget {host}')
    connect = asyncio.open_connection(host, 80)
    print("$$$$$44")
    reader, writer = yield from connect  # 语法可以让我们方便地调用另一个generator
    header = f'GET / Http/1.0\r\nHost: {host}\r\n\r\n'
    writer.write(header.encode('utf-8'))
    yield from writer.drain()

    print("*******")
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        # print(f'{host} header > {line.decode(\'utf-8\')} ')
        print('%s header > %s ' % (host, line.decode('utf-8').strip()))

    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
