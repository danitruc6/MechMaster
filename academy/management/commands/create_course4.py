from django.core.management.base import BaseCommand
from academy.models import Course, Module, Lesson

class Command(BaseCommand):
    help = 'Create the Ergonomical Split Keyboard course with its modules and lessons'

    def handle(self, *args, **options):
        course = Course.objects.create(
            title="Ergonomical Split Keyboard",
            description="Learn about the design, benefits, and usage of ergonomic split keyboards. This course covers the principles of split keyboard layouts, ergonomic positioning, and the advantages of using split keyboards for improved comfort and productivity.",
            duration = "10 hours",
            course_img = "https://pbs.twimg.com/media/ELZcw1HVUAABIjh.jpg:large",
            course_video = "https://youtu.be/wTMcH7u-vu0"
        )

        module1 = Module.objects.create(course=course, title="Module 1: Introduction to Split Keyboards")
        Lesson.objects.create(module=module1, title="Lesson 1: What are Split Keyboards?")
        Lesson.objects.create(module=module1, title="Lesson 2: Benefits of Ergonomic Split Keyboards")
        Lesson.objects.create(module=module1, title="Lesson 3: Understanding Ergonomics in Keyboard Design")

        module2 = Module.objects.create(course=course, title="Module 2: Split Keyboard Layouts")
        Lesson.objects.create(module=module2, title="Lesson 1: Different Split Keyboard Designs")
        Lesson.objects.create(module=module2, title="Lesson 2: Ortholinear vs. Staggered Layouts")
        Lesson.objects.create(module=module2, title="Lesson 3: Adjustability and Customization Options")

        module3 = Module.objects.create(course=course, title="Module 3: Ergonomic Positioning")
        Lesson.objects.create(module=module3, title="Lesson 1: Proper Hand and Wrist Placement")
        Lesson.objects.create(module=module3, title="Lesson 2: Keyboard Tenting and Tilting")
        Lesson.objects.create(module=module3, title="Lesson 3: Importance of Ergonomic Accessories")

        module4 = Module.objects.create(course=course, title="Module 4: Advantages of Split Keyboards")
        Lesson.objects.create(module=module4, title="Lesson 1: Reduced Strain and Discomfort")
        Lesson.objects.create(module=module4, title="Lesson 2: Enhanced Typing Speed and Accuracy")
        Lesson.objects.create(module=module4, title="Lesson 3: Benefits for Individuals with Repetitive Strain Injuries")

        module5 = Module.objects.create(course=course, title="Module 5: Choosing the Right Split Keyboard")
        Lesson.objects.create(module=module5, title="Lesson 1: Factors to Consider when Selecting a Split Keyboard")
        Lesson.objects.create(module=module5, title="Lesson 2: Popular Split Keyboard Brands and Models")
        Lesson.objects.create(module=module5, title="Lesson 3: Evaluating Ergonomic Features and Functionality")

        module6 = Module.objects.create(course=course, title="Module 6: Transitioning to a Split Keyboard")
        Lesson.objects.create(module=module6, title="Lesson 1: Getting Started with a Split Keyboard")
        Lesson.objects.create(module=module6, title="Lesson 2: Overcoming Typing Challenges and Adaptation")
        Lesson.objects.create(module=module6, title="Lesson 3: Tips for Efficient Workflow and Productivity")

        module7 = Module.objects.create(course=course, title="Module 7: Maintaining and Customizing Split Keyboards")
        Lesson.objects.create(module=module7, title="Lesson 1: Cleaning and Maintenance Tips")
        Lesson.objects.create(module=module7, title="Lesson 2: Customizing Key Layout and Keycaps")
        Lesson.objects.create(module=module7, title="Lesson 3: Programming and Macros for Split Keyboards")
