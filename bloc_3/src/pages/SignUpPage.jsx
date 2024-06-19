import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const SignUpPage = () => {
  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h2 className="card-title text-center">Inscription</h2>
              <form>
                <div className="mb-3">
                  <label htmlFor="username" className="form-label">Nom d'utilisateur</label>
                  <input type="text" className="form-control" id="username" placeholder="Entrez votre nom d'utilisateur" />
                </div>
                <div className="mb-3">
                  <label htmlFor="email" className="form-label">Email</label>
                  <input type="email" className="form-control" id="email" placeholder="Entrez votre email" />
                </div>
                <div className="mb-3">
                  <label htmlFor="password" className="form-label">Mot de passe</label>
                  <input type="password" className="form-control" id="password" placeholder="Entrez votre mot de passe" />
                </div>
                <div className="mb-3">
                  <label htmlFor="confirm-password" className="form-label">Confirmez le mot de passe</label>
                  <input type="password" className="form-control" id="confirm-password" placeholder="Confirmez votre mot de passe" />
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
