import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Global styles, if any
import App from './App'; // Importing the root component

// Rendering the App component into the DOM
ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root') // Assuming there's a 'root' div in your index.html
);
