# Getting Started with Create React App

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
# app
how to run the project:
- run the backend in the flask terminal by: >>>python backend.py
- run the frontend and the project website in the main terminal by: npm start

# Adapting-music-to-dramatic-scenes-in-movies



# Project Organization
├── README.md                        <- Project overview and instructions.
├── LICENSE                          <- Project license.
├── .gitignore                       <- Files and folders to ignore in version control.

├── Assignments/                     <- Project documentation.
│   ├── Detailed Design SDD.docx
│   ├── Detailed requirements.docx
│   └── Literature Review.docx

├── music/                           <- Music tracks to be analyzed and recommended.
├── uploads/                         <- Uploaded videos from users.
├── videos/                          <- Processed/final videos with music applied.

├── src/                             <- Frontend React source code.
│   ├── App.js                       <- Main React component.
│   ├── DramaTune.js                 <- Core UI logic: handles upload, analysis, preview, final merge.
│   ├── index.js                     <- React entry point.
│   └── index.css                    <- Styling for the React components.

├── backend.py                       <- Flask backend: handles API routes for analysis and merging.
├── analyze_rhythm.py                <- Extracts rhythm features from video (e.g., tempo, intensity).
├── analyze_tempo.py                 <- Extracts tempo features from music tracks.

├── match_music_random_forest.py     <- Music recommendation via Random Forest model.
├── match_music_to_videos.py         <- Matches music to videos based on tempo/rhythm distance.
├── match_top3_music.py              <- Selects top 3 matching tracks per video.
├── music_recommendation.py          <- Wraps analysis and matching into a unified recommendation flow.

├── random_forest_model.pkl          <- Trained Random Forest model for music prediction.

├── normalized_music_tempo.csv       <- Scaled music tempo features.
├── normalized_video_rhythm.csv      <- Scaled video rhythm features.
├── music_tempo_scores.csv           <- Raw tempo scores from music analysis.
├── video_rhythm_results.csv         <- Raw rhythm scores from video analysis.

├── video_music_matches.csv          <- Full table of music-to-video match scores.
├── top_3_matches.csv                <- Top 3 recommended music tracks for each video.

├── package.json                     <- Frontend project metadata (React, npm).
├── package-lock.json                <- Locked npm dependency versions.

├── .venv/                           <- Python virtual environment (excluded from version control).
└── node_modules/                    <- Node.js packages (auto-generated, excluded from version control).

