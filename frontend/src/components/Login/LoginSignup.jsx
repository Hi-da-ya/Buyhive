import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import "./Login.css";

const LoginSignup = () => {
  const [isSignup, setIsSignup] = useState(true);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');

  const navigate = useNavigate();

  const handleUserNameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (isSignup && !email) {
      setError('Email is required.');
      return;
    }

    if (password.length < 6) {
      setError('Password must be at least 6 characters long.');
      return;
    }

    setError('');

    if (isSignup) {
      // Handle signup logic here
      setIsSignup(false);
    } else {
      // Handle login logic here
      navigate('/profile', { state: { username, email } });
    }
  };

  return (
    <div className="loginsignup">
      <div className="loginsignup-container">
        <h1>{isSignup ? 'Sign Up' : 'Login'}</h1>
        <form onSubmit={handleSubmit}>
          <div className="loginsignup-fields">
            <input
              type="text"
              placeholder="Your Name"
              value={username}
              onChange={handleUserNameChange}
              required
            />
            {isSignup && (
              <input
                type="email"
                placeholder="Email Address"
                value={email}
                onChange={handleEmailChange}
                required
              />
            )}
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={handlePasswordChange}
              required
            />
          </div>
          {error && <p style={{ color: 'red' }}>{error}</p>}
          <button type="submit">Continue</button>
        </form>
        <p className="loginsignup-login">
          {isSignup
            ? 'Already have an account '
            : "Don't have an account "}
          <span onClick={() => setIsSignup(!isSignup)}>
            {isSignup ? 'Login here' : 'Sign up here'}
          </span>
        </p>
        {isSignup && (
          <div className="loginsignup-agree">
            <input type="checkbox" name="" id="" required />
            <p>By continuing, I agree to the terms of use & privacy policy.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default LoginSignup;
