import React, { useState } from "react";
import "./about.css";
import Header from "./header";
import Footer from "./footer";

const Profile = () => {
  const [mail] = useState("contact@yourwebsite.com");
  const [name] = useState("Nidarshana");
  return (
    <div>
      <Header></Header>
      <div className="banner-container">
        <div className="container">
          <div className="centered-container">
            <div className="col">
              <section id="about">
                <h2>Profile</h2>
                <br></br>
              </section>
              <br></br>
              <section id="about1">
                <h3>Email</h3>
                <br></br>
                <p>{mail}</p>
              </section>
              <br></br>
              <section id="about1">
                <h3>Name</h3>
                <br></br>
                <p>{name}</p>
              </section>
             <section>
              <br></br>
             <div>
                <button id="lgout" className="logout">LogOut</button>
              </div>
             </section>
            </div>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
  );
};

export default Profile;
