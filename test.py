from main import StudentsInMLOps
import pytest

@pytest.fixture
def students():
    return StudentsInMLOps()

def test_enrollStudents(students):
    students.enrollStudents(5)
    assert students.getTotalStrength() == 5

def test_dropStudents(students):
    students.enrollStudents(10)
    students.dropStudents(3)
    assert students.getTotalStrength() == 7
