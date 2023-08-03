# StudySnap

StudySnap is a comprehensive, user-friendly, machine learning-powered flashcard website. Although focusing on software engineering study, it allows users to freely create flashcard sets for any subject.

## Authors

- **PM**: Yueyue Zhu
- **Backend**: Ayush Dixit, Jean Paul Azopardi
- **Frontend**: Sujith Emmanuel Battu
- **Testing**: Jennifer Monti
- **Usability**: Wei Wang


## Usage

After opening the main website, users can:
1. **Without Logging In**: Click 'Flashcard' to view card sets, search card sets and study.
2. **Sign Up / Log In**: View card sets, study, create, edit, delete card sets, add cards into card sets, and see their own dashboards for all card sets belonging to them.

When in study mode, the cards are shown in a smart sequence that most effectively helps to learn and memorize. The detail is listed in the algorithm section below.

## Tools

- **Backend**: Django
- **Frontend**: HTML
- **Database**: PostgreSQL

## Algorithm

We use a bank of software engineering class questions for training and used machine learning models to predict the difficulty level (easy, medium, and difficult) of each question. In detail, a group of prior users took the questions and compared their answers to the correct answer to label the difficulty level of each question. For example, if all prior users answered correctly, it is marked as easy, vice versa.

The training took into account relevant features including question length, answer length, author, etc. After determining the difficulty, we used an effective learning sequence to show the cards to learners, starting from easy and then progressing to medium/difficult (shuffled). This rationale is based on the pedagogical principle that a gradual increase in complexity aids in retention and understanding, following the natural progression of learning.

## Feedback

For feedback, suggestions, or any questions, please contact Team 4 group members.

