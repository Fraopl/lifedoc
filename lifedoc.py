import argparse
import csv
import datetime
import os


def add_header(path):
    with open(path, "a") as csvfile:
        _writer = csv.writer(csvfile)
        _writer.writerow(['#Time', 'Task']) 


def add_task(task, path):
    with open(path, "a") as csvfile:
        _writer = csv.writer(csvfile)
        _writer.writerow([datetime.datetime.now(), task])


def main():
    parser = argparse.ArgumentParser(description='Document your life tasks.')
    parser.add_argument("-p", '--path', type=str,
                        help='path of the storage file',
                        default='/home/zoro/tasks.csv')
    parser.add_argument('task', type=str,
                        help='task to document')

    args = parser.parse_args()
    print(args.path)
    print(args.task)

    if not os.path.exists(args.path):
        add_header(args.path)
        
    add_task(args.task, args.path)    

if __name__ == '__main__':
    main()
