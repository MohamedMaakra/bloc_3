import React, { useContext, useState } from "react";
import { CartContext } from "../CartContext";
import { useAuth } from "../AuthContext";
import { useNavigate } from 'react-router-dom';
import { v4 as uuidv4 } from "uuid";
import QRCode from "qrcode.react";

const Cart = () => {
  const { cart, removeFromCart, clearCart } = useContext(CartContext);
  const { auth } = useAuth();
  const navigate = useNavigate();
  const [qrCodeValue, setQrCodeValue] = useState(null);

  const totalPrice = cart.reduce((total, item) => total + item.prix, 0);

  const handleCheckout = async () => {
    if (!auth.key) {
      navigate('/signin'); 
    } else {
      // Simuler le paiement
      console.log('Paiement en cours...');

      // Générer une nouvelle clé
      const newKey = uuidv4();

      // Concaténer la nouvelle clé avec la clé existante de l'utilisateur
      const finalKey = auth.key + newKey;

      // Générer le QR Code
      setQrCodeValue(finalKey);
     
      clearCart();
    }
  };

  return (
    <div>
      <h2>Panier</h2>
      <ul className="list-group">
        {cart.map((item) => (
          <li key={item.cartId} className="list-group-item">
            <div>
              <strong>{item.titre}</strong> - {item.prix} €
              <button
                className="btn btn-danger btn-sm ms-3"
                onClick={() => removeFromCart(item.cartId)}
              >
                Supprimer
              </button>
            </div>
          </li>
        ))}
      </ul>
      {cart.length > 0 && (
        <div className="mt-3">
          <h4>Total : {totalPrice} €</h4>
          <button className="btn btn-primary me-3" onClick={handleCheckout}>Payer</button>
          <button
            className="btn btn-secondary"
            onClick={() => clearCart()}
          >
            Vider le panier
          </button>
        </div>
      )}
      {qrCodeValue && (
        <div className="mt-3">
          <h3>Votre e-billet :</h3>
          <QRCode value={qrCodeValue} />
        </div>
      )}
    </div>
  );
};

export default Cart;
