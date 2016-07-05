#Process

##os模块（创建一个子进程）

```python
import os
print('Process (%s) start...' %os.getpid())
pid = os.fork() #创建一个新的进程
if pid == 0:
	print('I am child process (%s) and my parent is %s.' %(os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child process (%s).' %(os.getpid(), pid))
```

运行结果

```python
Process (876) start...
I (876) just created a child process (877).     #新进程之行
I am child process (877) and my parent is 876.  #原进程执行
```

##multiprocessing

```python
from multiprocessing import Process
import os

def run_proc(name):
	print('Parent process %s (%s)...' %(name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' %os.getpid())
	p = Process(target = run_proc, args=('test',))
	print('child process will start.')
	p.start()#启动子进程
	p.join()#等待子进程结束后再继续往下运行，通常用于进程间的同步
	print('child process end.')
```

##pool

```python

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...' %(name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name,(end - start)))

if __name__ = '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')

```