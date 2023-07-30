from django.core.management.base import BaseCommand
from academy.models import Course, Module, Lesson

class Command(BaseCommand):
    help = 'Create the Intro to Mechanical Keyboards course with its modules and lessons'

    def handle(self, *args, **options):
        intro_course = Course.objects.create(
            title="Intro to Mechanical Keyboards",
            description="This course provides an introduction to mechanical keyboards, covering their design, components, and benefits. Whether you're a beginner or an enthusiast, this course will help you understand the world of mechanical keyboards.",
            duration = "20 hours",
            course_img = "https://gmkkeycap.com/wp-content/uploads/2022/07/135-Keys-GMK-Dracula-Keycaps-Cherry-Profile-PBT-Dye-Sublimation-Mechanical-Keyboard-Keycap-For-MX-Switch-4.jpg",
            course_video = "https://youtu.be/s6SY7AQsyI0"
            
        )

        module1 = Module.objects.create(course=intro_course, title="Module 1: Introduction")
        Lesson.objects.create(module=module1, title="Lesson 1: What are Mechanical Keyboards?")
        Lesson.objects.create(module=module1, title="Lesson 2: Benefits of Using Mechanical Keyboards")
        Lesson.objects.create(module=module1, title="Lesson 3: Types of Mechanical Switches")

        module2 = Module.objects.create(course=intro_course, title="Module 2: Keyboard Anatomy")
        Lesson.objects.create(module=module2, title="Lesson 1: Keycap Materials and Profiles")
        Lesson.objects.create(module=module2, title="Lesson 2: Key Switches and Stabilizers")
        Lesson.objects.create(module=module2, title="Lesson 3: Backlighting and Customization")

        module3 = Module.objects.create(course=intro_course, title="Module 3: Choosing the Right Keyboard")
        Lesson.objects.create(module=module3, title="Lesson 1: Factors to Consider when Buying a Mechanical Keyboard")
        Lesson.objects.create(module=module3, title="Lesson 2: Popular Keyboard Brands and Models")
        Lesson.objects.create(module=module3, title="Lesson 3: Ergonomics and Layout Options")

        module4 = Module.objects.create(course=intro_course, title="Module 4: Keyboard Maintenance")
        Lesson.objects.create(module=module4, title="Lesson 1: Cleaning and Maintenance Tips")
        Lesson.objects.create(module=module4, title="Lesson 2: Dealing with Keycap and Switch Issues")
        Lesson.objects.create(module=module4, title="Lesson 3: Upgrading and Modifying Your Keyboard")

        module5 = Module.objects.create(course=intro_course, title="Module 5: Keyboard Customization")
        Lesson.objects.create(module=module5, title="Lesson 1: Keycap Customization and Artisan Keycaps")
        Lesson.objects.create(module=module5, title="Lesson 2: Switch Modification and Lubrication")
        Lesson.objects.create(module=module5, title="Lesson 3: Case Modifications and Custom Designs")

        module6 = Module.objects.create(course=intro_course, title="Module 6: Advanced Keyboard Features")
        Lesson.objects.create(module=module6, title="Lesson 1: Programmable Keyboards and Macros")
        Lesson.objects.create(module=module6, title="Lesson 2: RGB Lighting and Effects")
        Lesson.objects.create(module=module6, title="Lesson 3: Wireless and Bluetooth Connectivity")

        module7 = Module.objects.create(course=intro_course, title="Module 7: Mechanical Keyboard Community")
        Lesson.objects.create(module=module7, title="Lesson 1: Online Forums and Communities")
        Lesson.objects.create(module=module7, title="Lesson 2: Group Buys and Limited Edition Keyboards")
        Lesson.objects.create(module=module7, title="Lesson 3: Meetups and Keyboard Events")
