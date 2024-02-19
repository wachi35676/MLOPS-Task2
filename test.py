from main import StudentInMLOps


def test_enrollStudents():
    student = StudentInMLOps()
    assert student.enrollStudents(10) == 10


def test_dropStudents():
    student = StudentInMLOps()
    student.enrollStudents(10)
    assert student.dropStudents(5) == 5


def test_getTotalStrength():
    student = StudentInMLOps()
    student.enrollStudents(10)
    assert student.getTotalStrength() == 10


def test_getClassName():
    student = StudentInMLOps()
    assert student.getClassName() == "StudentInMLOps"
