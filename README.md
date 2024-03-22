## Design for Flask Application: Lipaksha Language Learning Website

### HTML Files

**index.html:**
- **Purpose:** Welcome page of the website, providing an overview and language selection options.
- **Content:**
    - Header with a title and brief description of the website.
    - Navigation bar with links to different language sections.
    - Main section showcasing available languages and their progress.

**language.html:**
- **Purpose:** Dedicated page for each language, displaying lessons and exercises.
- **Content:**
    - Header with the name of the language and its proficiency level.
    - Sections for lessons, exercises, and interactive games.
    - Progress tracker to monitor learning progress.

**lesson.html:**
- **Purpose:** Page for displaying individual lessons within a language section.
- **Content:**
    - Lesson title and description.
    - Content area with text, audio, or video material.
    - Quizzes or interactive exercises to reinforce learning.

**exercise.html:**
- **Purpose:** Page for practicing exercises and testing language proficiency.
- **Content:**
    - Exercise instructions and questions.
    - Input fields, multiple choice options, or other interactive elements for user responses.
    - Automated scoring and feedback based on user input.

### Routes

**main.py:**

**@app.route('/')**
- **Purpose:** Main page (index.html).
- **Function:** Displays the welcome page and language selection options.

**@app.route('/language/<language_id>')**
- **Purpose:** Language-specific page (language.html).
- **Function:** Displays the dedicated page for the selected language, providing lessons and exercises.

**@app.route('/language/<language_id>/lesson/<lesson_id>')**
- **Purpose:** Specific lesson page (lesson.html) within a language section.
- **Function:** Displays the content and exercises for the selected lesson.

**@app.route('/language/<language_id>/exercise/<exercise_id>')**
- **Purpose:** Specific exercise page (exercise.html) within a language section.
- **Function:** Displays the exercise and evaluates user responses.

**@app.route('/progress')**
- **Purpose:** Progress tracking page.
- **Function:** Displays the user's progress across different languages and lessons.