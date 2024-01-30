import React, { useState } from "react";
import './login.css';
import { withSignIn } from 'react-auth-kit'




function Login() {
  // React States
  const [errorMessages, setErrorMessages] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  // User Login info
  const database = [
    {
      username: "user1",
      password: "pass1",
      password1: "pass1"
    },
    {
      username: "user2",
      password: "pass2",
      password1: "pass2"
    }
  ];

  const errors = {
    uname: "invalid username",
    pass: "invalid password",
    pass1: "invalid password"
  };

  const handleSubmit = (event) => {
    //Prevent page reload
    event.preventDefault();

    var { uname, pass, pass1 } = document.forms[0];

    // Find user login info
    const userData = database.find((user) => user.username === uname.value);

    // Compare user info
    if (userData) {
      if (userData.password !== pass.value && userData.password1 !== pass1.value) {
        // Invalid password
        setErrorMessages({ name: "pass", message: errors.pass });
       
      } else {
        setIsSubmitted(true);
      }
    } else {
      // Username not found
      setErrorMessages({ name: "uname", message: errors.uname });
    }
  };

  // Generate JSX code for error message
  const renderErrorMessage = (name) =>
    name === errorMessages.name && (
      <div className="error">{errorMessages.message}</div>
    );

  // JSX code for login form
  const renderForm = (
    <div className="form">
      
      <form onSubmit={handleSubmit} className="formBox">
        <div className="input-container">
          <label>Username </label>
          <input type="text" name="uname" required />
          {renderErrorMessage("uname")}
        </div>
        <div className="input-container">
          <label>Password </label>
          <input type="password" name="pass" required />
          {renderErrorMessage("pass")}
        </div>
       
        <div className="button-container">
          <input type="submit" />
        </div>
      </form>
      
    </div>
  );

  return (
    <div className="app">
      
      <div className="login-form">
        {/* <div className="hed">
            <h2>Fitness Web</h2>
        </div> */}
      <div className="rap">
        <div className="title">Login</div>
        {isSubmitted ? <div>User is successfully Signed Up</div> : renderForm}
      </div>
      </div>
    </div>
  );
}

export default Login;