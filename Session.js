import React, { useState, useEffect } from 'react';
import Cookies from "js-cookie";

export default function SessionExample() {
  const [username, setUsername] = useState("");
  const [sessionUser, setSessionUser] = useState("");

  useEffect(() => {
    const user = sessionStorage.getItem("sessionUser");
    const cookieUser = Cookies.get("cookieUser");

    if (user) setSessionUser(user);
    else if (cookieUser) setSessionUser(cookieUser);
  }, []);

  const handleLogin = () => {
    sessionStorage.setItem("sessionUser", username);
    Cookies.set("cookieUser", username, { expires: 1 }); // expires in 1 day
    setSessionUser(username);
  };

  const handleLogout = () => {
    sessionStorage.removeItem("sessionUser");
    Cookies.remove("cookieUser");
    setSessionUser("");
  };

  return (
    <div style={{ margin: 30 }}>
      {!sessionUser ? (
        <>
          <h2>Session Management Example</h2>
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
