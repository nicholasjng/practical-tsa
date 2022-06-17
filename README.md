# practical-tsa
Classical and DL-based Time Series Analysis, with pretty visualizations in the browser.

## Goals
* Quick prototyping of time series algorithms for a dataset (algo selection -> fitting -> inference -> result plots).
* Support classical algorithms (statsmodels/darts/etc.) and/or neural network algos (e.g. TF/pytorch/JAX/…).
* Present data + results in a web-frontend.
* LATER: Cloud-ready deployments for pushing out local solutions to larger platform.
* LATER: Dynamic selection of different algorithms and computational backends.

## Technologies
* Visualization frontend: [streamlit](https://github.com/streamlit/streamlit).
* Backend: A small api server (FastAPI ?), fetching results either from disk (local storage) or a database.
* TBD: Add a database for larger-scale operations and have the backend interact with it.

## The road to v1
- [ ] Procure some example data, e.g. historical stocks or any other well-known open TSA dataset.
- [ ] Build the first prototype visualization in streamlit, values (y) vs. time axis (x).
- [ ] Set up a TSA fitting backend with a library of choice (SM/Prophet/etc).
- [ ] Add frontend features for easy operation (algo selection, start/stop of fitted data region, "Run" button).
- [ ] Plot obtained results, including residuals and gliding confidence intervals.
- [ ] Implement inference, plot resulting extrapolated values together with the actual historic data.
