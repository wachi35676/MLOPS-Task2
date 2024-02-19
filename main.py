class StudentInMLOps:
    def enrollStudents(self, num):
        self.totalStudents = num
        return self.totalStudents

    def dropStudents(self, num):
        self.totalStudents -= num
        return self.totalStudents

    def getTotalStrength(self):
        return self.totalStudents

    def getClassName(self):
        return "StudentInMLOps"


