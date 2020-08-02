import asyncio   # asyncio的编程模型就是一个消息循环。

@asyncio.coroutine
def countdown(name,num):
    while num > 0:
        print(f'countdown[{name}]:{num}')
        yield from asyncio.sleep(1)
        num -= 1

@asyncio.coroutine
def hello():
    print("Hello, world")
    r = yield from asyncio.sleep(3)
    print("Hell0 , agaim")

def main():
    loop = asyncio.get_event_loop()  # 获取EventLoop 应用
    tasks = [countdown("A",10),countdown("B",5),hello()]  # 需要执行的协程扔到
    loop.run_until_complete(asyncio.wait(tasks))  # 执行

    loop.close()





if __name__ == "__main__":
    print(type(hello))
    main()
