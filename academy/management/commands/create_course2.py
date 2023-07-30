from django.core.management.base import BaseCommand
from academy.models import Course, Module, Lesson

class Command(BaseCommand):
    help = 'Create the Everything you need to know about ortholinear keyboards course with its modules and lessons'

    def handle(self, *args, **options):
        course = Course.objects.create(
            title="Everything you need to know about ortholinear keyboards",
            description="Explore the world of ortholinear keyboards, a unique keyboard layout that arranges keys in a grid-like pattern. Discover the benefits, customization options, and popular ortholinear keyboard designs. Dive into key programming, firmware customization, and ergonomic considerations for a comfortable typing experience. Whether you're a keyboard enthusiast or a curious learner, this course will equip you with the knowledge to embrace and master ortholinear keyboards.",
            duration = "15 hours",
            course_img = "https://peterxjang.com/img/xd75re.jpg",
            course_video = "https://youtu.be/Ho_CFfdsmc8"
            
        )

        module1 = Module.objects.create(course=course, title="Module 1: Introduction to Ortholinear Keyboards")
        Lesson.objects.create(module=module1, title="Lesson 1: What are Ortholinear Keyboards?")
        Lesson.objects.create(module=module1, title="Lesson 2: Benefits of Using Ortholinear Keyboards")
        Lesson.objects.create(module=module1, title="Lesson 3: Comparison with Traditional Keyboard Layouts")

        module2 = Module.objects.create(course=course, title="Module 2: Popular Ortholinear Keyboard Designs")
        Lesson.objects.create(module=module2, title="Lesson 1: Pre-built Ortholinear Keyboards")
        Lesson.objects.create(module=module2, title="Lesson 2: DIY Ortholinear Keyboard Kits")
        Lesson.objects.create(module=module2, title="Lesson 3: Customization and Keycap Compatibility")

        module3 = Module.objects.create(course=course, title="Module 3: Key Programming and Firmware Customization")
        Lesson.objects.create(module=module3, title="Lesson 1: Understanding QMK and VIA")
        Lesson.objects.create(module=module3, title="Lesson 2: Programming Layers and Macros")
        Lesson.objects.create(module=module3, title="Lesson 3: Advanced Firmware Customization")

        module4 = Module.objects.create(course=course, title="Module 4: Ergonomics and Comfort with Ortholinear Keyboards")
        Lesson.objects.create(module=module4, title="Lesson 1: Ergonomic Considerations and Typing Posture")
        Lesson.objects.create(module=module4, title="Lesson 2: Adjusting to Ortholinear Layouts")
        Lesson.objects.create(module=module4, title="Lesson 3: Ortholinear Split and Ergo Layouts")

        module5 = Module.objects.create(course=course, title="Module 5: Advanced Ortholinear Keyboard Techniques")
        Lesson.objects.create(module=module5, title="Lesson 1: Switch Modifications and Lubrication")
        Lesson.objects.create(module=module5, title="Lesson 2: Stabilizer Tuning and Modding")
        Lesson.objects.create(module=module5, title="Lesson 3: Sound Dampening and Acoustics")

        module6 = Module.objects.create(course=course, title="Module 6: Ortholinear Keyboard Community and Resources")
        Lesson.objects.create(module=module6, title="Lesson 1: Online Communities and Forums")
        Lesson.objects.create(module=module6, title="Lesson 2: Group Buys and Limited Edition Ortholinear Keyboards")
        Lesson.objects.create(module=module6, title="Lesson 3: Ortholinear Keyboard Meetups and Events")
