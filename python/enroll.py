import json

# load data
with open("../data/courses.json") as f:
    courses = json.load(f)

with open("../data/students.json") as f:
    students = json.load(f)


def find_student(student_id):
    return next((s for s in students if s["id"] == student_id), None)


def find_course(code):
    return next((c for c in courses if c["code"] == code), None)


def check_prerequisites(student, course):
    return all(pr in student["completedCourses"] for pr in course["prerequisites"])


def check_capacity(course):
    return len(course["enrolledStudents"]) < course["capacity"]


def enroll(student, course, courses):
    # already enrolled
    if course["code"] in student["enrolledCourses"]:
        return "Already enrolled"

    # capacity
    if len(course["enrolledStudents"]) >= course["capacity"]:
        return "Course full"

    # prerequisites
    for pre in course["prerequisites"]:
        if pre not in student["completedCourses"]:
            return f"Missing prerequisite: {pre}"

    # time conflict
    for c_code in student["enrolledCourses"]:
        c = next(c for c in courses if c["code"] == c_code)
        if c["timeSlot"] == course["timeSlot"]:
            return "Time conflict"

    # enroll
    student["enrolledCourses"].append(course["code"])
    course["enrolledStudents"].append(student["id"])

    return "Enroll success"


if __name__ == "__main__":
    sid = input("Student ID: ")
    cid = input("Course Code: ")
    enroll(sid, cid)