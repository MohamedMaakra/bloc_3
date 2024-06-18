import React from "react";
import { NavLink } from "react-router-dom";

const Header = () => {
  return (
    <header>
      <nav>
        <ul>
          <li>
            <NavLink to="/" exact="true">Accueil</NavLink>
          </li>
          <li>
            <NavLink to="/offers" exact="true">Offres</NavLink>
          </li>
          <li>
            <NavLink to="/reservation" exact="true">Réservation</NavLink>
          </li>
          <li>
            <NavLink to="/admin" exact="true">Admin</NavLink>
          </li>
          <li>
            <NavLink to="/signin" exact="true">Connexion</NavLink>
          </li>
          <li>
            <NavLink to="/signup" exact="true">Inscription</NavLink>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
