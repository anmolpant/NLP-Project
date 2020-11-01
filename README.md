<p align="center">
 <img height="80" src = "https://github.com/IshaanOhri/NLP-Project/blob/master/Assets/img/Graphle.png">
</p>

<p align="center">
 <img height="100" src = "https://github.com/IshaanOhri/NLP-Project/blob/master/Assets/img/Quote.svg">
</p>

<p align="center">Graphle is a service build to make learning easy for autistic students. It takes in real time input from the teacher, and arranges it in a visual manner</p>

<div align="center">
  <a href="https://graphle.ml">Start Graphling</a>
</div>
<br>
<br>
<p align="center">Autistic kids often receive education in a special way where concepts are delivered in a graphical way. Research says that visual memory is 60,000x faster than text/auditory memory. Inspired by graphical learning we created Graphle, a very effective visual learning tool for strengthening visual memory of our students.
</p>
<br>
<p align="center">
With use of cutting-edge technology, Graphle can be of great use in remote education, where teachers can take their classroom boards to their students and allow Graphle simplify concepts for them.
</p>

<br>
<h2 align="center">Market Research</h2>
<br>

<p align="center">
 <img src = "https://github.com/IshaanOhri/NLP-Project/blob/master/Assets/img/Stats.svg">
</p>

<br>
<h2 align="center">User Research</h2>
<br>

<p align="center">
 <img src = "https://github.com/IshaanOhri/NLP-Project/blob/master/Assets/img/stats2.svg">
</p>

<br>
<h2 align="center">What have we built?</h2>
<br>

 - **Android App:** Built with native Android SDK and Java, it captures the speech of the teacher/instructor and converts it into text using Google's Speech-to-Text API and sends it to our Node.js backend.
 
  - **Neural Network (Flask API):** The text received is processed and keywords are extracted from the same using a sequence to sequence encoder-decoder model. Both the models have been served with the help of Flask API which receive the text, preprocess it, extract keywords and send them to the Node.js Backend.
  
  - **Clipboard:** Designed with HTML/CSS/JS and websockets, it facilitates the display of the generated images in real-time, along with story recitation. The generated images can be shown onto the smart screen in a classroom or onto the individual screen of the student (Remote Classroom)-Sessions can be viewed on our website.
  
  - **Node.js Backend:** It acts as the control center for our service. It accepts the story snippet as text from the android application, sends it to the Flask API for keyword detection, gets the image URL (for the received keywords) from Microsoft Bing API and stores the entire backup on MongoDB. The story snippet along with the image URLs and audio clip's URL is sent via Pusher to all the devices connected to the session in real-time. 

<p align="center">
 <img src = "https://github.com/IshaanOhri/NLP-Project/blob/master/Assets/img/remote.png">
</p>
<br>
<br>
<p align="center">
 <img src = "https://github.com/IshaanOhri/NLP-Project/blob/master/Assets/img/classroom.png">
</p>

<br>
<h2 align="center">How it works?</h2>
<br>

<p align="center">
 <img src = "https://github.com/IshaanOhri/NLP-Project/blob/master/Assets/img/workflow.svg">
</p>

<br>
<h2 align="center">Tech Stacks</h2>
<br>

<p align="center">
 <img height=500 src = "https://github.com/IshaanOhri/NLP-Project/blob/master/Assets/img/TechStacks.png">
</p>
