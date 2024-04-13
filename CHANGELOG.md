Future, goals, to/dos by priority:
- deploy docker image to cloud run
-- Write pytest and rapidapi tests and run them in ci/cd
--- Draw from other APIs

April 12,2024
- Docker image pushes to artifact registry
-- Added to Github Actions!

April 10,2024
- Created working docker image for streamlit app

April 8,2024
- github actions: pytest runs locally. delaying setting it up on Actions till new API is set up. CodeQL is implemented.
- A big fork in the road: city bike data API was removed by creator. API still calls and returns, just no updated data.
While I ignore this issue, in the meantime Ive decided to finish writing the CI/CD and docker image deployment for learning purposes. 
I acknowloedge that the API will not be drawing new data. Ill replace it once I finish with the current goals!

April 7,2024
-Set up safety checks: streamlit tests
-- pytest for running these tests and set up in pipeline

April 6,2024
- Improved map face by implementing MapBox by Plotly. 
-- Map points on hover show bike details such as name, company, city and country. 
- Prefect Scheduling Up and Running for every 12 hours.
- Show updated time on Streamlit. Implemented proper site restructuring.
- Implemented CI/CD Github Actions for security: CodeQL

April 5,2024
- Fixed Streamlit bug and security risks
-- App would work locally but wouldn't deploy. Showed Google Cloud IAM permission errors and couldn't locate account. Service Keys for authenticating cloud project were 
stored in streamlit secrets and that fixed the issue.

Beginning of log.
