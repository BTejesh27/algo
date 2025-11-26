import React, { useState } from "react";

export default function AuthExample() {
  const [user, setUser] = useState(null);
  const [uname, setUname] = useState("");
  const [pwd, setPwd] = useState("");

  const handleLogin = () => {
    if (uname === "admin" && pwd === "123") {
      setUser({ name: uname });
    } else {
      alert("Invalid Credentials");
    }
  };

  const handleLogout = () => setUser(null);

  return (
    <div style={{ margin: 30 }}>
      {!user ? (
        <>
          <h2>User Authentication Example</h2>
          <input
            placeholder="Username"
            onChange={(e) => setUname(e.target.value)}
          /><br />
          <input
            placeholder="Password"
            type="password"
            onChange={(e) => setPwd(e.target.value)}
          /><br />
          <button onClick={handleLogin}>Login</button>
        </>
      ) : (
        <>
          <h2>Welcome, {user.name}</h2>
          <button onClick={handleLogout}>Logout</button>
        </>
      )}
    </div>
  );
}
