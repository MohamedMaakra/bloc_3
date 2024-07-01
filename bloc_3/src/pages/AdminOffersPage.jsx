// AdminOffersPage.js
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const AdminOffersPage = () => {
  const [offers, setOffers] = useState([]);
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    price: '',
  });
  const [editOfferId, setEditOfferId] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchOffers();
  }, []);

  const fetchOffers = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/offers');
      const data = await response.json();
      setOffers(data);
    } catch (error) {
      console.error('Erreur lors de la récupération des offres:', error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const method = editOfferId ? 'PUT' : 'POST';
    const url = editOfferId ? `http://127.0.0.1:5000/api/offers/${editOfferId}` : 'http://127.0.0.1:5000/api/offers';
    try {
      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      setMessage(data.message);
      setFormData({
        title: '',
        description: '',
        price: '',
      });
      setEditOfferId(null);
      fetchOffers();
    } catch (error) {
      console.error('Erreur lors de l\'envoi du formulaire:', error);
      setMessage('Erreur lors de l\'envoi du formulaire. Veuillez réessayer.');
    }
  };

  const handleEdit = (offer) => {
    setEditOfferId(offer.id);
    setFormData({
      title: offer.title,
      description: offer.description,
      price: offer.price,
    });
  };

  const handleDelete = async (id) => {
    try {
      await fetch(`http://127.0.0.1:5000/api/offers/${id}`, {
        method: 'DELETE',
      });
      fetchOffers();
    } catch (error) {
      console.error('Erreur lors de la suppression de l\'offre:', error);
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8">
          <div className="card">
            <div className="card-body">
              <h2 className="card-title text-center">Gestion des offres</h2>
              {message && <div className="alert alert-info">{message}</div>}
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="title" className="form-label">Titre</label>
                  <input
                    type="text"
                    className="form-control"
                    id="title"
                    name="title"
                    value={formData.title}
                    onChange={handleChange}
                    placeholder="Entrez le titre de l'offre"
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="description" className="form-label">Description</label>
                  <textarea
                    className="form-control"
                    id="description"
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                    placeholder="Entrez la description de l'offre"
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="price" className="form-label">Prix</label>
                  <input
                    type="number"
                    className="form-control"
                    id="price"
                    name="price"
                    value={formData.price}
                    onChange={handleChange}
                    placeholder="Entrez le prix de l'offre"
                    required
                  />
                </div>
                <button type="submit" className="btn btn-primary w-100">
                  {editOfferId ? 'Mettre à jour' : 'Ajouter'} l'offre
                </button>
              </form>
            </div>
          </div>
          <div className="mt-5">
            <h3 className="text-center">Liste des offres</h3>
            <table className="table table-bordered">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Titre</th>
                  <th>Description</th>
                  <th>Prix</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {offers.map((offer) => (
                  <tr key={offer.id}>
                    <td>{offer.id}</td>
                    <td>{offer.title}</td>
                    <td>{offer.description}</td>
                    <td>{offer.price}</td>
                    <td>
                      <button className="btn btn-warning btn-sm me-2" onClick={() => handleEdit(offer)}>Modifier</button>
                      <button className="btn btn-danger btn-sm" onClick={() => handleDelete(offer.id)}>Supprimer</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminOffersPage;
