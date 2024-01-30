import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
  const [active, setActive] = useState('nav__menu');
  const [toggleIcon, setToggleIcon] = useState('nav__toggler');

  const navToggle = () => {
    active === 'nav__menu'
      ? setActive('nav__menu nav__active')
      : setActive('nav__menu');

    toggleIcon === 'nav__toggler'
      ? setToggleIcon('nav__toggler toggle')
      : setToggleIcon('nav__toggler');
  };

  return (
    <nav className="nav">
      

      <Link to="/homePage" className="nav__brand">
        Fitness Web
      </Link>
      <ul className={active}>
      

        <li className="nav__item">
          <Link to="/homePage" className="nav__link">
            Home
          </Link>
        </li>
        <li className="nav__item">
          <Link to="/about" className="nav__link">
            About
          </Link>
        </li>
        <li className="nav__item">
          <Link to="/profile" className="nav__link">
            Profile
          </Link>
        </li>
      </ul>
      <div onClick={navToggle} className={toggleIcon}>
        <div className="line1"></div>
        <div className="line2"></div>
        <div className="line3"></div>
      </div>
    </nav>
  );
};

export default Header;
