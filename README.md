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
## app

how to run the project: (in Win64, Pycharm)
- run the backend in the flask terminal by: >>>python backend.py
- run the frontend and the project website in the main terminal by: npm start

### Project Overview

This project uses Machine learning model by Random Forest to compile a merged video with uploaded by the user,
and by the user choice out of 3 audios suggested to him, the user receives a merged video with the selected audio,
and later on will have finetune components.

### Dataset

The dataset used is music dataset that consists of dramatic soundtracks from kaggle,
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

- here is the last page of the app, where the user can preview the merged video, alongside audio effects component which hasn't been properly implemented yet,
with an option for download.

# Project Organization
```
├── README.md                  <- Project overview and instructions.
│
├── Assignments               <- Project documentation.
│   ├── Detailed Design SDD.docx
│   ├── Detailed requirements.docx
│   └── Literature Review.docx
│
├── music                     <- Music tracks to be analyzed and matched.
│
├── uploads                   <- User-uploaded video files.
│
├── videos                    <- Final output videos with music applied.
│
├── .venv                     <- Python virtual environment (not tracked by Git).
│
├── node_modules              <- Node.js dependencies (auto-generated, not tracked by Git).
│
├── package.json              <- Frontend project metadata and dependencies.
├── package-lock.json         <- Locked versions of installed npm packages.
│
├── backend.py                <- Flask backend server: handles analysis and merging requests.
│
├── analyze_rhythm.py         <- Extracts rhythmic features from user-uploaded videos.
├── analyze_tempo.py          <- Extracts tempo and features from music tracks.
│
├── match_music_random_forest.py  <- Matches music to video using trained Random Forest model.
├── match_music_to_videos.py      <- Matches music by comparing normalized rhythm/tempo.
├── match_top3_music.py           <- Selects top 3 closest music tracks per video.
├── music_recommendation.py       <- Orchestrates the full recommendation pipeline.
│
├── random_forest_model.pkl   <- Trained model used for music recommendation.
│
├── music_tempo_scores.csv        <- Raw tempo values from music analysis.
├── video_rhythm_results.csv      <- Raw rhythm values from video analysis.
├── normalized_music_tempo.csv    <- Normalized version of music tempo data.
├── normalized_video_rhythm.csv   <- Normalized version of video rhythm data.
│
├── top_3_matches.csv             <- Output file: top 3 recommended tracks for each video.
├── video_music_matches.csv       <- Output file: all video–music similarity scores.
│
├── src                      <- Frontend React source code.
│   ├── App.js               <- Main app component for DramaTune.
│   ├── DramaTune.js         <- Core UI and frontend logic for upload, analysis, and playback.
│   ├── index.js             <- React entry point.
│   └── index.css            <- Styling for the user interface.
```
