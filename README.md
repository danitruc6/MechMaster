# CS50W Final Project - MechMaster

#### 🎥 YouTube URL: https://youtu.be/ZMG5NZv4R14
[![Watch the video](https://img.youtube.com/vi/ZMG5NZv4R14/hqdefault.jpg)](https://youtu.be/nTQUwghvy5Q)

## Distinctiveness and Complexity

MechMaster is a unique online learning platform that stands out from other projects in the course due to its innovative approach to education and its comprehensive feature set. While many projects in the course focused on basic CRUD operations, MechMaster implements a complex ecosystem of features including user profiles, course enrollment, a dynamic forum, and interactive quizzes.

The complexity of MechMaster is evident in various aspects:
- **Interactive Learning Experience**: Unlike other projects, MechMaster incorporates video lessons, online resources, and interactive quizzes within each course module, providing a rich and engaging learning experience.
- **User Profiles and Enrollment**: MechMaster's user profile system allows learners to track their progress, view their enrolled courses, and manage their learning journey.
- **Forum with Real-Time Updates**: The integrated forum fosters community engagement among learners. Real-time updates on likes and views in forum topics enhance the user experience.
- **Sophisticated Quiz System**: MechMaster's quiz system allows instructors to create quizzes with multiple-choice questions. It displays a score at the end.

## Project Structure

The project is structured as follows:

- **academy**: The main Django app containing settings, URLs, and core project configurations.
- **users**: Manages user authentication, registration, and user profile functionality.
- **courses**: Handles courses, modules, lessons, and resources.
- **forum**: Implements the dynamic forum with categories, topics, and posts.
- **quizzes**: Manages the quiz creation, attempts, and scoring.
- **static**: Contains static files like CSS, JavaScript, and images.
- **templates**: Holds HTML templates for rendering the frontend.

## Running the Application

To run MechMaster on your local machine, follow these steps:

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/mechmaster.git
   cd mechmaster
   ```
2. Install the required Python packages:
    ```shell
    pip install -r requirements.txt
    ```
3. Set up the database:
    ```shell
    python manage.py migrate
    ```
4. Create a superuser for admin access:
    ```shell
    python manage.py createsuperuser
    ```
5. Run the development server:
    ```shell
        python manage.py runserver
    ```
6. Access the application in your browser at http://localhost:8000.

## Additional Information

- MechMaster makes use of third-party packages like Django's embed_video for video content.
- User authentication and permissions are carefully managed to ensure security and data integrity.
- The project showcases extensive use of Django's ORM for complex database relationships and queries.
- MechMaster employs responsive design principles to ensure optimal user experience across devices.

The project's complexity lies in its holistic approach to online learning, incorporating multimedia content, community engagement, and interactive assessments. MechMaster aims to redefine the e-learning experience and sets itself apart through its comprehensive feature set and user-centric design.