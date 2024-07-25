class First_Students:
    first_class_students = "Excellent students"

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def description(self):
        return (f"{self.name} is {self.age} years old."
                f"\n{self.name}is {self.height} tall, {self.weight}."
                f"\n{self.name} is an {self.first_class_students}")


student1 = First_Students("Atilola Olayinka", 22, "1.69cm", "56kg")
student2 = First_Students("West Preciuos", 23, "1.50cm", "60kg")
student3 = First_Students("Kumasi Blessing", 20, "1.73cm", "52kg")
student4 = First_Students("Majesty Perela", 21, "1.46cm", "49kg")
student5 = First_Students("Ayanyemi John", 22, "1.70cm", "53kg")
student5 = First_Students(name="ayan", )

print(student1.description())

print()

print(student2.description())

print()

print(student3.description())

print()

print(student4.description())

print()

print(student5.description())

print()

print(f"{student1.name} is an {First_Students.first_class_students}")
