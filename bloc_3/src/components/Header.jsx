import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css'; 

const Header = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">JO 2024</Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <NavLink className="nav-link" to="/">Accueil</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/offers">Offres</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/reservation">Réservation</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/signin">Connexion</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/signup">Inscription</NavLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Header;
