import React from 'react';
import './about.css';
import Header from './header';
import Footer from './footer';


const HomePage = () => {

  return (
    <div>
        <Header></Header>
      <div className="banner-container">
        <div className="container">
          <div className="centered-container">
            <div className="col">
             <section id='about'>
             <h2>About Us </h2>
             <br></br>
             <p>We are a team of dedicated individuals passionate about health and fitness. Our mission is to provide personalized fitness recommendations to help you achieve your wellness goals.</p>
        <p>Founded in 2023, we have been working on creating a Personalized Fitness Recommender System that leverages the power of machine learning to offer tailored workout and diet plans to our users.</p>
             </section>
             <br></br>
             <section id="mission">
        <h2>Our Mission</h2>
        <br></br>
        <p>We are committed to helping you on your wellness journey. Our Personalized Fitness Recommender System is designed to create tailored workout and diet plans that fit your unique needs, motivating you to achieve your fitness goals.</p>
    </section>
    <br></br>
    <section id="contact">
        <h2>Contact Us</h2>
        <br></br>
        <p>If you have any questions or feedback, please don't hesitate to reach out to us. You can contact us at contact@yourwebsite.com.</p>
    </section>
            </div>
          
           
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
  );
  }

export default HomePage;
