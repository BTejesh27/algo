import React, { useState, useEffect } from 'react';

export default function SessionExample() {
  const [username, setUsername] = useState("");
  const [sessionUser, setSessionUser] = useState("");

  useEffect(() => {
    const user = sessionStorage.getItem("sessionUser");
    if (user) setSessionUser(user);
  }, []);

  const handleLogin = () => {
    sessionStorage.setItem("sessionUser", username);
    setSessionUser(username);
  };

  const handleLogout = () => {
    sessionStorage.removeItem("sessionUser");
    setSessionUser("");
  };

  return (
    <div style={{ margin: 30 }}>
      {!sessionUser ? (
        <>
          <h2>Session Management Example (No Cookies)</h2>
          <input
            placeholder="Enter username"
            onChange={(e) => setUsername(e.target.value)}
          />
          <button onClick={handleLogin}>Save Session</button>
        </>
      ) : (
        <>
          <h2>Welcome {sessionUser}</h2>
          <button onClick={handleLogout}>Logout</button>
        </>
      )}
    </div>
  );
}
