import React, { useState } from 'react';
import './homePage.css';
import Header from './header';
import Footer from './footer';

const Results = () => {
  const [textBoxValue, setTextBoxValue] = useState('');
  const [name] = useState('Nidarshana');
  const [bp] = useState('120/80');
  const [sugar] = useState('200/120');

  const handleTextBoxChange = (e) => {
    setTextBoxValue(e.target.value);
  };

  return (
    <div>
     <Header></Header>
<div className='upper'>
    <div className='ucontainer'>
        <div className="centered-container1 col1">
            <div className="col1">
                <h2>Your Info :</h2>
            </div>
            <div className="col1">
                <div className='h2'>
                <h3>{name }</h3>
                <br></br>
                <h3>{bp }</h3>
                <br></br>
                <h3>{sugar }</h3>
                <br></br>

                </div>
            </div>
        </div>
    </div>
</div>
      <div className="banner-container">
        <div className="container">
        <div className="centered-container">
            <div className="col">
              <h2>Meal Plan</h2>
            </div>
            <br></br>
            <div className='text-center1'>
              <input
                type="text"
                className="textb" 
                placeholder="Enter your text here"
                value={textBoxValue}
                onChange={handleTextBoxChange}
                style={{ width: '730px', height: '500px' }}
              />
            </div>
          </div>
          <div className="centered-container">
            <div className="col">
              <h2>Workout Routine</h2>
            </div>
            <br></br>
            <div className='text-center1'>
              <input
                type="text"
                className="textb" 
                placeholder="Enter your text here"
                value={textBoxValue}
                onChange={handleTextBoxChange}
                style={{ width: '730px', height: '500px' }}
              />
            </div>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
  );
}

export default Results;
 