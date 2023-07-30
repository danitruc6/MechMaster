from django.core.management.base import BaseCommand
from academy.models import Course, Module, Lesson

class Command(BaseCommand):
    help = 'Create the Designing and Building Your Custom Mechanical Keyboard from Scratch course with its modules and lessons'

    def handle(self, *args, **options):
        course = Course.objects.create(
            title="Designing and Building Your Custom Mechanical Keyboard from Scratch",
            description="Embark on an exciting journey to design, engineer, and build your very own custom mechanical keyboard from scratch. This comprehensive course takes you through every step of the process, from creating schematics and PCB design using KiCAD, to manufacturing and assembly. Gain hands-on experience in selecting components, soldering techniques, 3D printing or using FR4 cases, switch and keycap customization, sound profile modifications, stabilizer tuning, switch modifications, and more. Unleash your creativity and create a truly unique keyboard that reflects your personal style and preferences.",
            duration = "45 hours",
            course_img = "https://camo.githubusercontent.com/9afd34335b6e5d7197576c0a144c48d56ad67bddb8e9bdb96ab614598e342a62/68747470733a2f2f692e696d6775722e636f6d2f76587771754e432e706e67",
            course_video = "https://youtu.be/iv__343ZwE0"
        )

        module1 = Module.objects.create(course=course, title="Module 1: Keyboard Design and Schematics")
        Lesson.objects.create(module=module1, title="Lesson 1: Introduction to Custom Mechanical Keyboards")
        Lesson.objects.create(module=module1, title="Lesson 2: Understanding Keyboard Architecture and Layouts")
        Lesson.objects.create(module=module1, title="Lesson 3: Creating Keyboard Schematics using KiCAD")

        module2 = Module.objects.create(course=course, title="Module 2: PCB Design and Manufacturing")
        Lesson.objects.create(module=module2, title="Lesson 1: PCB Design Principles and Best Practices")
        Lesson.objects.create(module=module2, title="Lesson 2: Translating Schematics into PCB Layout")
        Lesson.objects.create(module=module2, title="Lesson 3: PCB Prototyping and Manufacturing")

        module3 = Module.objects.create(course=course, title="Module 3: Case Design and Production")
        Lesson.objects.create(module=module3, title="Lesson 1: Exploring Case Design Options and Materials")
        Lesson.objects.create(module=module3, title="Lesson 2: 3D Printing Techniques for Custom Cases")
        Lesson.objects.create(module=module3, title="Lesson 3: Alternative Options: FR4 Case Construction")

        module4 = Module.objects.create(course=course, title="Module 4: Component Selection and Sourcing")
        Lesson.objects.create(module=module4, title="Lesson 1: Selecting Switches: Options and Considerations")
        Lesson.objects.create(module=module4, title="Lesson 2: Keycap Materials, Profiles, and Customization")
        Lesson.objects.create(module=module4, title="Lesson 3: Other Components: Microcontrollers, LEDs, etc.")

        module5 = Module.objects.create(course=course, title="Module 5: Soldering and Assembly")
        Lesson.objects.create(module=module5, title="Lesson 1: Essential Soldering Tools and Techniques")
        Lesson.objects.create(module=module5, title="Lesson 2: Soldering Switches, LEDs, and Components")
        Lesson.objects.create(module=module5, title="Lesson 3: Testing and Troubleshooting the Keyboard")

        module6 = Module.objects.create(course=course, title="Module 6: Customization and Modifications")
        Lesson.objects.create(module=module6, title="Lesson 1: Sound Dampening and Foam Inserts")
        Lesson.objects.create(module=module6, title="Lesson 2: Stabilizer Modifications and Lubrication")
        Lesson.objects.create(module=module6, title="Lesson 3: Switch Modifications: Springs, Lubrication, etc.")

        module7 = Module.objects.create(course=course, title="Module 7: Firmware Programming and Configuration")
        Lesson.objects.create(module=module7, title="Lesson 1: Introduction to Keyboard Firmware (QMK)")
        Lesson.objects.create(module=module7, title="Lesson 2: Flashing Firmware and Keymap Configuration")
        Lesson.objects.create(module=module7, title="Lesson 3: Advanced Customization: Macros, Layers, etc.")

        module8 = Module.objects.create(course=course, title="Module 8: Final Touches and Personalization")
        Lesson.objects.create(module=module8, title="Lesson 1: Fine-tuning the Keyboard's Performance")
        Lesson.objects.create(module=module8, title="Lesson 2: RGB Lighting Effects and Control")
        Lesson.objects.create(module=module8, title="Lesson 3: Showcasing Your Custom Keyboard")

        self.stdout.write(self.style.SUCCESS('Successfully created the course.'))
