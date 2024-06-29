import React from "react";
import { NavLink } from "react-router-dom";
import { useAuth } from "../AuthContext"; // Importer useAuth
import 'bootstrap/dist/css/bootstrap.min.css';

const Header = () => {
  const { isLoggedIn, logout } = useAuth(); // Utiliser le contexte d'authentification

  return (
    <header className="bg-dark text-white p-3">
      <nav className="container d-flex justify-content-between align-items-center">
        <h1>Jeux Olympiques 2024</h1>
        <ul className="nav">
          <li className="nav-item">
            <NavLink className="nav-link text-white" exact to="/">Accueil</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link text-white" to="/offers">Offres</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link text-white" to="/reservation">Réservation</NavLink>
          </li>
          {isLoggedIn ? (
            <>
              <li className="nav-item">
                <NavLink className="nav-link text-white" to="/admin">Admin</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link text-white" to="/cart">Panier</NavLink>
              </li>
              <li className="nav-item">
                <button className="btn btn-link text-white" onClick={logout}>Déconnexion</button>
              </li>
            </>
          ) : (
            <>
              <li className="nav-item">
                <NavLink className="nav-link text-white" to="/signin">Connexion</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link text-white" to="/signup">Inscription</NavLink>
              </li>
            </>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default Header;
