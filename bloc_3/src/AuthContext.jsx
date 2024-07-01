// AuthContext.js
import React, { createContext, useState, useContext } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = useState({ key: null, isAdmin: false });

  const signin = (key, isAdmin) => {
    setAuth({ key, isAdmin });
  };

  const signout = () => {
    setAuth({ key: null, isAdmin: false });
  };

  return (
    <AuthContext.Provider value={{ auth, signin, signout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
export { AuthContext }; // Ajoutez cette ligne pour exporter AuthContext
