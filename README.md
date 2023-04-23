# Quizard
 Quiz hosting and AI tutoring in one app!

## Inspiration

Active recall and feedback is proven to be one of the most effective learning methods. However, teachers have difficulty implementing this as it requires large amounts of individual attention to each student, leaving teachers feeling exhausted and student's needs not completely met.. We wanted to have a way to use this learning method alongside a classroom through quizzes and AI tutoring.

## What it does

Our application can be used in two ways - a teacher creating a quiz or a student joining a quiz. Teachers can enter in questions and our code generates a join code, placing these questions into a JSON file. Then, students can enter this code in a join the quiz. While they are taking the quiz, they can get answers right and move on, and when they get answers wrong, a new tab is opened, containing an AI chatbot that helps them with their questions until they are confident in their understanding. Then, students will resume the quiz and continue this process. 

## How we built it

We used a Flask backend and HTML/CSS/JS frontend using the Bulma package for styling and the Bubbles package for our chatbot UI. We also used the OpenAI gpt-3.5-turbo API to generate AI tutor responses. A JSON file was accessed from both the backend and the frontend for storing rooms and quizzes. Lastly, we made heavy use of the Chrome Developer Console to debug and analyze our code.

## Challenges we ran into

Creating the AI chatbot UI was a major problem. Having a chatbot UI that looked natural was too hard for us, so we had to find a UI package. Finally, we found an obscure package that could work for us called Bubbles. Using the Bubbles package was still a challenge for us because it had almost no documentation and had an extremely specific use method. We had to reverse-engineer the package to figure out how to use it and have a working chatbot UI. We also had issues fetching the OpenAI API response, as there was no published documentation for how to access it from vanilla JS. We ended up looking at the curl example and interpreting it to create a fetch request.

## Accomplishments that we're proud of

We are proud of uniting chatbots and tutoring with quizzes to create a much better end product. We are also proud of our work making a system to keep track of rooms and adding students to quizzes through JSON and requests.

## What we learned

We learned a lot about CSS and styling with Bulma, and we also learned a lot about more intermediate uses of Flask. Lastly, we learned how to use JSON and Flask requests, as we did not have any experience with these previously.

## What's next for Quizard

We plan to improve this with a React UI and Postgres database, instead of Bulma and JSON. We will also design our own UI for the chatbot and possibly fine tune the ChatGPT model to be more tailored towards our needs with an AI tutor.
