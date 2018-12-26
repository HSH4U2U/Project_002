from .models import Subject
import csv
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
all_classes = os.path.join(BASE_DIR, './asitis/all_classes.csv')


def importing_class_list():
    f = open(all_classes, 'r', encoding='utf-8-sig')
    lines = csv.reader(f)
    i = 1
    for line in lines:
        class_info = line[0].split()
        if "\ufeff" in class_info[0]:
            class_info[0] = class_info[0].split("\ufeff")[1]

        if len(class_info) >= 8:
            if len(class_info[7]) == 1 or "I" in class_info[7] or "C" == class_info[6]:
                class_info[6] = str(class_info[6]) + str(class_info[7])
                del class_info[7]

        while len(class_info) > 8:
            class_info[7] = str(class_info[7]) + ", " + str(class_info[8])
            del class_info[8]

        subjects = Subject.objects.all()
        if len(class_info) == 8:
            new_subject = Subject(
                id=len(subjects) + 1,
                name=class_info[6],
                professor=class_info[7],
                code=class_info[5],
                department=class_info[1],
                major=class_info[2],
                course=class_info[4],
                grade=class_info[3],
                semester=class_info[0]
            )
        else:
            new_subject = Subject(
                id=len(subjects) + 1,
                name=class_info[6],
                professor="",
                code=class_info[5],
                department=class_info[1],
                major=class_info[2],
                course=class_info[4],
                grade=class_info[3],
                semester=class_info[0]
            )
        j = 0
        for subject in subjects:
            if new_subject.code == subject.code:
                if new_subject.professor == subject.professor:
                    if new_subject.semester not in subject.semester:
                        subject.semester = str(subject.semester) + ", " + str(new_subject.semester)
                        subject.save()
                    j = 1
                    break
        if j == 0:
            new_subject.save()
        print(str(i) + "-" + str(len(subjects) + 1))
        i += 1
    print("done")
    f.close()
