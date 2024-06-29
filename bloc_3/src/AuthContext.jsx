import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState(null); // Stocker les détails de l'utilisateur connecté si nécessaire

  const login = () => {
    setIsLoggedIn(true);
    // Définir l'utilisateur connecté si besoin est
    // setUser(userDetails);
  };

  const logout = () => {
    setIsLoggedIn(false);
    // Réinitialiser les détails de l'utilisateur si nécessaire
    // setUser(null);
  };

  return (
    <AuthContext.Provider value={{ isLoggedIn, login, logout, user }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
