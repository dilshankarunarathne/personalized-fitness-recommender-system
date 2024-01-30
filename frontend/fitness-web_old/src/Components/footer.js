import React from 'react';
import './Footer.css';

const Footer = () => {
    return (
        <div className="bg-footer">
            <footer className="footer p-10 text-center">
                <div className="footer-row">
                    <div id='Se' className='tag'>
                        <div>
                            <span className="footer-title">Services</span>
                            <a className="link link-hover">Branding</a>
                            <a className="link link-hover">Design</a>
                            <a className="link link-hover">Developing</a>
                            <a className="link link-hover">Advertisement</a>
                        </div>
                    </div>
                    <div className='tag'>
                        <div>
                            <span className="footer-title">Company</span>
                            <a className="link link-hover">About us</a>
                            <a className="link link-hover">Contact</a>
                            <a className="link link-hover">Jobs</a>
                            <a className="link link-hover">Press kit</a>
                        </div>
                    </div>
                    <div id='Le' className='tag'>
                        <div>
                            <span className="footer-title">Legal</span>
                            <a className="link link-hover">Terms of use</a>
                            <a className="link link-hover">Privacy policy</a>
                            <a className="link link-hover">Cookie policy</a>
                        </div>
                    </div>
                </div>
            </footer>
            <div id='bot' className="text-center" >
                <p>Copyright © 2023 - All rights reserved by Fitness Web</p>
            </div>
        </div>
    );
};

export default Footer;
