# Adapting-music-to-dramatic-scenes-in-movies

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
# App

how to run the project: 

## 🛠 How to Set Up and Run This Project (All Environments)

Follow these steps to get the project running on **Windows, macOS, or Linux**.

This guide covers **Command Prompt**, **PowerShell**, **Git Bash**, and Unix-based terminals.

---

##  Step 1: Clone the Repository

```
git clone https://github.com/KimTsadok/Adapting-music-to-dramatic-scenes-in-movies.git
cd Adapting-music-to-dramatic-scenes-in-movies
```

---

##  Step 2: Create a Virtual Environment (if you don’t have one yet)

```
python -m venv .venv
```

This creates a folder called `.venv` with your isolated Python environment.

---

##  Step 3: Activate the Virtual Environment

### ▶ Windows

Choose based on your terminal:

#### • Command Prompt (cmd.exe):

```
.venv\Scripts\activate
```

#### • PowerShell:

```
.venv\Scripts\Activate.ps1
```

> If you get a policy error, run PowerShell as Administrator and run:
>
> ```
> Set-ExecutionPolicy RemoteSigned
> ```

#### • Git Bash (MINGW64):

```
source .venv/Scripts/activate
```

### ▶ macOS / Linux:

```
source .venv/bin/activate
```

You should now see `(.venv)` at the start of your terminal prompt ✅

---

##  Step 4: Install Dependencies

```
pip install -r requirements.txt
```

---

##  Step 5: Download the Machine Learning Model

Run the following script to automatically download the trained `.pkl` model from Google Drive:

```
python load_model_from_drive.py
```

---

##  Step 6: Test the Model

To confirm the model works and generates music matches:

```
python match_music_random_forest.py
```

This will output top 3 music matches per video and confirm the ML model runs successfully.

---

Need help? Open an issue or contact the repository maintainer.

You're done ! 🎉 Now you can proceed with running the project smoothly!
- run the backend in the flask terminal by: >>>python backend.py
- run the frontend and the project website in the main terminal by: npm start

### Project Overview

This project uses Machine learning model by Random Forest to compile a merged video with uploaded by the user,
and by the user choice out of 3 audios suggested to him, the user receives a merged video with the selected audio,
and later on will have finetune components.

### Dataset

The dataset used is music dataset that consists of dramatic soundtracks from kaggle,

https://www.kaggle.com/datasets/shanmukh05/music-classification

and video dataset that consists of short videos with a dramatic tempo up to 30 seconds.

### Applications

This application consists of a few main files.

Dramatune.js - in charge of the main aspects of the website, alongside connecting to the backend for various components (video, audio)

backend.py - in charge of connecting between the UI (frontend) and the backend (ML model, csvs - data collected and tagged)

index.css - in charge of personilizing the website's various accents

here is the various stages of using the app:
- landing page where the user is requested to upload a video (with an option for changing it)
![image](https://github.com/user-attachments/assets/a8ea7850-9b31-40f7-a741-d4bec1d17c51)
- after analyzing said video, user is requested to choose between 3 audio tracks to suit the video, with an option for playing them.
![image](https://github.com/user-attachments/assets/48b8478d-0170-4748-85ba-b831fe140469)
- then, the user can Generate a new video by clicking the button appearing after selecting the requested audio.
![image](https://github.com/user-attachments/assets/bfa1e7e2-0a0a-481a-9b65-8ac5e14fa203)

- here is the last page of the app, where the user can preview the merged video, with an option for download,
 alongside audio effects component which haven't been properly implemented yet.


# Project Organization
```
├── README.md                     <- Project overview and instructions.
├── LICENSE                       <- MIT License.

├── .gitignore                    <- Git ignore rules.
├── requirements.txt              <- Python dependencies for backend.
├── package.json                  <- Node.js frontend dependencies.
├── package-lock.json             <- Locked versions of npm packages.

├── backend.py                    <- Flask backend: handles upload, analysis, merge.
├── load_model_from_drive.py      <- Downloads the ML model from Google Drive.

├── analyze_rhythm.py             <- Rhythm detection from video (BPM etc.).
├── analyze_audio_features.py     <- Feature extraction from audio.
├── emotion_utils.py              <- Detects dominant facial emotion from video.
├── music_recommendation.py       <- Core logic: matches video to music using ML model.

├── match_music_random_forest.py  <- Music-video matching using random forest model.
├── match_music_to_videos.py      <- Basic matching using rhythm/tempo only.
├── match_music_with_emotion.py   <- Matching including emotion filtering.
├── match_music_combined.py       <- Combined method.
├── match_top3_music.py           <- Top 3 closest tracks script.

├── batch_emotion_detector.py     <- Detect emotions for a batch of videos.

│
├── music/                        <- Music tracks (MP3s).
├── uploads/                      <- Uploaded videos via frontend (temporary).
├── videos/                       <- Final output videos (with music).
├── public/                       <- React public folder (HTML shell, etc.).
├── src/                          <- React frontend source code (DramaTune app).
│   ├── App.js                    <- Main app logic.
│   ├── DramaTune.js              <- Core frontend for video/music interaction.
│   ├── index.js                  <- Entry point for React.
│   └── index.css                 <- Styling.

│
Assignments/
├── Detailed Design SDD.docx            <- System architecture, components, and data flow.
├── Detailed requirements.docx          <- Functional and non-functional requirements.
├── Literature Review.docx              <- Academic and technical background research.
├── Software Test Design (STD) - DramaTune.docx  <- Test cases and expected outcomes.
├── Software Test Plan (STP) - DramaTune.docx    <- Strategy, scope, tools, and schedule for testing.

│
├── random_forest_model.pkl       <- Trained ML model for matching (needs to be locally downloaded from GD).
│
├── final_video_music_matches.csv <- Final results: video to best matching tracks.
├── top_3_matches.csv             <- Top 3 matches per video.
├── video_music_matches.csv       <- All match scores (video × music).
├── video_emotions.csv            <- Detected emotion for each video.
├── video_rhythm_results.csv      <- Raw video rhythm scores.
├── normalized_video_rhythm.csv   <- Normalized video rhythm data.
├── music_tempo_scores.csv        <- Raw music tempo results.
├── normalized_music_tempo.csv    <- Normalized music tempo data.
├── music_audio_features.csv      <- Music tempo + volume features.
├── normalized_music_features.csv <- Final merged CSV (tempo, volume, normalized).

```
