import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Utiliser useNavigate pour la navigation
import { useAuth } from '../AuthContext'; // Importer useAuth
import 'bootstrap/dist/css/bootstrap.min.css';

const SignUpPage = () => {
  const navigate = useNavigate(); // Hook de navigation
  const { login } = useAuth(); // Utiliser le contexte d'authentification
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
  });
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (formData.password !== formData.confirmPassword) {
      setMessage("Les mots de passe ne correspondent pas.");
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/api/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: formData.email,
          password: formData.password,
        }),
      });
      const data = await response.json();
      if (response.ok) {
        setMessage('Inscription réussie !');
        setFormData({
          email: '',
          password: '',
          confirmPassword: '',
        });
        login(); // Appeler la fonction login du contexte d'authentification
        navigate('/signin'); // Rediriger vers la page de connexion après inscription réussie
      } else {
        setMessage(data.message || 'Erreur lors de l\'inscription. Veuillez réessayer.');
      }
    } catch (error) {
      setMessage('Erreur lors de l\'inscription. Veuillez réessayer.');
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h2 className="card-title text-center">Inscription</h2>
              {message && <div className="alert alert-info">{message}</div>}
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="email" className="form-label">Email</label>
                  <input
                    type="email"
                    className="form-control"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    placeholder="Entrez votre email"
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="password" className="form-label">Mot de passe</label>
                  <input
                    type="password"
                    className="form-control"
                    id="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    placeholder="Entrez votre mot de passe"
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="confirmPassword" className="form-label">Confirmez le mot de passe</label>
                  <input
                    type="password"
                    className="form-control"
                    id="confirmPassword"
                    name="confirmPassword"
                    value={formData.confirmPassword}
                    onChange={handleChange}
                    placeholder="Confirmez votre mot de passe"
                    required
                  />
                </div>
                <button type="submit" className="btn btn-primary w-100">S'inscrire</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignUpPage;
