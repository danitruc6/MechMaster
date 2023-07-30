from django.core.management.base import BaseCommand
from academy.models import Course, Module, Lesson

class Command(BaseCommand):
    help = 'Create the Basics of QMK course with its modules and lessons'

    def handle(self, *args, **options):
        course = Course.objects.create(
            title="Basics of QMK",
            description="Delve into the fundamentals of QMK firmware, a powerful open-source software that enables advanced customization and programming for mechanical keyboards. Learn about the architecture and structure of QMK, keycodes, layers, and macros. Explore how to configure and compile firmware, flash it onto your keyboard, and utilize popular QMK features such as RGB lighting control and tap-dancing. By the end of this course, you'll have a solid understanding of QMK and the ability to unleash the full potential of your mechanical keyboard.",
            duration = "15 hours",
            course_img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVcXjxKNdkEj7QYAkD4iAsbWE_w0OF6yG1CQ&usqp=CAU",
            course_video = "https://youtu.be/Ho_CFfdsmc8"
        )

        module1 = Module.objects.create(course=course, title="Module 1: Introduction to QMK")
        Lesson.objects.create(module=module1, title="Lesson 1: What is QMK Firmware?")
        Lesson.objects.create(module=module1, title="Lesson 2: Benefits and Advantages of Using QMK")
        Lesson.objects.create(module=module1, title="Lesson 3: QMK Supported Keyboards and Hardware")

        module2 = Module.objects.create(course=course, title="Module 2: QMK Architecture and Structure")
        Lesson.objects.create(module=module2, title="Lesson 1: Understanding the QMK Codebase")
        Lesson.objects.create(module=module2, title="Lesson 2: Keycodes and Keymaps")
        Lesson.objects.create(module=module2, title="Lesson 3: Layers and Layering Concepts")

        module3 = Module.objects.create(course=course, title="Module 3: Advanced Customization with QMK")
        Lesson.objects.create(module=module3, title="Lesson 1: Macros and Functionality Expansion")
        Lesson.objects.create(module=module3, title="Lesson 2: Advanced Keycode Features")
        Lesson.objects.create(module=module3, title="Lesson 3: Tap-Dancing and Layer Toggling")

        module4 = Module.objects.create(course=course, title="Module 4: Configuration and Compilation")
        Lesson.objects.create(module=module4, title="Lesson 1: QMK Configurator and Web-based Tools")
        Lesson.objects.create(module=module4, title="Lesson 2: Building and Compiling Firmware")
        Lesson.objects.create(module=module4, title="Lesson 3: Firmware Flashing and Updating")

        module5 = Module.objects.create(course=course, title="Module 5: QMK Features and Extensions")
        Lesson.objects.create(module=module5, title="Lesson 1: RGB Lighting Control")
        Lesson.objects.create(module=module5, title="Lesson 2: Encoder and Rotary Support")
        Lesson.objects.create(module=module5, title="Lesson 3: Bluetooth and Wireless Connectivity")

        module6 = Module.objects.create(course=course, title="Module 6: Troubleshooting and Debugging")
        Lesson.objects.create(module=module6, title="Lesson 1: Debugging Techniques and Tools")
        Lesson.objects.create(module=module6, title="Lesson 2: Common Issues and Solutions")
        Lesson.objects.create(module=module6, title="Lesson 3: Community Resources and Support")
