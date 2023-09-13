import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  render() {
    const containerStyle = {
      display: 'flex',
      flexDirection: 'column', // Stack the child elements vertically
      alignItems: 'center',
      justifyContent: 'center',
      height: '100vh',
      color: 'white',
      background: 'black',
    };

    const paragraphStyle = {
      borderBottom: '1px solid white', // Add a white border line between paragraphs
      padding: '10px', // Add some padding for spacing
    };

    return (
      <div style={containerStyle}>
        <h1>Good Job</h1>
        <p style={paragraphStyle}>React is working</p>
        <p style={paragraphStyle}>DB is working</p>
        <p style={paragraphStyle}>Django is working</p>
        <p style={paragraphStyle}>API is working</p>
        <h2>You are the best</h2>
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);

export default App;
