import os
import sys
import django
import random

# Setup Django environment
base_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(base_dir, 'Math-practice', 'backend')
sys.path.append(backend_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from problems.models import Problem

def generate_math_problems(count):
    print(f'Generating {count} math problems...')
    for _ in range(count):
        problem_type = random.choice(['arithmetic', 'equation', 'sequence'])
        
        if problem_type == 'arithmetic':
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            op = random.choice(['+', '-', '*', '/'])
            
            if op == '+':
                content = f"计算：{a} + {b} = ?"
                answer = str(a + b)
                difficulty = 1
                topic = "加法"
            elif op == '-':
                if a < b: a, b = b, a
                content = f"计算：{a} - {b} = ?"
                answer = str(a - b)
                difficulty = 1
                topic = "减法"
            elif op == '*':
                a = random.randint(1, 20)
                b = random.randint(1, 20)
                content = f"计算：{a} × {b} = ?"
                answer = str(a * b)
                difficulty = 2
                topic = "乘法"
            else: # /
                b = random.randint(1, 10)
                a = b * random.randint(1, 10)
                content = f"计算：{a} ÷ {b} = ?"
                answer = str(a // b)
                difficulty = 2
                topic = "除法"
                
        elif problem_type == 'equation':
            x = random.randint(1, 20)
            a = random.randint(1, 10)
            b = random.randint(1, 50)
            # ax + b = c
            c = a * x + b
            content = f"解方程：{a}x + {b} = {c}，求 x = ?"
            answer = str(x)
            difficulty = 3
            topic = "一元一次方程"

        elif problem_type == 'sequence':
            start = random.randint(1, 10)
            diff = random.randint(2, 5)
            seq = [start + i*diff for i in range(5)]
            content = f"找规律填空：{seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, (__?__)"
            answer = str(seq[4])
            difficulty = 2
            topic = "数列"

        Problem.objects.get_or_create(
            content=content,
            defaults={
                'correct_answer': answer,
                'difficulty_level': difficulty,
                'category': 'math',
                'topic': topic,
                'estimated_time': random.randint(1, 5)
            }
        )

def generate_cs_problems():
    print('Generating CS problems...')
    
    cs_problems = [
        # Data Structures
        {
            "content": "在栈（Stack）数据结构中，元素的插入和删除操作遵循什么原则？（请填写英文缩写，如FIFO）",
            "correct_answer": "LIFO",
            "difficulty_level": 1,
            "category": "ds",
            "topic": "栈",
            "estimated_time": 1
        },
        {
            "content": "二叉树的前序遍历顺序是：根 -> 左 -> 右。已知某二叉树的前序遍历为 ABDECFG，中序遍历为 DBEAFCG，请问其后序遍历是什么？",
            "correct_answer": "DEBFGCA",
            "difficulty_level": 3,
            "category": "ds",
            "topic": "树",
            "estimated_time": 5
        },
        {
            "content": "链表（Linked List）相比于数组（Array），主要的优势是什么？\nA. 随机访问速度快\nB. 内存空间利用率高\nC. 插入和删除操作更高效\nD. 代码实现更简单\n(请填写选项字母)",
            "correct_answer": "C",
            "difficulty_level": 2,
            "category": "ds",
            "topic": "链表",
            "estimated_time": 2
        },
        {
            "content": "一个最大容量为 n 的循环队列，队头指针为 front，队尾指针为 rear，则队列为空的条件是？",
            "correct_answer": "front == rear",
            "difficulty_level": 2,
            "category": "ds",
            "topic": "队列",
            "estimated_time": 2
        },
        
        # Algorithms
        {
            "content": "快速排序（Quick Sort）在最坏情况下的时间复杂度是多少？",
            "correct_answer": "O(n^2)",
            "difficulty_level": 2,
            "category": "algorithm",
            "topic": "排序",
            "estimated_time": 2
        },
        {
            "content": "Dijkstra 算法用于解决什么问题？\nA. 最小生成树\nB. 单源最短路径\nC. 拓扑排序\nD. 字符串匹配\n(请填写选项字母)",
            "correct_answer": "B",
            "difficulty_level": 3,
            "category": "algorithm",
            "topic": "图论",
            "estimated_time": 2
        },
        {
            "content": "动态规划（Dynamic Programming）的核心思想包括最优子结构和什么？",
            "correct_answer": "重叠子问题",
            "difficulty_level": 3,
            "category": "algorithm",
            "topic": "动态规划",
            "estimated_time": 3
        },
        
        # Network
        {
            "content": "在 TCP/IP 协议五层模型中，HTTP 协议属于哪一层？",
            "correct_answer": "应用层",
            "difficulty_level": 1,
            "category": "network",
            "topic": "HTTP",
            "estimated_time": 1
        },
        {
            "content": "TCP 三次握手中，第一次握手发送的报文标志位是？（填写英文缩写）",
            "correct_answer": "SYN",
            "difficulty_level": 2,
            "category": "network",
            "topic": "TCP/IP",
            "estimated_time": 2
        },
        
        # OS
        {
            "content": "进程与线程的主要区别中，哪一个拥有独立的资源（如内存地址空间）？",
            "correct_answer": "进程",
            "difficulty_level": 2,
            "category": "os",
            "topic": "进程",
            "estimated_time": 2
        },
        {
            "content": "死锁产生的四个必要条件是：互斥条件、请求与保持条件、不剥夺条件和什么条件？",
            "correct_answer": "循环等待条件",
            "difficulty_level": 3,
            "category": "os",
            "topic": "死锁",
            "estimated_time": 3
        },
        
        # ML
        {
            "content": "在机器学习中，用于防止模型过拟合（Overfitting）的技术有哪些？\nA. 增加数据量\nB. 正则化（Regularization）\nC. Dropout\nD. 以上都是\n(请填写选项字母)",
            "correct_answer": "D",
            "difficulty_level": 2,
            "category": "ml",
            "topic": "机器学习基础",
            "estimated_time": 2
        },
        {
            "content": "CNN（卷积神经网络）中最核心的操作层是卷积层和什么层？",
            "correct_answer": "池化层",
            "difficulty_level": 2,
            "category": "ml",
            "topic": "深度学习",
            "estimated_time": 2
        }
    ]

    for p_data in cs_problems:
        Problem.objects.get_or_create(
            content=p_data['content'],
            defaults={
                'correct_answer': p_data['correct_answer'],
                'difficulty_level': p_data['difficulty_level'],
                'category': p_data['category'],
                'topic': p_data['topic'],
                'estimated_time': p_data['estimated_time']
            }
        )

if __name__ == '__main__':
    print('Starting problem population...')
    generate_math_problems(count=50)
    generate_cs_problems()
    print('Successfully populated problems.')

