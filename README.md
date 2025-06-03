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
README.md                        <- Project overview and instructions.
Assignments/                    <- Project documentation 
music/                          <- Music tracks to be analyzed and recommended.
uploads/                        <- Uploaded videos from users.
videos/                         <- Processed/final videos with music applied.

src/                            <- Frontend React source code.
│
├── App.js                      <- Main React component.
├── DramaTune.js                <- Core UI logic: handles upload, analysis, preview, and final merge.
├── index.js                    <- React entry point.
└── index.css                   <- Styling for the React components.

backend.py                      <- Flask backend: handles API routes for analysis and video/music merging.
analyze_rhythm.py               <- Extracts rhythmic features from user-uploaded videos.
analyze_tempo.py                <- Extracts tempo features from music tracks.

match_music_random_forest.py    <- Recommends music using a trained Random Forest model.
match_music_to_videos.py        <- Matches music to videos by comparing normalized tempo and rhythm.
match_top3_music.py             <- Selects top 3 matching tracks per video.

music_recommendation.py         <- Orchestrates the full matching process.
random_forest_model.pkl         <- Trained model used by `match_music_random_forest.py`.

normalized_music_tempo.csv      <- Preprocessed and scaled music tempo features.
normalized_video_rhythm.csv     <- Preprocessed and scaled video rhythm features.
music_tempo_scores.csv          <- Raw tempo scores from music analysis.
video_rhythm_results.csv        <- Raw rhythm scores from video analysis.

top_3_matches.csv               <- Output: top 3 matches for each video.
video_music_matches.csv         <- Full list of video–music match scores.

package.json                    <- Node.js project metadata and dependencies for frontend.
package-lock.json               <- Locked versions of installed npm packages.

.venv/                          <- Python virtual environment (not version controlled).
node_modules/                   <- Node.js dependencies (not version controlled).
.gitignore                      <- Files and folders to ignore in version control.
LICENSE                         <- Project license.

