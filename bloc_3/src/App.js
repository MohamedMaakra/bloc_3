import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomePage from "./pages/HomePage";
import OfferPage from "./pages/OffersPage";
import ReservationPage from "./pages/ReservationPage";
import AdminOffersPage from "./pages/AdminOffersPage"; // Importer la page admin
import SignInPage from "./pages/SignInPage";
import SignUpPage from "./pages/SignUpPage";
import Cart from "./components/Cart";
import { CartProvider } from "./CartContext";
import { AuthProvider } from "./AuthContext"; // Importer le AuthProvider
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
  return (
    <AuthProvider>
      <CartProvider>
        <Router>
          <div className="App">
            <Header />
            <main>
              <div className="container mt-3">
                <Routes>
                  <Route exact path="/" element={<HomePage />} />
                  <Route path="/offers" element={<OfferPage />} />
                  <Route path="/reservation" element={<ReservationPage />} />
                  <Route path="/admin" element={<AdminOffersPage />} />{" "}
                  <Route path="/signin" element={<SignInPage />} />
                  <Route path="/signup" element={<SignUpPage />} />
                  <Route path="/cart" element={<Cart />} />
                </Routes>
              </div>
            </main>
            <Footer />
          </div>
        </Router>
      </CartProvider>
    </AuthProvider>
  );
};

export default App;
