# -*- encoding: utf-8 -*-

# 依赖倒置原则


class Course():
    def study(self):
        print('study...')


class PythonCourse(Course):
    def study(self):
        print('study python...')


class JavaCourse(Course):
    def study(self):
        print('study java...')


class Tom():
    def study(self, course: Course):
        course.study()


if __name__ == "__main__":
    tom = Tom()
    tom.study(JavaCourse())

