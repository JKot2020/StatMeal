// App.js
// Main file for StatMeal application
// Author: Jason Kotowski

import './App.css';
import axios from "axios";
import React, { Component } from "react";

class App extends Component {
  state = {
      // Initially, no file is selected
      selectedFile: null,
  };

  // On file select (from the pop up)
  onFileChange = (event) => {
      // Update the state
      this.setState({
          selectedFile: event.target.files[0],
      });
  };

  // On file upload (click the upload button)
  onFileUpload = () => {
      // Create an object of formData
      const formData = new FormData();

      // Update the formData object
      formData.append(
          "myFile",
          this.state.selectedFile,
          this.state.selectedFile.name
      );

      // Details of the uploaded file
      console.log(this.state.selectedFile);

      // Request made to the backend api
      // Send formData object
      axios.post("api/uploadfile", formData);
  };

  // File content to be displayed after
  // file upload is complete
  fileData = () => {
      if (this.state.selectedFile) {
          return (
              <div className="App-file-desc">
                <button
                className="chooseFileButton"
                onClick={this.onFileUpload}>
                    <p>Upload</p>
                </button>
                  <h2>File Details:</h2>
                  <p>
                      File Name:{" "}
                      {this.state.selectedFile.name}
                  </p>

                  <p>
                      File Type:{" "}
                      {this.state.selectedFile.type}
                  </p>

                  <p>
                      Last Modified:{" "}
                      {this.state.selectedFile.lastModifiedDate.toDateString()}
                  </p>
              </div>
          );
      }
  };

  render() {
      return (
          <div className="App">
            <header className="App-header">
              <h1>StatMeal</h1>
            </header>
            <p className="App-basic">Upload spreadsheet file</p>
              <div className="App-file">
                  <input
                    className="chooseFileButton"
                    type="file"
                    onChange={this.onFileChange}
                  />
                  <br></br>
              </div>
              {this.fileData()}
          </div>
      );
  }
}

export default App;