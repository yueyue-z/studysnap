# StudySnap

StudySnap is a comprehensive, user-friendly, machine learning-powered flashcard website. Although focusing on software engineering study, it allows users to freely create flashcard sets for any subject.

Web link: https://studysnap-17c1fd4618f5.herokuapp.com/

## Authors

- **PM**: Yueyue Zhu
- **Backend**: Ayush Dixit
- **Backend & Algorithm**:Jean Paul Azopardi
- **Frontend**: Sujith Emmanuel Battu
- **Testing**: Jennifer Monti
- **Usability**: Wei Wang

## Usage

### For Learners (Visitors):
- **Explore**: Click 'Flashcard' to view and search card sets, and study without needing to log in.

### For Creators (Registered Users):
- **Study**: Click 'Flashcard' to view and search card sets, and study.
- **Creating**: View, create, edit and delete card sets; View, add, edit and delete cards.
- **Dashboard**: Monitor all your card sets and learning progress.

In study mode, the cards are intelligently ordered to enhance learning and retention. More details can be found in the algorithm section below.

## Tools

- **Backend**: Django
- **Frontend**: HTML
- **Database**: PostgreSQL

## Algorithm

StudySnap’s machine learning algorithm categorizes questions into three difficulty levels: easy, medium, and difficult. This classification is based on the following:

1. **Training Data**: A collection of software engineering questions answered by prior users, compared with the correct answers to label difficulty.
2. **Features**: Consideration of question length, answer length, author, and other relevant aspects.
3. **Classification**: If all prior users answered correctly, the question is marked as easy, and so forth.

After classifying difficulty, the system utilizes an optimal learning sequence, starting with easy questions and gradually progressing to medium and difficult ones. This strategy follows a pedagogical approach where a gradual increase in challenge aligns with the natural learning curve, aiding comprehension and memory retention.

## Feedback

For feedback, inquiries, or collaboration, please contact the project team members.

